from Data.LastEpisodes import get_last_episode
from Data.PlayerData import get_players_in_season, get_is_mol
from scipy.stats import ttest_rel, wilcoxon
from sklearn.metrics import log_loss
from typing import Callable, Set, Tuple
from Validators.Precomputer import Precomputer
import numpy as np

def get_predictions(validate_seasons: Set[int], folder: str, episode_used: Callable[[int, Set[int]], bool]) \
        -> Tuple[np.array, np.array]:
    """ Get the likelihood predictions.

    Arguments:
        train_seasons (Set[int]): The seasons for which we get the likelihood predictions.
        folder (str): The folder in which the precomputed distribution are stored.
        episode_used (Callable[[int, Set[int]], bool]): A function which determines when an episode should be included
            in the data. The first argument of this function is the episode number and the second argument is the set of
            all episodes that can be used of that season.
    """
    likelihoods = []
    labels = []
    for season in sorted(validate_seasons):
        episode_range = set(range(get_last_episode(season) + 1))
        player_range = sorted(get_players_in_season(season), key = lambda p: p.value)
        precomputer = Precomputer(folder)
        for episode in sorted(episode_range):
            if not episode_used(episode, episode_range):
                continue
            distribution = precomputer.load_distribution(season, episode)
            for player in player_range:
                likelihoods.append(distribution[player])
                labels.append(1.0 if get_is_mol(player) else 0.0)
    return likelihoods, labels

def t_test(likelihoods1: np.array, likelihoods2: np.array) -> Tuple[float, float]:
    """ Do the paired student-t test, with "greater than" as alternative hypothesis.

    Arguments:
        likelihoods1 (np.array): All mol likelihoods for the first prediction model.
        likelihoods2 (np.array): All mol likelihoods for the second prediction model.

    Returns:
        The t statistic value and the p-value corresponding to this test.
    """
    statistic, p_value = ttest_rel(likelihoods1, likelihoods2)
    p_value = 1 - p_value / 2 if statistic < 0 else p_value / 2
    return statistic, p_value

def mol_log_loss(likelihoods: np.array) -> float:
    """ Compute the log loss score for only mol data.

    Arguments:
        likelihoods (np.array): All mol likelihoods.

    Returns:
        The corresponding log loss score.
    """
    return -1 * np.sum(np.log(likelihoods)) / len(likelihoods)

def compare(folder1: str, folder2: str, validate_seasons: Set[int], episode_used: Callable[[int, Set[int]], bool]):
    """ Compare 2 prediction models with each other.

    Arguments:
        folder1 (str): The folder in which the precomputed distribution are stored for the first prediction model.
        folder2 (str): The folder in which the precomputed distribution are stored for the second prediction model.
        validate_seasons (Set[int]): All season on which the models are evaluated.
        episode_used (Callable[[int, Set[int]], bool]): A function which determines when an episode should be included
            in the data. The first argument of this function is the episode number and the second argument is the set of
            all episodes that can be used of that season.
    """
    likelihoods1, labels1 = get_predictions(validate_seasons, folder1, episode_used)
    likelihoods2, labels2 = get_predictions(validate_seasons, folder2, episode_used)
    mol_likelihoods1 = np.array([likelihood for likelihood, label in zip(likelihoods1, labels1) if label == 1.0])
    mol_likelihoods2 = np.array([likelihood for likelihood, label in zip(likelihoods2, labels2) if label == 1.0])
    print(folder1 + " vs. " + folder2)
    print("Paired T-Test (Greater): " + str(t_test(mol_likelihoods1, mol_likelihoods2)))
    print("Log Paired T-Test (Greater): " + str(t_test(np.log(mol_likelihoods1), np.log(mol_likelihoods2))))
    print("Wilcoxon Test (Greater): " + str(tuple(wilcoxon(mol_likelihoods1, mol_likelihoods2, alternative = "greater"))))
    print("Mol Log Losses: " + str(mol_log_loss(mol_likelihoods1)) + " vs. " + str(mol_log_loss(mol_likelihoods2)))
    print("Total Log Losses: " + str(log_loss(labels1, likelihoods1)) + " vs. " + str(log_loss(labels2, likelihoods2)))

compare("MoldelV2", "ExamUniform", {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, lambda x, y: True)