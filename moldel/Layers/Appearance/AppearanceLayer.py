from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.Appearance.AppearanceExtractor import AppearanceExtractor
from Layers.Appearance.VideoParser import VideoParser
from Layers.MultiLayer.EmptyMultiLayer import EmptyMultiLayer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.MultiLayer.MultiplyAggregateLayer import MultiplyAggregateLayer
from Layers.Special.CutLayer import CutLayer
from scipy.stats import gaussian_kde
from statistics import mean
from typing import Dict, Set, Tuple
import numpy as np

class InnerAppearanceLayer(MultiLayer):
    # Values related to computing the cumulative distribution function and to determine the boundaries.
    MIN_VALUE = -6.0 # The lowest value used when searching for the boundaries. It is also used to compute the cdf.
    MAX_VALUE = 6.0 # The highest value used when searching for the boundaries.
    SEARCH_STEPS = 12 # In how many steps the boundary is found. The precision of the boundary is (MAX_VALUE - MIN_VALUE) / 2^(SEARCH_STEPS)

    def __init__(self, first_season: int, aug_num_cuts: int, aug_min_cuts_on: int,
                 cdf_cutoff: float, outlier_cutoff: float):
        self.__first_season = first_season
        self.__aug_num_cuts = aug_num_cuts
        self.__aug_min_cuts_on = aug_min_cuts_on
        self.__cdf_cutoff = cdf_cutoff
        self.__outlier_cutoff = outlier_cutoff

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, np.array]:
        train_seasons = {season for season in train_seasons if season >= self.__first_season}
        max_episode = self.__latest_available_episode(predict_season, latest_episode)
        if max_episode == 0 or predict_season < self.__first_season:
            return EmptyMultiLayer().predict(predict_season, latest_episode, train_seasons)

        extractor = AppearanceExtractor(predict_season, max_episode, train_seasons, self.__aug_num_cuts,
                                        self.__aug_min_cuts_on, self.__outlier_cutoff)
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

    def __training(self, extractor: AppearanceExtractor) -> Tuple[gaussian_kde, gaussian_kde]:
        """ Execute the training phase of the Appearance Layer.

        Arguments:
            extractor (AppearanceExtractor): The extractor which delivers the training data.

        Returns:
            The kernel density estimator for respectively the Mol data and non-Mol data.
        """
        train_input, train_output = extractor.get_train_data()
        non_mol_input = np.array([ti[0] for ti, to in zip(train_input, train_output) if to == 0.0])
        mol_input = np.array([ti[0] for ti, to in zip(train_input, train_output) if to == 1.0])
        non_mol_kde = self.kernel_density_estimation(non_mol_input)
        mol_kde = self.kernel_density_estimation(mol_input)
        return non_mol_kde, mol_kde

    def __prediction(self, extractor: AppearanceExtractor, non_mol_kde: gaussian_kde, mol_kde: gaussian_kde,
                     predict_season: int) -> Dict[Player, MultiLayerResult]:
        """ Execute the prediction phase of the Appearance Layer.

        Arguments:
            extractor (AppearanceExtractor): The extractor which delivers the prediction data.
            non_mol_kde (gaussian_kde): The Kernel Density Estimator for non-Mol appearance values.
            mol_kde (gaussian_kde): The Kernel Density Estimator for Mol appearance values.
            predict_season (int): For which season we make the prediction.

        Returns:
            A dictionary with as key the players that participated in the prediction season and as value a
            MultiLayerResult which contains the predictions.
        """
        all_predictions = dict()
        predict_data = extractor.get_predict_data()
        if not predict_data:
            return EmptyMultiLayer().predict(predict_season, 0, set())

        min_value = self.get_boundary(non_mol_kde, mol_kde, len(predict_data), self.__cdf_cutoff / 2, self.MIN_VALUE,
                                      self.MAX_VALUE)
        max_value = self.get_boundary(non_mol_kde, mol_kde, len(predict_data), 1 - self.__cdf_cutoff / 2, self.MIN_VALUE,
                                      self.MAX_VALUE)
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
    def kernel_density_estimation(train_input: np.array) -> gaussian_kde:
        """ Do a Kernel Density Estimation for the data.

        Arguments:
            train_input (np.array): The data on which Kernel Density Estimation is applied.

        Returns:
            The Kernel Density Estimator.
        """
        return gaussian_kde(train_input, bw_method = 'silverman')

    @classmethod
    def get_boundary(self, non_mol_kde: gaussian_kde, mol_kde: gaussian_kde, num_players: int, cdf: float,
                     lowerbound: float, upperbound: float) -> float:
        """ Get the approximated boundary value x such that the cumulative distribution function of x is equal to cdf.

        Arguments:
            non_mol_kde (gaussian_kde): The Kernel Density Estimation of the non-mol data.
            mol_kde (gaussian_kde): The Kernel Density Estimation of the mol data.
            num_players (int): The number of players still in the game.
            cdf (float): The cumulative distribution value of this x.
            lowerbound (float): The lowest value used when searching for the boundary
            upperbound (float): The highest value used when searching for the boundary.

        Returns:
            The boundary value x.
        """
        middle = (lowerbound + upperbound) / 2
        for _ in range(self.SEARCH_STEPS):
            cur_cdf = non_mol_kde.integrate_box_1d(self.MIN_VALUE, middle) * (num_players - 1) / num_players + \
                      mol_kde.integrate_box_1d(self.MIN_VALUE, middle) / num_players
            if cur_cdf < cdf:
                lowerbound = middle
            else:
                upperbound = middle
            middle = (lowerbound + upperbound) / 2
        return middle

class AppearanceLayer(CutLayer):
    """ The Appearance Layer predict which player is the Mol based on how often this player appears during the episode.
    This code is based on the project of mattijn: https://github.com/mattijn/widm """

    def __init__(self, predict_lowerbound: float, first_season: int, aug_num_cuts: int, aug_min_cuts_on: int,
                 cdf_cutoff: float, outlier_cutoff: float):
        """ Constructor of the Appearance Layer.

        Arguments:
            predict_lowerbound (float): The relative lowerbound with respect to the highest likelihood. All predictions
                with a lower likelihood than this lowerbound will be set equal to the lowerbound (after that the
                likelihoods will be normalized).
            first_season (int): The first season for which the Appearance Layer can do predictions. So on earlier
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
        super().__init__(MultiplyAggregateLayer(InnerAppearanceLayer(first_season, aug_num_cuts, aug_min_cuts_on,
                                                                     cdf_cutoff, outlier_cutoff)), mean, 1.0, predict_lowerbound)