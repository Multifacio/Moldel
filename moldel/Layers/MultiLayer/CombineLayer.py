from Data.Player import Player
from Layers.Layer import Layer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from typing import Dict, List, Set
import numpy as np

class CombineLayer(MultiLayer):
    """ The Combine Layer combines the results of multiple layers into 1 Multi Layer. """

    def __init__(self, layers: List[Layer], normalize: bool):
        """ Constructor of the Combine Layer.

        Arguments:
            layers (List[Layer]): The layers which are combined into 1 Multi Layer.
            normalize (bool): If True then all likelihoods will be normalized over all players that are not excluded by
                any layer. If False then this won't happen.
        """
        self.__layers = layers
        self.__normalize = normalize

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        predictions = dict()
        for layer in self.__layers:
            prediction = layer.compute_distribution(predict_season, latest_episode, train_seasons)
            for player, likelihood in prediction.items():
                predictions[player] = predictions.get(player, []) + [likelihood]

        likelihood_sums = np.zeros(len(self.__layers))
        if self.__normalize:
            for player, likelihoods in predictions.items():
                if 0.0 not in likelihoods:
                    likelihood_sums += np.array(likelihoods)

        result = dict()
        for player, likelihoods in predictions.items():
            excluded = 0.0 in likelihoods
            if not self.__normalize:
                likelihoods = np.array(likelihoods)
            elif excluded:
                likelihoods = np.zeros(len(self.__layers))
            else:
                likelihoods = np.divide(np.array(likelihoods), likelihood_sums)
            result[player] = MultiLayerResult(likelihoods, excluded)

        return result