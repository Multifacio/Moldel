# Count the occurrences of each job for a given player
from Data.Player import Player
from Data.Wikipedia.Job import Job
from Layers.Wikipedia.WikipediaParser import WikipediaParser

PLAYER = Player.NADJA_7

dictionary = WikipediaParser.get_standard_dictionary()
features = WikipediaParser.extract_player_features(PLAYER, dictionary)
print("Number of words: " + str(features.number_words))
for job in Job:
    print(str(job) + ": " + str(features.job_counts[job]))
