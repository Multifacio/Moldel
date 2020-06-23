from Data.Player import Player
from Layers.Layer import Layer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Dict, Set
import math

class InnerCutLayer(Layer):
    def __init__(self, layer: Layer, upperbound: float, lowerbound: float):
        self.__layer = layer
        self.__upperbound = upperbound
        self.__lowerbound = lowerbound

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        layer_distribution = self.__layer.compute_distribution(predict_season, latest_episode, train_seasons)
        uniform_likelihood = 1.0 / sum(likelihood > 0.0 for likelihood in layer_distribution.values())
        min_likelihood = self.__lowerbound * uniform_likelihood
        max_likelihood = self.__upperbound * uniform_likelihood
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

    def __init__(self, layer: Layer, upperbound: float = math.inf,  lowerbound: float = 0.0):
        """ Constructor of the Uppercut Layer.

        Parameters:
            layer (Layer): The layer of which the likelihoods get cut off for too low and high values.
            upperbound (float): The relative upperbound with respect to the uniform likelihood.
            lowerbound (float): The relative lowerbound with respect to the uniform likelihood.
        """
        super().__init__(InnerCutLayer(NormalizeLayer(layer), upperbound, lowerbound))
