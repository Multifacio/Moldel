from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.Layer import Layer
from Layers.MultiLayer.MultiLayer import MultiLayer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Dict, Set

class InnerMultiplyAggregateLayer(Layer):
    def __init__(self, layer: MultiLayer):
        self.__layer = layer

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        all_predictions = self.__layer.predict(predict_season, latest_episode, train_seasons)
        if not all_predictions:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        distribution = dict()
        all_players = get_players_in_season(predict_season)
        for player in all_players:
            if player in all_predictions:
                total_likelihood = 1.0
                for likelihood in all_predictions[player]:
                    total_likelihood *= likelihood
                distribution[player] = total_likelihood
            else:
                distribution[player] = 0.0

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