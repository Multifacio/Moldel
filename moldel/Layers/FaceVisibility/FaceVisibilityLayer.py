from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
from Layers.FaceVisibility.VideoParser import VideoParser
from Layers.MultiLayer.EmptyMultiLayer import EmptyMultiLayer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.MultiLayer.MultiplyAggregateLayer import MultiplyAggregateLayer
from Layers.Special.CutLayer import CutLayer
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KernelDensity
from sklearn.preprocessing import KBinsDiscretizer
from statistics import mean
from typing import Dict, Set, Tuple
import math
import numpy as np
import scipy as sc

class InnerFaceVisibilityLayer(MultiLayer):
    def __init__(self, dec_season_weight: float, first_season: int, max_multiplier: float):
        self.__dec_season_weight = dec_season_weight
        self.__first_season = first_season
        self.__max_multiplier = max_multiplier

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, np.array]:
        max_episode = self.__latest_available_episode(predict_season, latest_episode)
        if max_episode == 0 or predict_season < self.__first_season:
            return EmptyMultiLayer().predict(predict_season, latest_episode, train_seasons)

        extractor = FaceVisibilityExtractor(predict_season, max_episode, train_seasons, self.__dec_season_weight)
        non_mol_kde, mol_kde = self.__training(extractor)
        return self.__prediction(extractor, non_mol_kde, mol_kde, predict_season)

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

    def __training(self, extractor: FaceVisibilityExtractor) -> Tuple[KernelDensity, KernelDensity]:
        """ Execute the training phase of the Face Visibility Layer.

        Arguments:
            extractor (FaceVisibilityExtractor): The extractor which delivers the training data.

        Returns:
            The classifier model and the discretizer model (discretize data into bins).
        """
        train_input, train_output, train_weights = extractor.get_train_data()
        non_mol_input = np.array([ti[0] for ti, to in zip(train_input, train_output) if to == 0.0])
        non_mol_weights = np.array([w for w, to in zip(train_weights, train_output) if to == 0.0])
        mol_input = np.array([ti[0] for ti, to in zip(train_input, train_output) if to == 1.0])
        mol_weights = np.array([w for w, to in zip(train_weights, train_output) if to == 1.0])
        non_mol_kde = self.__kernel_density_estimation(non_mol_input, non_mol_weights, 1.0)
        mol_kde = self.__kernel_density_estimation(mol_input, mol_weights, 1.0)
        return non_mol_kde, mol_kde

    def __kernel_density_estimation(self, train_input: np.array, train_weights: np.array, multiplier: float) -> KernelDensity:
        bandwidth = self.__get_bandwidth(train_input) * multiplier
        kde = KernelDensity(bandwidth = bandwidth)
        reshaped_input = np.expand_dims(train_input, axis = 1)
        kde.fit(reshaped_input, sample_weight = train_weights)
        return kde

    @staticmethod
    def __get_bandwidth(data: np.array) -> float:
        """ Compute bandwith for kernel density estimation using the Normal reference rule. """
        return 1.06 * min(np.std(data), sc.stats.iqr(data) / 1.34) * len(data) ** (-1 / 5)

    def __prediction(self, extractor: FaceVisibilityExtractor, non_mol_kde: KernelDensity, mol_kde: KernelDensity,
                     predict_season: int) -> Dict[Player, MultiLayerResult]:
        """ Execute the prediction phase of the Face Visibility Layer.

        Arguments:
            extractor (FaceVisibilityExtractor): The extractor which delivers the prediction data.
            classifier (LogisticRegression): The trained machine learning model used to classify instances.
            discretizer (KBinsDiscretizer): The trained discretizer used to discetize the data into bins.
            predict_season (int): For which season we make the prediction.

        Returns:
            A dictionary with as key the players that participated in the prediction season and as value a
            MultiLayerResult which contains the predictions.
        """
        all_predictions = dict()
        predict_data = extractor.get_predict_data()
        if not predict_data:
            return EmptyMultiLayer().predict(predict_season, 0, set())

        min_likelihood = 1 / (len(predict_data) * self.__max_multiplier)
        max_likelihood = self.__max_multiplier / len(predict_data)
        for player in get_players_in_season(predict_season):
            if player in predict_data:
                predictions = []
                for data in predict_data[player]:
                    non_mol_likelihood = math.exp(non_mol_kde.score(np.array([data]))) * \
                                         (len(predict_data) - 1) / len(predict_data)
                    mol_likelihood = math.exp(mol_kde.score(np.array([data]))) / len(predict_data)
                    likelihood = mol_likelihood / (non_mol_likelihood + mol_likelihood)
                    likelihood = min(max(likelihood, min_likelihood), max_likelihood)
                    predictions.append(likelihood)
                all_predictions[player] = MultiLayerResult(np.array(predictions), False)
            else:
                all_predictions[player] = MultiLayerResult(np.array([]), True)

        return all_predictions

class FaceVisibilityLayer(CutLayer):
    """ The Face Visibility Layer predict which candidate is the Mol based on how often this candidate appears during
    the episode. This code is based on the project of mattijn: https://github.com/mattijn/widm """

    def __init__(self, predict_lowerbound: float, dec_season_weight: float, first_season: int, max_multiplier: float):
        """ Constructor of the Face Visibility Layer.

        Arguments:
            predict_lowerbound (float): The relative lowerbound with respect to the uniform likelihood. All predictions
                with a lower likelihood than this lowerbound will be set equal to the lowerbound (after that the
                likelihoods will be normalized).
            dec_season_weight (float): The exponential decrease in weight when the absolute difference between the train
                season and predict season becomes larger. This value is used to give closer seasons a higher weight and
                0.0 < dec_season_weight <= 1.0 should hold. If dec_season_weight is larger then seasons further away
                will have more influence on the prediction.
            first_season (int): The first season for which the Face Visibility Layer can do predictions. So on earlier
                seasons it will give an uniform prediction back. Note however that earlier seasons are still used as
                training data.
            cdf_cutoff (float)
        """
        super().__init__(MultiplyAggregateLayer(InnerFaceVisibilityLayer(dec_season_weight, first_season, max_multiplier)),
                         mean, 1.0, predict_lowerbound)