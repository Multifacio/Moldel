from Layers.Special.EqualLayer import EqualLayer
from Layers.Layer import Layer

class CompositeLayer(Layer):
    """ The Composite Layer combines multiple layers by taking the product of likelihoods out of each layer for every player. """

    def __init__(self, layers: list):
        """ Constructor of the Composite Layer.

        Parameters:
            layers (list): A list of layers which will be combined by the CompositeLayer into a single layer.
        """
        self.__layers = layers

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: set) -> dict:
        equal_layer = EqualLayer()
        new_distribution = equal_layer.compute_distribution(predict_season, latest_episode, train_seasons)
        for layer in self.__layers:
            layer_distribution = layer.compute_distribution(predict_season, latest_episode, train_seasons)
            for player, likelihood in new_distribution.items():
                new_distribution[player] = layer_distribution[player] * likelihood
        return new_distribution