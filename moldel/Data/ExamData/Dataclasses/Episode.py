from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List, TYPE_CHECKING, Set
import math

from .TestInput import TestInput
if TYPE_CHECKING:
    from .Answer import Answer
    from .Question import Question
    from ...Player import Player

@dataclass
class Episode:
    """ Representation of the test data (what happened during test and execution) for an episode. If there are multiple
    tests/executions/voluntary drops then you should create an Episode instance for each those situations.

    Attributes:
        players (List[Player]): A list of players that participated in the test of this episode (including the person
            that dropped off).
        result (Result): Contains the data what happened during the execution (after the test).
        input (Dict[Player, TestInput]): What the players did during the test. The key is a player and the value is a
            TestInput instance.
        questions (dict): The questions of the test that were visible for the viewers. The key is the question number
            (int) and the value is a Question instance.
        num_questions (int): The total number of questions the test had.
        id (float): The identifier of the episode, which is the used key in the dictionary of the Season instance for
            this episode. Note the identifier is not the same as the episode number.
    """
    players: List[Player]
    result: Result
    input: Dict[Player, TestInput]
    questions: Dict[int, Question]
    num_questions: int = 20
    id: float = 0.0

    def __post_init__(self):
        """ Players that are not contained in inputs set have not answered any visible question, do not have immunity
        and have used 0 jokers. """
        for player in self.players:
            if player not in self.input:
                self.input[player] = TestInput()

    def __eq__(self, other: Episode) -> bool:
        """ Check if both Episodes are the same, assuming that both Episodes take place in the same Season.

        Arguments:
            other (Episode): The Episode to check against.

        Returns:
            True if both Episodes are the same, false otherwise.
        """
        return self.id == other.id

    def __le__(self, other: Episode) -> bool:
        """ Check if an Episode happens earlier or is equal to the other Episode, assuming that both Episodes take place
        in the same Season.

        Arguments:
            other (Episode): The Episode to check against.

        Returns:
            True if this Episode happens earlier or is equal to the other Episode, false otherwise.
        """
        return self.id <= other.id

    def __lt__(self, other: Episode) -> bool:
        """ Check if an Episode happens earlier than the other Episode, assuming that both Episodes take place in the
        same Season.

        Arguments:
            other (Episode): The Episode to check against.

        Returns:
            True if this Episode happens earlier than the other Episode, false otherwise.
        """
        return self.id < other.id

    def __len__(self) -> int:
        """ Count the number of players still alive in this episode.

        Returns:
            The number of players still alive.
        """
        return len(self.players)

    def episode_number(self) -> int:
        """ Get the episode number of this episode. The episode has number 1.

        Returns:
            The episode number of this episode.
        """
        return int(math.ceil(self.id))

    def total_joker_usage(self, exemption_value: int) -> Dict[Player, int]:
        """ Compute the total joker usage of all players in this episode, where exemptions are given a certain joker
        value.

        Arguments:
            exemption_value (int): The value of an exemption expressed in jokers.

        Returns:
            The joker usage of all players, which include the joker value of exemptions.
        """
        joker_usage = dict()
        for player, test_input in self.input.items():
            joker_usage[player] = test_input.joker_usage(exemption_value)
        return joker_usage

    def same_pick_probabilities(self, picked_answer: Set[Player], max_episode: int) -> Dict[Player, float]:
        """ Get the probability for each player that it selects one of the players in the given answer. If the player
        did not fill in a question on another player then it is assumed that the player uniform randomly selects another
        player as Mol.

        Arguments:
            picked_answer (Set[Player]): The given answer.
            max_episode (int): Only answers which are known before/at this episode might be used.

        Returns:
            A dictionary with as key every player still alive in this episode and as value the probability that this
            player selects one of the players in the given answer.
        """
        probabilities = dict()
        for player, test_input in self.input.items():
            probabilities[player] = test_input.same_pick_probability(player, self, picked_answer, max_episode)
        return probabilities

    def get_all_answers(self, players: Set[Player], max_episode: int) -> List[Answer]:
        """ Get all answers on questions in this Episode.

        Arguments:
            players (Set[Player]): The players of which their answers on questions are returned.
            max_episode (int): Only answers which are known before/at this episode might be used, assuming that this
                episode number is less or equal than the max_episode.

        Returns:
            A list of all answers.
        """
        all_answers = []
        for player, test_input in self.input.items():
            if player in players:
                all_answers.extend(test_input.get_all_answers(player, self, max_episode))
        return all_answers