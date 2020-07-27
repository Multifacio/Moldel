from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, Set, TYPE_CHECKING

if TYPE_CHECKING:
    from .Answer import Answer
    from .DropType import DropType
    from .Episode import Episode
    from ...Player import Player

@dataclass
class Season:
    """ Representation of the episodes in a season and players participating in this episode.

    Attributes:
        players (List[Player]): A list of all players that participated in this season (which also includes
            early drop offs and which includes the Mol).
        episodes (Dict[float, Episode]): The execution/test/drop off moments during a season. The key (float) is an
            episode number, if multiple executions/test/drop off moments happen then the keys should be different values
            in the range e - 1 < key <= e where e is the episode number of that episode in which these moments happen.
            The order of the moments matters: the earliest moment should get the lowest key and the latest moment should
            get the key value e. The values of this dict are Episode instances.
    """
    players: List[Player]
    episodes: Dict[float, Episode]

    def __post_init__(self):
        for id, episode in self.episodes.items():
            episode.id = id

    def get_alive_players(self, max_episode: int) -> Set[Player]:
        """  Get all players that are still alive (did not drop off) after a given episode.

        Arguments
            max_episode (int): The episode after which we do this check.

        Returns:
            All players that are still alive.
        """
        drop_players = set()
        for id, episode in self.episodes.items():
            if id <= max_episode:
                result = episode.result
                if result.drop.value:
                    drop_players.update(set(result.players))
        return set(self.players).difference(drop_players)

    def get_drop_mapping(self, drop_type: DropType, max_episode: int) -> Dict[Player, List[Episode]]:
        """ Map the players that dropped off with a given cause to the id of the episode in which they dropped off.

        Arguments:
            drop_type (DropType): Only players that dropped off because of this reason will be considered.
            max_episode (int): Only players that dropped off before/at this episode will be considered.

        Returns:
            A dictionary mapping all players satisfying these drop conditions to the ids of episodes in which they
            dropped off.
        """
        drop_mapping = dict()
        for id, episode in self.episodes.items():
            if id <= max_episode and episode.result.drop == drop_type:
                for player in episode.result.players:
                    drop_mapping[player] = drop_mapping.get(player, []) + [episode]
        return drop_mapping

    def get_all_answers(self, players: Set[Player], max_episode: int) -> List[Answer]:
        """ Get all answers on questions in this Season.

        Arguments:
            players (Set[Player]): The players of which their answers on questions are returned.
            max_episode (int): Only answers which are known before/at this episode might be used.

        Returns:
            A list of all answers.
        """
        all_answers = []
        for id, episode in self.episodes.items():
            if id <= max_episode:
                all_answers.extend(episode.get_all_answers(players, max_episode))
        return all_answers