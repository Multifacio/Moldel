from __future__ import annotations
from dataclasses import dataclass
from .TestInput import TestInput

@dataclass
class Episode:
    """ Representation of the test data (what happened during test and execution) for an episode.

    Attributes:
        players (list): A list of players that participated in the test of this episode (including the person that dropped off).
        result (Result): Contains the data what happened during the execution (after the test).
        input (dict): What the players did during the test. The key is a player and the value is a TestInput instance.
        questions (dict): The questions of the test that were visible for the viewers. The key is the question number (int)
            and the value is a Question instance.
        num_questions (int): The total number of questions the test had.
        skip_regression (bool): If true then the episode is not used for regression training and for regression
            prediction. However every player that has dropped off will be excluded from being the Mol (even in episodes
            with skip_regression equal to true).
    """
    players: list
    result: Result
    input: dict
    questions: dict
    num_questions: int = 20
    skip_regression: bool = False

    def __post_init__(self):
        """ Players that are not contained in inputs set have not answered any visible question, do not have immunity
        and have used 0 jokers. """
        for player in self.players:
            if player not in self.input:
                self.input[player] = TestInput()