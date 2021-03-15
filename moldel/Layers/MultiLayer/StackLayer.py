from Data.LastEpisodes import get_last_episode
from Data.Player import Player
from Data.PlayerData import get_is_mol
from Layers.Layer import Layer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.Special.NormalizeLayer import NormalizeLayer
from sklearn.decomposition import PCA
from scipy.optimize import root
from scipy.special import expit, logit
from typing import Dict, List, Set, Tuple
import math
import numpy as np

class InnerStackLayer(Layer):
    # The maximal difference between the actual sum of weights and the expected sum of weights
    PRECISION = 1e-4

    def __init__(self, predict_layer: MultiLayer, train_layer: MultiLayer, splits: List[Set[int]]):
        self.__predict_layer = predict_layer
        self.__train_layer = train_layer
        self.__splits = splits

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        prediction = self.__predict_layer.predict(predict_season, latest_episode, train_seasons)
        predict_alive = {player for player, result in prediction.items() if not result.exclusion}
        if len(predict_alive) == 1:
            return {player: 1.0 if player in predict_alive else 0.0 for player in prediction}

        alives_group = next(group for group in self.__splits if len(predict_alive) in group)
        weights = self.__train(train_seasons, alives_group)
        return self.__stack_predictions(prediction, weights, len(predict_alive))

    def __train(self, train_seasons: Set[int], alives_group: Set[int]) -> np.array:
        """ Train the Stack Layer.

        Arguments:
            train_seasons (Set[int]): All seasons used for training the stacking algorithm.
            alives_group (Set[int]): Only episodes with any of these numbers of players that could still potentially
                be the mol are used as training data.

        Returns:
            The classifier used to predict the mol based on the predictions of the layers.
        """
        train_input, train_output = self.__get_train_data(train_seasons, alives_group)
        start = np.ones(len(train_input[0]) + 1)
        while True:
            weights = root(self.__zero_function, start, args = (train_input, train_output)).x
            print(self.__zero_function(weights, train_input, train_output))
            bias = weights[-2]
            weights = np.power(weights[:-2], 2)
            if abs(np.sum(weights) - len(weights)) < self.PRECISION:
                weights = np.append(weights / np.sum(weights) * len(weights), [bias])
                break
            start = np.random.uniform(size = len(train_input[0]) + 1)
        print(weights)
        return weights

    def __stack_predictions(self, prediction: Dict[Player, MultiLayerResult], weights: np.array, num_alives: int) \
            -> Dict[Player, float]:
        """ Stack the predictions.

        Arguments:
            prediction (Dict[Player, MultiLayerResult]): All predictions for every player.
            classifier (Set[int]): The classifier used to predict the mol based on the predictions of the layers.
            num_alives (int): How many players are alive in the last prediction episode.

        Returns:
            The prediction for every player after stacking all predictions
        """
        return {p: 0.0 if r.exclusion else self.__sigmoid(weights, self.__input_encoding(r, num_alives))
                for p, r in prediction.items()}

    def __get_train_data(self, train_seasons: Set[int], alives_group: Set[int]) -> Tuple[np.array, np.array]:
        """ Get the train data used to train the stacking algorithm.

        Arguments:
            train_seasons (Set[int]): All seasons used for training the stacking algorithm.
            alives_group (Set[int]): Only episodes with any of these numbers of players that could still potentially
                be the mol are used as training data.

        Returns:
            The train input which is a 2d matrix where each row represents a train case. Also it returns the train
            output which is a 1d array where each value indicates whether the corresponding train case row was the mol
            or not.
        """
        train_input = []
        train_output = []
        for train_season in train_seasons:
            for episode in range(get_last_episode(train_season) + 1):
                train_prediction = self.__train_layer.predict(train_season, episode,
                                                              train_seasons.difference({train_season}))
                train_alive = {player for player, result in train_prediction.items() if not result.exclusion}
                if len(train_alive) in alives_group:
                    for player, result in train_prediction.items():
                        if not result.exclusion:
                            train_input.append(self.__input_encoding(result, len(train_alive)))
                            train_output.append(1.0 if get_is_mol(player) else 0.0)
        return np.array(train_input), np.array(train_output)

    def __input_encoding(self, result: MultiLayerResult, num_alives: int) -> np.array:
        """ Get the input encoding of a single Multi Layer Result.

        Arguments:
            result (MultiLayerResult): The predictions of the different layers for this case.
            num_alives (int): How many players could still potentially be the mol.

        Returns:
            The input encoding for this case.
        """
        likelihoods = np.append(result.predictions, [1 / num_alives])
        return np.append(logit(likelihoods), [1])

    def __zero_function(self, weights: np.array, train_input: np.array, train_output: np.array) -> np.array:
        bias = weights[-2]
        laplacian = weights[-1]
        weights = weights[:-2]
        sigmoid_weights = np.append(np.power(weights, 2), [bias])
        zero_function = []
        for j, weight in enumerate(weights):
            result = -sum([(self.__sigmoid(sigmoid_weights, input) - output) * 2 * weight * input[j] for input, output
                           in zip(train_input, train_output)])
            result -= 2 * laplacian * weight
            zero_function.append(result)
        result = -sum([(self.__sigmoid(sigmoid_weights, input) - output) * input[-1] for input, output
                       in zip(train_input, train_output)])
        zero_function.append(result)
        result = sum(weight for weight in sigmoid_weights[:-1])
        result -= len(train_input[0]) - 1
        zero_function.append(result)
        return zero_function

    def __sigmoid(self, weights: np.array, input: np.array) -> float:
        return expit(np.dot(weights, input))

class StackLayer(NormalizeLayer):
    """ The Stack Layer combines multiple layers into a single prediction by applying a Logistic Regression on the
    predictions of each layer. """

    def __init__(self, predict_layer: MultiLayer, train_layer: MultiLayer, splits: List[Set[int]]):
        """ Constructor of the Stack Layer.

        Arguments:
            predict_layer (MultiLayer): The MultiLayer which contains the layers of which the predictions get combined
                into a single prediction.
            train_layer (MultiLayer): The MultiLayer which contains the layers of which the predictions are used to
                train the Logistic Regression. This should of course correspond to the predict layer, but could be
                implemented slightly different, such that it can compute results quicker or that it weights certain
                layers lesser.
            splits (List[Set[int]]): The groups of number of players alive in which the aggregation happens.
        """
        super().__init__(InnerStackLayer(predict_layer, train_layer, splits))