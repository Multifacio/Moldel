from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Exams.All import EXAM_DATA
from Data.LastEpisodes import get_last_episode
from Data.Player import Player
from Data.PlayerData import get_is_mol
from Layers.ExamDrop.ExamDropExtractor import ExamDropExtractor
from Layers.ExamPass.ExamPassEncoder import ExamPassEncoder, ExamPassSample
from sklearn.decomposition import PCA
from sklearn.feature_selection import VarianceThreshold, SelectFpr, f_classif
from sklearn.preprocessing import PolynomialFeatures
from typing import Dict, List, Set, Tuple, Union
from Validators.Precomputer import Precomputer
import itertools as it
import numpy as np

class ExamPassExtractor:
    PRECOMPUTED_DISTRIBUTIONS_FOLDER = "ForExamPass"

    def __init__(self, predict_season: int, predict_episode: int, prediction: Dict[Player, float], train_seasons: Set[int],
                 dec_episode_weight: float, anova_f_significance: float, pca_explain: float, poly_degree: int):
        """ Constructor of the Exam Drop Extractor.

        Arguments:
            predict_season (int): The season for which we make the prediction.
            predict_episode (int): The latest episode in the predict season that could be used.
            prediction (Dict[Player, float]): The prediction of the other layers for this layer.
            train_seasons (Set[int]): The seasons which are used as train data.
            anova_f_significance (float): Only features with a p-value lower than this value will be selected by the
                ANOVA F filter.
            pca_explain (float): PCA will select the least number of components that at least explain this amount
                of variance in the features.
            max_splits (int): How many additional bins should be used to discretize the features.
        """
        self.__predict_season = predict_season
        self.__predict_episode = predict_episode
        self.__prediction = prediction
        self.__train_seasons = train_seasons
        self.__dec_episode_weight = dec_episode_weight
        self.__anova_f_significance = anova_f_significance
        self.__pca_explain = pca_explain
        self.__poly_degree = poly_degree

    def get_train_data(self) -> Tuple[np.array, np.array, float]:
        """ Get the formatted and sampled train data useable for machine learning algorithms.

        Returns:
            The train input, train output and train weights in this order. The train input is a 2d array where each row
            represents a different train element. The train output is 1d array of labels, such that the ith row of the
            train input corresponds to the ith element of the train output.
        """
        train_data = self.__get_train_samples()
        train_input = np.array([ExamPassEncoder.extract_features(sample) for sample in train_data])
        train_output = np.array([1.0 if get_is_mol(sample.player) else 0.0 for sample in train_data])

        self.__poly_transform = PolynomialFeatures(degree = self.__poly_degree, include_bias = False)
        train_input = self.__poly_transform.fit_transform(train_input)
        self.__zero_variance_remover = VarianceThreshold()
        train_input = self.__zero_variance_remover.fit_transform(train_input)
        self.__anova_f_filter = SelectFpr(f_classif, alpha = self.__anova_f_significance)
        train_input = self.__anova_f_filter.fit_transform(train_input, train_output)
        self.__pca = PCA(n_components = self.__pca_explain)
        train_input = self.__pca.fit_transform(train_input)

        return train_input, train_output, np.sum(train_output) / len(train_output)

    def get_predict_data(self) -> Union[Dict[Player, List[np.array]], None]:
        predict_data = self.__get_predict_samples()
        if not predict_data:
            return None
        predict_input = np.array([ExamPassEncoder.extract_features(sample) for sample in predict_data])

        predict_input = self.__poly_transform.transform(predict_input)
        predict_input = self.__zero_variance_remover.transform(predict_input)
        predict_input = self.__anova_f_filter.transform(predict_input)
        predict_input = self.__pca.transform(predict_input)

        grouped_input = dict()
        for data, input in zip(predict_data, predict_input):
            grouped_input[data.player] = grouped_input.get(data.player, []) + [input]
        return grouped_input

    def __get_train_samples(self) -> List[ExamPassSample]:
        precomputer = Precomputer(self.PRECOMPUTED_DISTRIBUTIONS_FOLDER)
        distributions = dict()
        for season in self.__train_seasons:
            for episode in range(1, get_last_episode(season) + 1):
                distribution = precomputer.load_distribution(season, episode)
                if distribution is None:
                    continue
                distributions[(season, episode)] = distribution

        data = []
        for season_id in self.__train_seasons:
            season = EXAM_DATA[season_id]
            final_players = season.get_alive_players(get_last_episode(season_id))
            for exam_episode, latest_episode in it.product(season.episodes.values(), repeat = 2):
                episode_id = latest_episode.episode_number()
                if exam_episode > latest_episode or not exam_episode.result.drop == DropType.EXECUTION_DROP or \
                        (season_id, episode_id) not in distributions:
                    continue

                distribution = distributions[(season_id, episode_id)]
                for player in final_players:
                    covered = exam_episode.get_covered(player, episode_id)
                    data.append(ExamPassSample(player, latest_episode, exam_episode, distribution, covered))
        return data

    def __get_predict_samples(self) -> List[ExamPassSample]:
        data = []
        season = EXAM_DATA[self.__predict_season]
        latest_episode = season.get_latest_episode(self.__predict_episode)
        if latest_episode is None:
            return []
        for exam_episode in season.episodes.values():
            if exam_episode > latest_episode or not exam_episode.result.drop == DropType.EXECUTION_DROP:
                continue

            for player in season.get_alive_players(self.__predict_episode):
                covered = exam_episode.get_covered(player, self.__predict_episode)
                data.append(ExamPassSample(player, latest_episode, exam_episode, self.__prediction, covered))
        return data