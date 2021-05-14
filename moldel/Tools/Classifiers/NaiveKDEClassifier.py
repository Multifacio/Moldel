from Tools.Classifiers.Classifier import Classifier
from scipy.stats import gaussian_kde
from typing import List, Union
import numpy as np

class NaiveKDEClassifier(Classifier):
    """ A Naive KDE Classifier uses kernel density estimation independently per feature combined with naïve bayes to
    predict how likely cases belong to the positive/negative class. """

    # How often the bandwidth is subtracted and added to respectively the lowest and highest value to get the search
    # range.
    BANDWIDTH_TIMES = 10

    # In how many steps the boundaries are found. The difference between the actual boundary and the estimated boundary
    # is 2^(-SEARCH_STEPS).
    SEARCH_STEPS = 20

    def __init__(self, weights: Union[List[float], None] = None, cdf_cutoff: Union[float, None] = None):
        """ Constructor of the Naive KDE Classifier.

        Arguments:
            weights (Union[List[float], None]): A list of weights indicating how important each feature is. If None then
                all features are treated equally important.
            cdf_cutoff (Union[float, None]): How many cumulative likelihood is cutoff from the left and right of the
                KDE distributions. If None then there is not cutoff.
        """
        self.__weights = weights
        self.__cdf_cutoff = cdf_cutoff

    def train(self, train_input: np.array, train_output: np.array):
        self.negative_kde = self.__train_kde(train_input, train_output, False)
        self.positive_kde = self.__train_kde(train_input, train_output, True)
        self.ratio = sum(train_output) / len(train_output)

        if self.__cdf_cutoff is not None:
            self.lowerbounds = np.array([self.__get_boundary(self.__cdf_cutoff / 2, self.ratio, neg_kde, pos_kde,
                column) for neg_kde, pos_kde, column in zip(self.negative_kde, self.positive_kde, train_input.T)])
            self.upperbounds = np.array([self.__get_boundary(1 - self.__cdf_cutoff / 2, self.ratio, neg_kde, pos_kde,
                column) for neg_kde, pos_kde, column in zip(self.negative_kde, self.positive_kde, train_input.T)])

    def predict_proba(self, predict_input: np.array) -> float:
        if self.__cdf_cutoff is not None:
            predict_input = np.minimum(np.maximum(predict_input, self.lowerbounds), self.upperbounds)

        negative = (1 - self.ratio) * self.class_likelihood(predict_input, False)
        positive = self.ratio * self.class_likelihood(predict_input, True)
        return positive / (negative + positive)

    def class_likelihood(self, predict_input: np.array, positive_class: bool) -> float:
        """ Determine the likelihood of being generated by either the positive/negative class.

        Arguments:
            predict_input (np.array): An 1-dimensional array which represents the encoding of a prediction case.
            positive_class (bool): True if the likelihood of being generated by the positive class is checked, false
                if the likelihood of being generated by the negative class is checked.

        Returns:
            The likelihood of being generated by that class.
        """
        if self.__weights is None:
            self.__weights = [1 for _ in predict_input]

        kdes = self.positive_kde if positive_class else self.negative_kde
        likelihoods = [kde.pdf(pi) for kde, pi in zip(kdes, predict_input)]
        return np.prod([likelihood ** weight for likelihood, weight in zip(likelihoods, self.__weights)])

    def __train_kde(self, train_input: np.array, train_output: np.array, positive_class: bool) -> List[gaussian_kde]:
        """ Train the gaussian kernel density estimators for the data.

        Arguments:
            train_input (np.array): The train input used to train gaussian kernel density estimators.
            train_output (np.array): The train output indicating whether cases belong to the positive/negative class.
            positive_class (bool): True if the gaussian kernel density estimator are trained for positive classes,
                false if they are trained for negative classes.

        Returns:
            A list of gaussian kernel density estimators for every feature.
        """
        selected_output = 1.0 if positive_class else 0.0
        selected_input = np.array([ti for ti, to in zip(train_input, train_output) if to == selected_output])
        return [gaussian_kde(column, bw_method = 'silverman') for column in selected_input.T]

    @classmethod
    def __get_boundary(self, cdf: float, ratio: float, neg_kde: gaussian_kde, pos_kde: gaussian_kde, column: np.array) \
            -> float:
        """ Get the approximated boundary value x such that the cumulative distribution function of x is equal to cdf.

        Arguments:
            cdf (float): The cumulative distribution value of this x.
            ratio (float): The ratio of cases that belong to the positive class.
            neg_kde (gaussian_kde): The kernel density estimator for the negative class.
            pos_kde (gaussian_kde): The kernel density estimator for the positive class.
            column (np.array): The column of feature corresponding to the kernel density estimators.

        Returns:
            The boundary value x.
        """
        bw = max(neg_kde.factor, pos_kde.factor)
        min_value = lowerbound = np.min(column) - self.BANDWIDTH_TIMES * bw
        upperbound = np.max(column) + self.BANDWIDTH_TIMES * bw
        middle = (lowerbound + upperbound) / 2
        for _ in range(self.SEARCH_STEPS):
            cur_cdf = (1 - ratio) * neg_kde.integrate_box_1d(min_value, middle) + ratio * \
                      pos_kde.integrate_box_1d(min_value, middle)
            if cur_cdf < cdf:
                lowerbound = middle
            else:
                upperbound = middle
            middle = (lowerbound + upperbound) / 2
        return middle
