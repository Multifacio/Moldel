# Show at which frames each player occurs in a given episode.
from Data.PlayerData import get_name
from Layers.FaceVisibility.VideoParser import VideoParser, ParsedVideo

SEASON = 20
EPISODE = 4

player_occurrences = VideoParser.load_parsed_video(SEASON, EPISODE).player_occurrences
for player, occurrences in player_occurrences.items():
    print(get_name(player))
    print(sorted(list(occurrences)))

total_face_frames = 0
for occurrences in player_occurrences.values():
    total_face_frames += len(occurrences)

for player, occurrences in player_occurrences.items():
    print(get_name(player))
    print(len(occurrences) / total_face_frames)