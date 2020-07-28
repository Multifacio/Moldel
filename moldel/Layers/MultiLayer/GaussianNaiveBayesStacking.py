from Data.Player import Player
from Data.PlayerData import get_is_mol
from Layers.Layer import Layer
from Layers.MultiLayer.MultiLayer import MultiLayer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from numpy.random import RandomState
from scipy.stats import f
from sklearn.naive_bayes import GaussianNB
from typing import Dict, List, NamedTuple, Set
import numpy as np
import sys

ValidationSample = NamedTuple("ValidationSample", [("predictions", np.array), ("is_mol", bool)])
class InnerGaussianNaiveBayesStacking(Layer):
    SAMPLE_SIZE = 500

    def __init__(self, layer: MultiLayer, sampling_significance: float, random_generator: RandomState):
        self.__layer = layer
        self.__sampling_significance = sampling_significance
        self.__random_generator = random_generator

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, np.array]:
        final_predictions = self.__layer.predict(predict_season, latest_episode, train_seasons)
        if not final_predictions:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        predictions_size = max([len(prediction.predictions) for prediction in final_predictions.values() \
                                if not prediction.exclusion])
        validation_data = self.__get_validation_data(train_seasons, predictions_size)
        validation_data = self.__resample_data(validation_data, predictions_size)

        train_input = np.array([data.predictions for data in validation_data])
        train_output = np.array([1.0 if data.is_mol else 0.0 for data in validation_data])
        classifier = GaussianNB()
        classifier.fit(train_input, train_output)

        distribution = dict()
        for player, prediction in final_predictions.items():
            if prediction.exclusion:
                distribution[player] = 0.0
            else:
                predictions = np.sort(prediction.predictions)
                distribution[player] = classifier.predict_proba(np.array([predictions]))[0][1]
        return distribution

    def __get_validation_data(self, train_seasons: Set[int], predictions_size: int) -> List[ValidationSample]:
        validation_data = []
        for season in train_seasons:
            predictions = self.__layer.predict(season, sys.maxsize, train_seasons.difference({season}))
            predictions = [ValidationSample(prediction.predictions, get_is_mol(player)) for player, prediction in \
                           predictions.items() if self.__sampling_allowed(len(prediction.predictions), predictions_size)]
            validation_data.extend(predictions)
        return validation_data

    def __resample_data(self, validation_data: List[ValidationSample], prediction_size: int) -> List[ValidationSample]:
        resampled_data = []
        for data in validation_data:
            for _ in range(self.SAMPLE_SIZE):
                resample = self.__random_generator.choice(data.predictions, prediction_size, True)
                resampled_data.append(ValidationSample(np.sort(resample), data.is_mol))
        return resampled_data

    def __sampling_allowed(self, from_size: int, to_size: int) -> bool:
        if to_size <= from_size:
            return True
        elif from_size <= 2:
            return False
        else:
            f_value = self.__student_t_variance(to_size) / self.__student_t_variance(from_size)
            likelihood = f.cdf(f_value, to_size - 1, to_size - 1)
            return likelihood >= (1 - self.__sampling_significance) / 2

    def __student_t_variance(self, dof: int):
        return dof / (dof - 2)

class GaussianNaiveBayesStacking(NormalizeLayer):
    def __init__(self, layer: MultiLayer, sampling_significance: float, random_generator: RandomState):
        super().__init__(InnerGaussianNaiveBayesStacking(layer, sampling_significance, random_generator))