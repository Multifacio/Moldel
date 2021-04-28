from Layers.Money.MoneyEncoder import MoneyEncoder
from numpy.random.mtrand import RandomState
import math
import numpy as np
import matplotlib.pyplot as plt

QUANTILES = 6
SPLINE_CLUSTERS = 4
MIN_RANGE = -10000
MAX_RANGE = 10000
TEST_SEASONS = {8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}

encoder = MoneyEncoder(SPLINE_CLUSTERS, QUANTILES, RandomState())
samples = encoder.get_money_samples(TEST_SEASONS, math.inf)

major_likelihood_function = encoder.major_money_pattern(samples)
X = np.linspace(MIN_RANGE, MAX_RANGE, 10000)
Y = np.array([major_likelihood_function(x) for x in X])
plt.plot(X, Y, color = 'r')
plt.xticks(np.linspace(MIN_RANGE, MAX_RANGE, 21))
plt.grid()
plt.show()

minor_likelihood_function = encoder.minor_money_pattern(samples)
X = np.linspace(MIN_RANGE, MAX_RANGE, 10000)
Y = np.array([minor_likelihood_function(x) for x in X])
plt.plot(X, Y, color = 'r')
plt.xticks(np.linspace(MIN_RANGE, MAX_RANGE, 21))
plt.grid()
plt.show()