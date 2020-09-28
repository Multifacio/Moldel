from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.ExamPass.ExamPassExtractor import ExamPassExtractor
from Layers.Layer import Layer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.MultiLayer.MultiplyAggregateLayer import MultiplyAggregateLayer
from sklearn.linear_model import LogisticRegression
from typing import Dict, Set, Tuple
import numpy as np

class InnerExamPassLayer(MultiLayer):
    def __init__(self, layer: Layer, dec_episode_weight: float, anova_f_significance: float, pca_explain: float,
                 max_splits: int):
        self.__layer = layer
        self.__dec_episode_weight = dec_episode_weight
        self.__anova_f_significance = anova_f_significance
        self.__pca_explain = pca_explain
        self.__max_splits = max_splits

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        prediction = self.__layer.compute_distribution(predict_season, latest_episode, train_seasons)
        extractor = ExamPassExtractor(predict_season, latest_episode, prediction, train_seasons, self.__dec_episode_weight,
                                      self.__anova_f_significance, self.__pca_explain, self.__max_splits)
        classifier, likelihood_cutoff = self.__training(extractor)
        return self.__predict(predict_season, extractor, classifier, likelihood_cutoff)

    def __training(self, extractor: ExamPassExtractor) -> Tuple[LogisticRegression, float]:
        train_input, train_output, likelihood_cutoff = extractor.get_train_data()
        classifier = LogisticRegression(solver = "lbfgs")
        classifier.fit(train_input, train_output)
        return classifier, likelihood_cutoff

    def __predict(self, predict_season: int, extractor: ExamPassExtractor, classifier: LogisticRegression,
                  likelihood_cutoff: float) -> Dict[Player, MultiLayerResult]:
        predict_input = extractor.get_predict_data()
        if predict_input is None:
            return {player: MultiLayerResult(np.array([]), False) for player in get_players_in_season(predict_season)}

        result = dict()
        for player in get_players_in_season(predict_season):
            if player in predict_input:
                predictions = []
                for input in predict_input[player]:
                    predictions.append(classifier.predict_proba(np.array([input]))[0][1])
                result[player] = MultiLayerResult(np.array(predictions), False)
            else:
                result[player] = MultiLayerResult(np.array([]), True)
        return result

class ExamPassLayer(MultiplyAggregateLayer):
    def __init__(self, layer: Layer, dec_episode_weight: float, anova_f_significance: float, pca_explain: float, max_splits: int):
        super().__init__(InnerExamPassLayer(layer, dec_episode_weight, anova_f_significance, pca_explain, max_splits))