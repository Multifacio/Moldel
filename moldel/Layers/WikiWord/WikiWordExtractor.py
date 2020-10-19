from Data.Player import Player
from Data.PlayerData import get_is_mol
from Layers.WikiWord.WikiWordParser import WikiWordSample, WikiWordParser
from numpy.random import RandomState
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import KBinsDiscretizer
from typing import Dict, Set, Tuple
import numpy as np

class WikiWordExtractor:
    """ The Wiki Word Extractor transforms an array of features in a new array of features which can be used by the
    classification algorithm. """

    # How often a Gaussian Mixture model is tried to fit through the data (from which the best result is taken).
    # Putting this value higher will make the results more stable, however it will decrease the running time.
    GAUSSIAN_MIXTURE_ATTEMPTS = 8

    # Up to which degree the total number of words is polynomial transformed.
    WORD_COUNT_POLY_DEGREE = 2

    def __init__(self, predict_season: int, train_seasons: Set[int], pca_components: int, random_generator: RandomState):
        """ Constructor of the Wiki Word Extractor.

        Arguments:
            predict_season (int): The season for which we make the prediction.
            train_seasons (Set[int]): The seasons which are used as train data.
            pca_components (int): The number of PCA components extracted from the job features before LDA is applied.
            random_generator (RandomState): The random generator used to generate random values.
        """
        self.__predict_season = predict_season
        self.__train_seasons = train_seasons
        self.__pca_components = pca_components
        self.__random_generator = random_generator

    def get_train_data(self) -> Tuple[np.array, np.array]:
        """ Get all formatted train data useable for the machine learning algorithms to do training.

        Returns:
            The train input and train output. The train input is a 2d array where each row represents a different train
            element. The train output is 1d array of labels, where a 1 means that this player was the 'Mol' and a 0
            means that this player was not the 'Mol'.
        """
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
        train_input = self.__lda.fit_transform(train_input, train_output)
        return train_input, train_output

    def get_predict_data(self) -> Dict[Player, np.array]:
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
        return predict_data

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