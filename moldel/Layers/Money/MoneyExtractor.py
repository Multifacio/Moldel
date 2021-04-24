from Data.MoneyData.Earnings.All import MONEY_DATA
from Data.Player import Player
from Data.PlayerData import get_is_mol
from Layers.Money.MoneyEncoder import MoneyEncoder
from numpy.random import RandomState
from sklearn.decomposition import PCA
from typing import List, Set, Tuple, Dict
import math
import numpy as np

class MoneyExtractor:
    """ The Money Extractor deals with obtaining the train data and predict data for the Money Layer. """

    def __init__(self, predict_season: int, predict_episode: int, train_seasons: Set[int], pca_explain: float,
                 spline_clusters: int, num_other_money_quantiles: int, random_generator: RandomState):
        """ Constructor of the Money Extractor

        Arguments:
            predict_season (int): The season for which we make the prediction.
            predict_episode (int): The latest episode in the predict season that could be used.
            train_seasons (Set[int]): The seasons which are used as train data.
            pca_explain (float): PCA will select the least number of components that at least explain this amount
                of variance in the features.
            spline_clusters (int): The number of KMeans clusters used in the Semi Rank Transformation and in the
                Spline Encoding to estimate how likely a player is the Mol based on how many money that player earned.
            num_other_likelihood_quantiles (int): The number of quantiles used to extract features from the likelihoods
                based on what others earn.
            random_generator (RandomState): The random generator used to generate random values.
        """
        self.__predict_season = predict_season
        self.__predict_episode = predict_episode
        self.__train_seasons = train_seasons
        self.__pca_explain = pca_explain
        self.__spline_clusters = spline_clusters
        self.__num_other_money_quantiles = num_other_money_quantiles
        self.__random_generator = random_generator

    def get_train_data(self) -> Tuple[np.array, np.array]:
        """ Get the train data useable for machine learning algorithms.

        Returns:
            The train input and train output. The train input is a 2d array where each row represents a different train
            element. The train output is 1d array of labels, where a 1 means that this player was the 'Mol' and a 0
            means that this player was not the 'Mol'.
        """
        self.__encoder = MoneyEncoder(self.__spline_clusters, self.__num_other_money_quantiles, self.__random_generator)
        samples = self.__encoder.get_money_samples(self.__train_seasons, math.inf)
        self.__major_pattern = self.__encoder.major_money_pattern(samples)
        self.__minor_pattern = self.__encoder.minor_money_pattern(samples)
        train_input = np.array([self.__encoder.extract_features(sample, self.__major_pattern, self.__minor_pattern)
                                for sample in samples])
        train_output = np.array([1.0 if get_is_mol(sample.player) else 0.0 for sample in samples])

        self.__pca = PCA(n_components = self.__pca_explain)
        train_input = self.__pca.fit_transform(train_input)
        return train_input, train_output

    def get_predict_data(self) -> Dict[Player, List[np.array]]:
        """ Get all formatted predict data useable for the machine learning algorithms to do a prediction.

        Returns:
            A dictionary with as key a player and as value a list of all feature rows associated to that player.
        """
        samples = self.__encoder.get_money_samples({self.__predict_season}, self.__predict_episode)
        predict_input = np.array([self.__encoder.extract_features(sample, self.__major_pattern, self.__minor_pattern)
                                for sample in samples])
        predict_input = self.__pca.transform(predict_input)

        alive_players = MONEY_DATA[self.__predict_season].get_alive(self.__predict_episode)
        predict_data = dict()
        for row, sample in zip(predict_input, samples):
            if sample.player in alive_players:
                predict_data[sample.player] = predict_data.get(sample.player, []) + [row]
        return predict_data

