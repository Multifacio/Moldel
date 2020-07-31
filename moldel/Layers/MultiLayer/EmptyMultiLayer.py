from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from typing import Dict, Set, Union
import numpy as np

class EmptyMultiLayer(MultiLayer):
    """ The Empty Multi Layer gives no predictions to every player. """

    def __init__(self, alive_players: Union[Set[Player], None] = None):
        """ Constructor of the Empty Multi Layer.

        Arguments:
            alive_players (Union[Set[Player], None]): The players that could still potentially be the Mol. If this
                value is not set then everyone could potentially be the Mol.
        """
        self.__alive_player = alive_players

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        season_players = get_players_in_season(predict_season)
        return {player: MultiLayerResult(np.array([]), self.__is_excluded_player(player)) for player in season_players}

    def __is_excluded_player(self, player: Player) -> bool:
        """ Check if a player is excluded from being the Mol.

        Returns:
            False if the player could potentially be the Mol and True if the player cannot be the Mol anymore.
        """
        if self.__alive_player is None:
            return False
        return player not in self.__alive_player

