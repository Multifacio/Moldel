from __future__ import annotations
from dataclasses import dataclass
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .DropType import DropType
    from ...Player import Player

@dataclass
class Result:
    """ Representation of what happend during execution (after the test).

    Attributes:
        drop (DropType): Whether someone dropped out of the game or not and how they dropped out of the game.
        players (List[Player]): A list of players. The meaning of this list depends on the DropType. In the DropType
            class is explained what the meaning of the list is for every DropType value.
    """
    drop: DropType
    players: List[Player]