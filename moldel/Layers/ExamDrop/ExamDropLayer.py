from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.ExamDrop.ExamDropExtractor import ExamDropExtractor
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from sklearn.linear_model import LogisticRegression
from typing import Set, Dict
import numpy as np

class InnerExamDropLayer(Layer):
    def __init__(self, outlier_neighbors: int, anova_f_significance: float, pca_explain: float, poly_degree: int):
        self.__outlier_neighbors = outlier_neighbors
        self.__anova_f_significance = anova_f_significance
        self.__pca_explain = pca_explain
        self.__poly_degree = poly_degree

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        available_seasons = EXAM_DATA.keys()
        train_seasons = train_seasons.intersection(available_seasons)
        if predict_season not in available_seasons or not train_seasons:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        extractor = ExamDropExtractor(predict_season, latest_episode, train_seasons, self.__outlier_neighbors,
                                      self.__anova_f_significance, self.__pca_explain, self.__poly_degree)
        train_input, train_output = extractor.get_train_data()
        classifier = LogisticRegression(solver="lbfgs")
        classifier.fit(train_input, train_output)

        season_players = get_players_in_season(predict_season)
        alive_players = EXAM_DATA[predict_season].get_alive_players(latest_episode)
        distribution = dict()
        for player in season_players:
            distribution[player] = 1.0 if player in alive_players else 0.0

        predict_input = extractor.get_predict_data()
        for input in predict_input:
            correct_probability = classifier.predict_proba(np.array([input.features]))[1]
            single_correct_probability = correct_probability / len(input.correct_players)
            single_wrong_probability = (1 - correct_probability) / len(input.wrong_players)
            for player in alive_players:
                distribution[player] *= single_correct_probability if player in input.correct_players else \
                    single_wrong_probability

        return distribution

class ExamDropLayer(NormalizeLayer):
    def __init__(self, outlier_neighbors: int, anova_f_significance: float, pca_explain: float, poly_degree: int):
        super().__init__(InnerExamDropLayer(outlier_neighbors, anova_f_significance, pca_explain, poly_degree))