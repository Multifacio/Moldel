# Count all words for these seasons
from collections import Counter
from Data.Player import Player
from Data.PlayerData import get_season
from Layers.WikiWord.WikiWordParser import WikiWordParser
from nltk.corpus import stopwords

SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

pure_counter = Counter()
for player in Player:
    if get_season(player) in SEASONS:
        pure_counter += WikiWordParser.wiki_file_parse(player)

compound_counter = Counter()
dictionary = WikiWordParser.get_standard_dictionary()
stop_words = set(stopwords.words('dutch'))
for word, count in pure_counter.items():
    sub_words = WikiWordParser.get_all_sub_words(word, dictionary, WikiWordParser.MIN_LENGTH_COMPOUND_WORD)
    sub_words.difference_update(stop_words)
    for sub_word in sub_words:
        compound_counter[sub_word] += count

print(compound_counter)