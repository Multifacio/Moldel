from Data.Player import Player
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from typing import Dict, Set
import numpy as np

class NormalizeMultiLayer(MultiLayer):
    """ The Normalize Layer will scale every likelihood by the same constant for each prediction such that the
    likelihoods sum up to 1 for each prediction. This layer can only be used if the likelihoods for each player
    corresponds index-wise to each other. """

    def __init__(self, layer: MultiLayer):
        """ Constructor of the Normalize Multi Layer.

        Parameters:
            layer (Layer): The Multi Layer of which all likelihoods will be index-wise transformed to sum up to 1.
        """
        self.__layer = layer

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        all_predictions = self.__layer.predict(predict_season, latest_episode, train_seasons)
        max_size = max([len(row) for row, _ in all_predictions.values()])
        prediction_matrix = np.array([np.pad(row, (0, max_size - len(row)), 'constant') for row, _ in all_predictions.values()])
        likelihood_sums = prediction_matrix.sum(axis = 0)
        for player, prediction in all_predictions.items():
            all_predictions[player] = prediction / likelihood_sums

        return all_predictions