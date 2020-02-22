from Data.Player import Player
from Data.SocialMediaData.SocialMediaData import SUSPICION_DATA
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Dict, Set

class InnerSocialMediaLayer(Layer):
    """ The Social Media Layer checks whether someone was active during the recording of "Wie is de Mol" which indicates
    that this player dropped of earlier and did not reach the finals (so this player cannot be the Mol). It also checks
    whether there is information leaked on Social Media that a player stayed longer in the game (so this player is more
    likely to be the Mol). Suspicion Levels for each player should be manually inserted in the Social Media Data file.
    Credits for this layer go to the research of Jaap van Zessen. """

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        if predict_season in SUSPICION_DATA:
            season_data = SUSPICION_DATA[predict_season]
            distribution = dict()
            for player, suspicion in season_data.items():
                distribution[player] = suspicion.value

            return distribution
        else:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

class SocialMediaLayer(NormalizeLayer):
    def __init__(self):
        super().__init__(InnerSocialMediaLayer())