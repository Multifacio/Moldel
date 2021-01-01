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

mol_norm = norm.fit(mol)
X = np.linspace(-1.5, 1.0, 500)
mol_Y = [norm.pdf(x, loc = mol_norm[0], scale = mol_norm[1]) for x in X]
plt.plot(X, mol_Y, color = 'r')

non_mol_norm = norm.fit(non_mol)
non_mol_Y = [norm.pdf(x, loc = non_mol_norm[0], scale = non_mol_norm[1]) for x in X]
plt.plot(X, non_mol_Y, color = 'g')

non_mol_multiplier = len(non_mol) / len(train_output)
mol_multiplier = len(mol) / len(train_output)
posterior = [my * mol_multiplier / (my * mol_multiplier + ny * non_mol_multiplier) for my, ny in zip(mol_Y, non_mol_Y)]
plt.plot(X, posterior, color = 'b')

mol_Y = [norm.pdf(x[0], loc = mol_norm[0], scale = mol_norm[1]) for x in train_input]
non_mol_Y = [norm.pdf(x[0], loc = non_mol_norm[0], scale = non_mol_norm[1]) for x in train_input]
posterior = [my * mol_multiplier / (my * mol_multiplier + ny * non_mol_multiplier) for my, ny in zip(mol_Y, non_mol_Y)]
# print(sorted([poster for poster, is_mol in zip(posterior, train_output) if is_mol == 1.0]))

train_output += np.random.uniform(-0.1, 0.00, len(train_output))
plt.scatter(train_input, train_output, s = 4)
plt.show()

