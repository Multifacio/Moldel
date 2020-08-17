from Data.Player import Player
from Layers.Layer import Layer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from typing import Dict, List, Set
import numpy as np

class LayersIntoMulti(MultiLayer):
    """ The Layers Into Multi layer combines the results of multiple layers into 1 MultiLayer. """

    def __init__(self, layers: List[Layer]):
        """ Constructor of the Layer Into Multi class.

        Arguments:
            layers (List[Layer]): The layers which are combined into 1 MultiLayer
        """
        self.__layers = layers

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        predictions = dict()
        for layer in self.__layers:
            prediction = layer.compute_distribution(predict_season, latest_episode, train_seasons)
            for player, likelihood in prediction.items():
                predictions[player] = predictions.get(player, []) + [likelihood]

        result = dict()
        for player, likelihoods in predictions.items():
            result[player] = MultiLayerResult(np.array(likelihoods), 0.0 in likelihoods)
        return result