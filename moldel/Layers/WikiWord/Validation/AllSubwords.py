from Layers.WikiWord.WikiWordParser import WikiWordParser

LARGER_WORD = "nieuwsprogramma"
MINIMUM_LENGTH = 4

dictionary = WikiWordParser.get_standard_dictionary()
sub_words = list(WikiWordParser.get_all_sub_words(LARGER_WORD, dictionary, MINIMUM_LENGTH))
sub_words = sorted(sub_words, key = lambda w: (-len(w), w))
print(sub_words)