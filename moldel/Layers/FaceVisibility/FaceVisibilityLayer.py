from Data.Player import Player
from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
from Layers.FaceVisibility.VideoParser import VideoParser
from Layers.HypertunedLayer import HypertunedLayer
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from sklearn.linear_model import LogisticRegression
from sklearn.mixture import GaussianMixture
from typing import Dict, Set, Tuple
import numpy as np

class InnerFaceVisibilityLayer(Layer):
    GAUSSIAN_MIXTURE_ATTEMPTS = 3

    def __init__(self, num_components: int, likelihood_limit: float, dec_season_weight: float):
        """ Constructor of the Inner Face Visibility Layer. """
        self.__num_components = num_components
        self.__likelihood_limit = likelihood_limit
        self.__dec_season_weight = dec_season_weight

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        max_episode = self.__latest_available_episode(predict_season, latest_episode)
        if max_episode == 0:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        extractor = FaceVisibilityExtractor(predict_season, max_episode, train_seasons, self.__dec_season_weight)
        train_input, train_output = extractor.get_train_data()
        clustering = GaussianMixture(self.__num_components, covariance_type = "full", n_init = self.GAUSSIAN_MIXTURE_ATTEMPTS)
        clustering.fit(train_input)
        print(clustering.means_)
        train_input = clustering.predict_proba(train_input)
        train_input = np.minimum(train_input, self.__likelihood_limit)
        classifier = LogisticRegression(solver = "lbfgs")
        classifier.fit(train_input, train_output)

        distribution = dict()
        predict_data = extractor.get_predict_data()
        season_players = [player for player in Player if player.value.season == predict_season]
        for player in season_players:
            if player in predict_data:
                likelihood = 1.0
                for data in predict_data[player]:
                    data = clustering.predict_proba(np.array([data]))
                    data = np.minimum(data, self.__likelihood_limit)
                    print(player)
                    print(data)
                    likelihood *= classifier.predict_proba(data)[0][1]
                distribution[player] = likelihood ** (1 / len(predict_data[player]))
            else:
                distribution[player] = 0.0

        return distribution

    def __latest_available_episode(self, predict_season: int, latest_episode: int) -> int:
        """ Determine the latest episode that is available and can be used in the prediction season.

        Arguments:
            predict_season (int): The season for which the prediction is made.
            latest_episode (int): The latest episode of the prediction season which may be used as data.

        Returns:
            The latest available and usable episode of the prediction season.
        """
        max_episode = 0
        for i in range(1, latest_episode + 1):
            if VideoParser.has_parsed_video(predict_season, i):
                max_episode = i
            else:
                return max_episode
        return max_episode