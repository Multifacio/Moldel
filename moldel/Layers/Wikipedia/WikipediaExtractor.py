from sklearn.preprocessing import QuantileTransformer

from Data.Player import Player
from Data.PlayerData import get_is_mol, get_season
from Layers.Wikipedia.WikipediaParser import WikipediaParser, WikipediaSample
from numpy.random import RandomState
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.mixture import GaussianMixture
from typing import Dict, Set, Tuple
import numpy as np
import scipy as sc

class WikipediaExtractor:
    """ The Wikipedia Extractor transforms an array of features in a new array of features which can be used by the
    classification algorithm. """

    def __init__(self, predict_season: int, train_seasons: Set[int]):
        """ Constructor of the Wikipedia Extractor.

        Arguments:
            predict_season (int): The season for which we make the prediction.
            train_seasons (Set[int]): The seasons which are used as train data.
        """
        self.__predict_season = predict_season
        self.__train_seasons = train_seasons

    def get_train_data(self):
        """ Execute the training process for the Wikipedia Extractor.

        Returns:
            The preprocessed training input, the corresponding labels and the feature weights.
        """
        raw_train_data = WikipediaParser.parse(self.__train_seasons)
        train_output = np.array([1.0 if get_is_mol(player) else 0.0 for player in raw_train_data])
        job_input = np.array([data.job_features for data in raw_train_data.values()])
        self.__pca = PCA()
        job_input = self.__pca.fit_transform(job_input)
        word_input = np.array([[data.word_feature] for data in raw_train_data.values()])
        train_input = np.concatenate((job_input, word_input), axis = 1)
        self.__rank_transformer = QuantileTransformer(n_quantiles = len(train_input))
        train_input = self.__rank_transformer.fit_transform(train_input)
        return train_input, train_output, np.concatenate((self.__pca.explained_variance_ratio_, [1]))

    def get_predict_data(self) -> Dict[Player, np.array]:
        """ Get all formatted predict data useable for the machine learning algorithms to do a prediction.

        Returns:
            A dictionary with as key the players of that season and as value the formatted predict input.
        """
        raw_predict_data = WikipediaParser.parse({self.__predict_season})
        predict_data = dict()
        for player, data in raw_predict_data.items():
            job_input = np.array([data.job_features])
            job_input = self.__pca.transform(job_input)
            word_input = np.array([[data.word_feature]])
            predict_input = np.concatenate((job_input, word_input), axis = 1)
            predict_data[player] =  self.__rank_transformer.transform(predict_input)[0]

        return predict_data