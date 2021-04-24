import numpy as np

class Encoder:
    """ An Encoder transforms features to a different and better format of features. """

    def fit(self, X: np.array):
        """ Prepare the encoder.

        Arguments:
            X (np.array): A two dimensional matrix where every column represents a feature and every row represents a
                data point.
        """
        pass

    def transform(self, X: np.array) -> np.array:
        """ Transforms a given feature matrix.

        Arguments:
            X (np.array): A two dimensional matrix where every column represents a feature and every row represents a
                data point.

        Returns:
            A transformed version of X.
        """
        pass