from bisect import bisect_left
from collections import Counter as counter
from k_means_constrained import KMeansConstrained
from numpy.random import RandomState
from Tools.Encoders.Encoder import Encoder
from typing import List
import numpy as np

class StableDiscretizer(Encoder):
    """ The Stable Discretizer is a stable version of One Hot Encoding for categorical features that deals with feature
    values that do not occur often. For this we cluster every feature individually, where every cluster must contain
    a minimum number of elements. The centers of these clusters will be used for a continuous One Hot Encoding. """

    def __init__(self, min_cluster_size: int, random_generator: RandomState):
        """ Constructor of the Stable Discretizer.

        Arguments:
            min_cluster_size (int): The minimum number of elements every cluster must have for every feature.
            random_generator (RandomState): The random generator used to generate random values.
        """
        self.__min_cluster_size = min_cluster_size
        self.__random_generator = random_generator

    def fit(self, X: np.array):
        self.bins = [self.__fit_clusters(column) for column in X.T]

    def transform(self, X: np.array) -> np.array:
        output = []
        for row in X:
            encoding = []
            for i, value in enumerate(row):
                encoding.extend(self.__transform_value(value, i))
            output.append(encoding)
        return np.array(output)

    def __transform_value(self, value: float, feature_index: int) -> List[float]:
        """ Transform a single value using stable discretization.

        Arguments:
            value (float): The value which is discretized.
            feature_index (int): The index of this feature.

        Returns:
            A list of values between 0 and 1 representing the encoding of that value.
        """
        bins = self.bins[feature_index]
        if value <= bins[0]:
            return [1] + [0 for _ in bins[1:]]
        elif value >= bins[-1]:
            return [0 for _ in bins[1:]] + [1]
        else:
            i = bisect_left(bins, value)
            ratio = (value - bins[i - 1]) / (bins[i] - bins[i - 1])
            return [0 for _ in range(i - 1)] + [1 - ratio, ratio] + [0 for _ in range(i + 1, len(bins))]

    def __fit_clusters(self, column: np.array) -> List[float]:
        """ Fit the clusters for a given feature.

        Arguments:
            column (np.array): All the values for a single feature.

        Returns:
            The cluster centers for this feature.
        """
        column = np.sort(column)
        distinct_counter = counter(column)
        max_clusters = sum(min(count, self.__min_cluster_size) for count in distinct_counter.values()) // \
                       self.__min_cluster_size
        for num_clusters in range(max_clusters, 0, -1):
            clustering = KMeansConstrained(n_clusters = num_clusters, size_min = self.__min_cluster_size,
                                           random_state = self.__random_generator)
            clusters = clustering.fit_predict(column[:, np.newaxis])
            if self.__correct_clustering(column, clusters):
                return self.__cluster_centers(column, clusters)

    def __correct_clustering(self, column: np.array, clusters: np.array) -> bool:
        """ Check if the clustering is correct.

        Arguments:
            column (np.array): All the values for a single feature sorted.
            clusters (np.array): The corresponding clusters for the column values.

        Returns:
            True if the clustering is correct, false otherwise.
        """
        previous_value = column[0]
        previous_cluster = clusters[0]
        for value, cluster in zip(column, clusters):
            if cluster != previous_cluster:
                if value == previous_value:
                    return False
                previous_cluster = cluster
                previous_value = value
        return True

    def __cluster_centers(self, column: np.array, clusters: np.array) -> List[float]:
        """ Compute all the cluster centers for the given feature given the values and corresponding clusters.

        Arguments:
            column (np.array): All the values for a single feature sorted.
            clusters (np.array): The corresponding clusters for the column values.

        Returns:
            A list of cluster centers for the given feature.
        """
        centers = []
        total = 0
        count = 0
        previous_cluster = clusters[0]
        for value, cluster in zip(column, clusters):
            if cluster != previous_cluster:
                centers.append(total / count)
                total = 0
                count = 0
                previous_cluster = cluster
            total += value
            count += 1
        centers.append(total / count)
        return centers