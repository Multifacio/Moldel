from numpy.random import RandomState

from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.ExamDrop.ExamDropExtractor import ExamDropExtractor, PredictSample
from Layers.MultiLayer.EmptyMultiLayer import EmptyMultiLayer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.MultiLayer.MultiplyAggregateLayer import MultiplyAggregateLayer
from Layers.Special.PotentialMolLayer import PotentialMolLayer
from sklearn.linear_model import LogisticRegression
from typing import Dict, List, Set, Tuple
import numpy as np

class InnerExamDropLayer(MultiLayer):
    MAX_TRAIN_ITERATIONS = 1000 # The maximum iterations to train the Logistic Regression

    def __init__(self, min_cluster_size: int, spline_curves: int, random_generator: RandomState):
        self.__min_cluster_size = min_cluster_size
        self.__spline_curves = spline_curves
        self.__random_generator = random_generator

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        available_seasons = EXAM_DATA.keys()
        train_seasons = train_seasons.intersection(available_seasons)
        if predict_season not in available_seasons:
            return EmptyMultiLayer().predict(predict_season, latest_episode, train_seasons)

        extractor = ExamDropExtractor(predict_season, latest_episode, train_seasons, self.__min_cluster_size,
                                      self.__spline_curves)
        in_classifier, out_classifier = self.__training(extractor)
        predict_data = extractor.get_predict_data()
        if not predict_data:
            alive_players = EXAM_DATA[predict_season].get_alive_players(latest_episode)
            return EmptyMultiLayer(alive_players).predict(predict_season, latest_episode, train_seasons)

        return self.__predict(predict_season, latest_episode, predict_data, in_classifier, out_classifier)

    def __training(self, extractor: ExamDropExtractor) -> Tuple[LogisticRegression, LogisticRegression]:
        """ Execute the training phase of the Exam Drop Layer.

        Arguments:
            extractor (ExamDropExtractor): The extractor which delivers the training data.

        Returns:
            Two trained machine learning model used to make predictions. The first model makes predictions for cases
            where a player is in the answer and the second model makes predictions for cases where a player is out the
            answer.
        """
        train_input, train_output, in_answer, train_weights = extractor.get_train_data()

        in_input = [ti for ti, answer in zip(train_input, in_answer) if answer == 1.0]
        in_output = [to for to, answer in zip(train_output, in_answer) if answer == 1.0]
        in_weights = [tw for tw, answer in zip(train_weights, in_answer) if answer == 1.0]
        in_classifier = LogisticRegression(solver = "lbfgs", max_iter = self.MAX_TRAIN_ITERATIONS,
                                           random_state = self.__random_generator)
        in_classifier.fit(in_input, in_output, in_weights)

        out_input = [ti for ti, answer in zip(train_input, in_answer) if answer == 0.0]
        out_output = [to for to, answer in zip(train_output, in_answer) if answer == 0.0]
        out_weights = [tw for tw, answer in zip(train_weights, in_answer) if answer == 0.0]
        out_classifier = LogisticRegression(solver = "lbfgs", max_iter = self.MAX_TRAIN_ITERATIONS,
                                            random_state = self.__random_generator)
        out_classifier.fit(out_input, out_output, out_weights)
        return in_classifier, out_classifier

    def __predict(self, predict_season: int, latest_episode: int, predict_data: List[PredictSample],
            in_classifier: LogisticRegression, out_classifier: LogisticRegression) -> Dict[Player, MultiLayerResult]:
        """ Execute the prediction phase of the Exam Drop Layer.

        Arguments:
            predict_season (int): The season for which the predictions are made.
            latest_episode (int): The latest episode useable in the predict season.
            predict_data (List[PredictSample]): The prediction data with features used to make predictions.
            in_classifier (LogisticRegression): The machine learning model used to make predictions for cases where
                a player is in the answer.
            out_classifier (LogisticRegression): The machine learning model used to make predictions for cases where
                a player is out the answer.

        Returns:
            A dictionary with as key the players that participated in the prediction season and as value a
            MultiLayerResult which contains the predictions.
        """
        all_predictions = dict()
        season_players = get_players_in_season(predict_season)
        for player in season_players:
            all_predictions[player] = []

        alive_players = EXAM_DATA[predict_season].get_alive_players(latest_episode)
        for data in predict_data:
            in_likelihood = in_classifier.predict_proba(np.array([data.features]))[0][1]
            out_likelihood = out_classifier.predict_proba(np.array([data.features]))[0][1]
            if out_likelihood < in_likelihood:
                in_likelihood = out_likelihood = 1 / len(alive_players)
            in_likelihood = in_likelihood ** data.weight
            out_likelihood = out_likelihood ** data.weight
            for player in data.in_answer:
                all_predictions[player] = all_predictions[player] + [in_likelihood]
            for player in data.out_answer:
                all_predictions[player] = all_predictions[player] + [out_likelihood]

        return {player: MultiLayerResult(np.array(predictions), player not in alive_players)
                for player, predictions in all_predictions.items()}

class ExamDropLayer(PotentialMolLayer):
    """ The Exam Drop Layer predicts whether you are the Mol based on what dropouts have answered during the test. """

    def __init__(self, min_cluster_size: int, spline_curves: int, random_generator: RandomState):
        """ Constructor of the Exam Drop Layer

        Arguments:
            min_cluster_size (int): The minimum number of elements every cluster must have in the stable discretization
                of discrete features.
            spline_curves (int): The number of curves used for the natural spline encoding of the continuous features.
            random_generator (RandomState): The random generator used to generate random values.
        """
        super().__init__(MultiplyAggregateLayer(InnerExamDropLayer(min_cluster_size, spline_curves, random_generator),
                                                False))