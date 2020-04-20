from Data.Player import Player
from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor, Encoding
from Layers.FaceVisibility.VideoParser import VideoParser
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler
from typing import Dict, Set, List, Tuple
import itertools as it
import numpy as np

class InnerFaceVisibilityLayer(Layer):
    MAX_OCCURRENCE_FEATURES = 1

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        upto_episode = self.__get_upto_episode(predict_season, latest_episode)
        if upto_episode == 0:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        train_data = FaceVisibilityExtractor.get_train_data(train_seasons, upto_episode)
        predict_data = FaceVisibilityExtractor.get_predict_data(predict_season, upto_episode)
        scaler = self.__initialize_scaler(train_data)
        train_data = [self.__scale_data(d, scaler) for d in train_data]
        predict_data = {p: self.__scale_data(d, scaler) for p, d in predict_data.items()}

        season_players = [player for player in Player if player.value.season == predict_season]
        train_input = np.array([[d.season, sum(d.occurrences)] for d in train_data])
        train_output = np.array([1.0 if d.is_mol else 0.0 for d in train_data])
        model = KNeighborsRegressor(n_neighbors=len(train_input), weights='distance')
        model.fit(train_input, train_output)

        distribution = dict()
        for player in season_players:
            if player in predict_data:
                predict_input = [[predict_data[player].season, sum(predict_data[player].occurrences)]]
                distribution[player] = model.predict(np.array(predict_input))[0]
            else:
                distribution[player] = 0.0

        return distribution

    def __get_upto_episode(self, predict_season: int, latest_episode: int) -> int:
        """ Determine the last episode in the predict season for which we still have Face Visibility data that is
        considered to be known for the layers.

        Returns:
            The episode number of that last episode.
        """
        upto_episode = 0
        for i in range(1, latest_episode + 1):
            if VideoParser.has_parsed_video(predict_season, i):
                upto_episode = i
            else:
                break
                
        return upto_episode

    def __initialize_scaler(self, train_data: List[Encoding]):
        scaler = StandardScaler()
        scaler.fit(np.array([[d.season] + d.occurrences for d in train_data]))
        return scaler

    def __scale_data(self, data: Encoding, scaler: StandardScaler):
        scaled_data = scaler.transform(np.array([[data.season] + data.occurrences]))[0]
        return Encoding(scaled_data[0], scaled_data[1:], data.is_mol)

class FaceVisibilityLayer(NormalizeLayer):
    """ The Face Visibility Layer predict which candidate is the Mol based on how often this candidate appears during
    the episode. This code is based on the project of mattijn: https://github.com/mattijn/widm """

    def __init__(self):
        super().__init__(InnerFaceVisibilityLayer())