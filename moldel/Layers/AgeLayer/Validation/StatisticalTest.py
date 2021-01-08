# A significant difference test between two Kernel Density Estimates. See:
# https://mvstat.net/tduong/research/publications/duong-2013-jns.pdf (pages 637 and 638)
# https://stats.stackexchange.com/questions/90656/kernel-bandwidth-scotts-vs-silvermans-rules
from Data.Player import Player
from Data.PlayerData import get_season, get_age, get_is_mol
from Layers.Appearance.AppearanceLayer import InnerAppearanceLayer
from scipy.stats import chi2, gaussian_kde
import math
import numpy as np
import scipy as sc

def silverman_bandwidth(data: np.array):
    return 1.06 * min(np.std(data), sc.stats.iqr(data) / 1.34) * len(data) ** (-1 / 5)

def test_statistic(x: float, non_mol_kde: gaussian_kde, non_mol_bandwidth: float, non_mol_points: int,
                   mol_kde: gaussian_kde, mol_bandwidth: float, mol_points: int) -> float:
    u = (non_mol_kde.pdf(x)[0] - mol_kde.pdf(x)[0]) ** 4
    r = 1 / (2 * math.sqrt(math.pi))
    non_mol_term = non_mol_kde.pdf(x)[0] / (non_mol_points * math.sqrt(non_mol_bandwidth))
    mol_term = mol_kde.pdf(x)[0] / (mol_points * math.sqrt(mol_bandwidth))
    sigma = (r * (non_mol_term + mol_term)) ** 2
    return u / sigma

TEST_SEASONS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
ALPHA = 0.05

players = [player for player in Player if get_season(player) in TEST_SEASONS]
train_input = [float(get_age(player)) for player in players]
train_output = [1.0 if get_is_mol(player) else 0.0 for player in players]
non_mol = np.array([data for data, label in zip(train_input, train_output) if label == 0.0])
mol = np.array([data for data, label in zip(train_input, train_output) if label == 1.0])

non_mol_kde = InnerAppearanceLayer.kernel_density_estimation(non_mol)
non_mol_bandwidth = silverman_bandwidth(np.array(non_mol))
non_mol_points = len(non_mol)
mol_kde = InnerAppearanceLayer.kernel_density_estimation(mol)
mol_bandwidth = silverman_bandwidth(np.array(mol))
mol_points = len(mol)

ages = [float(age) for age in range(20, 59)]
statistic_values = [test_statistic(age, non_mol_kde, non_mol_bandwidth, non_mol_points, mol_kde, mol_bandwidth,
                                   mol_points) for age in ages]
p_values = [chi2.cdf(x, 1) for x in statistic_values]
p_order = sorted(p_values)
hochman = [ALPHA / (len(p_order) - j + 1) for j in range(1, len(p_order) + 1)]
indices = [i for i, pair in enumerate(zip(p_order, hochman)) if pair[0] <= pair[1]]
print(indices)