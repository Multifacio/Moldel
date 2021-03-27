from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import KBinsDiscretizer, QuantileTransformer
from Data.MoneyData.Earnings.All import MONEY_DATA
from Data.PlayerData import get_is_mol
from statistics import mean
import math
import numpy as np
import matplotlib.pyplot as plt

INTERVALS = 6
TEST_SEASONS = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

train_input = []
train_output = []
for season in TEST_SEASONS:
    for exercise in MONEY_DATA[season].get_exercises(math.inf):
        for player, money in exercise.major_earned().items():
            train_input.append([money])
            train_output.append(1.0 if get_is_mol(player) else 0.0)
train_input = np.array(train_input)
train_output = np.array(train_output)
min_money = min(train_input)
max_money = max(train_input)

rank_transformer = QuantileTransformer(n_quantiles = len(train_input), output_distribution = 'uniform')
train_input = rank_transformer.fit_transform(train_input)
discretizer = KBinsDiscretizer(n_bins = INTERVALS, strategy = 'kmeans', encode = 'onehot-dense')
train_input = discretizer.fit_transform(train_input)
regression = LogisticRegression(penalty = 'none')
regression.fit(train_input, train_output)

X = np.linspace(min_money, max_money, 10000)
Y = np.array([regression.predict_proba(discretizer.transform(rank_transformer.transform([x])))[0][1] for x in X])
print(Y)
plt.plot(X, Y, color = 'r')
plt.show()