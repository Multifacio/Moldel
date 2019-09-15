from dataclasses import dataclass

@dataclass
class TestInput:
    """ Representation of what a player did during the test.

    Attributes:
        answers (dict): What the player visibly answered during the test. The key is the question number (int) and
        the value is the answer number (int) that the player answered on that question. If a question number is not
        contained in this dict then it is unknown what the player answered on this question.
        immunity (bool): Whether the player used/had a 'Vrijstelling' for the test. If this value is equal to true
        then the player used/had a 'Vrijstelling' for the test, false otherwise.
        jokers (int): How many jokers the player used on the test.
    """
    answers: dict = None
    immunity: bool = False
    jokers: int = 0

    def __post_init__(self):
        if self.answers is None:
            self.answers = dict()