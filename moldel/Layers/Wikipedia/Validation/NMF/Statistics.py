from Data.PlayerData import get_is_mol
from Layers.Wikipedia.WikipediaParser import WikipediaParser
from Tools.Encoders.NaturalSplineEncoding import NaturalSplineEncoding
from scipy.stats import mannwhitneyu
from sklearn.decomposition import NMF
import matplotlib.pyplot as plt
import numpy as np

SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
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

for features, weights in zip(trans_input.T, nmf.components_):
    non_mol = [value for value, is_mol in zip(features, train_output) if is_mol == 0.0]
    mol = [value for value, is_mol in zip(features, train_output) if is_mol == 1.0]
    _, p_value = mannwhitneyu(mol, non_mol, alternative = "two-sided")
    print([wiki_parser.selected_words[i] for i in weights.argsort()[-PRINT_NUM_WORDS_PER_TOPIC:]])
    print(p_value)
