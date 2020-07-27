from Data.Player import Player
from Layers.Layer import Layer
from Layers.MultiLayer.MultiLayer import MultiLayer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Dict, Set
import numpy as np

class InnerMultiplyAggregateLayer(Layer):
    def __init__(self, layer: MultiLayer):
        self.__layer = layer

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, np.array]:
        all_predictions = self.__layer.predict(predict_season, latest_episode, train_seasons)
        if not all_predictions:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        distribution = dict()
        for player, predict in all_predictions.items():
            if predict.exclusion:
                distribution[player] = 0.0
            else:
                total_likelihood = 1.0
                for likelihood in predict.predictions:
                    total_likelihood *= likelihood
                distribution[player] = total_likelihood

        return distribution

class MultiplyAggregateLayer(NormalizeLayer):
    """ The Multiply Aggregate Layer aggregates a Multi Layer into a Layer by multiplying all likelihoods for each
    participant, which is justifiable in case the predictions are assumed to be independent. The results do not have to
    be normalized before applying this aggregation technique and players without prediction results are assumed to have
    a probability of 0, except if there are no predictions at all then they get an equal likelihood. """

    def __init__(self, layer: MultiLayer):
        """ Constructor of the Multiply Aggregate Layer.

        Arguments:
            layer (MultiLayer): The Multi Layer which gets aggregated into a Layer.
        """
        super().__init__(InnerMultiplyAggregateLayer(layer))