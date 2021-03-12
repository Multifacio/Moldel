from Data.LastEpisodes import get_last_episode
from Data.PlayerData import get_mol_in_season
from Layers.Special.ExamUniformLayer import ExamUniformLayer
from Layers.Moldel import Moldel
from numpy.random.mtrand import RandomState
from progress.bar import Bar
from scipy.stats import ttest_rel, wilcoxon
from typing import Tuple

from Layers.Special.CompositeLayer import CompositeLayer
from Layers.Special.ManualExclusionLayer import ManualExclusionLayer
from Validators.ValidationMetrics import ValidationMetrics
import numpy as np

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

def evaluate(likelihoods1: np.array, likelihoods2: np.array):
    print("Sample Size: " + str(len(likelihoods1)) )
    print("Paired T-Test (Greater): " + str(t_test(likelihoods1, likelihoods2)))
    print("Log Paired T-Test (Greater): " + str(t_test(np.log(likelihoods1), np.log(likelihoods2))))
    print("Wilcoxon Test (Greater): " + str(tuple(wilcoxon(likelihoods1, likelihoods2, zero_method = "zsplit",
                                                           alternative = "greater"))))

RANDOM_SEED = 949019755
VALIDATE_SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
TRAIN_SEASONS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
EPISODE_GROUPS = 9
POTENTIAL_MOL_GROUPS = [2, 3, 4, 5, 6, 7, 8, 9, 10]

distributions1 = dict()
distributions2 = dict()
random_generator = RandomState(RANDOM_SEED)
model1 = Moldel(random_generator)
model2 = CompositeLayer([ExamUniformLayer(), ManualExclusionLayer()])

# Obtain the predictions from the first model, which is supposed to be the better performing model.
total_tasks = sum([get_last_episode(season) + 1 for season in VALIDATE_SEASONS])
progress_bar = Bar("Distributions Computed of First Model: ", max = total_tasks)
for season in VALIDATE_SEASONS:
    train_seasons = TRAIN_SEASONS.difference({season})
    for episode in range(get_last_episode(season) + 1):
        distributions1[(season, episode)] = model1.compute_distribution(season, episode, train_seasons)
        progress_bar.next()
progress_bar.finish()

# Obtain the predictions from the second model, which is supposed to be the worser performing model.
progress_bar = Bar("Distributions Computed of Second Model: ", max = total_tasks)
for season in VALIDATE_SEASONS:
    train_seasons = TRAIN_SEASONS.difference({season})
    for episode in range(get_last_episode(season) + 1):
        distributions2[(season, episode)] = model2.compute_distribution(season, episode, train_seasons)
        progress_bar.next()
progress_bar.finish()
print()

# Compare the predictions based on episode number
for episode in range(EPISODE_GROUPS + 1):
    dis1 = ValidationMetrics.filter_prediction_episode_num(distributions1, episode, EPISODE_GROUPS)
    dis2 = ValidationMetrics.filter_prediction_episode_num(distributions2, episode, EPISODE_GROUPS)
    likelihoods1 = np.array([dis[get_mol_in_season(id[0])] for id, dis in dis1.items()])
    likelihoods2 = np.array([dis[get_mol_in_season(id[0])] for id, dis in dis2.items()])

    print("Episode Number: " + str(episode))
    evaluate(likelihoods1, likelihoods2)
    print()

# Compare the predictions based on number potential mol players
for num_potential_mol in POTENTIAL_MOL_GROUPS:
    dis1 = ValidationMetrics.filter_prediction_potential_mols(distributions1, num_potential_mol)
    dis2 = ValidationMetrics.filter_prediction_potential_mols(distributions2, num_potential_mol)
    if dis1 and dis2:
        likelihoods1 = np.array([dis[get_mol_in_season(id[0])] for id, dis in dis1.items()])
        likelihoods2 = np.array([dis[get_mol_in_season(id[0])] for id, dis in dis2.items()])

        print("Number potential mol players: " + str(num_potential_mol))
        evaluate(likelihoods1, likelihoods2)
        print()
