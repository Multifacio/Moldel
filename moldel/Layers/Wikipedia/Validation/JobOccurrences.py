from Data.Wikipedia.Job import Job
from Layers.Wikipedia.WikipediaParser import WikipediaParser

SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

dictionary = WikipediaParser.get_standard_dictionary()
job_occurrences = dict()
all_data = dict()
for season in SEASONS:
    all_data.update(WikipediaParser.parse_raw(season, dictionary))

for data in all_data.values():
    for job in Job:
        count = data.job_counts[job]
        job_occurrences[job] = job_occurrences.get(job, []) + [count]

for job, occurrences in job_occurrences.items():
    print(job)
    print(sorted(occurrences))

print("Number of words:")
print(sorted([data.number_words for data in all_data.values()]))