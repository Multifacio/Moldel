from jenkspy import jenks_breaks
from Tools.Encoders.Encoder import Encoder
from numpy.random import RandomState
from typing import List
import numpy as np

class NaturalSplineEncoding(Encoder):
    """ Natural Spline Encoding encodes every feature individually as piecewise cubic spline with the following
    requirements:
        - The first and last splines are linear splines.
        - The cubic splines are continuous, differentiable and smooth everywhere.
    See https://en.wikipedia.org/wiki/Spline_(mathematics) and Section 2.4.5 of the book 'Regression Modeling Strategies'
    for more information.
    """

    def __init__(self, num_curves: List[int]):
        """ Constructor of the Natural Spline Encoding.

        Arguments:
            num_curves (List[int]): How many polynomials per feature should be used to encode the natural spline.
        """
        self.num_curves = num_curves

    def fit(self, X: np.array):
        self.__determine_knots(X)

    def transform(self, X: np.array) -> np.array:
        rows = []
        for row in X:
            features = []
            for x, knot in zip(row, self.knots.T):
                features.extend(self.__single_natural_spline_encoding(x, knot))
            rows.append(features)
        return np.array(rows)

    def __determine_knots(self, X: np.array):
        """ Determine the locations of the knots for every feature using Jenks Natural Breaks.

        Arguments:
            X (np.array): The train input used to determine the location of the knots.
        """
        self.knots = []
        for column, num_curves in zip(X.T, self.num_curves):
            breaks = jenks_breaks(column, nb_class = num_curves)
            self.knots.append(breaks)
        self.knots = np.array(self.knots).T

    @classmethod
    def __single_natural_spline_encoding(self, x: float, knots: List[float]) -> List[float]:
        """ Compute the spline encoding for a single value.

        Arguments:
            x (float): The value on which a spline encoding is applied.
            knots (List[float]): The locations where the knots are placed.

        Returns:
            The spline encoding of this value.
        """
        return [x] + [self.__feature_encoding(x, i, knots) for i in range(len(knots) - 2)]

    @classmethod
    def __feature_encoding(self, x: float, i: int, knots: List[float]) -> float:
        """ Compute the value of X_{i + 1} as defined in Section 2.4.5 of the book 'Regression Modeling Strategies'.

        Arguments:
            x (float): The value on which a spline encoding is applied.
            i (int): The index i which corresponds to the X_{i + 1} we want to compute.
            knots (List[float]): The locations where the knots are placed.

        Returns:
            The value of X_{i + 1}.
        """
        return self.__ramp(x - knots[i]) ** 3 - self.__ramp(x - knots[-2]) ** 3 * (knots[-1] - knots[i]) / \
            (knots[-1] - knots[-2]) + self.__ramp(x - knots[-1]) ** 3 * (knots[-2] - knots[i]) / (knots[-1] - knots[-2])

    @staticmethod
    def __ramp(x: float):
        """ The ramp function (also known as the ReLu function).

        Arguments:
            x (float): The value of on which the ramp function is applied.

        Returns:
            The outcome of the ramp function.
        """
        return max(x, 0)