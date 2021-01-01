from Data.PlayerData import get_is_mol
from Layers.Wikipedia.WikipediaParser import WikipediaParser
import matplotlib.pyplot as plt

SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

data = WikipediaParser.parse(SEASONS)
train_input = [d.word_feature for p, d in data.items()]
train_output = [1.0 if get_is_mol(p) else 0.0 for p in data]

plt.figure(figsize=(12, 3))
plt.xlabel("Relative Appearance")
plt.ylabel("Is 'mol'")
plt.yticks([0.0, 1.0])
plt.gcf().subplots_adjust(bottom = 0.15)
plt.scatter(train_input, train_output, s = 4)
plt.show()