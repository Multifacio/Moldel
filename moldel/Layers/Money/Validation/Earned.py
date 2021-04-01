from Data.MoneyData.Earnings.All import MONEY_DATA
from Data.PlayerData import get_is_mol
from statistics import mean
import math
import numpy as np

TEST_SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
QUANTILES = np.linspace(0, 1, 21)

np.set_printoptions(suppress = True)

major_mol_earned = []
major_non_mol_earned = []
for season in TEST_SEASONS:
    for exercise in MONEY_DATA[season].get_exercises(math.inf):
        for player, money in exercise.major_earned().items():
            if get_is_mol(player):
                major_mol_earned.append(money)
            else:
                major_non_mol_earned.append(money)

print(mean(major_mol_earned))
print(mean(major_non_mol_earned))
print(mean(major_mol_earned + major_non_mol_earned))
print(np.quantile(major_mol_earned, QUANTILES))
print(np.quantile(major_non_mol_earned, QUANTILES))
print(np.quantile(major_mol_earned + major_non_mol_earned, QUANTILES))
print(sorted(major_mol_earned + major_non_mol_earned))

minor_mol_earned = []
minor_non_mol_earned = []
for season in TEST_SEASONS:
    for exercise in MONEY_DATA[season].get_exercises(math.inf):
        for player, money in exercise.minor_earned().items():
            if get_is_mol(player):
                minor_mol_earned.append(money)
            else:
                minor_non_mol_earned.append(money)

print(mean(minor_mol_earned))
print(mean(minor_non_mol_earned))
print(mean(minor_mol_earned + minor_non_mol_earned))
print(np.quantile(minor_mol_earned, QUANTILES))
print(np.quantile(minor_non_mol_earned, QUANTILES))
print(np.quantile(minor_mol_earned + minor_non_mol_earned, QUANTILES))
print(sorted(minor_mol_earned + minor_non_mol_earned))