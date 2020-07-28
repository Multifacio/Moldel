from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.ExamDrop.ExamDropExtractor import ExamDropExtractor, PredictSample
from Layers.MultiLayer.GaussianNaiveBayesStacking import GaussianNaiveBayesStacking
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from numpy.random import RandomState
from sklearn.linear_model import LogisticRegression
from typing import Dict, List, Set
import numpy as np

class InnerExamDropLayer(MultiLayer):
    def __init__(self, anova_f_significance: float, pca_explain: float, poly_degree: int):
        self.__anova_f_significance = anova_f_significance
        self.__pca_explain = pca_explain
        self.__poly_degree = poly_degree

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        available_seasons = EXAM_DATA.keys()
        train_seasons = train_seasons.intersection(available_seasons)
        if predict_season not in available_seasons or not train_seasons:
            return dict()

        extractor = ExamDropExtractor(predict_season, latest_episode, train_seasons, self.__anova_f_significance,
                                      self.__pca_explain, self.__poly_degree)
        classifier = self.__training(extractor)
        predict_input = extractor.get_predict_data()
        if predict_input is None:
            return dict()

        return self.__predict(predict_season, latest_episode, predict_input, classifier)

    def __training(self, extractor: ExamDropExtractor) -> LogisticRegression:
        train_input, train_output, train_weights = extractor.get_train_data()
        classifier = LogisticRegression(solver="lbfgs")
        classifier.fit(train_input, train_output, train_weights)
        return classifier

    def __predict(self, predict_season: int, latest_episode: int, predict_input: List[PredictSample],
                  classifier: LogisticRegression) -> Dict[Player, MultiLayerResult]:
        all_predictions = dict()
        season_players = get_players_in_season(predict_season)
        for player in season_players:
            all_predictions[player] = []

        for input in predict_input:
            for player in input.episode_players:
                correct_probability = classifier.predict_proba(np.array([input.features]))[0][1]
                num_wrong_players = len(input.episode_players) - len(input.correct_players)
                single_probability = correct_probability / len(input.correct_players) if player in \
                    input.correct_players else (1 - correct_probability) / num_wrong_players
                all_predictions[player] = all_predictions[player] + [single_probability]

        alive_players = EXAM_DATA[predict_season].get_alive_players(latest_episode)
        return {player: MultiLayerResult(np.array(predictions), player not in alive_players) for player, predictions in \
                all_predictions.items()}

class ExamDropLayer(GaussianNaiveBayesStacking):
    def __init__(self, anova_f_significance: float, pca_explain: float, poly_degree: int, sampling_significance: float,
                 random_generator: RandomState):
        super().__init__(InnerExamDropLayer(anova_f_significance, pca_explain, poly_degree), sampling_significance,
                         random_generator)