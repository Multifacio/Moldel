from Layers.Appearance.AppearanceLayer import InnerAppearanceLayer
from Layers.Appearance.AppearanceExtractor import AppearanceExtractor
from Tools.Classifiers.NaiveKDEClassifier import NaiveKDEClassifier
import matplotlib.pyplot as plt
import numpy as np

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
AUGMENTATION_CUTS = 4
AUGMENTATION_MIN_CUTS_ON = 2
CDF_CUTOFF = 0.01

extractor = AppearanceExtractor(0, 0, TEST_SEASONS, AUGMENTATION_CUTS, AUGMENTATION_MIN_CUTS_ON)
train_input, train_output = extractor.get_train_data()
cutoff_classifier = NaiveKDEClassifier(cdf_cutoff = CDF_CUTOFF)
cutoff_classifier.train(train_input, train_output)
normal_classifier = NaiveKDEClassifier()
normal_classifier.train(train_input, train_output)

plt.figure(figsize=(12, 3))
plt.xlabel("Relative Appearance")
plt.ylabel("Is 'mol'")
plt.yticks(np.linspace(0.0, 1.0, 11))
plt.gcf().subplots_adjust(bottom = 0.15)

plt.axvline(x = cutoff_classifier.lowerbounds[0], c = 'black')
plt.axvline(x = cutoff_classifier.upperbounds[0], c = 'black')
X = np.linspace(-3.0, 2.0, 500)
non_mol_Y = [normal_classifier.class_likelihood([x], False) for x in X]
mol_Y = [normal_classifier.class_likelihood([x], True) for x in X]
posterior_Y = [normal_classifier.predict_proba([x]) for x in X]
plt.plot(X, non_mol_Y, color = 'g')
plt.plot(X, mol_Y, color = 'r')
plt.plot(X, posterior_Y, color = 'b')
plt.show()