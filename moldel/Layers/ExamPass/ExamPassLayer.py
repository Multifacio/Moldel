from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Dataclasses.Episode import Episode
from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.Layer import Layer
from Layers.Special.NormalizeLayer import NormalizeLayer
from sklearn.linear_model import LogisticRegression
from typing import Dict, List, Set, Tuple
import itertools as it
import numpy as np
import sys

class InnerExamPassLayer(Layer):
    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        estimator = self.__train(train_seasons)
        alive_players = EXAM_DATA[predict_season].get_alive_players(latest_episode)
        result = {player: 1.0 if player in alive_players else 0.0 for player in get_players_in_season(predict_season)}
        for episode in EXAM_DATA[predict_season].episodes.values():
            if episode.id > latest_episode or episode.result.drop != DropType.EXECUTION_DROP:
                continue
            prediction = self.__predict_for_episode(episode, alive_players, estimator)
            for player, likelihood in prediction.items():
                result[player] *= likelihood
        return result

    @classmethod
    def __train(self, train_seasons: Set[int]) -> LogisticRegression:
        """ Train the estimator, which estimates the probability that someone drops off, based on the jokers used.

        Arguments:
            train_seasons (Set[int]):  All seasons used as training data.

        Returns:
            The estimator used to estimate the likelihood that someone drops out based on the joker usage.
        """
        train_input, train_output = self.__get_train_data(train_seasons)
        estimator = LogisticRegression()
        estimator.fit(train_input, train_output)
        return estimator

    @classmethod
    def __predict_for_episode(self, episode: Episode, alive_players: Set[Player], estimator: LogisticRegression) \
            -> Dict[Player, float]:
        """ Determine the likelihood that someone is the mol based on the dropouts and joker usage during an episode.

        Arguments:
            episode (Episode): The episode for which a prediction is made.
            alive_players (Set[Player]): The players that could still be the mol.
            estimator (LogisticRegression): The estimator used to estimate the likelihood that someone drops out based
                on the joker usage.

        Returns:
            A dictionary with as key a player that could be the Mol and as value the likelihood of being the Mol (float).
        """
        drop_likelihoods = self.__get_drop_likelihoods(episode, estimator)
        mol_likelihoods = dict()
        dropouts = episode.result.players
        drop_likelihood = np.prod([drop_likelihoods[p] for p in dropouts])
        for mol in alive_players:
            possible_dropouts = set(episode.players).difference({mol})
            drop_sum = 0.0
            for players in it.combinations(possible_dropouts, len(dropouts)):
                drop_sum += np.prod([drop_likelihoods[p] for p in players])
            mol_likelihoods[mol] = drop_likelihood / drop_sum
        likelihood_sum = sum(mol_likelihoods.values())
        return {player: likelihood / likelihood_sum for player, likelihood in mol_likelihoods.items()}

    @classmethod
    def __get_train_data(self, train_seasons: Set[int]) -> Tuple[np.array, np.array]:
        """ Get the train data used to estimate the likelihood of being the dropout based on joker usage.

        Arguments:
            train_seasons (Set[int]):  All seasons used as training data.

        Returns:
            All train input, which is an encoding of the jokers used for every player, and all train output, which
            is whether that player dropped out.
        """
        train_input = []
        train_output = []
        for season in train_seasons:
            season = EXAM_DATA[season]
            for episode in season.episodes.values():
                if episode.result.drop != DropType.EXECUTION_DROP:
                    continue

                joker_usage = episode.total_joker_usage(sys.maxsize)
                for player in episode.players:
                    train_input.append(self.__get_input(player, joker_usage))
                    train_output.append(1.0 if player in episode.result.players else 0.0)
        return np.array(train_input), np.array(train_output)

    @classmethod
    def __get_drop_likelihoods(self, episode: Episode, estimator: LogisticRegression) -> Dict[Player, float]:
        """ Get the drop likelihoods for all players in an episode, based on only the joker usage.

        Arguments:
            episode (Episode): The episode for which we determine the drop likelihoods.
            estimator (LogisticRegression): The estimator used to estimate the likelihood that someone drops out based
                on the joker usage.

        Returns:
            A dictionary with as key a player that was alive in this episode and as value the likelihood of dropping out
            during the executie (float).
        """
        joker_usage = episode.total_joker_usage(sys.maxsize)
        drop_likelihoods = dict()
        for player in episode.players:
            if episode.input[player].immunity:
                drop_likelihoods[player] = 0.0
            else:
                features = self.__get_input(player, joker_usage)
                drop_likelihoods[player] = estimator.predict_proba(np.array([features]))[0][1]
        probability_sum = sum(drop_likelihoods.values())
        return {player: likelihood / probability_sum for player, likelihood in drop_likelihoods.items()}

    @staticmethod
    def __get_input(player: Player, joker_usage: Dict[Player, int]) -> List[float]:
        """ Get the input encoding for a player based on the joker usage.

        Arguments:
            player (Player): The input encoding for a player.
            joker_usage (Dict[Player, int]): How many jokers are used by every player during this episode. The value
                is sys.maxsize if the player used an exemption.

        Returns:
            The feature encoding for that player.
        """
        own_usage = joker_usage[player]
        less_1_joker = sum(usage <= own_usage - 1 for p, usage in joker_usage.items() if p != player)
        same_jokers = sum(usage == own_usage for p, usage in joker_usage.items() if p != player)
        more_1_joker = sum(usage >= own_usage + 1 for p, usage in joker_usage.items() if p != player)
        return [less_1_joker, same_jokers, more_1_joker]

class ExamPassLayer(NormalizeLayer):
    """ The Exam Pass Layer predicts whether you are the Mol based on how many jokers and exemptions players used during
    the test. """
    def __init__(self):
        super().__init__(InnerExamPassLayer())