from Layers.Money.MoneyEncoder import MoneyEncoder
from numpy.random import RandomState
from sklearn.decomposition import PCA
import math
import numpy as np

TRAIN_SEASONS = {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
NUM_CURVES = 4
LIKELIHOOD_QUANTILES = 9
EXPLAINED_VARIANCE = 0.98

encoder = MoneyEncoder(NUM_CURVES, LIKELIHOOD_QUANTILES, RandomState())
samples = encoder.get_money_samples(TRAIN_SEASONS, math.inf)
major_likelihood_function = encoder.major_money_pattern(samples)
minor_likelihood_function = encoder.minor_money_pattern(samples)
train_input = np.array([encoder.extract_features(sample, major_likelihood_function, minor_likelihood_function)
                        for sample in samples])
pca = PCA(n_components = EXPLAINED_VARIANCE)
print(len(train_input[0]))
train_input = pca.fit_transform(train_input)
print(len(train_input[0]))