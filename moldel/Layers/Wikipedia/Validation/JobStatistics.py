from Data.PlayerData import get_is_mol
from Data.Wikipedia.Job import Job
from Layers.Wikipedia.WikipediaParser import WikipediaParser
from scipy.stats import kruskal, levene
import numpy as np

TRAIN_SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

data = WikipediaParser.parse(TRAIN_SEASONS)
predict_input = np.array([d.job_features for p, d in data.items()])
predict_output = np.array([1.0 if get_is_mol(p) else 0.0 for p in data])
for job, column in zip(Job, predict_input.T):
    mol_features = [value for value, is_mol in zip(column, predict_output) if is_mol == 1.0]
    non_mol_features = [value for value, is_mol in zip(column, predict_output) if is_mol == 0.0]
    _, mean_p_value = kruskal(mol_features, non_mol_features)
    _, std_p_value = levene(mol_features, non_mol_features)
    print(str(job) + " - Mean: " + str(mean_p_value) + ", Std: " + str(std_p_value))