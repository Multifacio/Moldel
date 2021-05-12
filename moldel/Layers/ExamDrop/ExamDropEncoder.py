from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Dataclasses.Episode import Episode
from Data.ExamData.Dataclasses.Question import Question
from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from statistics import mean
from typing import NamedTuple, Set, Tuple, Union
import numpy as np

# If the selected player is a bool value then the meaning is whether that player is included in the answer (True) or
# not included in the answer (False).
TrainSample = NamedTuple("TrainSample", [("player", Player), ("season", int), ("drop_episode", Episode),
                                         ("exam_episode", Episode), ("question", Question), ("answer", Set[Player]),
                                         ("selected_player", Union[Player, None])])
class ExamDropEncoder:
    """ The Exam Drop Encoder deals with the encoding of the features used for the Exam Drop Layer. """
    FEATURE_NAMES = ["Exam Episode Number", "Drop Episode Number", "Fail Executie", "Real Executie", "Exam Players",
                     "Drop Players", "Answer Players",  "Same Pickers", "Drop Test Jokers More", "Drop Test Jokers Less",
                     "Exam Test Jokers More", "Exam Test Jokers Less", "Drop More Jokers", "Drop Less Jokers",
                     "Entropy", "Answer Probability", "Probability Same Picker"]
    NUM_CONTINUOUS_FEATURES = 3 # The number of continuous features, which should always be the last features.

    MAX_EPISODE_NUMBER = 9 # The highest possible episode number.
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
        exam_dropouts = set(sample.exam_episode.result.players) if sample.exam_episode.result.drop == \
            DropType.EXECUTION_DROP else set()
        drop_dropouts = set(sample.drop_episode.result.players)
        drop_episode, exam_episode, fail_test, execution_episode = self.__episode_features(sample)
        num_players_drop, num_players_exam = self.__num_players_features(sample)
        entropy, num_answer_players, answer_probability = self.__answer_features(sample)
        num_same_pickers, prob_same_picker = self.__same_pick_features(sample, max_episode, exam_dropouts)
        drop_jokers_more, drop_jokers_less = self.__joker_discretization(sample.player, sample.drop_episode, drop_dropouts)
        exam_jokers_more, exam_jokers_less = self.__joker_discretization(sample.player, sample.exam_episode, exam_dropouts)
        drop_player_jokers_more, drop_player_jokers_less = self.__exam_joker_features(sample.player, sample.exam_episode)

        return np.array([exam_episode, drop_episode, fail_test, execution_episode, num_players_exam, num_players_drop,
            num_answer_players, num_same_pickers, drop_jokers_more, drop_jokers_less, exam_jokers_more,
            exam_jokers_less, drop_player_jokers_more, drop_player_jokers_less,
            entropy, answer_probability, prob_same_picker])

    @classmethod
    def __episode_features(self, sample: TrainSample) -> Tuple[float, ...]:
        """ Get all features related to the drop and exam episodes.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            The feature values.
        """
        return min(sample.drop_episode.episode_number(), self.MAX_EPISODE_NUMBER), \
               min(sample.exam_episode.episode_number(), self.MAX_EPISODE_NUMBER), \
               sample.drop_episode == sample.exam_episode, sample.exam_episode.result.drop == DropType.EXECUTION_DROP

    @staticmethod
    def __num_players_features(sample: TrainSample) -> Tuple[float, ...]:
        """ Get all features related to the number of players in the drop and exam episodes.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            The feature values.
        """
        return len(sample.drop_episode) - 1, len(sample.exam_episode) - 1

    @staticmethod
    def __answer_features(sample: TrainSample) -> Tuple[float, ...]:
        """ Get all simple features related to the answers given in the exam episode.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            The feature values.
        """
        self_excluding_answer = sample.answer.difference({sample.player})
        return sample.question.entropy(), len(self_excluding_answer), \
               len(self_excluding_answer) / (len(sample.exam_episode.players) - 1)

    @staticmethod
    def __same_pick_features(sample: TrainSample, max_episode: int, exam_dropouts: Set[Player]) -> Tuple[float, ...]:
        """ Get all features related to whether other players also select the same Mol.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.
            exam_dropouts (Set[Player]): The players that dropped out in the exam episode by execution.

        Returns:
            The feature values.
        """
        picked_answer = sample.answer.difference({sample.player})
        probabilities = sample.exam_episode.same_pick_probabilities(picked_answer, max_episode)
        selected_players = set(probabilities.keys()).difference(exam_dropouts).difference({sample.player})
        num_same_pickers = sum([prob > 0.0 for player, prob in probabilities.items() if player in selected_players])
        prob_same_picker = mean([prob for player, prob in probabilities.items() if player in selected_players])
        return num_same_pickers, prob_same_picker

    @classmethod
    def __joker_discretization(self, player: Player, episode: Episode, excluded: Set[Player]) -> Tuple[float, ...]:
        """ Get the features related to joker & exemption usage in the exam and drop episode of the given player
        compared to the other players.

        Arguments:
            player (Player): The player of which we measure its joker & exemption usage.
            episode (Episode): The episode in which we measure the joker & exemption usage.
            excluded (Set[Player]): All players that will be excluded in comparison.

        Returns:
            The feature values.
        """
        joker_usage = episode.total_joker_usage(self.EXEMPTION_JOKER_VALUE)
        included = set(joker_usage.keys()).difference(excluded)
        jokers_more = sum([usage > joker_usage[player] for p, usage in joker_usage.items() if p in included])
        jokers_less = sum([usage < joker_usage[player] for p, usage in joker_usage.items() if p in included])
        return jokers_more, jokers_less

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
        dropouts = episode.result.players if episode.result.drop == DropType.EXECUTION_DROP else []
        drop_more_jokers = any([joker_usage[p] > joker_usage[player] for p in dropouts])
        drop_less_jokers = any([joker_usage[p] < joker_usage[player] for p in dropouts])
        return drop_more_jokers, drop_less_jokers