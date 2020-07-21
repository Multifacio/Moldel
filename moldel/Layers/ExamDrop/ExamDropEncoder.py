from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Dataclasses.Episode import Episode
from Data.ExamData.Dataclasses.Question import Question
from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from statistics import mean
from typing import NamedTuple, Set, Tuple
import numpy as np

TrainSample = NamedTuple("TrainSample", [("player", Player), ("season", int), ("drop_episode", Episode),
                                         ("exam_episode", Episode), ("question", Question), ("answer", Set[Player])])
class ExamDropEncoder:
    """ The Exam Drop Encoder deals with the encoding of the features used for the Exam Drop Layer. """

    EXEMPTION_JOKER_VALUE = 1000 # The value of an exemption expressed in jokers.

    @classmethod
    def extract_features(self, sample: TrainSample, max_episode: int) -> np.array:
        """ Convert a Train Sample into an array of features.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.
            max_episode (int): Only information which is known before/at this episode might be used.

        Returns:
            An array of features.
        """
        drop_episode, exam_episode, fail_test, execution_episode = self.__episode_features(sample)
        num_players_drop, num_players_drop_reciprocal, num_players_exam, num_players_exam_reciprocal = \
            self.__num_players_features(sample)
        entropy, num_answer_players, num_answer_players_reciprocal, answer_probability = self.__answer_features(sample)
        num_same_pickers, num_same_pickers_reciprocal, prob_same_picker = self.__same_pick_features(sample, max_episode)
        drop_jokers2_more, drop_jokers1_more, drop_jokers1_less = self.__joker_discretization(sample.player, sample.drop_episode)
        exam_jokers2_more, exam_jokers1_more, exam_jokers1_less = self.__joker_discretization(sample.player, sample.exam_episode)
        weighted_jokers2_more, weighted_jokers1_more, weighted_jokers1_less = self.__weighted_past_jokers(sample)
        drop_player_jokers_more, drop_player_jokers_less = self.__exam_joker_features(sample.player, sample.exam_episode)

        return np.array([drop_episode, exam_episode, fail_test, execution_episode, num_players_drop,
            num_players_drop_reciprocal, num_players_exam, num_players_exam_reciprocal, entropy, num_answer_players,
            num_answer_players_reciprocal, answer_probability, num_same_pickers, num_same_pickers_reciprocal,
            prob_same_picker, drop_jokers2_more, drop_jokers1_more, drop_jokers1_less, exam_jokers2_more,
            exam_jokers1_more, exam_jokers1_less, weighted_jokers2_more, weighted_jokers1_more, weighted_jokers1_less,
            drop_player_jokers_more, drop_player_jokers_less])

    @staticmethod
    def __episode_features(sample: TrainSample) -> Tuple[float, ...]:
        """ Get all features related to the drop and exam episodes.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            The feature values.
        """
        return sample.drop_episode.episode_number(), sample.exam_episode.episode_number(), \
               sample.drop_episode == sample.exam_episode, sample.exam_episode.result.drop == DropType.EXECUTION_DROP

    @staticmethod
    def __num_players_features(sample: TrainSample) -> Tuple[float, ...]:
        """ Get all features related to the number of players in the drop and exam episodes.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            The feature values.
        """
        num_players_drop = len(sample.drop_episode) - 1
        num_players_exam = len(sample.exam_episode) - 1
        return num_players_drop, 1 / num_players_drop, num_players_exam, 1 / num_players_exam

    @staticmethod
    def __answer_features(sample: TrainSample) -> Tuple[float, ...]:
        """ Get all simple features related to the answers given in the exam episode.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            The feature values.
        """
        self_excluding_answer = sample.answer.difference({sample.player})
        return sample.question.entropy(), len(self_excluding_answer), 1 / max(len(self_excluding_answer), 1), \
               len(self_excluding_answer) / (len(sample.exam_episode.players) - 1)

    @staticmethod
    def __same_pick_features(sample: TrainSample, max_episode: int) -> Tuple[float, ...]:
        """ Get all features related to whether other players also select the same Mol.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            The feature values.
        """
        picked_answer = sample.answer.difference({sample.player})
        probabilities = sample.exam_episode.same_pick_probabilities(picked_answer, max_episode)
        num_same_pickers = sum([prob > 0.0 for prob in probabilities.values()])
        prob_same_picker = mean([prob for player, prob in probabilities.items() if player != sample.player])
        return num_same_pickers / len(sample.exam_episode.players), 1 / max(num_same_pickers, 1), prob_same_picker

    @classmethod
    def __weighted_past_jokers(self, sample: TrainSample) -> Tuple[float, ...]:
        """ Get the features related to the overall usage of jokers/exemptions in previous episodes.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            The feature values.
        """
        season = EXAM_DATA[sample.season]
        weights = jokers2_more = jokers1_more = jokers1_less = []
        for episode in season.episodes.values():
            if episode <= sample.drop_episode:
                weights.append(1 / (len(episode) - 1))
                joker_features = self.__joker_discretization(sample.player, episode)
                jokers2_more.append(joker_features[0])
                jokers1_more.append(joker_features[1])
                jokers1_less.append(joker_features[2])

        return np.average(jokers2_more, weights=weights), np.average(jokers1_more, weights=weights), \
               np.average(jokers1_less, weights=weights)

    @classmethod
    def __joker_discretization(self, player: Player, episode: Episode) -> Tuple[float, ...]:
        """ Get the features related to joker & exemption usage in the exam and drop episode of the given player
        compared to the other players.

        Arguments:
            player (Player): The player of which we measure its joker & exemption usage.
            episode (Episode): The episode in which we measure the joker & exemption usage.

        Returns:
            The feature values.
        """
        joker_usage = episode.total_joker_usage(self.EXEMPTION_JOKER_VALUE)
        num_players = len(episode) - 1
        jokers2_more = sum([usage >= joker_usage[player] + 2 for usage in joker_usage.values()]) / num_players
        jokers1_more = sum([usage == joker_usage[player] + 1 for usage in joker_usage.values()]) / num_players
        jokers1_less = sum([usage <= joker_usage[player] - 1 for usage in joker_usage.values()]) / num_players
        return jokers2_more, jokers1_more, jokers1_less

    @classmethod
    def __exam_joker_features(self, player: Player, episode: Episode) -> Tuple[float, ...]:
        """ Get the features related to joker & exemption usage in the exam and drop episode of the given player
        compared to the player(s) that dropped off.

        Arguments:
            player (Player): The player of which we measure its joker & exemption usage compared to the player(s) that
                dropped off.
            episode (Episode): The episode in which we measure the joker & exemption usage.

        Returns:
            The feature values.
        """
        joker_usage = episode.total_joker_usage(self.EXEMPTION_JOKER_VALUE)
        if episode.result.drop == DropType.EXECUTION_DROP:
            drop_more_jokers = any([joker_usage[p] > joker_usage[player] for p in episode.result.players])
            drop_less_jokers = any([joker_usage[p] < joker_usage[player] for p in episode.result.players])
            return drop_more_jokers, drop_less_jokers
        else:
            return 0.5, 0.5