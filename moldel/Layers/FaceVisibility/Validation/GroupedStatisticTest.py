from Data.PlayerData import get_is_mol
from Layers.FaceVisibility.VideoParser import VideoParser
from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
from scipy.stats import mannwhitneyu
from statistics import mean
import itertools
import matplotlib.pyplot as plt
import numpy as np

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20, 21}

appearances = dict()
for season in TEST_SEASONS:
    for episode in itertools.count(1):
        parsed_video = VideoParser.load_parsed_video(season, episode)
        if parsed_video is None:
            break

        for player in parsed_video.alive_players:
            appearance = FaceVisibilityExtractor.get_relative_occurrence(player, parsed_video, [True])
            appearances[player] = appearances.get(player, []) + [appearance]

train_input = []
train_output = []
for player, features in appearances.items():
    train_input.append(mean(features))
    train_output.append(1.0 if get_is_mol(player) else 0.0)

non_mol = [data for data, label in zip(train_input, train_output) if label == 0.0]
mol = [data for data, label in zip(train_input, train_output) if label == 1.0]
statistics, p_value = mannwhitneyu(mol, non_mol, alternative = "less")
print("Score: " + str(statistics))
print("p-value: " + str(p_value))

train_output += np.random.uniform(-0.1, 0.1, len(train_output))
print("Number of non-Mol players: " + str(len(non_mol)))
print("Number of Mol players: " + str(len(mol)))
plt.figure(figsize=(12, 3))
plt.scatter(train_input, train_output, s = 4)
plt.xlabel("Relative Appearance")
plt.ylabel("Is 'mol'")
plt.yticks([0.0, 1.0])
plt.gcf().subplots_adjust(bottom = 0.15)

plt.show()