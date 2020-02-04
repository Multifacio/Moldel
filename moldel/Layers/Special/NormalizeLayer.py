from Data.Player import Player
from Layers.Layer import Layer
from typing import Dict, Set

class NormalizeLayer(Layer):
    """ The Normalize Layer will scale every likelihood by the same constant such that all likelihoods sum up to 1. """

    def __init__(self, layer: Layer):
        """ Constructor of the Normalize Layer.

        Parameters:
            layer (Layer): The layer of which all likelihoods will be transformed to sum up to 1.
        """
        self.__layer = layer

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        layer_distribution = self.__layer.compute_distribution(predict_season, latest_episode, train_seasons)
        new_distribution = dict()
        likelihood_sum = sum(layer_distribution.values())
        for player, likelihood in layer_distribution.items():
            new_distribution[player] = likelihood / likelihood_sum
        return new_distribution