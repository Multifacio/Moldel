from Data.ExamData.Dataclasses.Episode import Episode
from Data.ExamData.Dataclasses.Question import Question
from Data.Player import Player
from Layers.ExamDrop.ExamDropEncoder import ExamDropEncoder
from typing import Dict, NamedTuple, Set, Tuple
import numpy as np
import statistics

ExamPassSample = NamedTuple("TrainSample", [("player", Player), ("latest_episode", Episode), ("exam_episode", Episode),
                                         ("distribution", Dict[Player, float]), ("covered", Set[Player])])
class ExamPassEncoder:
    @classmethod
    def extract_features(self, sample: ExamPassSample) -> np.array:
        """ Convert a Train Sample into an array of features.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            An array of features.
        """
        exam_episode, num_players_exam = self.__episode_features(sample)
        answer_seen, max_likelihood, avg_likelihood = self.__answer_features(sample)
        jokers1_less, jokers2_less = self.__own_joker_features(sample)
        drop_less_jokers = self.__drop_joker_features(sample)
        return np.array([exam_episode, num_players_exam, answer_seen, max_likelihood, avg_likelihood, jokers1_less,
                         jokers2_less, drop_less_jokers])

    @staticmethod
    def __episode_features(sample: ExamPassSample) -> Tuple[float, ...]:
        return sample.exam_episode.episode_number(), len(sample.exam_episode) - 1

    @staticmethod
    def __answer_features(sample: ExamPassSample) -> Tuple[float, ...]:
        covered, distribution = sample.covered, sample.distribution
        if covered:
            uniform_prob = 1 / sum(likelihood > 0.0 for likelihood in distribution.values())
            answer_likelihoods = [distribution[player] for player in covered]
            return 1.0, min(max(answer_likelihoods), uniform_prob), min(statistics.mean(answer_likelihoods), uniform_prob)
        else:
            return 0.0, 0.0, 0.0

    @staticmethod
    def __own_joker_features(sample: ExamPassSample) -> Tuple[float, ...]:
        player, episode = sample.player, sample.exam_episode
        joker_usage = episode.total_joker_usage(ExamDropEncoder.EXEMPTION_JOKER_VALUE)
        num_players = len(episode)
        jokers1_less = sum([usage == joker_usage[player] - 1 for usage in joker_usage.values()]) / num_players
        jokers2_less = sum([usage <= joker_usage[player] - 2 for usage in joker_usage.values()]) / num_players
        return jokers1_less, jokers2_less

    @staticmethod
    def __drop_joker_features(sample: ExamPassSample) -> Tuple[float, ...]:
        player, episode = sample.player, sample.exam_episode
        joker_usage = episode.total_joker_usage(ExamDropEncoder.EXEMPTION_JOKER_VALUE)
        drop_less_jokers = any([joker_usage[p] < joker_usage[player] for p in episode.result.players])
        return drop_less_jokers