from sklearn.decomposition import PCA

from Data.Player import Player
from Data.PlayerData import get_is_mol
from Data.WikiWord.Job import Job
from Layers.WikiWord.WikiWordParser import WikiWordParser
from sklearn.mixture import GaussianMixture
from typing import Dict, List, NamedTuple, Set, Tuple, Union
import math
import numpy as np

TrainSample = NamedTuple("TrainSample", [("job_frequency", Union[Dict[Job, float], List[float]]),
                                         ("number_words", List[float]), ("is_mol", Union[bool, None])])
class WikiWordExtractor:
    """ The Wiki Word Extractor excludes and transforms features into a array of floats which can be used by the
    classification algorithm. """

    # How often a Gaussian Mixture model is tried to fit through the data (from which the best result is taken).
    # Putting this value higher will make the results more stable, however it will decrease the running time.
    GAUSSIAN_MIXTURE_ATTEMPTS = 8

    def __init__(self, predict_season: int, train_seasons: Set[int], pca_components: int, minimum_log: float,
                 degree_total_count: int):
        """ Constructor of the Wiki Word Extractor.

        Arguments:
            predict_season (int): The season for which we make the prediction.
            train_seasons (Set[int]): The seasons which are used as train data.
            pca_components (int): How many PCA components should be extracted from the job counts as features.
            minimum_log (float): The lower bound on the job count and total count before applying a logarithm.
            degree_total_count (int): Up to which degree a polynomial transformation should be applied on the log
                of the total word count.
        """
        self.__predict_season = predict_season
        self.__train_seasons = train_seasons
        self.__pca_components = pca_components
        self.__minimum_log = minimum_log
        self.__degree_total_count = degree_total_count

    def get_train_data(self) -> Tuple[np.array, np.array]:
        """ Get the formatted train data useable for machine learning algorithms.

        Returns:
            A 2d array which represents the train input where each row represents a different train element. And this
            function also returns a 1d array which represents the train output. The ith row of the train input
            corresponds to the ith element of the train output.
        """
        raw_data = WikiWordParser.parse(self.__train_seasons)
        train_data = [TrainSample(data.job_frequency, [data.number_words], get_is_mol(player)) for player, data in
                      raw_data.items()]
        train_data = [self.__transform_number_words(data) for data in train_data]
        train_data = [self.__transform_job_frequency(data) for data in train_data]
        self.__train_job_clusters(train_data)
        train_data = [self.__discretize_jobs(data) for data in train_data]
        self.__train_job_pca(train_data)
        train_data = [self.__apply_job_pca(data) for data in train_data]
        return np.array([data.job_frequency + data.number_words for data in train_data]), \
               np.array([1.0 if data.is_mol else 0.0 for data in train_data])

    def get_predict_data(self) -> Dict[Player, List[np.array]]:
        """ Get all formatted predict data useable for the machine learning algorithms to do a prediction.

        Returns:
            A dictionary with as key the players that are still present in the predict episode and as value a list of
            the predict input for every episode up to (and including) the predict episode.
        """
        raw_data = WikiWordParser.parse({self.__predict_season})
        predict_data = {player: TrainSample(data.job_frequency, [data.number_words], None)
                        for player, data in raw_data.items()}
        predict_data = {player: self.__transform_number_words(data) for player, data in predict_data.items()}
        predict_data = {player: self.__transform_job_frequency(data) for player, data in predict_data.items()}
        predict_data = {player: self.__discretize_jobs(data) for player, data in predict_data.items()}
        predict_data = {player: self.__apply_job_pca(data) for player, data in predict_data.items()}
        return {player: np.array([data.job_frequency + data.number_words]) for player, data in predict_data.items()}

    def __transform_number_words(self, data: TrainSample) -> TrainSample:
        """ Transform the number of word feature of a TrainSample using logarithmic transformation and polynomial
        transformation.

        Arguments:
            A TrainSample which will be transformed.

        Returns:
            The transformed TrainSample
        """
        total_count = math.log(max(data.number_words[0], self.__minimum_log))
        poly_transform = [total_count ** i for i in range(1, self.__degree_total_count + 1)]
        return TrainSample(data.job_frequency, poly_transform, data.is_mol)

    def __transform_job_frequency(self, data: TrainSample) -> TrainSample:
        """ Transform the job frequencies features of a TrainSample using logarithmic transformation.

        Arguments:
            A TrainSample which will be transformed.

        Returns:
            The transformed TrainSample
        """
        job_frequencies = {job: math.log(max(frequency, self.__minimum_log)) for job, frequency in
                           data.job_frequency.items()}
        return TrainSample(job_frequencies, data.number_words, data.is_mol)

    def __train_job_clusters(self, train_data: List[TrainSample]):
        """ Train the Gaussian Mixture clustering for classifying the jobs.

        Arguments:
            All TrainSamples used for training the Gaussian Mixture clustering.
        """
        self.__clusters = dict()
        for job in Job:
            job_frequencies = np.array([[data.job_frequency[job]] for data in train_data])
            cluster = GaussianMixture(n_components = 2, covariance_type = "full", n_init = self.GAUSSIAN_MIXTURE_ATTEMPTS)
            cluster.fit(job_frequencies)
            self.__clusters[job] = cluster

    def __discretize_jobs(self, data: TrainSample) -> TrainSample:
        """ Discretize the jobs counts of a TrainSample into 0/1 features by checking to which cluster they belong.

        Arguments:
            A TrainSample which will be transformed.

        Returns:
            The transformed TrainSample
        """
        job_frequencies = {job: self.__clusters[job].predict(np.array([[frequency]]))[0] for job, frequency in
                           data.job_frequency.items()}
        return TrainSample(job_frequencies, data.number_words, data.is_mol)

    def __train_job_pca(self, train_data: List[TrainSample]):
        """ Train the principal component analysis used to extract features from the job features.

        Arguments:
            All TrainSamples used for training the principal component analysis.
        """
        all_data = np.array([[data.job_frequency[job] for job in Job] for data in train_data])
        self.__pca = PCA(n_components = self.__pca_components)
        self.__pca.fit(all_data)

    def __apply_job_pca(self, data: TrainSample) -> TrainSample:
        """ Transform the jobs counts of a TrainSample by reducing the features using principal component analysis.

        Arguments:
            A TrainSample which will be transformed.

        Returns:
            The transformed TrainSample
        """
        job_frequencies = self.__pca.transform(np.array([[data.job_frequency[job] for job in Job]]))[0]
        return TrainSample(job_frequencies.tolist(), data.number_words, data.is_mol)
