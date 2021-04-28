from Tools.Encoders.Encoder import Encoder
from numpy.random import RandomState
from sklearn.cluster import KMeans
from sklearn.preprocessing import QuantileTransformer
from typing import List, NamedTuple, Set
import numpy as np

Setting = NamedTuple("Setting", [("num_clusters", int), ("ignore_values", Set[float])])
IgnoredBound = NamedTuple("IgnoredBound", [("lower_bound", float), ("lower_rank", float), ("upper_bound", float),
                                           ("upper_rank", float)])
class SemiRankTransformer(Encoder):
    """ Semi-Rank Transformer applies a rank transformation individually per feature at some regions and linear
    interpolates ranks at other regions individually per feature. """

    def __init__(self, settings: List[Setting], random_generator: RandomState):
        """ Constructor of the Semi Rank Transformer.

        Arguments:
            settings (List[Setting]): A list of settings, where each setting represents how many clusters should be
                used per feature and which clusters containing a particular value should not be rank transformed.
            random_generator (RandomState): The Random State used for the KMeans procedure.
        """
        self.__settings = settings
        self.__random_generator = random_generator

    def fit(self, X: np.array):
        self.__fit_rank_transformers(X)
        self.__fit_clusters(X)
        self.__fit_ignored_bounds(X)

    def transform(self, X: np.array):
        Y = []
        for feature_index, column in enumerate(X.T):
            Y.append([self.__transform_value(value, feature_index) for value in column])
        return np.array(Y).T

    def __transform_value(self, value: float, feature_index: int) -> float:
        """ Semi-Rank Transform a single value.

        Arguments:
            value (float): The value that is Semi-Rank transformed.
            feature_index (int): The index of the feature column which contained this value.

        Returns:
            The Semi-Rank Transformed value.
        """
        cluster = self.clusterings[feature_index].predict(np.array([[value]]))[0]
        if cluster in self.ignored_bounds[feature_index]:
            lowerbound, lowerrank, upperbound, upperrank = self.ignored_bounds[feature_index][cluster]
            value = min(max(value, lowerbound), upperbound)
            return (upperrank - lowerrank) * (value - lowerbound) / (upperbound - lowerbound)
        else:
            return self.rank_transformers[feature_index].transform(np.array([[value]]))[0][0]

    def __fit_rank_transformers(self, X: np.array):
        """ Fit all the rank transformers for every feature.

        Arguments:
            X (np.array): The train input used to train the rank transformers.
        """
        self.rank_transformers = []
        for column, setting in zip(X.T, self.__settings):
            column = column[:, np.newaxis]
            rank_transformer = QuantileTransformer(n_quantiles = len(column))
            rank_transformer.fit(column)
            self.rank_transformers.append(rank_transformer)

    def __fit_clusters(self, X: np.array):
        """ Fit all the KMeans clusters for every feature.

        Arguments:
            X (np.array): The train input used to train the KMeans clusters.
        """
        self.clusterings = []
        for column, setting in zip(X.T, self.__settings):
            column = column[:, np.newaxis]
            clustering = KMeans(n_clusters = setting.num_clusters, random_state = self.__random_generator)
            clustering.fit(column)
            self.clusterings.append(clustering)

    def __fit_ignored_bounds(self, X: np.array):
        """ For every ignored cluster for every feature determine the lowest & highest rank and the lowest & highest
        value belonging to that cluster.

        Arguments:
            X (np.array): The train input used.
        """
        self.ignored_bounds = []
        for column, setting, rank_transformer, clustering in zip(X.T, self.__settings, self.rank_transformers,
                                                                    self.clusterings):
            column = column[:, np.newaxis]
            # Clusters are not numbered in chronological order by the KMeans library in sklearn, so we use a cluster
            # order mapping that maps chronological numbers to the corresponding cluster.
            cluster_order = {center: i for i, center in enumerate(clustering.cluster_centers_[:,0])}
            splits = np.sort(clustering.cluster_centers_, axis = 0)
            cluster_order = {cluster_order[center]: i for i, center in enumerate(splits[:,0])}
            splits = np.array([(c1[0] + c2[0]) / 2 for c1, c2 in zip(splits, splits[1:])])
            splits = np.concatenate((np.array([np.min(column)]), splits, np.array([np.max(column)])))
            self.rank_splits = rank_transformer.transform(splits[:,np.newaxis])
            ignored_clusters = {clustering.predict(np.array([[value]]))[0] for value in setting.ignore_values}
            ignored_bounds = {c: IgnoredBound(splits[cluster_order[c]], self.rank_splits[cluster_order[c]][0],
                splits[cluster_order[c] + 1], self.rank_splits[cluster_order[c] + 1][0]) for c in ignored_clusters}
            self.ignored_bounds.append(ignored_bounds)