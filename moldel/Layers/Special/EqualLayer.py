from Layers.Layer import Layer
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from typing import Dict, Set

class EqualLayer(Layer):
    """ The Equal Layer gives all players an equal likelihood of 1. """

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        distribution = dict()
        all_players = get_players_in_season(predict_season)
        for player in all_players:
            distribution[player] = 1.0
        return distribution