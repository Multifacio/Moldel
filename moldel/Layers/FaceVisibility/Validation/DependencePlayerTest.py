from Data.PlayerData import get_is_mol
from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
from Layers.FaceVisibility.VideoParser import VideoParser, ParsedVideo
from scipy.stats import pearsonr, kendalltau
import itertools

TEST_SEASONS = {13, 14, 15, 16, 17, 18, 19, 20}

appearances = dict()
for season in TEST_SEASONS:
    for episode in itertools.count(1):
        parsed_video = VideoParser.load_parsed_video(season, episode)
        if parsed_video is None:
            break

        for player in parsed_video.alive_players:
            if not get_is_mol(player):
                appearance = FaceVisibilityExtractor.get_relative_occurrence(player, parsed_video, [True])
                appearances[player] = appearances.get(player, []) + [appearance]

input = []
output = []
for player, features in appearances.items():
    for feat1, feat2 in itertools.combinations(features, 2):
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
for player, features in appearances.items():
    if len(features) > 1:
        total = sum(features)
        for feature in features:
            avg = (total - feature) / (len(features) - 1)
            input.append(avg)
            output.append(feature)

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