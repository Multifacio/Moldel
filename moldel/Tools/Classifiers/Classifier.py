import numpy as np

class Classifier:
    """ A 2-class classifier (positive and negative class) that uses train data to train the classifier and use it to
    determine the probability how likely a case corresponds to a certain class. """

    def train(self, train_input: np.array, train_output: np.array):
        """ Train the classifier with training data.

        Arguments:
            train_input (np.array): A 2-dimensional array where each row corresponds with a training case and each
                column corresponds with a feature.
            train_output (np.array): An 1-dimensional array of 0 and 1 values where 0 represents being member of the
                negative class and a 1 represents being member of the positive class.
        """
        pass

    def predict_proba(self, predict_input: np.array) -> float:
        """ Predict how likely a case corresponds to the positive class.

        Arguments:
             predict_input (np.array): An 1-dimensional array which represents the encoding of a prediction case.

        Returns:
            A value between 0 and 1 representing how likely that case belongs to the positive class.
        """
        pass