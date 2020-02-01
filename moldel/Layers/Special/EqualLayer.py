from Layers.Layer import Layer
from Data.Player import Player

class EqualLayer(Layer):
    """ The Equal Layer gives all players an equal likelihood of 1. """

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: set) -> dict:
        new_distribution = dict()
        for player in Player:
            if player.value.season == predict_season:
                new_distribution[player] = 1.0
        return new_distribution