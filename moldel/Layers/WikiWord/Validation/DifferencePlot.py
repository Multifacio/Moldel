from Data.PlayerData import get_is_mol, get_season
from Data.WikiWord.Job import Job
from Layers.WikiWord.WikiWordParser import WikiWordParser
from scipy.stats import kruskal, levene
import matplotlib.pyplot as plt
import numpy as np

SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
DIFFERENCE = 1

data = WikiWordParser.parse(SEASONS, 1)
mol_input = dict()
for p, d in data.items():
    if get_is_mol(p):
        mol_input[get_season(p)] = d.job_features

train_input = np.array([np.abs(d.job_features - mol_input[get_season(p) - DIFFERENCE]) for p, d in data.items()
                        if get_season(p) - DIFFERENCE in SEASONS])
train_output = np.array([1.0 if get_is_mol(p) else 0.0 for p in data if get_season(p) - DIFFERENCE in SEASONS])
for job, column in zip(Job, train_input.T):
    mol_features = [value for value, is_mol in zip(column, train_output) if is_mol == 1.0]
    non_mol_features = [value for value, is_mol in zip(column, train_output) if is_mol == 0.0]
    _, mean_p_value = kruskal(mol_features, non_mol_features)
    _, std_p_value = levene(mol_features, non_mol_features)
    print(str(job) + " - Mean: " + str(mean_p_value) + ", Std: " + str(std_p_value))

for column in train_input.T:
    plt.figure(figsize=(12, 3))
    plt.xlabel("Relative Appearance")
    plt.ylabel("Is 'mol'")
    plt.yticks([0.0, 1.0])
    plt.gcf().subplots_adjust(bottom = 0.15)
    plt.scatter(column, train_output, s = 4)
    plt.show()