from jenkspy import JenksNaturalBreaks

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
        """
        self.__settings = settings

    def fit(self, X: np.array):
        self.__fit_rank_transformers(X)
        self.__fit_clusters(X)

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
        cluster = int(self.clusterings[feature_index].predict(value))
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
        """ Fit all the clusters for every feature and determine the lowest value & rank and highest value & rank for
        each cluster.

        Arguments:
            X (np.array): The train input used to train the clusters.
        """
        self.clusterings = []
        self.ignored_bounds = []
        for column, setting, rank_transformer in zip(X.T, self.__settings, self.rank_transformers):
            print(column)
            clustering = JenksNaturalBreaks(nb_class = setting.num_clusters)
            clustering.fit(column)
            self.clusterings.append(clustering)
            self.rank_splits = rank_transformer.transform(np.array(clustering.breaks_)[:, np.newaxis])
            ignored_clusters = {int(clustering.predict(value)) for value in setting.ignore_values}
            ignored_bounds = {c: IgnoredBound(clustering.breaks_[c], self.rank_splits[c][0], clustering.breaks_[c + 1],
                                              self.rank_splits[c + 1][0]) for c in ignored_clusters}
            self.ignored_bounds.append(ignored_bounds)