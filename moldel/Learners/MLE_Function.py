from .Predicter import Predicter
import numpy as np
import math

class MLE_Function(Predicter):
    """ The logarithm of the Maximum Likelihood Function which computes the probability for an input of having 1.0 as
    output based on the training data and the linear weights for the input features. """

    def __init__(self, coefs: np.array):
        """ Constructor for the MLE_Function.

        Arguments:
            coefs (np.array): An array of linear weights (float) for computing the likelihood of data. The ith number
                corresponds to the ith input feature. When this ith number is close to zero then it has little influence
                on the output. If this number is large positive then an increase in this feature value means a high
                probability of having 1.0 as output. If this number is large negative then an increase in this feature
                value means a low probability of having 1.0 as output.
        """
        self.__coefs = coefs

    def predict(self, input_data: tuple) -> float:
        # Predict the probability of having 1.0 as output for the given input.
        return self.__linear_sigmoid(input_data)

    def load(self) -> list:
        """ Get the coefficients used for this MLE function.

        Returns:
            A list of linear weights (float) used for this MLE function.
        """
        return list(self.__coefs)

    def evaluate(self, data_pairs: list) -> float:
        """ Computes the log likelihood of the data pairs (which is the logarithm of the MLE function).

        Arguments:
            data_pairs (list): List of IO_Pair for which the log likelihood is computed.
        Returns:
            The log likelihood of the data pairs (float).
        """
        result = 0.0
        for pair in data_pairs:
            sigmoid_output = self.__linear_sigmoid(pair.input)
            if pair.output == 1.0:
                result += math.log(sigmoid_output)
            else:
                result += math.log(1.0 - sigmoid_output)
        return result

    def gradient(self, data_pairs: list) -> np.array:
        """ Compute the gradient of the logarithm of the MLE function.

        Returns:
            The gradient, which is an array of partial derivatives with respect to the coefficients (linear weights).
        """
        return np.array([self.__derivative(i, data_pairs) for i in range(len(self.__coefs))])

    @staticmethod
    def sigmoid(x: float) -> float:
        return 1.0 / (1.0 + math.exp(-x))

    def __derivative(self, index: int, data_pairs: list) -> float:
        """ Find the partial derivate with respect to the c-indexth variable. """
        result = 0.0
        for pair in data_pairs:
            sigmoid_output = self.__linear_sigmoid(pair.input)
            if pair.output == 1.0:
                result += pair.input[index] * (1 - sigmoid_output)
            else:
                result += -pair.input[index] * sigmoid_output
        return result

    def __linear_sigmoid(self, input_vector) -> float:
        """ Get the sigmoid of the dot product of the coefficients and the input vector. """
        dot_prod = 0.0
        for coef, input_value in zip(self.__coefs, input_vector):
            dot_prod += coef * input_value
        return self.sigmoid(dot_prod)