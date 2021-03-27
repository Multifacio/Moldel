from sklearn.cluster import KMeans
from sklearn.preprocessing import QuantileTransformer

from Data.MoneyData.Earnings.All import MONEY_DATA
from Data.PlayerData import get_is_mol
from statistics import mean
import math
import numpy as np

KMEANS = 4
TEST_SEASONS = {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

major_earned = []
for season in TEST_SEASONS:
    for exercise in MONEY_DATA[season].get_exercises(math.inf):
        for player, money in exercise.major_earned().items():
            major_earned.append([money])
data = np.array(major_earned)

rank_transform = QuantileTransformer(n_quantiles = len(major_earned), output_distribution = 'uniform')
data = rank_transform.fit_transform(major_earned)
clustering = KMeans(n_clusters = KMEANS)
clustering.fit(data)
splits = np.sort(clustering.cluster_centers_, axis = 0)
print(splits)



