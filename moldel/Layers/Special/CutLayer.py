from Data.Player import Player
from Layers.Layer import Layer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Callable, Dict, List, Set
import math

class InnerCutLayer(Layer):
    def __init__(self, layer: Layer, aggregate: Callable[[List[float]], float], upperbound: float, lowerbound: float):
        self.__layer = layer
        self.__aggregate = aggregate
        self.__upperbound = upperbound
        self.__lowerbound = lowerbound

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        layer_distribution = self.__layer.compute_distribution(predict_season, latest_episode, train_seasons)
        likelihoods = [likelihood for likelihood in layer_distribution.values() if likelihood > 0.0]
        aggregation = self.__aggregate(likelihoods)
        min_likelihood = self.__lowerbound * aggregation
        max_likelihood = self.__upperbound * aggregation
        new_distribution = dict()
        for player, likelihood in layer_distribution.items():
            if likelihood > 0.0:
                new_distribution[player] = min(max(likelihood, min_likelihood), max_likelihood)
            else:
                new_distribution[player] = 0.0
        return new_distribution

class CutLayer(NormalizeLayer):
    """ The Cut Layer will limit all likelihoods to a certain interval based on the uniform likelihood (which is the
    likelihood if all participants with a non-zero likelihood get an equal likelihood). After this transformation the
    likelihoods get normalized. """

    def __init__(self, layer: Layer, aggregate: Callable[[List[float]], float], upperbound: float = math.inf,
                 lowerbound: float = 0.0):
        """ Constructor of the Uppercut Layer.

        Parameters:
            layer (Layer): The layer of which the likelihoods get cut off for too low and high values.
            aggregate (Callable[[List[float]], float]): The aggregate function that produces the aggregation result
                based on the given likelihoods.
            upperbound (float): The relative upperbound with respect to the aggregation result.
            lowerbound (float): The relative lowerbound with respect to the aggregation result.
        """
        super().__init__(InnerCutLayer(NormalizeLayer(layer), aggregate, upperbound, lowerbound))
