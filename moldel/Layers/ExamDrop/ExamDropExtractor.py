from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_is_mol
from Layers.ExamDrop.ExamDropEncoder import ExamDropEncoder, TrainSample
from Tools.Encoders.NaturalSplineEncoding import NaturalSplineEncoding
from Tools.Encoders.StableDiscretizer import StableDiscretizer
from numpy.random import RandomState
from queue import PriorityQueue
from scipy.stats import mannwhitneyu
from typing import List, NamedTuple, Set, Tuple
import numpy as np
import scipy as sc
import sys

FeatureSample = NamedTuple("FeatureSample", [("features", np.array), ("is_mol", bool)])
PredictSample = NamedTuple("PredictSample", [("in_answer", Set[Player]), ("out_answer", Set[Player]),
                                             ("features", np.array), ("weight", float)])
class ExamDropExtractor:
    """ The Exam Drop Extractor deals with obtaining the train data and predict data for the Exam Layer. For this we use
    a stable discretization technique for discrete feature and natural spline encoding for continuous features. """

    def __init__(self, predict_season: int, predict_episode: int, train_seasons: Set[int], min_cluster_size: int,
                 spline_curves: int, random_generator: RandomState):
        """ Constructor of the Exam Drop Extractor

        Arguments:
            predict_season (int): The season for which we make the prediction.
            predict_episode (int): The latest episode in the predict season that could be used.
            train_seasons (Set[int]): The seasons which are used as train data.
            min_cluster_size (int): The minimum number of elements every cluster must have in the stable discretization
                of discrete features.
            spline_curves (int): The number of curves used for the natural spline encoding of the continuous features.
            random_generator (RandomState): The random generator used to generate random values.
        """
        self.__predict_season = predict_season
        self.__predict_episode = predict_episode
        self.__train_seasons = train_seasons
        self.__min_cluster_size = min_cluster_size
        self.__spline_curves = spline_curves
        self.__random_generator = random_generator

    def get_train_data(self) -> Tuple[np.array, np.array, np.array, np.array]:
        """ Get the formatted and sampled train data with train weights useable for machine learning algorithms.

        Returns:
            The train input, train output, answered_on and train weights in this order. The train input is a 2d array
            where each row represents a different train element. The train output is 1d array of labels, such that the
            ith row of the train input corresponds to the ith element of the train output. The answered on is a 1d array
            of binary values where a 1 indicates if the selected player is included in the answer and 0 otherwise. The
            train weights is an array of weights indicating how important every train element is.
        """
        train_data = []
        for season in self.__train_seasons:
            train_data.extend(self.get_season_data(season, sys.maxsize, True))
        train_input = np.array([ExamDropEncoder.extract_features(sample, sys.maxsize) for sample in train_data])
        train_output = np.array([1.0 if get_is_mol(sample.selected_player) else 0.0 for sample in train_data])
        answered_on = np.array([1.0 if sample.selected_player in sample.answer else 0.0 for sample in train_data])
        m = ExamDropEncoder.NUM_CONTINUOUS_FEATURES

        self.__discretizer = StableDiscretizer(self.__min_cluster_size, self.__random_generator)
        discrete_input = self.__discretizer.fit_transform(train_input[:, :-m])
        self.__spline_encoder = NaturalSplineEncoding([self.__spline_curves for _ in range(m)])
        continuous_input = self.__spline_encoder.fit_transform(train_input[:, -m:])
        train_input = np.concatenate((discrete_input, continuous_input), axis = 1)
        return train_input, train_output, answered_on, self.__get_train_weights(train_data)

    def get_predict_data(self) -> List[PredictSample]:
        """ Get all formatted predict data useable for the machine learning algorithms to do a prediction.

        Returns:
            A list of prediction samples, where a prediction sample consists of a set of players included in the answer
            and not included in the answer. Also a prediction sample consist of the features for the participants
            included in the answer and not included in the answer.
        """
        predict_data = self.get_season_data(self.__predict_season, self.__predict_episode, False)
        if not predict_data:
            return []
        m = ExamDropEncoder.NUM_CONTINUOUS_FEATURES

        predict_input = np.array([ExamDropEncoder.extract_features(sample, self.__predict_episode) for sample in predict_data])
        discrete_input = self.__discretizer.transform(predict_input[:, :-m])
        continuous_input = self.__spline_encoder.transform(predict_input[:, -m:])
        predict_input = np.concatenate((discrete_input, continuous_input), axis = 1)

        predict_samples = []
        weights = self.__get_train_weights(predict_data)
        for data, features, weight in zip(predict_data, predict_input, weights):
            in_answer = data.answer
            out_answer = set(data.exam_episode.players).difference(data.answer)
            predict_samples.append(PredictSample(in_answer, out_answer, features, weight))
        return predict_samples

    @staticmethod
    def get_season_data(season_num: int, max_episode: int, training_data: bool) -> List[TrainSample]:
        """ Get all raw answer data from a season.

        Arguments:
            season_num (int): The season from which we obtain this data.
            max_episode (int): The latest episode which can still be extracted. If this value is sys.maxsize then all
                raw answer data is obtained from this season.
            training_data (bool): True if the data is used as training data and false if the data is used as prediction
                data. The difference is that in case it is used for predictions we don't have a selected_player which
                we have if it is used for training.

        Returns:
            A list of prediction samples, where a prediction sample consists of a set of players included in the answer,
            not included in the answer and feature representation.
        """
        season = EXAM_DATA[season_num]
        drop_players = season.get_drop_mapping(DropType.EXECUTION_DROP, max_episode)
        all_answers = season.get_all_answers(set(drop_players.keys()), max_episode)
        season_data = []
        for answer in all_answers:
            exam_episode = answer.episode
            drop_episodes = drop_players[answer.player]
            drop_episodes = [episode for episode in drop_episodes if exam_episode <= episode]
            if drop_episodes:
                if training_data:
                    for player in exam_episode.players:
                        season_data.append(TrainSample(answer.player, season_num, min(drop_episodes), answer.episode,
                                                       answer.question, answer.answer, player))
                else:
                    season_data.append(TrainSample(answer.player, season_num, min(drop_episodes), answer.episode,
                                                       answer.question, answer.answer, None))
        return season_data

    @staticmethod
    def __get_train_weights(train_data: List[TrainSample]) -> np.array:
        """ Get the weight for the training data, which is 1 / num_answers where num_answers is the number of answers
        given by that player in that episode.

        Arguments:
            train_data (List[TrainSample]): All raw train data from which it is extracted to which episode an answer
                belongs.

        Returns:
            An 1d array of weights which pairwise corresponds to the train_data (and therefore pairwise corresponds
            with each row in the train input).
        """
        train_weights = []
        for sample in train_data:
            num_answers = sample.exam_episode.get_all_answers({sample.player}, sys.maxsize)
            train_weights.append(1 / len(num_answers))
        return np.array(train_weights)