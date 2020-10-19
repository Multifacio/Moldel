from Data.PlayerData import get_is_mol
from Layers.FaceVisibility.FaceVisibilityLayer import InnerFaceVisibilityLayer
from Layers.WikiWord.WikiWordExtractor import WikiWordExtractor
from numpy.random.mtrand import RandomState
from scipy.stats import kruskal, levene, norm
import matplotlib.pyplot as plt
import numpy as np

TRAIN_SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
PREDICT_SEASON = 5
TRAIN_SEASONS.difference_update({PREDICT_SEASON})
RANDOM_SEED = 949019755
PCA_COMPONENTS = 4
LOWER_Z_SCORE = -0.674

extractor = WikiWordExtractor(PREDICT_SEASON, TRAIN_SEASONS, PCA_COMPONENTS, RandomState(RANDOM_SEED))
train_input, train_output = extractor.get_train_data()
train_input = np.squeeze(train_input)

mol_features = [value for value, is_mol in zip(train_input, train_output) if is_mol == 1.0]
non_mol_features = [value for value, is_mol in zip(train_input, train_output) if is_mol == 0.0]
_, mean_p_value = kruskal(mol_features, non_mol_features)
_, std_p_value = levene(mol_features, non_mol_features)
print("Mean: " + str(mean_p_value) + ", Std: " + str(std_p_value))

mol_kde = InnerFaceVisibilityLayer.kernel_density_estimation(mol_features)
non_mol_kde = InnerFaceVisibilityLayer.kernel_density_estimation(non_mol_features)

predict_data = extractor.get_predict_data()
predict_input = np.array([data for data in predict_data.values()])
predict_output = np.array([1.0 if get_is_mol(player) else 0.0 for player in predict_data.keys()])
mean, std = norm.fit(predict_input)
z_cutoff = mean + std * LOWER_Z_SCORE

train_output += np.random.uniform(-0.1, 0.1, len(train_output))
predict_output += np.random.uniform(-0.1, 0.1, len(predict_output))

plt.figure(figsize=(12, 3))
plt.xlabel("Job Feature")
plt.ylabel("Is 'mol'")
plt.yticks([0.0, 1.0])
plt.gcf().subplots_adjust(bottom = 0.15)
# plt.plot(X, mol_y, color = "r")
# plt.plot(X, non_mol_y, color = "g")
# plt.plot(X, posterior, color = "b")
plt.axvline(x = z_cutoff, c = 'black')
plt.scatter(predict_input, predict_output, s = 4, c = "r")
plt.scatter(train_input, train_output, s = 4, c = "g")
plt.show()