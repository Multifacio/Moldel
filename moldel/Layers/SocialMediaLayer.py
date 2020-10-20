from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Data.SocialMediaData.SocialMediaData import SUSPICION_DATA
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Dict, Set

class InnerSocialMediaLayer(Layer):
    """ The Social Media Layer determines based on Social Media Analysis whether a player cannot be the 'Mol' anymore,
    because it was clear that the player left early during the recording period. Conclusion based on this analysis
    should manually be inserted in the Social Media Data file. Credits for this layer Jaap van Zessen:
    http://www.jaapvanzessen.nl/tag/wie-is-de-mol/ """

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        if predict_season in SUSPICION_DATA:
            exclude_players = SUSPICION_DATA[predict_season]
            distribution = dict()
            for player in get_players_in_season(predict_season):
                distribution[player] = 0.0 if player in exclude_players else 1.0
            return distribution
        else:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

class SocialMediaLayer(NormalizeLayer):
    def __init__(self):
        super().__init__(InnerSocialMediaLayer())