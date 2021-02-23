from collections import Counter
from Data.MentionData.Linker import LINKER
from Data.PlayerData import get_players_in_season
import csv

# Before parsing an episode WAV file, you have to do the follow things with Audacity on the WAV file:
# 1. Change the tempo of the sound file by -25%
# 2. Amplify the sound file by 6 dB

SEASON = 22
TEXT_FILE = "/home/haico/Dropbox/WIDM/Seizoen 22/Speeches/Episode 2.csv"

counter = Counter()
players = get_players_in_season(SEASON)
last_players = set()
with open(TEXT_FILE, newline='') as file:
    reader = csv.reader(file, delimiter=',', quotechar='"')
    for row in reader:
        for interpretation in row:
            interpretation = " " + interpretation.lower() + " "
            detected = set()
            for player in players:
                for keyword in LINKER[player]:
                    keyword = " " + keyword + " "
                    if keyword in interpretation:
                        detected.add(player)
                        break
            for player in detected.difference(last_players):
                counter[player] += 1
            if detected:
                last_players = detected

print(counter)