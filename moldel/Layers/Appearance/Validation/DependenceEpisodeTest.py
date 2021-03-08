from Data.PlayerData import get_is_mol
from Layers.Appearance.AppearanceExtractor import AppearanceExtractor
from Layers.Appearance.VideoParser import VideoParser, ParsedVideo
from scipy.stats import pearsonr, kendalltau
import itertools

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20, 21}

input = []
output = []
for season in TEST_SEASONS:
    for episode in itertools.count(1):
        appearances = []
        parsed_video = VideoParser.load_parsed_video(season, episode)
        if parsed_video is None:
            break

        for player in parsed_video.alive_players:
            if not get_is_mol(player):
                appearance = AppearanceExtractor.get_relative_occurrence(player, parsed_video, [True])
                appearances.append(appearance)

        for feat1, feat2 in itertools.permutations(appearances, 2):
            input.append(feat1)
            output.append(feat2)

r, p_value = pearsonr(input, output)
print("Pearson Test (Between):")
print("R value: " + str(r))
print("R-squared value: " + str(r ** 2))
print("p-value: " + str(p_value))
print()

t, p_value = kendalltau(input, output)
print("Kendall Test (Between):")
print("Tau value: " + str(t))
print("p-value: " + str(p_value))
print()

input = []
output = []
for season in TEST_SEASONS:
    for episode in itertools.count(1):
        appearances = []
        parsed_video = VideoParser.load_parsed_video(season, episode)
        if parsed_video is None:
            break

        for player in parsed_video.alive_players:
            if not get_is_mol(player):
                appearance = AppearanceExtractor.get_relative_occurrence(player, parsed_video, [True])
                appearances.append(appearance)

        total = sum(appearances)
        for feature in appearances:
            avg = (total - feature) / (len(appearances) - 1)
            input.append(feature)
            output.append(avg)

r, p_value = pearsonr(input, output)
print("Pearson Test (Mean):")
print("R value: " + str(r))
print("R-squared value: " + str(r ** 2))
print("p-value: " + str(p_value))
print()

t, p_value = kendalltau(input, output)
print("Kendall Test (Mean):")
print("Tau value: " + str(t))
print("p-value: " + str(p_value))