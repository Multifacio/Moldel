from Data.ManualExclusionData import MANUAL_EXCLUSIONS
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.Layer import Layer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Dict, Set

class InnerManualExclusionLayer(Layer):
    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        season_players = get_players_in_season(predict_season)
        season_exclusions = MANUAL_EXCLUSIONS.get(predict_season, [])
        distribution = {player: 1.0 for player in season_players}
        for excluded_player, known_from_episode in season_exclusions:
            if latest_episode >= known_from_episode:
                distribution[excluded_player] = 0.0
        return distribution

class ManualExclusionLayer(NormalizeLayer):
    """ The Manual Exclusion Layer excludes certain players from being the Mol when an episode has passed (for these
    excluded players the likelihood will be set to 0.0). """

    def __init__(self):
        super().__init__(InnerManualExclusionLayer())