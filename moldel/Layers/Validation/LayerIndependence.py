from Data.LastEpisodes import get_last_episode
from Data.PlayerData import get_players_in_season, get_is_mol
from Layers.Special.MemoryLayer import MemoryLayer
from scipy.stats import pearsonr, kendalltau
import math

TRAIN_SEASONS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
TEST_SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
layer1 = MemoryLayer("Wikipedia Stacker")
layer2 = MemoryLayer("Appearance Stacker")

pairs = []
for season in TEST_SEASONS:
    players = {player for player in get_players_in_season(season) if not get_is_mol(player)}
    for episode in range(get_last_episode(season) + 1):
        prediction1 = layer1.compute_distribution(season, episode, TRAIN_SEASONS)
        prediction2 = layer2.compute_distribution(season, episode, TRAIN_SEASONS)
        excluded = {player for player, prob in prediction1.items() if prob == 0.0}
        excluded.update({player for player, prob in prediction2.items() if prob == 0.0})
        included = players.difference(excluded)

        num_players = len(included) + 1
        uniform = 1 / num_players
        excluded = {player for player, prob in prediction1.items() if math.isclose(prob, uniform, abs_tol = 2e-3)}
        excluded.update({player for player, prob in prediction2.items() if math.isclose(prob, uniform, abs_tol = 2e-3)})
        included.difference_update(excluded)
        pairs += [(prediction1[player] * num_players, prediction2[player] * num_players) for player in included]

print(pairs)
print(len(pairs))
predictions1 = [p1 for p1, p2 in pairs]
predictions2 = [p2 for p1, p2 in pairs]

r, p_value = pearsonr(predictions1, predictions2)
print("Pearson Test (Between):")
print("R value: " + str(r))
print("R-squared value: " + str(r ** 2))
print("p-value: " + str(p_value))
print()

t, p_value = kendalltau(predictions1, predictions2)
print("Kendall Test (Between):")
print("Tau value: " + str(t))
print("p-value: " + str(p_value))
print()