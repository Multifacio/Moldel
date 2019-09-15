from dataclasses import dataclass
from Data import Player

@dataclass
class Question:
    """ Representation of a visible question during the test.

    Attributes:
        answers (dict): All the possible answers for this question. The key (int) is the answer number which starts
        with 1 and are numbered from top to bottom, from left to right. The value is a list of players corresponding
        to this answer. Questions should always be a partitioning, meaning that every player is represented by
        exactly 1 answer.
    """
    answer: dict

    def answer_for_player(self, player: Player) -> int:
        """ Get the answer number of the answer which contains the player """
        for answer_num, players in self.answer:
            if player in players:
                return answer_num