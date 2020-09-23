from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
from Layers.FaceVisibility.VideoParser import VideoParser
from Layers.MultiLayer.EmptyMultiLayer import EmptyMultiLayer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.MultiLayer.MultiplyAggregateLayer import MultiplyAggregateLayer
from Layers.Special.CutLayer import CutLayer
from scipy.stats import gaussian_kde
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import KBinsDiscretizer
from typing import Dict, Set, Tuple
import math
import numpy as np
import scipy as sc

class InnerFaceVisibilityLayer(MultiLayer):
    # Values related to computing the cumulative distribution function and to determine the boundaries.
    MIN_VALUE = -6.0 # The lowest value used when searching for the boundaries. It is also used to compute the cdf.
    MAX_VALUE = 6.0 # The highest value used when searching for the boundaries.
    SEARCH_STEPS = 12 # In how many steps the boundary is found. The precision of the boundary is (MAX_VALUE - MIN_VALUE) / 2^(SEARCH_STEPS)

    def __init__(self, dec_season_weight: float, first_season: int, aug_num_cuts: int, aug_min_cuts_on: int,
                 cdf_cutoff: float, outlier_cutoff: float):
        self.__dec_season_weight = dec_season_weight
        self.__first_season = first_season
        self.__aug_num_cuts = aug_num_cuts
        self.__aug_min_cuts_on = aug_min_cuts_on
        self.__cdf_cutoff = cdf_cutoff
        self.__outlier_cutoff = outlier_cutoff

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, np.array]:
        max_episode = self.__latest_available_episode(predict_season, latest_episode)
        if max_episode == 0 or predict_season < self.__first_season:
            return EmptyMultiLayer().predict(predict_season, latest_episode, train_seasons)

        extractor = FaceVisibilityExtractor(predict_season, max_episode, train_seasons, self.__dec_season_weight,
                        self.__aug_num_cuts, self.__aug_min_cuts_on, self.__outlier_cutoff)
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

    def __training(self, extractor: FaceVisibilityExtractor) -> Tuple[gaussian_kde, gaussian_kde]:
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
        non_mol_kde = self.kernel_density_estimation(non_mol_input, non_mol_weights)
        mol_kde = self.kernel_density_estimation(mol_input, mol_weights)
        return non_mol_kde, mol_kde

    def __prediction(self, extractor: FaceVisibilityExtractor, non_mol_kde: gaussian_kde, mol_kde: gaussian_kde,
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

        min_value = min(self.get_boundary(non_mol_kde, self.__cdf_cutoff / 2), self.get_boundary(mol_kde, self.__cdf_cutoff / 2))
        max_value = max(self.get_boundary(non_mol_kde, 1 - self.__cdf_cutoff / 2), self.get_boundary(mol_kde, 1 - self.__cdf_cutoff / 2))
        for player in get_players_in_season(predict_season):
            if player in predict_data:
                predictions = []
                for data in predict_data[player]:
                    data = min(max(data, min_value), max_value)
                    non_mol_likelihood = non_mol_kde.pdf(data)[0] * (len(predict_data) - 1) / len(predict_data)
                    mol_likelihood = mol_kde.pdf(data)[0] / len(predict_data)
                    likelihood = mol_likelihood / (non_mol_likelihood + mol_likelihood)
                    predictions.append(likelihood)
                all_predictions[player] = MultiLayerResult(np.array(predictions), False)
            else:
                all_predictions[player] = MultiLayerResult(np.array([]), True)

        return all_predictions

    @staticmethod
    def kernel_density_estimation(train_input: np.array, train_weights: np.array) -> gaussian_kde:
        """ Do a Kernel Density Estimation for the data.

        Arguments:
            train_input (np.array): The data on which Kernel Density Estimation is applied.
            train_weights (np.array): The weights for all train input, which corresponds elementwise to the train_input.

        Returns:
            The bandwidth used for the Kernel Density Estimation.
        """
        bandwidth = InnerFaceVisibilityLayer.__get_bandwidth(train_input)
        return gaussian_kde(train_input, bandwidth, train_weights)

    @staticmethod
    def __get_bandwidth(data: np.array) -> float:
        """ Compute bandwidth for kernel density estimation using the Normal reference rule.

        Arguments:
            data (np.array): The data on which Kernel Density Estimation is applied

        Returns:
            The bandwidth used for the Kernel Density Estimation.
        """
        return 1.06 * min(np.std(data), sc.stats.iqr(data) / 1.34) * len(data) ** (-1 / 5)

    @classmethod
    def get_boundary(self, kde: gaussian_kde, cdf: float) -> Tuple[float, float]:
        """ Get the approximated boundary value x such that the cumulative distribution function of x is equal to cdf.

        Arguments:
            kde (gaussian_kde): The Kernel Density Estimation of the data
            cdf (float): The cumulative distribution value of this x.

        Returns:
            The boundary value x.
        """
        lowerbound = self.MIN_VALUE
        upperbound = self.MAX_VALUE
        middle = (lowerbound + upperbound) / 2
        for _ in range(self.SEARCH_STEPS):
            cur_cdf = kde.integrate_box_1d(self.MIN_VALUE, middle)
            if cur_cdf < cdf:
                lowerbound = middle
            else:
                upperbound = middle
            middle = (lowerbound + upperbound) / 2
        return middle

class FaceVisibilityLayer(CutLayer):
    """ The Face Visibility Layer predict which player is the Mol based on how often this player appears during
    the episode. This code is based on the project of mattijn: https://github.com/mattijn/widm """

    def __init__(self, predict_lowerbound: float, dec_season_weight: float, first_season: int, aug_num_cuts: int,
                 aug_min_cuts_on: int, cdf_cutoff: float, outlier_cutoff: float):
        """ Constructor of the Face Visibility Layer.

        Arguments:
            predict_lowerbound (float): The relative lowerbound with respect to the highest likelihood. All predictions
                with a lower likelihood than this lowerbound will be set equal to the lowerbound (after that the
                likelihoods will be normalized).
            dec_season_weight (float): The exponential decrease in weight when the absolute difference between the train
                season and predict season becomes larger. This value is used to give closer seasons a higher weight and
                0.0 < dec_season_weight <= 1.0 should hold. If dec_season_weight is larger then seasons further away
                will have more influence on the prediction.
            first_season (int): The first season for which the Face Visibility Layer can do predictions. So on earlier
                seasons it will give an uniform prediction back. Note however that earlier seasons are still used as
                training data.
            aug_num_cuts (int): In how many cuts the episodes get divided. All cuts are turned on/off, where the
                appearance value is computed over only the cuts that are turned on. This is done to create more data.
            aug_min_cuts_on (int): How many cuts should be turned on at least.
            cdf_cutoff (float): This is the total cumulative density which is cutoff from both sides of the
                distributions (mol and non-mol distribution). All appearance values that lie in the cutoff zone of both
                distributions are changed to the closest value that lies in the range of at least one of the
                distributions.
            outlier_cutoff (float): This is the relative amount of highest and lowest appearance values that get removed.
        """
        super().__init__(MultiplyAggregateLayer(InnerFaceVisibilityLayer(dec_season_weight, first_season, aug_num_cuts,
                        aug_min_cuts_on, cdf_cutoff, outlier_cutoff)), max, 1.0, predict_lowerbound)