from Data.Player import Player
from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
from Layers.FaceVisibility.VideoParser import VideoParser
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from sklearn.linear_model import LogisticRegression
from typing import Dict, Set
import numpy as np

class InnerFaceVisibilityLayer(Layer):
    MAX_TRAINING_ITERATIONS = 10000  # For how many iterations the logistic regression has to be trained

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        # Get the latest episode that is still available as data used for the prediction.
        max_episode = 0
        for i in range(1, latest_episode + 1):
            if VideoParser.has_parsed_video(predict_season, i):
                max_episode = i
            else:
                break

        if max_episode == 0:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        train_input = []
        train_output = []
        for train_season in train_seasons:
            input, output = FaceVisibilityExtractor.get_train_data(train_season, max_episode)
            train_input.extend(input)
            train_output.extend(output)

        classifier = LogisticRegression(solver='lbfgs', max_iter=self.MAX_TRAINING_ITERATIONS)
        classifier.fit(np.array(train_input), np.array(train_output))

        distribution = dict()
        predict_data = FaceVisibilityExtractor.get_predict_data(predict_season, max_episode)
        season_players = [player for player in Player if player.value.season == predict_season]
        for player in season_players:
            if player in predict_data:
                predict_input = predict_data[player]
                distribution[player] = classifier.predict_proba(np.array([predict_input]))[0][1]
                print(player)
                print(distribution[player])
            else:
                distribution[player] = 0.0

        return distribution

class FaceVisibilityLayer(NormalizeLayer):
    """ The Face Visibility Layer predict which candidate is the Mol based on how often this candidate appears during
    the episode. This code is based on the project of mattijn: https://github.com/mattijn/widm """

    def __init__(self):
        super().__init__(InnerFaceVisibilityLayer())