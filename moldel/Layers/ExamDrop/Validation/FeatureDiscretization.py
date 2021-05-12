from Data.PlayerData import get_is_mol
from Layers.ExamDrop.ExamDropEncoder import ExamDropEncoder
from Layers.ExamDrop.ExamDropExtractor import ExamDropExtractor
from Tools.Encoders.StableDiscretizer import StableDiscretizer
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import sys

TRAIN_SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
MIN_CLUSTER_SIZE = 120

train_data = []
for season in TRAIN_SEASONS:
    train_data.extend(ExamDropExtractor.get_season_data(season, sys.maxsize, True))
train_input = np.array([ExamDropEncoder.extract_features(sample, sys.maxsize) for sample in train_data])
train_output = np.array([1.0 if get_is_mol(sample.selected_player) else 0.0 for sample in train_data])
m = ExamDropEncoder.NUM_CONTINUOUS_FEATURES

for column, feature_name in zip(train_input.T[:-m], ExamDropEncoder.FEATURE_NAMES[:-m]):
    trans_data = column[:,np.newaxis]
    discretizer = StableDiscretizer(MIN_CLUSTER_SIZE)
    trans_data = discretizer.fit_transform(trans_data)
    print(feature_name + " - Num Features: " + str(len(trans_data[0])))

    in_answer_input = [row for row, data in zip(trans_data, train_data) if data.selected_player in data.answer]
    in_answer_output = [to for to, data in zip(train_output, train_data) if data.selected_player in data.answer]
    regression = LinearRegression()
    regression.fit(in_answer_input, in_answer_output)

    X = np.array([pi for pi in sorted(set(column))])
    predict_input = discretizer.transform(X[:, np.newaxis])
    predict_output = regression.predict(predict_input)
    plt.plot(X, predict_output)
    plt.title(feature_name + " - In Answer")
    plt.show()