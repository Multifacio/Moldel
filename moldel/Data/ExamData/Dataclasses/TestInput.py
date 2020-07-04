from dataclasses import dataclass
from typing import Dict, NamedTuple, Union

# A Delayed Answer is an answer on a question which is revealed in later episodes. The answer value contains which
# answer was selected for that question and known_from contains the episode number during which the answer was revealed.
DelayedAnswer = NamedTuple("DelayedAnswer", [("answer", int), ("known_from", int)])

@dataclass
class TestInput:
    """ Representation of what a player did during the test.

    Attributes:
        answers (dict): What the player visibly answered during the test. The key is the question number (int) and
            the value is the answer number (int) that the player answered on that question or a DelayedAnswer in case
            the answer was revealed in a later episode. If a question number is not contained in this dict then it is
            unknown what the player answered on this question.
        immunity (bool): Whether the player used/had a 'Vrijstelling' for the test. If this value is equal to true
            then the player used/had a 'Vrijstelling' for the test, false otherwise.
        jokers (int): How many jokers the player used on the test.
    """
    answers: Dict[int, Union[int, DelayedAnswer]] = None
    immunity: bool = False
    jokers: int = 0

    def __post_init__(self):
        if self.answers is None:
            self.answers = dict()