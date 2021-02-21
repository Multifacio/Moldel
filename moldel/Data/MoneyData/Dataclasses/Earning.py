from __future__ import annotations
from dataclasses import dataclass
from typing import Set, TYPE_CHECKING

if TYPE_CHECKING:
    from ...Player import Player

@dataclass
class Earning:
    """ Representation of an amount of money that has been earned during an exercise.

    Attributes:
        money (float): The amount of money that has been earned.
        major (Set[Player]): The players that are directly responsible for earning that amount of money.
        minor (Set[Player]): The players that are not directly responsible but indirectly for earning that amount of
            money.
    """
    money: float
    major: Set[Player] = None
    minor: Set[Player] = None

    def __post_init__(self):
        if self.major is None:
            self.major = set()
        if self.minor is None:
            self.minor = set()

    def major_earned(self, player: Player) -> float:
        """ Determine how much money a player is directly responsible for.

        Arguments:
            player (Player): The player for which this is determined.

        Returns:
            The amount of money the player is directly responsible for.
        """
        if player in self.major:
            return self.money / len(self.major)
        else:
            return 0.0

    def minor_earned(self, player: Player) -> float:
        """ Determine how much money a player is indirectly responsible for.

        Arguments:
            player (Player): The player for which this is determined.

        Returns:
            The amount of money the player is indirectly responsible for.
        """
        if player in self.major or player in self.minor:
            return self.money / (len(self.major.union(self.minor)))
        else:
            return 0.0