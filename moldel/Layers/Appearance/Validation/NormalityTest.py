from Layers.Appearance.AppearanceExtractor import AppearanceExtractor
from scipy.stats import shapiro

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20}

extractor = AppearanceExtractor(0, 0, TEST_SEASONS, 1, 1)
train_input, train_output = extractor.get_train_data()

non_mol = [data[0] for data, label in zip(train_input, train_output) if label == 0.0]
statistic, p_value = shapiro(non_mol)
print("Non-mol score: " + str(statistic))
print("Non-mol p-value: " + str(p_value))

mol = [data[0] for data, label in zip(train_input, train_output) if label == 1.0]
statistic, p_value = shapiro(mol)
print("Mol score: " + str(statistic))
print("Mol p-value: " + str(p_value))