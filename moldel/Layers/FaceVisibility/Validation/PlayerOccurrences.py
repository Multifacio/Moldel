# Show at which frames each player occurs in a given episode.
from Data.PlayerData import get_name
from Layers.FaceVisibility.VideoParser import VideoParser, ParsedVideo

SEASON = 17
EPISODE = 5

parsed_video = VideoParser.load_parsed_video(SEASON, EPISODE)
player_occurrences = parsed_video.player_occurrences
alive_players = parsed_video.alive_players

for player, occurrences in player_occurrences.items():
    if player in alive_players:
        print(get_name(player))
        print(sorted(list(occurrences)))

total_face_frames = 0
for player, occurrences in player_occurrences.items():
    if player in alive_players:
        total_face_frames += len(occurrences)

for player, occurrences in player_occurrences.items():
    if player in alive_players:
        print(get_name(player))
        print(len(occurrences) / total_face_frames)