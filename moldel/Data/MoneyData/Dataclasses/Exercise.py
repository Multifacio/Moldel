from __future__ import annotations
from collections import Counter as counter
from dataclasses import dataclass
from typing import Set, TYPE_CHECKING, Union, List, Counter
import itertools as it

if TYPE_CHECKING:
    from . import Earning
    from ...Player import Player

@dataclass
class Exercise:
    """ Representation of an exercise.

    Attributes:
        episode (float): From which episode the exercise is known.
        alive (Set[Player]): Which players are alive during this exercise.
        maximum (Union[float, None]): The maximum amount of money that can be earned. This value is equal to None if
            nothing can be earned during this exercise, if an infinite amount of money can be earned during this
            exercise or if the maximum amount of money that can be earned is unknown.
        earned (List[Earning]): The list with amounts of money that have been earned during this exercise.
    """
    episode: float
    alive: Set[Player]
    maximum: Union[float, None]
    earned: List[Earning]

    def contains_information(self) -> bool:
        """ Check if the exercise has any information.

        Returns:
            True if this exercise contains information, false otherwise.
        """
        return bool(self.earned)

    def major_earned(self) -> Counter[Player]:
        """ Determine how much money all players directly earned in this exercise.

        Returns:
            The amount of money that every player is directly responsible for.
        """
        earned = counter()
        for player, earning in it.product(self.alive, self.earned):
            earned[player] += earning.major_earned(player)
        return earned

    def minor_earned(self) -> Counter[Player]:
        """ Determine how much money all players indirectly earned in this exercise.

        Returns:
            The amount of money that every player is indirectly responsible for.
        """
        earned = counter()
        for player, earning in it.product(self.alive, self.earned):
            earned[player] += earning.minor_earned(player)
        return earned