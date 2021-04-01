from Layers.Appearance.AppearanceExtractor import AppearanceExtractor
import matplotlib.pyplot as plt
import numpy as np

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20, 21}
AUGMENTATION_CUTS = 1
AUGMENTATION_MIN_CUTS_ON = 1
OUTLIER_CUTOFF = 0.00

extractor = AppearanceExtractor(0, 0, TEST_SEASONS, AUGMENTATION_CUTS, AUGMENTATION_MIN_CUTS_ON, OUTLIER_CUTOFF)
train_input, _ = extractor.get_train_data()
train_input = np.squeeze(np.exp(train_input) - AppearanceExtractor.SMALL_LOG_ADDITION, axis = 1)

plt.hist(train_input, bins = 10, edgecolor = 'black')
plt.xlabel("Absolute Appearance")
plt.ylabel("#Occurrences")
plt.show()