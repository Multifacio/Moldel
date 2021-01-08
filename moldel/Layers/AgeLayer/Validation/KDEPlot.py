from Data.Player import Player
from Data.PlayerData import get_age, get_season, get_is_mol
from Layers.Appearance.AppearanceLayer import InnerAppearanceLayer
import matplotlib.pyplot as plt
import numpy as np

TEST_SEASONS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

players = [player for player in Player if get_season(player) in TEST_SEASONS]
train_input = [float(get_age(player)) for player in players]
train_output = [1.0 if get_is_mol(player) else 0.0 for player in players]
non_mol = np.array([data for data, label in zip(train_input, train_output) if label == 0.0])
mol = np.array([data for data, label in zip(train_input, train_output) if label == 1.0])

plt.figure(figsize=(12, 3))
plt.xlabel("Age")
plt.ylabel("Is 'mol'")
plt.yticks(np.linspace(0.0, 1.0, 101))
plt.gcf().subplots_adjust(bottom = 0.15)

non_mol_kde = InnerAppearanceLayer.kernel_density_estimation(non_mol)
mol_kde = InnerAppearanceLayer.kernel_density_estimation(mol)
x = InnerAppearanceLayer.get_boundary(non_mol_kde, mol_kde, 10, 0.01, 0, 100)
plt.axvline(x = x, c = 'black')
x = InnerAppearanceLayer.get_boundary(non_mol_kde, mol_kde, 10, 0.99, 0, 100)
plt.axvline(x = x, c = 'black')
X = np.linspace(15.0, 75.0, 500)
non_mol_Y = [non_mol_kde.pdf([x]) for x in X]
mol_Y = [mol_kde.pdf([x]) for x in X]
posterior_Y = [(mY / 10) / (9 * nY / 10 + mY / 10) for nY, mY in zip(non_mol_Y, mol_Y)]
plt.plot(X, non_mol_Y, color = 'g')
plt.plot(X, mol_Y, color = 'r')
plt.plot(X, posterior_Y, color = 'b')
plt.show()