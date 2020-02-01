import math
import itertools

from DistributionTransformers.NormalizeTransformer import NormalizeTransformer
from EqualLayer import EqualLayer
from FaceVisibilityLayers.Data import DATA
from Layer import Layer, DataError

class FaceVisibilityLayer(Layer):
    """ The Face Visibility Layer predict which candidate is the Mol based on how often this candidate appears during
    the episode. This code is based on the project of mattijn: https://github.com/mattijn/widm """

    def __init__(self, strict, distance_weights):
        """ Create a Face Visibility Layer.
        Arguments:
            strict (bool): If true then only seasons before the predict season will be used as training data. If false
            then all seasons are used as training data except the season for which we predict the result.
            distance_weights (dict): A dictionary with as keys the episode (int) and as value the distance_weight after
            that episode.
        """
        self.strict = strict
        self.distance_weights = distance_weights

    def compute_distribution(self, season, episode):
        if season not in DATA:
            raise DataError("Face Visibility Layer - Missing data season " + str(season))
        if episode == 0:
            return EqualLayer().compute_distribution(season, episode)

        max_episode = max(DATA[season].keys())
        if episode is None or episode > max_episode:
            episode = max_episode
        predict_input, input_length = self.get_predict_input(season, episode)
        train_pairs = self.get_train_pairs(season, input_length)
        predict_output = self.get_predict_output(predict_input, train_pairs, self.distance_weights[episode])
        # Give all candidates that dropped of so far a likelihood of 0
        for candidate in DATA[season][1].keys():
            if candidate not in predict_output:
                predict_output[candidate] = 0.0
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(predict_output)

    def get_predict_input(self, season, episode):
        """ Get the predict input for a certain season """
        episode_candidates = list(DATA[season][episode].keys())
        season_data = self.get_season_data(season, episode)
        predict_input = dict()
        input_length = len(season_data[episode_candidates[0]])
        for candidate in episode_candidates:
            predict_input[candidate] = sum(season_data[candidate]) / len(season_data[candidate])
        return (predict_input, input_length)

    def get_train_pairs(self, season, input_length):
        """ Get the train input & output """
        train_seasons = [s for s in DATA.keys() if s < season] if self.strict else [s for s in DATA.keys() if s != season]

        # Get the data vectors of all training seasons
        train_input = dict()
        for season in train_seasons:
            train_input.update(self.get_season_data(season, math.inf))

        # Get the train pairs which is an input-output combination
        train_pairs = []
        for candidate, vector in train_input.items():
            mol_value = 1 if candidate.value.is_mol else 0
            for perm in itertools.combinations(vector, input_length):
                train_pairs.append((sum(perm) / len(perm), mol_value))
        return train_pairs

    def get_season_data(self, season, max_episode):
        """ Get the data vectors for a certain season """
        season_data = dict()
        for episode in sorted(DATA[season].keys()):
            if episode > max_episode:
                break
            episode_data = DATA[season][episode]
            occ_sum = sum(episode_data.values())
            for candidate, value in episode_data.items():
                # Multiply every value by the number of candidates in that episode to normalize the value and divide
                # by the total sum of occurrences by all candidates during that episode
                season_data[candidate] = season_data.get(candidate, []) + [value * len(episode_data) / occ_sum]
        return season_data

    def get_predict_output(self, predict_input, train_pairs, distance_weight):
        """ Get the output for the predict data """
        predict_output = dict()
        for candidate, predict_value in predict_input.items():
            score = 0
            weight_sum = 0
            for train_value, mol_value in train_pairs:
                # Take a weighted score of the mol values
                weight = 1 / (1 + distance_weight * math.pow(predict_value - train_value, 2.0))
                weight_sum += weight
                score += weight * mol_value
            predict_output[candidate] = score / weight_sum
        return predict_output