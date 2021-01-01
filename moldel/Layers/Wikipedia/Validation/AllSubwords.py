from Layers.Wikipedia.WikipediaParser import WikipediaParser

LARGER_WORD = "nieuwsprogramma"
MINIMUM_LENGTH = 4

dictionary = WikipediaParser.get_standard_dictionary()
sub_words = list(WikipediaParser.get_all_sub_words(LARGER_WORD, dictionary, MINIMUM_LENGTH))
sub_words = sorted(sub_words, key = lambda w: (-len(w), w))
print(sub_words)