from scipy.special import logit, expit

from Data.PlayerData import get_is_mol
from Layers.ExamDrop.ExamDropEncoder import ExamDropEncoder
from Layers.ExamDrop.ExamDropExtractor import ExamDropExtractor
from Tools.Encoders.NaturalSplineEncoding import NaturalSplineEncoding
from Tools.Encoders.StableDiscretizer import StableDiscretizer
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np
import sys

TRAIN_SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
MIN_CLUSTER_SIZE = 120
NUM_CURVES = 4

train_data = []
for season in TRAIN_SEASONS:
    train_data.extend(ExamDropExtractor.get_season_data(season, sys.maxsize, True))
train_input = np.array([ExamDropEncoder.extract_features(sample, sys.maxsize) for sample in train_data])
train_output = np.array([1.0 if get_is_mol(sample.selected_player) else 0.0 for sample in train_data])
m = ExamDropEncoder.NUM_CONTINUOUS_FEATURES

discretizer = StableDiscretizer(MIN_CLUSTER_SIZE)
discrete_input = discretizer.fit_transform(train_input[:,:-m])
spline_encoder = NaturalSplineEncoding([NUM_CURVES for _ in range(m)])
continuous_input = spline_encoder.fit_transform(train_input[:,-m:])
trans_input = np.concatenate((discrete_input, continuous_input), axis = 1)

in_answer_input = [row for row, data in zip(trans_input, train_data) if data.selected_player in data.answer]
in_answer_output = [to for to, data in zip(train_output, train_data) if data.selected_player in data.answer]
classifier = LogisticRegression(max_iter = 1000)
classifier.fit(in_answer_input, in_answer_output)
ratio = sum(in_answer_output) / len(in_answer_output)
logit_ratio = logit(ratio)

l = 0
for i, item in enumerate(zip(discretizer.bins, ExamDropEncoder.FEATURE_NAMES[:-m])):
    bins, name = item
    h = l + len(bins)
    coefs = classifier.coef_[0, l:h]
    output = dict()
    for row, trans in zip(train_input, trans_input):
        output[row[i]] = np.dot(coefs, trans[l:h])
    X = np.array([x for x in sorted(output.keys())])
    Y = np.array([output[x] for x in X])
    Y += logit_ratio - np.mean(Y)
    Y = expit(Y) - ratio
    plt.plot(X, Y)
    plt.title(name + " - In Answer")
    plt.xticks(X)
    plt.grid(True)
    plt.show()
    l = h

for i, name in enumerate(ExamDropEncoder.FEATURE_NAMES[-m:]):
    i = len(ExamDropEncoder.FEATURE_NAMES) - m + i
    h = l + NUM_CURVES
    coefs = classifier.coef_[0, l:h]
    output = dict()
    for row, trans in zip(train_input, trans_input):
        output[row[i]] = np.dot(coefs, trans[l:h])
    X = np.array([x for x in sorted(output.keys())])
    Y = np.array([output[x] for x in X])
    Y += logit_ratio - np.mean(Y)
    Y = expit(Y) - ratio
    plt.plot(X, Y)
    plt.title(name + " - In Answer")
    plt.grid(True)
    plt.show()
    l = h