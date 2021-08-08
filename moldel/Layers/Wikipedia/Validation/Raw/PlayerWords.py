from Data.Player import Player
from Layers.Wikipedia.WikipediaParser import WikipediaParser
import textwrap

PLAYER = Player.MEREL_19
OCCURRENCE_MODE = False
SUBWORD_MODE = False
MIN_SUBWORD_LENGTH = 4
MAX_PRINT_LINE = 160

dictionary = WikipediaParser.get_standard_dictionary()
if SUBWORD_MODE:
    words = WikipediaParser.full_wiki_parse(PLAYER, dictionary, MIN_SUBWORD_LENGTH)
    words = WikipediaParser.get_word_occurrences(words)
else:
    words = WikipediaParser.wiki_parse(PLAYER)

print("Number of words: " + str(len(words)))
print("\n".join(textwrap.wrap(str(words), MAX_PRINT_LINE)))
