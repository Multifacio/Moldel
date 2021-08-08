from collections import Counter as counter
from Data.PlayerData import get_players_in_season
from Layers.Wikipedia.WikipediaParser import WikipediaParser
import textwrap

SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
MAX_PRINT_LINE = 160
MIN_WORD_OCCURRENCE = 8
MIN_SUBWORD_LENGTH = 4

dictionary = WikipediaParser.get_standard_dictionary()
occurrences = counter()
for season in SEASONS:
    for player in get_players_in_season(season):
        add_occurrences = WikipediaParser.full_wiki_parse(player, dictionary, MIN_SUBWORD_LENGTH)
        occurrences += WikipediaParser.get_word_occurrences(add_occurrences)
selection = {word for word, c in occurrences.items() if c >= MIN_WORD_OCCURRENCE}

words = counter()
for season in SEASONS:
    for player in get_players_in_season(season):
        words += WikipediaParser.full_wiki_parse(player, dictionary, MIN_SUBWORD_LENGTH)
words = counter({word: words[word] for word in selection})

print("Number of words: " + str(len(words)))
print("\n".join(textwrap.wrap(str(words), MAX_PRINT_LINE)))