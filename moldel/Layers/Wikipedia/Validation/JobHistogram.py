from Data.Wikipedia.Job import Job
from Layers.Wikipedia.WikipediaParser import WikipediaParser
import matplotlib.pyplot as plt
JOB = Job.ZANGER
SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

dictionary = WikipediaParser.get_standard_dictionary()
occurrences = []
all_data = dict()
for season in SEASONS:
    all_data.update(WikipediaParser.parse_raw(season, dictionary))

for data in all_data.values():
    count = data.job_counts[JOB]
    occurrences.append(count)

plt.hist(occurrences, bins = 10, edgecolor = 'black')
plt.xlabel("Singer Counter")
plt.ylabel("#Players")
plt.show()