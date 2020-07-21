from __future__ import annotations
from dataclasses import dataclass
from typing import Set, TYPE_CHECKING

if TYPE_CHECKING:
    from .Episode import Episode
    from .Question import Question
    from ...Player import Player

@dataclass
class Answer:
    """ An Answer is a combination of a player, episode, question that belongs to a given answer.

    Attributes:
        player (Player): The player that gave this answer.
        episode (Episode): The episode in which this answer was given.
        question (Question): The question to which this answer belongs.
        answer (Set[Player]): The answer itself, which are the players targeted by this Answer.
    """
    player: Player
    episode: Episode
    question: Question
    answer: Set[Player]