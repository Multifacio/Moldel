from Data.LastEpisodes import get_last_episode
from Data.Player import Player
from Data.PlayerData import get_is_mol
from Layers.Layer import Layer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.Special.NormalizeLayer import NormalizeLayer
from scipy.special import logit
from sklearn.linear_model import LogisticRegression
from typing import Dict, List, Set, Tuple
import numpy as np

class InnerStackLayer(Layer):
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
        classifier = self.__train(train_seasons, alives_group)
        return self.__stack_predictions(prediction, classifier, len(predict_alive))

    def __train(self, train_seasons: Set[int], alives_group: Set[int]) -> LogisticRegression:
        """ Train the Stack Layer.

        Arguments:
            train_seasons (Set[int]): All seasons used for training the stacking algorithm.
            alives_group (Set[int]): Only episodes with any of these numbers of players that could still potentially
                be the mol are used as training data.

        Returns:
            The classifier used to predict the mol based on the predictions of the layers.
        """
        train_input, train_output = self.__get_train_data(train_seasons, alives_group)
        classifier = LogisticRegression(solver = "lbfgs")
        classifier.fit(train_input, train_output)
        return classifier

    def __stack_predictions(self, prediction: Dict[Player, MultiLayerResult], classifier: LogisticRegression,
                            num_alives: int) -> Dict[Player, float]:
        """ Stack the predictions.

        Arguments:
            prediction (Dict[Player, MultiLayerResult]): All predictions for every player.
            classifier (Set[int]): The classifier used to predict the mol based on the predictions of the layers.
            num_alives (int): How many players are alive in the last prediction episode.

        Returns:
            The prediction for every player after stacking all predictions
        """
        return {p: 0.0 if r.exclusion else classifier.predict_proba(np.array([self.__input_encoding(r, num_alives)]))[0][1]
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
        return logit(likelihoods)

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