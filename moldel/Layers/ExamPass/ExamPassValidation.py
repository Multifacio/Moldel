from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Exams.All import EXAM_DATA
from Data.PlayerData import get_mol_in_season
from sklearn.linear_model import LogisticRegression
import numpy as np
import sys

TRAIN_SEASONS = {7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
train_input = []
train_output = []
for season in TRAIN_SEASONS:
    season = EXAM_DATA[season]
    for episode in season.episodes.values():
        if episode.result.drop != DropType.EXECUTION_DROP:
            continue

        joker_usage = episode.total_joker_usage(exemption_value = sys.maxsize)
        for player in episode.players:
            own_usage = joker_usage[player]
            less_1_joker = sum(joker_usage[p] <= own_usage - 1 for p in joker_usage if p not in episode.result.players)
            same_jokers = sum(joker_usage[p] == own_usage for p in joker_usage if p not in episode.result.players)
            more_1_joker = sum(joker_usage[p] >= own_usage + 1 for p in joker_usage if p not in episode.result.players)
            train_input.append([less_1_joker, same_jokers, more_1_joker])
            train_output.append(1.0 if player in episode.result.players else 0.0)
train_input = np.array(train_input)
train_output = np.array(train_output)

estimator = LogisticRegression()
estimator.fit(train_input, train_output)

for season_id in TRAIN_SEASONS:
    season = EXAM_DATA[season_id]
    for episode in season.episodes.values():
        if episode.result.drop != DropType.EXECUTION_DROP:
            continue

        drop_probabilities = dict()
        joker_usage = episode.total_joker_usage(exemption_value = sys.maxsize)
        for player in episode.players:
            if episode.input[player].immunity:
                drop_probabilities[player] = 0.0
            else:
                own_usage = joker_usage[player]
                less_1_joker = sum(joker_usage[p] <= own_usage - 1 for p in joker_usage if p != player)
                same_jokers = sum(joker_usage[p] == own_usage for p in joker_usage if p != player)
                more_1_joker = sum(joker_usage[p] >= own_usage + 1 for p in joker_usage if p != player)
                train_input = [less_1_joker, same_jokers, more_1_joker]
                train_output = 1.0 if player in episode.result.players else 0.0
                drop_probability = estimator.predict_proba(np.array([train_input]))[0][1]
                drop_probabilities[player] = drop_probability

        probability_sum = sum(prob for prob in drop_probabilities.values())
        drop_probabilities = {player: prob / probability_sum for player, prob in drop_probabilities.items()}
        print(drop_probabilities)
        for player in episode.result.players:
            print(player)
            print(drop_probabilities[player])
        print("Mol Probability: ")
        print(drop_probabilities[get_mol_in_season(season_id)])
        print("Uniform Probability: ")
        print(1 / len(drop_probabilities))