from Data.LastEpisodes import get_last_episode
from Data.Player import Player
from Data.PlayerData import get_is_mol, get_mol_in_season
from Layers.ExamUniformLayer import ExamUniformLayer
from Layers.Special.CompositeLayer import CompositeLayer
from Layers.Special.ManualExclusionLayer import ManualExclusionLayer
from scipy.stats import rankdata
from typing import Dict, Tuple, List
from Validators.Validator import Validator
import itertools as it
import math

class ValidationMetrics(Validator):
    """ Compute the validation metrics for the predictions, which include the Log Loss, Mol Log Loss,
    Concordant Discordant Ratio, Meam Mol Likelihood, Mean Mol Rank. """

    # If the difference between 2 floats is smaller than this value then they are considered to be equal
    FLOAT_DIFF_EQUALITY = 1e-9

    def __init__(self, episode_groups: int, potential_mol_groups: List[int]):
        """ Constructor of the Validation Metrics.

        Arguments:
            episode_groups (int): The number of episode groups in which we group all predictions based on episode number.
            potential_mol_groups (List[int]): The number of potential mol player groups in which we group all predictions.
        """
        self.__episode_groups = episode_groups
        self.__potential_mol_groups = potential_mol_groups

    def validate(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]):
        for episode in range(self.__episode_groups + 1):
            dis = self.filter_prediction_episode_num(distributions, episode, self.__episode_groups)
            if dis:
                print("Episode Number: " + str(episode))
                self.__evaluate(dis)
                print()

        for num_potential_mol in self.__potential_mol_groups:
            dis = self.filter_prediction_potential_mols(distributions, num_potential_mol)
            if dis:
                print("Number potential mol players: " + str(num_potential_mol))
                self.__evaluate(dis)
                print()

    @staticmethod
    def filter_prediction_episode_num(distributions: Dict[Tuple[int, int], Dict[Player, float]], episode_num: int,
                                      episode_groups: int) -> Dict[Tuple[int, int], Dict[Player, float]]:
        """ Select only the predictions with a certain episode number.

        Arguments:
            distributions (Dict[Tuple[int, int], Dict[Player, float]]): All the predictions.
            episode_num (int): The episode number which get selected.
            episode_groups (int): The number of episode groups in which we group all predictions based on episode number.

        Returns:
            The prediction filtered on episode number.
        """
        seasons = {id[0] for id in distributions.keys()}
        dis = dict()
        for season in seasons:
            num = int(round(get_last_episode(season) * episode_num / episode_groups))
            dis[(season, num)] = distributions[(season, num)]
        return dis

    @classmethod
    def filter_prediction_potential_mols(self, distributions: Dict[Tuple[int, int], Dict[Player, float]],
                                         num_potential_mol: int) -> Dict[Tuple[int, int], Dict[Player, float]]:
        """ Select only the last predictions of every season with this number of potential mols.

        Arguments:
            distributions (Dict[Tuple[int, int], Dict[Player, float]]): All the predictions.
            num_potential_mol (int): The number of potential mol players on which we filter.

        Returns:
            The prediction filtered on the number of potential mols.
        """
        latest_episodes = self.__latest_potential_mol_episode(distributions, num_potential_mol)
        return {(s, e): distributions[(s, e)] for s, e in latest_episodes.items()}

    @classmethod
    def __latest_potential_mol_episode(self, distributions: Dict[Tuple[int, int], Dict[Player, float]],
                                       num_potential_mol: int) -> Dict[int, int]:
        """ Get the last episodes on every season with this number of potential mol players.

        Arguments:
            distributions (Dict[Tuple[int, int], Dict[Player, float]]): All the predictions.
            num_potential_mol (int): The number of potential mol players on which we filter.

        Returns:
            A dictionary that represents for every season (key) the last episode (value) with this number of potential
            mol players.
        """
        latest_episodes = dict()
        for id, distribution in distributions.items():
            season, episode = id
            num = self.__num_potential_mol(season, episode)
            if num == num_potential_mol:
                latest_episodes[season] = max(episode, latest_episodes.get(season, -math.inf))
        return latest_episodes

    @staticmethod
    def __num_potential_mol(season: int, episode: int) -> float:
        """ Get the number of potential mol players after an episode in a given season.

        Arguments:
            season (int): The season for which we compute the number of potential mol player.
            episode (int): The episode after which we compute the number of potential mol player.

        Returns:
            The number of potential mol players
        """
        layer = CompositeLayer([ExamUniformLayer(), ManualExclusionLayer()])
        distribution = layer.compute_distribution(season, episode, set())
        return sum(prob > 0.0 for prob in distribution.values())

    def __evaluate(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]):
        print("Log Loss: " + str(self.__log_loss(distributions)))
        print("Mol Log Loss: " + str(self.__mol_log_loss(distributions)))
        print("Concordant-Discordant Ratio: " + str(self.__concordant_discordant_ratio(distributions)))
        print("Mean Mol Likelihood: " + str(self.__mean_mol_likelihood(distributions)))
        print("Mean Mol Rank: " + str(self.__mean_mol_rank(distributions)))

    def __log_loss(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]) -> float:
        """ Compute the log loss over the predictions.

        Arguments:
            distributions (Dict[Tuple[int, int], Dict[Player, float]]): All the predictions.

        Returns:
            The log loss over the predictions.
        """
        log_loss = 0.0
        num_pred = 0
        for distribution in distributions.values():
            for player, prob in distribution.items():
                log_loss -= math.log(prob) if get_is_mol(player) else math.log(1 - prob)
                num_pred += 1
        return log_loss / num_pred

    def __mol_log_loss(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]) -> float:
        """ Compute the Mol log loss over the predictions (which is the log loss over only the Mol players).

        Arguments:
            distributions (Dict[Tuple[int, int], Dict[Player, float]]): All the predictions.

        Returns:
            The Mol log loss over the predictions.
        """
        seasons = {s for s, e in distributions.keys()}
        all_mol = {s: get_mol_in_season(s) for s in seasons}
        mol_log_loss = 0.0
        num_pred = 0
        for id, distribution in distributions.items():
            mol = all_mol[id[0]]
            mol_log_loss -= math.log(distribution[mol])
            num_pred += 1
        return mol_log_loss / num_pred

    def __concordant_discordant_ratio(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]) -> float:
        """ Compute the concordant-discordant ratio over the predictions.

        Arguments:
            distributions (Dict[Tuple[int, int], Dict[Player, float]]): All the predictions.

        Returns:
            The concordant discordant ratio.
        """
        non_mol_likelihoods = []
        mol_likelihoods = []
        for id, distribution in distributions.items():
            s, e = id
            num_potential_mol = self.__num_potential_mol(s, e)
            for player, prob in distribution.items():
                if get_is_mol(player):
                    mol_likelihoods.append(num_potential_mol * prob)
                else:
                    non_mol_likelihoods.append(num_potential_mol * prob)

        concordant = 0
        discordant = 0
        for mol_likelihood, non_mol_likelihood in it.product(mol_likelihoods, non_mol_likelihoods):
            if math.isclose(mol_likelihood, non_mol_likelihood, abs_tol = self.FLOAT_DIFF_EQUALITY):
                continue
            if mol_likelihood > non_mol_likelihood:
                concordant += 1
            else:
                discordant += 1
        if concordant + discordant == 0:
            return 1/2
        else:
            return concordant / (concordant + discordant)

    def __mean_mol_likelihood(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]) -> float:
        """ Compute the mean Mol likelihood.

        Arguments:
            distributions (Dict[Tuple[int, int], Dict[Player, float]]): All the predictions.

        Returns:
            The mean Mol likelihood.
        """
        seasons = {s for s, e in distributions.keys()}
        all_mol = {s: get_mol_in_season(s) for s in seasons}
        likelihood_sum = 0.0
        num_pred = 0
        for id, distribution in distributions.items():
            mol = all_mol[id[0]]
            likelihood_sum += distribution[mol]
            num_pred += 1
        return likelihood_sum / num_pred

    def __mean_mol_rank(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]) -> float:
        """ Compute the mean Mol rank.

        Arguments:
            distributions (Dict[Tuple[int, int], Dict[Player, float]]): All the predictions.

        Returns:
            The mean Mol rank.
        """
        seasons = {s for s, e in distributions.keys()}
        all_mol = {s: get_mol_in_season(s) for s in seasons}
        rank_sum = 0.0
        num_pred = 0
        for id, distribution in distributions.items():
            likelihoods = [-prob for prob in distribution.values()]
            ranks = rankdata(likelihoods, method = "average")
            rank_map = dict(zip(likelihoods, ranks))

            mol = all_mol[id[0]]
            mol_likelihood = -distribution[mol]
            rank_sum += rank_map[mol_likelihood]
            num_pred += 1
        return rank_sum / num_pred

