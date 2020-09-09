from Data.ExamData.Dataclasses.Episode import Episode
from Data.ExamData.Dataclasses.Question import Question
from Data.Player import Player
from Layers.ExamDrop.ExamDropEncoder import ExamDropEncoder
from typing import Dict, NamedTuple, Set, Tuple
import numpy as np
import statistics

TrainSample = NamedTuple("TrainSample", [("player", Player), ("season", int), ("latest_episode", Episode),
                                         ("exam_episode", Episode), ("question", Question), ("answer", Set[Player])])
class ExamPassEncoder:
    @classmethod
    def extract_features(self, sample: TrainSample, distribution: Dict[Player, float]) -> np.array:
        """ Convert a Train Sample into an array of features.

        Arguments:
            sample (TrainSample): The Train Sample that will be converted.

        Returns:
            An array of features.
        """
        latest_episode, exam_episode, num_players_latest, num_players_exam = self.__episode_features(sample)
        answer_seen, max_likelihood, avg_likelihood = self.__answer_features(sample, distribution)
        jokers2_more, jokers1_more, jokers1_less, jokers2_less = self.__own_joker_features(sample)
        drop_more_jokers, drop_less_jokers = self.__drop_joker_features(sample)
        return np.array([latest_episode, exam_episode, num_players_latest, num_players_exam, answer_seen,
                         max_likelihood, avg_likelihood, jokers2_more, jokers1_more, jokers1_less, jokers2_less,
                         drop_more_jokers, drop_less_jokers])

    @staticmethod
    def __episode_features(sample: TrainSample) -> Tuple[float, ...]:
        return sample.latest_episode.episode_number(), sample.exam_episode.episode_number(), \
               len(sample.latest_episode) - 1, len(sample.exam_episode) - 1

    @staticmethod
    def __answer_features(sample: TrainSample, distribution: Dict[Player, float]) -> Tuple[float, ...]:
        uniform_prob = 1 / sum(likelihood > 0.0 for likelihood in distribution.values())
        answer_likelihoods = [distribution[player] for player in sample.answer]
        return 1.0 if sample.answer else 0.0, min(max(answer_likelihoods), uniform_prob), \
               min(statistics.mean(answer_likelihoods), uniform_prob) if sample.answer else 0.0

    @staticmethod
    def __own_joker_features(sample: TrainSample) -> Tuple[float, ...]:
        player, episode = sample.player, sample.exam_episode
        joker_usage = episode.total_joker_usage(ExamDropEncoder.EXEMPTION_JOKER_VALUE)
        num_players = len(episode)
        jokers2_more = sum([usage >= joker_usage[player] + 2 for usage in joker_usage.values()]) / num_players
        jokers1_more = sum([usage == joker_usage[player] + 1 for usage in joker_usage.values()]) / num_players
        jokers1_less = sum([usage == joker_usage[player] - 1 for usage in joker_usage.values()]) / num_players
        jokers2_less = sum([usage <= joker_usage[player] - 2 for usage in joker_usage.values()]) / num_players
        return jokers2_more, jokers1_more, jokers1_less, jokers2_less

    @staticmethod
    def __drop_joker_features(sample: TrainSample) -> Tuple[float, ...]:
        player, episode = sample.player, sample.exam_episode
        joker_usage = episode.total_joker_usage(ExamDropEncoder.EXEMPTION_JOKER_VALUE)
        drop_more_jokers = any([joker_usage[p] > joker_usage[player] for p in episode.result.players])
        drop_less_jokers = any([joker_usage[p] < joker_usage[player] for p in episode.result.players])
        return drop_more_jokers, drop_less_jokers