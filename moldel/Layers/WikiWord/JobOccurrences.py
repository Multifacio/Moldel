# Count the occurrences of each job for every player
from Data.WikiWord import Linker
from Layers.WikiWord.WikiWordExtractor import WikiWordExtractor
from Layers.WikiWord.WikiWordParser import WikiWordParser

seasons = {player.value.season for player in Linker.LINKER.keys()}
data = WikiWordParser.parse(seasons)
job_occurrences = WikiWordExtractor.get_job_occurrences(data)
for job, occurrences in job_occurrences.items():
    print(job)
    print(occurrences)
