from Layer import Layer
from Data.ManualExclusionData import MANUAL_EXCLUSIONS

class ManualExclusionLayer(Layer):
    """ The Manual Exclusion Layer excludes certain players from being the Mol when an episode has passed (for these
    excluded players the likelihood will be set to 0.0). """

    def __init__(self, layer: Layer):
        """ Constructor of the Manual Exclusion Layer

        Parameters:
            layer (Layer): The layer from which certain players will be excluded from being the Mol.
        """
        self.__layer = layer

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: set) -> dict:
        layer_distribution = self.__layer.compute_distribution(predict_season, latest_episode, train_seasons)
        new_distribution = layer_distribution.copy()
        season_exclusions = MANUAL_EXCLUSIONS[predict_season]
        for excluded_player, known_from_episode in season_exclusions:
            if latest_episode >= known_from_episode:
                new_distribution[excluded_player] = 0.0
        return new_distribution