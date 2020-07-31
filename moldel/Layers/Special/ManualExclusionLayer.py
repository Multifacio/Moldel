from Data.ManualExclusionData import MANUAL_EXCLUSIONS
from Data.Player import Player
from Layers.Layer import Layer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Dict, Set

class InnerManualExclusionLayer(Layer):
    def __init__(self, layer: Layer):
        self.__layer = layer

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        distribution = self.__layer.compute_distribution(predict_season, latest_episode, train_seasons)
        season_exclusions = MANUAL_EXCLUSIONS.get(predict_season, [])
        for excluded_player, known_from_episode in season_exclusions:
            if latest_episode >= known_from_episode:
                distribution[excluded_player] = 0.0
        return distribution

class ManualExclusionLayer(NormalizeLayer):
    """ The Manual Exclusion Layer excludes certain players from being the Mol when an episode has passed (for these
        excluded players the likelihood will be set to 0.0). """

    def __init__(self, layer: Layer):
        """ Constructor of the Manual Exclusion Layer

        Parameters:
            layer (Layer): The layer from which certain players will be excluded from being the Mol.
        """
        super().__init__(InnerManualExclusionLayer(layer))