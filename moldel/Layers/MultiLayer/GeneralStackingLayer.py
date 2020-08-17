from Data.Player import Player
from Data.PlayerData import get_is_mol, get_players_in_season
from Layers.Layer import Layer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from sklearn.linear_model import LogisticRegression
from typing import Dict, Set, Tuple, List, Union
import numpy as np
import scipy.special

class InnerGeneralStackingLayer(Layer):
    MAX_DISTANCE_INC_EPISODE = 8
    MAX_VALIDATION_EPISODE = 9

    def __init__(self, layer: MultiLayer, decrease_weight: float, max_distance_episode: int, max_validate_episode: int):
        self.__layer = layer
        self.__decrease_weight = decrease_weight
        self.__max_distance_episode = max_distance_episode
        self.__max_validate_episode = max_validate_episode

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        classifier = self.__train(train_seasons, latest_episode)
        raw_prediction = self.__layer.predict(predict_season, latest_episode, train_seasons)
        distribution = self.__predict(predict_season, raw_prediction, classifier)
        if distribution:
            return distribution
        else:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

    def __train(self, train_seasons: Set[int], predict_episode: int) -> LogisticRegression:
        all_input = []
        all_output = []
        all_weights = []

        predict_episode = min(predict_episode, self.__max_validate_episode)
        for season in train_seasons:
            other_seasons = train_seasons.difference({season})
            for episode in range(self.__max_validate_episode + 1):
                print("S" + str(season) + "E" + str(episode))
                prediction = self.__layer.predict(season, episode, other_seasons)
                input, output = self.__train_data(prediction)
                all_input.extend(input)
                all_output.extend(output)
                all_weights.extend([self.__compute_weight(episode, predict_episode) for _ in input])

        classifier = LogisticRegression(solver="lbfgs")
        classifier.fit(np.array(all_input), np.array(all_output), np.array(all_weights))
        return classifier

    def __predict(self, predict_season: int, raw_prediction: Dict[Player, MultiLayerResult],
                  classifier: LogisticRegression) -> Dict[Player, float]:
        filtered_predictions = [(player, result.predictions) for player, result in raw_prediction.items()
                                if not result.exclusion]
        if len(filtered_predictions) <= 1:
            return dict()

        distribution = dict()
        for player in get_players_in_season(predict_season):
            distribution[player] = 0.0

        for player, features in filtered_predictions:
            features = scipy.special.logit(features)
            distribution[player] = classifier.predict_proba(np.array([features]))[0][1]
        return distribution
    
    def __train_data(self, prediction: Dict[Player, MultiLayerResult]) -> Tuple[List[np.array], List[np.array]]:
        predictions = [(player, result) for player, result in prediction.items() if not result.exclusion]
        if len(predictions) <= 1:
            return [], []
        else:
            return [scipy.special.logit(pred[1].predictions) for pred in predictions], \
                   [1.0 if get_is_mol(pred[0]) else 0.0 for pred in predictions]

    def __compute_weight(self, train_episode: int, predict_episode: int) -> float:
        if predict_episode > self.__max_distance_episode:
            if predict_episode == train_episode:
                return 1.0
            elif train_episode >= self.__max_distance_episode:
                return self.__decrease_weight
            else:
                return self.__decrease_weight ** (self.__max_distance_episode - train_episode)
        else:
            return self.__decrease_weight ** abs(predict_episode - train_episode)

class GeneralStackingLayer(NormalizeLayer):
    def __init__(self, layer: MultiLayer, decrease_weight: float, max_distance_episode: int, max_validate_episode: int):
        super().__init__(InnerGeneralStackingLayer(layer, decrease_weight, max_distance_episode, max_validate_episode))