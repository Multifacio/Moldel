# Show at which frames each player occurs in a given episode.
from Layers.FaceVisibility.VideoParser import VideoParser, ParsedVideo

SEASON = 11
EPISODE = 1

player_occurrences = VideoParser.load_parsed_video(SEASON, EPISODE).player_occurrences
for player, occurrences in player_occurrences.items():
    print(player.value.name)
    print(sorted(list(occurrences)))

total_face_frames = 0
for occurrences in player_occurrences.values():
    total_face_frames += len(occurrences)

for player, occurrences in player_occurrences.items():
    print(player.value.name)
    print(len(occurrences) / total_face_frames)