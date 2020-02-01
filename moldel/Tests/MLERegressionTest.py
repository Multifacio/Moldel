from Learners.MLE_Function import MLE_Function
from Learners.Learner import IO_Pair
from Learners.MLE_Regression import MLE_Regression
import random
import unittest
import numpy as np

class MLERegressionTest(unittest.TestCase):
    TEST_CASES = 5  # How many times every test cases will be executed.
    MAXIMUM_ERROR = 0.025  # How large the absolute difference between the expected and actual error might be.
    INPUT_SIZE = 3  # The dimension of the input used.
    TRAIN_DATA_SIZE = 100000  # How many train data will be used.
    BATCH_SIZE = 100  # The batch size used for training the MLE Regression
    COEFS_RANGE = 10.0  # The range of the coefficients when generated randomly

    def test_basic_probability(self):
        """ A test case where every input has the same probability of corresponding to the output 1.0 independent on
        the input values. """
        for i in range(1, self.TEST_CASES + 1):
            actual_probability = random.random()
            train_data = []
            for _ in range(self.TRAIN_DATA_SIZE):
                input = self.random_vector(self.INPUT_SIZE, self.COEFS_RANGE, True)
                output = 1.0 if random.random() < actual_probability else 0.0
                train_data.append(IO_Pair(input, output))
            reg = MLE_Regression(self.BATCH_SIZE)
            MLE_func = reg.train(train_data)
            new_input = self.random_vector(self.INPUT_SIZE, self.COEFS_RANGE, True)
            expected_probability = MLE_func.predict(new_input)
            difference = abs(actual_probability - expected_probability)
            print("Absolute Difference: " + str(difference))
            self.assertTrue(difference <= self.MAXIMUM_ERROR,
                            "Difference between expected probability and actual probability is too large! (Basic)")
            print("Basic Probability test case " + str(i) + " passed.")

    def test_advanced_probability(self):
        """ A test case where the probability is determined by a sigmoid linear function with random coefficients.
        Beware: This test case takes some time to run. """
        for i in range(1, self.TEST_CASES + 1):
            coefs = np.array(self.random_vector(self.INPUT_SIZE + 1, self.COEFS_RANGE, False))
            train_data = []
            reg = MLE_Regression(self.BATCH_SIZE)
            for _ in range(self.TRAIN_DATA_SIZE):
                input = np.array(self.random_vector(self.INPUT_SIZE, self.COEFS_RANGE, True))
                probability = MLE_Function.sigmoid(np.inner(coefs, input))
                output = 1.0 if random.random() < probability else 0.0
                train_data.append(IO_Pair(input, output))
            MLE_func = reg.train(train_data)
            new_input = self.random_vector(self.INPUT_SIZE, self.COEFS_RANGE, True)
            actual_probability = MLE_Function.sigmoid(np.inner(coefs, np.array(new_input)))
            expected_probability = MLE_func.predict(new_input)
            difference = abs(actual_probability - expected_probability)
            print("Absolute Difference: " + str(difference))
            self.assertTrue(difference <= self.MAXIMUM_ERROR,
                            "Difference between expected probability and actual probability is too large! (Advanced)")
            print("Advanced Probability test case " + str(i) + " passed.")

    @staticmethod
    def random_vector(size, value_range, append_one):
        """ Create a list of uniform random numbers.

        Arguments:
            size (int): The size of the list of random numbers
            value_range(float): The numbers are random uniformly selected from the range (-value_range, value_range)
            append_one (bool): If true then a 1 value is appended to the random vector
        Returns:
            A list of random numbers
        """
        vector = [random.uniform(-value_range, value_range) for _ in range(size)]
        if append_one:
            vector.append(1.0)
        return tuple(vector)

if __name__ == '__main__':
    unittest.main()
