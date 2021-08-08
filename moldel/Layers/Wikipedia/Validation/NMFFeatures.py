from sklearn.linear_model import LogisticRegression

from Data.PlayerData import get_is_mol
from Layers.Wikipedia.WikipediaParser import WikipediaParser
from Tools.Encoders.NaturalSplineEncoding import NaturalSplineEncoding
from Tools.Encoders.SemiRankTransformer import SemiRankTransformer, Setting
from scipy.stats import gamma
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt
import numpy as np

SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
NUM_TOPICS = 45

PRINT_NUM_WORDS_PER_TOPIC = 50
MIN_SUBWORD_LENGTH = 4
MIN_WORD_OCCURRENCE = 8

wiki_parser = WikipediaParser(SEASONS, MIN_SUBWORD_LENGTH, MIN_WORD_OCCURRENCE)
train_data = wiki_parser.extract_features()
train_input = np.array([ti for ti in train_data.values()])
train_output = np.array([get_is_mol(p) for p in train_data.keys()])

nmf = NMF(n_components = NUM_TOPICS, max_iter = 1000, init = "nndsvd")
trans_input = nmf.fit_transform(train_input)
rank_transform = SemiRankTransformer([Setting(num_clusters = 3, ignore_values = {0}) for _ in range(NUM_TOPICS)])
trans_input = rank_transform.fit_transform(trans_input)

print("Error: ")
print(nmf.reconstruction_err_)

print()
print("Top Words per Topic")
for weights in nmf.components_:
    print([wiki_parser.selected_words[i] for i in weights.argsort()[-PRINT_NUM_WORDS_PER_TOPIC:]])
print()

for column in trans_input.T:
    # encoder = NaturalSplineEncoding([4])
    # column_input = encoder.fit_transform(np.array([[x] for x in column]))
    classifier = LogisticRegression()
    classifier.fit(np.array([[x] for x in column]), train_output)
    X = np.linspace(0, max(column), 10000)
    print(X)
    # Y = np.array([classifier.predict_proba(encoder.transform(np.array([[x]])))[0][1] for x in X])
    Y = classifier.predict_proba(np.array([[x] for x in X]))[:,1]
    print(Y)

    print("Probability Range: " + str(min(Y)) + " - " + str(max(Y)))

    plt.plot(X, Y)
    plt.scatter(column, train_output)
    plt.show()
