from sklearn.decomposition import PCA
from Layers.Money.MoneyEncoder import MoneyEncoder
import math
import numpy as np

TRAIN_SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
NUM_QUANTILES = 6
EXPLAINED_VARIANCE = 0.95

encoder = MoneyEncoder(NUM_QUANTILES)
samples = encoder.get_money_samples(TRAIN_SEASONS, math.inf)
train_input = np.array([encoder.extract_features(sample) for sample in samples])
pca = PCA(n_components = EXPLAINED_VARIANCE)
print(len(train_input[0]))
train_input = pca.fit_transform(train_input)
print(len(train_input[0]))
print(train_input)