from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_is_mol
from Layers.ExamDrop.ExamDropEncoder import ExamDropEncoder, TrainSample
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold, SelectFpr, f_classif
from sklearn.preprocessing import PolynomialFeatures
from typing import List, NamedTuple, Set, Tuple, Union
import numpy as np
import sys

FeatureSample = NamedTuple("FeatureSample", [("features", np.array), ("correct_answer", bool)])
PredictSample = NamedTuple("PredictSample", [("features", np.array), ("correct_players", Set[Player]),
                                             ("episode_players", Set[Player])])
class ExamDropExtractor:
    """ The Exam Drop Extractor deals with obtaining the train data and predict data for the Exam Layer. For this we use
    the following techniques: polynomial transformations, local outlier removal, zero variance removal, ANOVA_F filter
    and PCA. Furthermore we resample the data such that every episode has the same likelihood of being picked. """

    def __init__(self, predict_season: int, predict_episode: int, train_seasons: Set[int], anova_f_significance: float,
                 pca_explain: float, poly_degree: int):
        """ Constructor of the Exam Drop Extractor

        Arguments:
            predict_season (int): The season for which we make the prediction.
            predict_episode (int): The latest episode in the predict season that could be used.
            train_seasons (Set[int]): The seasons which are used as train data.
        """
        self.__predict_season = predict_season
        self.__predict_episode = predict_episode
        self.__train_seasons = train_seasons
        self.__anova_f_significance = anova_f_significance
        self.__pca_explain = pca_explain
        self.__poly_degree = poly_degree

    def get_train_data(self) -> Tuple[np.array, np.array, np.array]:
        train_input, train_output, train_weights = self.__get_weighted_train_data()
        self.__poly_transform = PolynomialFeatures(degree = self.__poly_degree, include_bias = False)
        train_input = self.__poly_transform.fit_transform(train_input)

        self.__zero_variance_remover = VarianceThreshold()
        train_input = self.__zero_variance_remover.fit_transform(train_input)
        self.__anova_f_filter = SelectFpr(f_classif, alpha = self.__anova_f_significance)
        train_input = self.__anova_f_filter.fit_transform(train_input, train_output)
        self.__pca = PCA(n_components = self.__pca_explain)
        train_input = self.__pca.fit_transform(train_input)
        print(len(train_input))
        print(len(train_input[0]))

        return train_input, train_output, train_weights

    def get_predict_data(self) -> Union[List[PredictSample], None]:
        predict_data = self.__get_season_data(self.__predict_season, self.__predict_episode)
        if not predict_data:
            return None

        predict_input = np.array([ExamDropEncoder.extract_features(sample, self.__predict_episode) for sample in predict_data])
        predict_input = self.__poly_transform.transform(predict_input)
        predict_input = self.__zero_variance_remover.transform(predict_input)
        predict_input = self.__anova_f_filter.transform(predict_input)
        predict_input = self.__pca.transform(predict_input)

        predict_samples = []
        for input, data in zip(predict_input, predict_data):
            predict_samples.append(PredictSample(input, data.answer, set(data.exam_episode.players)))
        return predict_samples

    def __get_weighted_train_data(self) -> Tuple[np.array, np.array, np.array]:
        train_data = []
        for season in self.__train_seasons:
            train_data.extend(self.__get_season_data(season, sys.maxsize))

        mapped_data = dict()
        for sample in train_data:
            key = (sample.season, sample.exam_episode.id)
            answer_correct = any([get_is_mol(player) for player in sample.answer])
            sample = ExamDropEncoder.extract_features(sample, sys.maxsize)
            mapped_data[key] = mapped_data.get(key, []) + [FeatureSample(sample, answer_correct)]

        train_input = []
        train_output = []
        train_weights = []
        for samples in mapped_data.values():
            train_input.extend([sample.features for sample in samples])
            train_output.extend([1.0 if sample.correct_answer else 0.0 for sample in samples])
            train_weights.extend([1 / len(samples) for _ in samples])

        return np.array(train_input), np.array(train_output), np.array(train_weights)

    @staticmethod
    def __get_season_data(season_num: int, max_episode: int) -> List[TrainSample]:
        season = EXAM_DATA[season_num]
        drop_players = season.get_drop_mapping(DropType.EXECUTION_DROP, max_episode)
        all_answers = season.get_all_answers(set(drop_players.keys()), max_episode)
        season_data = []
        for answer in all_answers:
            exam_episode = answer.episode
            drop_episodes = drop_players[answer.player]
            drop_episodes = [episode for episode in drop_episodes if exam_episode <= episode]
            if drop_episodes:
                season_data.append(TrainSample(answer.player, season_num, min(drop_episodes), answer.episode,
                                               answer.question, answer.answer))
        return season_data