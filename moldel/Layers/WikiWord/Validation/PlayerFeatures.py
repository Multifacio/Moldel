# Count the occurrences of each job for a given player
from Data.Player import Player
from Data.WikiWord.Job import Job
from Layers.WikiWord.WikiWordParser import WikiWordParser

PLAYER = Player.NADJA_7

dictionary = WikiWordParser.get_standard_dictionary()
features = WikiWordParser.extract_player_features(PLAYER, dictionary)
print("Number of words: " + str(features.number_words))
for job in Job:
    print(str(job) + ": " + str(features.job_counts[job]))
