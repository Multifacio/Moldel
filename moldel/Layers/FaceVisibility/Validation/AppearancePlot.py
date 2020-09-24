from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
import matplotlib.pyplot as plt
import numpy as np

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20}
AUGMENTATION_CUTS = 4
AUGMENTATION_MIN_CUTS_ON = 2
OUTLIER_CUTOFF = 0.01

extractor = FaceVisibilityExtractor(0, 0, TEST_SEASONS, AUGMENTATION_CUTS, AUGMENTATION_MIN_CUTS_ON, OUTLIER_CUTOFF)
train_input, train_output = extractor.get_train_data()

non_mol = [data[0] for data, label in zip(train_input, train_output) if label == 0.0]
mol = [data[0] for data, label in zip(train_input, train_output) if label == 1.0]
train_output += np.random.uniform(-0.1, 0.1, len(train_output))
print("Number of non-Mol cases: " + str(len(non_mol)))
print("Number of Mol cases: " + str(len(mol)))

plt.figure(figsize=(12, 3))
plt.xlabel("Relative Appearance")
plt.ylabel("Is 'mol'")
plt.yticks([0.0, 1.0])
plt.gcf().subplots_adjust(bottom = 0.15)
plt.scatter(train_input, train_output, s = 4)
plt.show()