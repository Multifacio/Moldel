from Data.Player import Player
from Data.PlayerData import get_players_in_season, get_is_mol
from Layers.Layer import Layer
from typing import Set, Dict

class PerfectLayer(Layer):
    """ The Perfect Layer is a cheating layer that perfectly predicts who the Mol is. It is mainly used for comparison
    purposes. """

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        return {player: 1.0 if get_is_mol(player) else 0.0 for player in get_players_in_season(predict_season)}