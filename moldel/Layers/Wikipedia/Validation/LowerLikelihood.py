from progress.bar import Bar

from Data.PlayerData import get_is_mol
from Layers.Wikipedia.WikipediaExtractor import WikipediaExtractor
from numpy.random.mtrand import RandomState

RANDOM_SEED = 949019755
SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
PCA_COMPONENTS = 5
UNLIKELY_Z_SCORE = 0.0

progress_bar = Bar("Distributions Computed:", max = len(SEASONS))

non_mol_outliers = 0
mol_outliers = 0
non_mol_inliers = 0
mol_inliers = 0

for season in SEASONS:
    random_generator = RandomState(RANDOM_SEED)
    train_seasons = SEASONS.difference({season})
    extractor = WikipediaExtractor(season, train_seasons, PCA_COMPONENTS, UNLIKELY_Z_SCORE, random_generator)
    extractor.train()
    predict_input = extractor.get_predict_data()
    for player, is_outlier in predict_input.items():
        if is_outlier[0]:
            if get_is_mol(player):
                mol_outliers += 1
            else:
                non_mol_outliers += 1
        else:
            if get_is_mol(player):
                mol_inliers += 1
            else:
                non_mol_inliers += 1
    progress_bar.next()

inlier_likelihood = mol_inliers / (non_mol_inliers + mol_inliers)
outlier_likelihood = mol_outliers / (non_mol_outliers + mol_outliers)
lower_likelihood = outlier_likelihood / inlier_likelihood
progress_bar.finish()

print("Non-Mol inliers: " + str(non_mol_inliers))
print("Mol inliers: " + str(mol_inliers))
print("Non-Mol outliers: " + str(non_mol_outliers))
print("Mol outliers: " + str(mol_outliers))
print("Outlier Likelihood: " + str(outlier_likelihood))
print("Inlier Likelihood: " + str(inlier_likelihood))
print("Lower Likelihood: " + str(lower_likelihood))