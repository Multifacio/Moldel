from types import SimpleNamespace

class Episode(SimpleNamespace):
    def __init__(self, players, result, test_inputs, visible_questions, num_questions = 20, skip_regression = False):
        """ Constructor for Episode (only include episodes that give information about who dropped off)
        Args:
            players (list): The players (string format) that participate in the final test of the episode
            result (Result): The result of the test
            test_inputs (dict): What the players did on the test. The key is the player (string format) and the value
            is a TestInput object
            visible_questions (dict): The questions of the test that were visible for viewers (key is the question
            number which is an integer and the values are Question objects)
            num_questions (int): The total number of questions the test had
            skip_regression (bool): When true then the episode is not used for training. Also it is skipped in the
            forward answer regression as prediction.
        """
        self.initialize_test(players, test_inputs)
        super().__init__(players = players, result = result, test_inputs = test_inputs, visible_questions = visible_questions,
                         num_questions = num_questions, num_invisible_questions = num_questions - len(visible_questions),
                         skip_regression = skip_regression)

    def initialize_test(self, players, test_inputs):
        """ For players not contained in test_inputs do not give any information about questions and use 0 jokers """
        for p in players:
            if p not in test_inputs:
                test_inputs[p] = TestInput()

class Result(SimpleNamespace):
    def __init__(self, drop, players):
        """ Constructor for Result (a Result is what happend after the test)
        Args:
            drop (bool): True means that player(s) did not survive the test, False means that everyone survived the test
            players (list): In case drop is true then this is the list of players (string format) that did not survive
            the test, in case drop is false then this is the list of players that possible would have failed the test
        """
        super().__init__(drop = drop, players = players)

class Question(SimpleNamespace):
    """ Constructor of Question
    Args:
        options (dict): The different options a player can choose at the question (the key is the option number (int):
        options are numbered from top to bottom, left to right. The value is the list of players (string format) that
        an option targets)
    """
    def __init__(self, options):
        super().__init__(options = options)

    def option_for_player(self, player):
        """ Get the option in the question that belongs to the player given as argument """
        for key in self.options:
            if player in self.options[key]:
                return key

class TestInput(SimpleNamespace):
    """ Constructor of Test Input (what a player did and filled in on the test)
    Args:
        answered_questions (dict): A dictionary where the key is the question number (int) and the value is the option
        number (int) that the player selected. If a question number is not contained in the dictionary then it is
        unknown what the player filled in at this question
        immunity (bool): Is equal to true if the player has used a "vrijstelling" otherwise is equal to false.
        jokers (int): How much jokers the player used on the test.
    """
    def __init__(self, answered_questions = None, immunity = False, jokers = 0):
        if answered_questions is None:
            answered_questions = dict()
        super().__init__(answered_questions = answered_questions, immunity = immunity, jokers = jokers)