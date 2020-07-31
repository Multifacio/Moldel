from Layers.Layer import Layer
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from typing import Dict, Set

class EqualLayer(Layer):
    """ The Equal Layer gives all players an equal likelihood summing up to 1.0. """

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        season_players = get_players_in_season(predict_season)
        likelihood = 1 / len(season_players)
        return {player: likelihood for player in season_players}