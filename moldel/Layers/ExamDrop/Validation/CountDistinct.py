from collections import Counter

from Data.PlayerData import get_is_mol
from Layers.ExamDrop.ExamDropEncoder import ExamDropEncoder
from Layers.ExamDrop.ExamDropExtractor import ExamDropExtractor
import numpy as np
import sys

TRAIN_SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}

train_data = []
for season in TRAIN_SEASONS:
    train_data.extend(ExamDropExtractor.get_season_data(season, sys.maxsize, True))
train_input = np.array([ExamDropEncoder.extract_features(sample, sys.maxsize) for sample in train_data])

in_answer_ratio = sum(1 for data, input in zip(train_data, train_input) if data.selected_player in data.answer) \
                  / len(train_data)
is_mol_ratio = sum(1 for data, input in zip(train_data, train_input) if get_is_mol(data.selected_player)) \
               / len(train_data)
both_ratio = sum(1 for data, input in zip(train_data, train_input) if get_is_mol(data.selected_player) and
              data.selected_player in data.answer) / len(train_data)

print("In answer ratio: " + str(in_answer_ratio))
print("Is mol ratio: " + str(is_mol_ratio))
print("Both ratio: " + str(both_ratio))
print()
for name, column in zip(ExamDropEncoder.FEATURE_NAMES, train_input.T):
    counter = Counter(column)
    print(name + ": ", [(value, counter[value]) for value in sorted(counter)])