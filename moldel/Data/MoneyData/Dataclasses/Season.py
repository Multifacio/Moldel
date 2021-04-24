from __future__ import annotations
from dataclasses import dataclass
from typing import List, Set, TYPE_CHECKING
from ...Player import Player
from ...PlayerData import get_players_in_season

if TYPE_CHECKING:
    from . import Exercise

@dataclass
class Season:
    """ Representation of a season with all its exercises.

    Attributes:
        exercises (List[Exercise]): The list of all exercises during a season.
    """
    exercises: List[Exercise]

    def get_exercises(self, latest_episode: float) -> List[Exercise]:
        """ Return all list of all exercises known up to the latest episode that have information.

        Arguments:
            latest_episode (float): The latest episode known so far. Use math.inf if you want to return all exercises.

        Returns:
            A list of all exercises up to the latest episode.
        """
        return [exercise for exercise in self.exercises if exercise.episode <= latest_episode and
                exercise.contains_information()]

    def get_alive(self, latest_episode: float) -> Set[Player]:
        """ Return all players alive till the latest episode. Return an empty set if there are no exercises.

        Arguments:
            latest_episode (float): The latest episode.

        Returns:
            The set of all players alive.
        """
        if self.exercises:
            alive = self.exercises[0].alive.copy()
            for exercise in self.exercises[1:]:
                if exercise.episode <= latest_episode:
                    alive.intersection_update(exercise.alive)
            return alive
        else:
            return set()