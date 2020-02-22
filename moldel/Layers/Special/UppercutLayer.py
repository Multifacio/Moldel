from Data.Player import Player
from Layers.Layer import Layer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Union, Set, Dict

class InnerUpperCutLayer(Layer):
    def __init__(self, layer: Layer, maximum_likelihood: Union[float, None]):
        self.__layer = layer
        self.__maximum_likelihood = maximum_likelihood

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        layer_distribution = self.__layer.compute_distribution(predict_season, latest_episode, train_seasons)
        maximum_likelihood = 1.0 / len(layer_distribution) if self.__maximum_likelihood is None else self.__maximum_likelihood
        new_distribution = dict()
        for player, likelihood in layer_distribution.items():
            new_distribution[player] = min(maximum_likelihood, likelihood)
        return new_distribution

class UppercutLayer(NormalizeLayer):
    """ The Uppercut Layer will limit all likelihoods higher than some given value to that value. After which the
    likelihoods get normalized. """

    def __init__(self, layer: Layer, maximum_likelihood: Union[float, None] = None):
        """ Constructor of the Uppercut Layer.

        Parameters:
            layer (Layer): The layer of which the likelihoods get cut off for too high values.
            maximum_likelihood (float): The maximum possible likelihood: all higher likelihoods will be cut off to this
            value. If this value is set to None then the uniform likelihood will be taken as maximum likelihood.
        """
        super().__init__(InnerUpperCutLayer(layer, maximum_likelihood))
