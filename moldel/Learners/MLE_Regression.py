from collections import namedtuple
from itertools import count
from .Learner import Learner
from .MLE_Function import MLE_Function
import math
import random
import numpy as np

Train_Variables = namedtuple("Train_Variables", ["coefs", "momentum", "learn_rates", "old_score"])

class MLE_Regression(Learner):
    """ Assumes the Input/Output Relation behaves like a Bernoulli variable with a probability of p of having 1.0 as
    outcome and a probability of 1 - p of having 0.0 as outcome, where p behaves as p = sig(c1 * x1 + c2 * x2 + ...)
    with sig being the sigmoid function and (x1, x2, x3, ...) being the input tuple. The global maximum of the MLE
    (Maximum Likelihood Estimator) function will be found by applying Stochastic Gradient Ascent on the logarithm of
    the MLE function. To speed up convergence we use Adam as described in:
    https://towardsdatascience.com/10-gradient-descent-optimisation-algorithms-86989510b5e9 """

    def __init__(self, batch_size: int, stop_rate: float = 0.015, stop_check_frequency: int = 2000,
                 step_size: float = 0.001, momentum_adj: float = 0.9, learn_adj: float = 0.999, epsilon: float = 1e-8):
        """ Constructor of the MLE Regression.

        Arguments:
            batch_size (int): How many data pairs will be sampled from the train data for every stochastic gradient
                ascent iteration (use a larger batch size if you have more training data).
            stop_rate (float): If the relative change between the score drops below this threshold then the algorithm
                will stop. Set this value lower if you want to train the algorithm better, set this value higher if you
                want a shorter running time.
            stop_check_frequency (int): Every stop_check_frequency step a new score will be computed and there will
                be a check if the relative difference between the new score and old score dropped below the stop_rate
                and if so the algorithm will halt.
            step_size (float): Determines the how large the coefficient changes are. If you set this value higher then
                the coefficient changes will also be larger.
            momentum_adj (float): How fast the momentum is changed (adjusted). If you set the value lower then the
                momentum changes faster which might influence how fast the algorithm will converge.
            learn_adj (float): How fast the learn rates will be changed (adjusted). If you set the value lower then the
                learn rates will more depend on the later gradients. If you set the value higher then it depends more on
                earlier gradients.
            epsilon (float): This value is used to prevent a large gradient change when the learn rate is close to zero.
                Increasing this value will decrease the maximum possible change in the coefficients. """
        self.__batch_size = batch_size
        self.__stop_rate = stop_rate
        self.__stop_check_frequency = stop_check_frequency
        self.__step_size = step_size
        self.__momentum_adj = momentum_adj
        self.__learn_adj = learn_adj
        self.__epsilon = epsilon

    def train(self, train_data: list) -> MLE_Function:
        train_vars = self.__initialize_train_variables(train_data)
        for i in count(1):
            train_vars = self.__update_train_variables(train_vars, train_data)
            stop, train_vars = self.__check_stop(train_vars, train_data, i)
            if stop:
                break
        return MLE_Function(train_vars.coefs)

    def __initialize_train_variables(self, train_data: list) -> Train_Variables:
        """ Set the start values for the coefficients, momentum, learning rates and the evaluation of the score. """
        coefs = np.zeros(len(train_data[0].input))
        momentum = np.zeros(len(train_data[0].input))
        learn_rates = np.zeros(len(train_data[0].input))
        MLE_func = MLE_Function(coefs)
        score = MLE_func.evaluate(train_data)
        return Train_Variables(coefs, momentum, learn_rates, score)

    def __update_train_variables(self, train_vars: Train_Variables, train_data: list) -> Train_Variables:
        """ Update the train variables once according to Stochastic Gradient Ascent with Adam. """
        MLE_func = MLE_Function(train_vars.coefs)
        train_batch = random.sample(train_data, self.__batch_size)
        # Multiply the gradient by a factor, because less data is used by stochastic gradient ascent.
        gradient = (len(train_data) / self.__batch_size) * MLE_func.gradient(train_batch)
        gradient_sqr = np.array([math.pow(val, 2) for val in gradient])
        new_momentum = self.__momentum_adj * train_vars.momentum + (1.0 - self.__momentum_adj) * gradient
        new_learn_rates = self.__learn_adj * train_vars.learn_rates + (1.0 - self.__learn_adj) * gradient_sqr
        coefs_change = self.__coefs_change(new_momentum, new_learn_rates)
        new_coefs = train_vars.coefs + coefs_change
        return Train_Variables(new_coefs, new_momentum, new_learn_rates, train_vars.old_score)

    def __coefs_change(self, momentum: np.array, learn_rates: np.array) -> np.array:
        """ Returns the changes in the coefficients. """
        normalized_momentum = (1.0 / (1.0 - self.__momentum_adj)) * momentum
        normalized_learn_rates = (1.0 / (1.0 - self.__learn_adj)) * learn_rates
        return np.array([self.__step_size * m / (math.sqrt(lr) + self.__epsilon)
                         for m, lr in zip(normalized_momentum, normalized_learn_rates)])

    def __check_stop(self, train_vars: Train_Variables, train_data: list, loop_iteration: int) -> tuple:
        """ Check if the stochastic gradient ascent has to stop, because the score did not change well enough.
        Returns a boolean that indicates whether the algorithm has to stop (in case it is true then the algorithm
        will stop) and returns the updated train_vars with the new score. """
        if loop_iteration % self.__stop_check_frequency == 0:
            # Only check every stop_check_frequency iteration whether the algorithm has to stop
            MLE_func = MLE_Function(train_vars.coefs)
            new_score = MLE_func.evaluate(train_data)
            relative_difference = abs((new_score - train_vars.old_score) / train_vars.old_score)
            stop = relative_difference < self.__stop_rate
            return (stop, Train_Variables(train_vars.coefs, train_vars.momentum, train_vars.learn_rates, new_score))
        else:
            return (False, train_vars)