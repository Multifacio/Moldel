from __future__ import annotations
from dataclasses import dataclass
from statistics import mean
from typing import Dict, List, NamedTuple, Union, Set, TYPE_CHECKING

from .Answer import Answer
if TYPE_CHECKING:
    from .Episode import Episode
    from ...Player import Player

# A Delayed Answer is an answer on a question which is revealed in later episodes. The answer value contains which
# answer was selected for that question and known_from contains the episode number during which the answer was revealed.
DelayedAnswer = NamedTuple("DelayedAnswer", [("answer", int), ("known_from", int)])

@dataclass
class TestInput:
    """ Representation of what a player did during the test.

    Attributes:
        answers (Dict[int, Union[int, DelayedAnswer]): What the player visibly answered during the test. The key is the
            question number (int) and the value is the answer number (int) that the player answered on that question or
            a DelayedAnswer in case the answer was revealed in a later episode. If a question number is not contained in
            this dict then it is unknown what the player answered on this question.
        mentions (Set[Player]): Who the player mentions he suspects to be the Mol.
        immunity (bool): Whether the player used/had a 'Vrijstelling' for the test. If this value is equal to true
            then the player used/had a 'Vrijstelling' for the test, false otherwise.
        jokers (int): How many jokers the player used on the test.
    """
    answers: Dict[int, Union[int, DelayedAnswer]] = None
    mentions: Set[Player] = None
    immunity: bool = False
    jokers: int = 0

    def __post_init__(self):
        if self.answers is None:
            self.answers = dict()
        if self.mentions is None:
            self.mentions = set()

    def joker_usage(self, exemption_value: int) -> int:
        """ Determine the joker usage of this player, where exemptions are given a certain joker value.

        Arguments:
            exemption_value (int): The value of an exemption expressed in jokers.

        Returns:
            The joker usage of this player, which include the joker value of exemptions.
        """
        return exemption_value if self.immunity else self.jokers

    def same_pick_probability(self, player: Player, episode: Episode, picked_answer: Set[Player], max_episode: int) -> float:
        """ Get the probability that the player selects one of the players in the given answer. If the player did not
        fill in a question on another player then it is assumed that the player uniform randomly selects another player
        as Mol.

        Arguments:
            player (Player): The player to which this Test Input belongs.
            episode (Episode): The episode to which this Test Input belongs.
            picked_answer (Set[Player]): The given answer.
            max_episode (int): Only answers which are known before/at this episode might be used.

        Returns:
            The probability that this player selects one of the players in the given answer.
        """
        probabilities = []
        for question, answer in self.answers.items():
            if isinstance(answer, DelayedAnswer):
                if answer.known_from > max_episode:
                    continue
                answer = answer.answer
                
            answer = set(episode.questions[question].answers[answer]).difference({player})
            if not answer:
                continue

            overlap = picked_answer.intersection(answer)
            probabilities.append(len(overlap) / len(answer))

        if probabilities:
            return mean(probabilities)
        else:
            picked_answer = picked_answer.difference({player})
            return len(picked_answer) / (len(episode) - 1)

    def get_all_answers(self, player: Player, episode: Episode, max_episode: int) -> List[Answer]:
        """ Get all the answers on questions for this Test Input.

        Arguments:
            player (Player): The player to which this Test Input belongs.
            episode (Episode): The episode to which this Test Input belongs.
            max_episode (int): Only answers which are known before/at this episode might be used.

        Returns:
            A list of all answers.
        """
        all_answers = []
        for qid, answer in self.answers.items():
            if isinstance(answer, DelayedAnswer):
                if answer.known_from > max_episode:
                    continue
                answer = answer.answer

            question = episode.questions[qid]
            answer = set(question.answers[answer])
            all_answers.append(Answer(player, episode, question, answer))

        return all_answers