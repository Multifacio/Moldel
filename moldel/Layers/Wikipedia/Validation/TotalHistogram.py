from Layers.Wikipedia.WikipediaParser import WikipediaParser
import matplotlib.pyplot as plt

SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

dictionary = WikipediaParser.get_standard_dictionary()
job_occurrences = dict()
all_data = dict()
for season in SEASONS:
    all_data.update(WikipediaParser.parse_raw(season, dictionary))

number_words = [data.number_words for data in all_data.values()]

plt.hist(number_words, bins = 10, edgecolor = 'black')
plt.xlabel("Total Number of Words")
plt.ylabel("#Players")
plt.show()