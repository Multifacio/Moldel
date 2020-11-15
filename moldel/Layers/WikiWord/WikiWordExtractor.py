from Data.Player import Player
from Data.PlayerData import get_is_mol, get_season
from Layers.WikiWord.WikiWordParser import WikiWordParser, WikiWordSample
from numpy.random import RandomState
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.mixture import GaussianMixture
from typing import Dict, Set, Tuple
import numpy as np
import scipy as sc

class WikiWordExtractor:
    """ The Wiki Word Extractor transforms an array of features in a new array of features which can be used by the
    classification algorithm. """

    # How often a Gaussian Mixture model is tried to fit through the data (from which the best result is taken).
    # Putting this value higher will make the results more stable, however it will decrease the running time.
    GAUSSIAN_MIXTURE_ATTEMPTS = 8

    # Up to which degree the total number of words is polynomial transformed.
    WORD_COUNT_POLY_DEGREE = 2

    def __init__(self, predict_season: int, train_seasons: Set[int], pca_components: int, unlikely_z_score: float,
                 random_generator: RandomState):
        """ Constructor of the Wiki Word Extractor.

        Arguments:
            predict_season (int): The season for which we make the prediction.
            train_seasons (Set[int]): The seasons which are used as train data.
            pca_components (int): The number of PCA components extracted from the job features before LDA is applied.
            unlikely_z_score (float): All players with a lower z-score than this value get a lower likelihood assigned.
            random_generator (RandomState): The random generator used to generate random values.
        """
        self.__predict_season = predict_season
        self.__train_seasons = train_seasons
        self.__pca_components = pca_components
        self.__unlikely_z_score = unlikely_z_score
        self.__random_generator = random_generator

    def train(self):
        """ Execute the training process for the WikiWord Extractor. """
        raw_train_data = WikiWordParser.parse(self.__train_seasons)
        train_output = np.array([1.0 if get_is_mol(player) else 0.0 for player in raw_train_data])
        job_input = np.array([data.job_features for data in raw_train_data.values()])
        self.__train_job_clusters(job_input)
        job_input = self.__discretize_jobs(job_input)
        self.__pca = PCA(n_components = self.__pca_components)
        job_input = self.__pca.fit_transform(job_input)
        word_input = np.array([[data.word_feature ** i for i in range(1, self.WORD_COUNT_POLY_DEGREE + 1)]
                               for data in raw_train_data.values()])
        train_input = np.concatenate((job_input, word_input), axis = 1)
        self.__lda = LinearDiscriminantAnalysis()
        self.__lda.fit(train_input, train_output)

    def get_predict_data(self) -> Dict[Player, bool]:
        """ Get all formatted predict data useable for the machine learning algorithms to do a prediction.

        Returns:
            A dictionary with as key the players of that season and as value the formatted predict input.
        """
        raw_predict_data = WikiWordParser.parse({self.__predict_season})
        predict_data = dict()
        for player, data in raw_predict_data.items():
            job_input = self.__discretize_jobs(np.array([data.job_features]))
            job_input = self.__pca.transform(job_input)
            word_input = np.array([[data.word_feature ** i for i in range(1, self.WORD_COUNT_POLY_DEGREE + 1)]])
            predict_input = np.concatenate((job_input, word_input), axis = 1)
            predict_input = self.__lda.transform(predict_input)
            predict_data[player] = predict_input[0]

        z_scores = sc.stats.zscore([data for data in predict_data.values()])
        return {player: z_score < self.__unlikely_z_score for player, z_score in zip(predict_data.keys(), z_scores)}

    def __train_job_clusters(self, job_input: np.array):
        """ Train the Gaussian Mixture clustering for classifying the jobs.

        Arguments:
            job_input (np.array): All job features of all train players.
        """
        self.__clusters = []
        for column in job_input.T:
            cluster = GaussianMixture(n_components = 2, covariance_type = "full", n_init = self.GAUSSIAN_MIXTURE_ATTEMPTS,
                                      random_state = self.__random_generator)
            cluster.fit(np.expand_dims(column, axis = 1))
            self.__clusters.append(cluster)

    def __discretize_jobs(self, job_input: np.array) -> np.array:
        """ Discretize the job input into 0/1 features by checking to which cluster they belong.

        Arguments:
            job_input (np.array): All job features of all train players.

        Returns:
            The transformed job input.
        """
        transformed_input = []
        for cluster, column in zip(self.__clusters, job_input.T):
            transformed_input.append(cluster.predict(np.expand_dims(column, axis = 1)))
        return np.array(transformed_input).T