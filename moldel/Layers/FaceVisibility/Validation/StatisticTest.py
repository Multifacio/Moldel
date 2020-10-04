from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
from scipy.stats import mannwhitneyu

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20}

extractor = FaceVisibilityExtractor(0, 0, TEST_SEASONS, 1, 1, 0.0)
train_input, train_output = extractor.get_train_data()

non_mol = [data[0] for data, label in zip(train_input, train_output) if label == 0.0]
mol = [data[0] for data, label in zip(train_input, train_output) if label == 1.0]
statistics, p_value = mannwhitneyu(non_mol, mol, alternative = "greater")
print("Score: " + str(statistics))
print("p-value: " + str(p_value))
print("Number of non-Mol players: " + str(len(non_mol)))
print("Number of Mol players: " + str(len(mol)))