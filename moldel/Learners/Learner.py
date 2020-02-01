from collections import namedtuple
from . import Predicter

# IO Pair is an abbreviation of Input/Output Pair. The input is a tuple of floats and the output is a float.
IO_Pair = namedtuple("IO_Pair", ["input", "output"])

class Learner:
    """ A Learner will learn the relation between input and output based on training data. """
    
    def train(self, train_data: list) -> Predicter:
        """ Train the Learner with training data to learn the relation between the input and the output.

        Arguments:
            train_data (list): The train data used for training which is a list of IO Pair.
        Returns:
            Predicter instance which predicts the relation between input and output. """
        pass