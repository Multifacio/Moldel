from __future__ import annotations
from dataclasses import dataclass
from typing import List, Set, TYPE_CHECKING

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