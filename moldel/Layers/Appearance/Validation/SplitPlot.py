from Layers.Appearance.AppearanceExtractor import AppearanceExtractor
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20}

extractor = AppearanceExtractor(0, 0, TEST_SEASONS, 1, 1, 0.0)
train_input, train_output = extractor.get_train_data()
non_mol = [data[0] for data, label in zip(train_input, train_output) if label == 0.0]
mol = [data[0] for data, label in zip(train_input, train_output) if label == 1.0]

plt.figure(figsize=(12, 3))
plt.xlabel("Relative Appearance")
plt.ylabel("Is 'mol'")
plt.yticks(np.linspace(0.0, 1.0, 11))
plt.gcf().subplots_adjust(bottom = 0.15)

split = np.median(train_input)
print(split)
lower_output = [output for input, output in zip(train_input, train_output) if input <= split]
lower_prob = sum(lower_output) / len(lower_output)
higher_output = [output for input, output in zip(train_input, train_output) if input > split]
higher_prob = sum(higher_output) / len(higher_output)
X = np.linspace(-1.5, 1.0, 500)
Y = [lower_prob if x <= split else higher_prob for x in X]
plt.plot(X, Y, color = 'r')

train_output += np.random.uniform(-0.1, 0.00, len(train_output))
plt.scatter(train_input, train_output, s = 4)
plt.show()