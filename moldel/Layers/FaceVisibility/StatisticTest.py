from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
from scipy.stats import mannwhitneyu

TEST_SEASONS = {14, 15, 16, 17, 18, 19}

extractor = FaceVisibilityExtractor(0, 0, TEST_SEASONS, 1.0)
train_input, train_output, _ = extractor.get_train_data()
non_mol = [data[0] for data, label in zip(train_input, train_output) if label == 0.0]
mol = [data[0] for data, label in zip(train_input, train_output) if label == 1.0]
statistics, p_value = mannwhitneyu(non_mol, mol, alternative = "two-sided")
print(statistics)
print(p_value)