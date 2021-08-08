from collections import Counter as counter
from Data.PlayerData import get_players_in_season
from Layers.Wikipedia.WikipediaParser import WikipediaParser
import textwrap

SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22}
OCCURRENCE_MODE = True
SUBWORD_MODE = True
MIN_SUBWORD_LENGTH = 4
MAX_PRINT_LINE = 160

dictionary = WikipediaParser.get_standard_dictionary()
words = counter()
for season in SEASONS:
    for player in get_players_in_season(season):
        if SUBWORD_MODE:
            add_words = WikipediaParser.full_wiki_parse(player, dictionary, MIN_SUBWORD_LENGTH)
            words += WikipediaParser.get_word_occurrences(add_words)
        else:
            words += WikipediaParser.wiki_parse(player)

print("Number of words: " + str(len(words)))
print("\n".join(textwrap.wrap(str(words), MAX_PRINT_LINE)))