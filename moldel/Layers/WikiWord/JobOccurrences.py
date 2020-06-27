# Count the occurrences of each job for every player

from Data.Player import Player
from Data.PlayerData import get_season
from Data.WikiWord import Linker
from Data.WikiWord.Job import Job
from Layers.WikiWord.WikiWordParser import WikiWordParser, WikiWordData
from typing import Dict, List

def get_job_occurrences(data: Dict[Player, WikiWordData]) -> Dict[Job, List[float]]:
    job_occurrences = dict()
    for job in Job:
        counts = [player_data.job_frequency[job] for player_data in data.values()]
        counts.sort()
        job_occurrences[job] = counts
    return job_occurrences

seasons = {get_season(player) for player in Linker.LINKER.keys()}
data = WikiWordParser.parse(seasons)
job_occurrences = get_job_occurrences(data)
for job, occurrences in job_occurrences.items():
    print(job)
    print(occurrences)
