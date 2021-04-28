from Data.MoneyData.Earnings.All import MONEY_DATA
import math

TEST_SEASON = {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}

num_non_mol = 0
num_mol = 0
for season in TEST_SEASON:
    for exercise in MONEY_DATA[season].get_exercises(math.inf):
        num_mol += 1
        num_non_mol += len(exercise.alive) - 1

print(num_mol)
print(num_non_mol)
