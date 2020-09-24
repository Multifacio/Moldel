from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.ExamDrop.ExamDropExtractor import ExamDropExtractor, PredictSample
from Layers.MultiLayer.EmptyMultiLayer import EmptyMultiLayer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.MultiLayer.MultiplyAggregateLayer import MultiplyAggregateLayer
from sklearn.linear_model import LogisticRegression
from typing import Dict, List, Set
import numpy as np

class InnerExamDropLayer(MultiLayer):
    def __init__(self, anova_f_significance: float, pca_explain: float, max_splits: int):
        self.__anova_f_significance = anova_f_significance
        self.__pca_explain = pca_explain
        self.__max_splits = max_splits

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        available_seasons = EXAM_DATA.keys()
        train_seasons = train_seasons.intersection(available_seasons)
        if predict_season not in available_seasons:
            return EmptyMultiLayer().predict(predict_season, latest_episode, train_seasons)

        extractor = ExamDropExtractor(predict_season, latest_episode, train_seasons, self.__anova_f_significance,
                                      self.__pca_explain, self.__max_splits)
        classifier = self.__training(extractor)
        predict_data = extractor.get_predict_data()
        if not predict_data:
            alive_players = EXAM_DATA[predict_season].get_alive_players(latest_episode)
            return EmptyMultiLayer(alive_players).predict(predict_season, latest_episode, train_seasons)

        return self.__predict(predict_season, latest_episode, predict_data, classifier)

    def __training(self, extractor: ExamDropExtractor) -> LogisticRegression:
        """ Execute the training phase of the Exam Drop Layer.

        Arguments:
            extractor (ExamDropExtractor): The extractor which delivers the training data.

        Returns:
            The trained machine learning model used to make predictions.
        """
        train_input, train_output, train_weights = extractor.get_train_data()
        classifier = LogisticRegression(solver="lbfgs")
        classifier.fit(train_input, train_output, train_weights)
        return classifier

    def __predict(self, predict_season: int, latest_episode: int, predict_data: List[PredictSample],
                  classifier: LogisticRegression) -> Dict[Player, MultiLayerResult]:
        """ Execute the prediction phase of the Exam Drop Layer.

        Arguments:
            predict_season (int): The season for which the predictions are made.
            latest_episode (int): The latest episode useable in the predict season.
            predict_data (List[PredictSample]): The prediction data with features used to make predictions.
            classifier (LogisticRegression): The machine learning model used to make predictions.

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
            in_likelihood = classifier.predict_proba(np.array([data.in_features]))[0][1]
            out_likelihood = classifier.predict_proba(np.array([data.out_features]))[0][1]
            if out_likelihood < in_likelihood:
                in_likelihood = out_likelihood = 1 / len(alive_players)
            for player in data.in_answer:
                all_predictions[player] = all_predictions[player] + [in_likelihood]
            for player in data.out_answer:
                all_predictions[player] = all_predictions[player] + [out_likelihood]

        return {player: MultiLayerResult(np.array(predictions), player not in alive_players) for player, predictions in \
                all_predictions.items()}

class ExamDropLayer(MultiplyAggregateLayer):
    def __init__(self, anova_f_significance: float, pca_explain: float, max_splits: int):
        """ Constructor of the Exam Drop Layer

        Arguments:
            anova_f_significance (float): Only features with a p-value lower than this value will be selected by the
                ANOVA F filter.
            pca_explain (float): PCA will select the least number of components that at least explain this amount
                of variance in the features.
            max_splits (int): How many additional bins should be used to discretize the features.
        """
        super().__init__(InnerExamDropLayer(anova_f_significance, pca_explain, max_splits), False)