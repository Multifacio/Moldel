from Data.Player import Player
from Layers.Appearance.ParserConfiguration import ALIVE_PLAYERS, FACE_IMAGE_LOCATIONS, EPISODE_VIDEO_LOCATION, \
    FRAME_SKIP, SAVE_FOLDER, SEASON_NUMBER, EPISODE_NUMBER
from typing import Dict, Set, List, NamedTuple, Union
import cv2
import face_recognition as fr
import os
import pickle
import rootpath

ParsedVideo = NamedTuple("ParsedVideo", [("player_occurrences", Dict[Player, Union[List[int], Set[int]]]),
                                         ("alive_players", Set[Player]), ("frame_skip", int)])
class VideoParser:
    """ The Video Parser parses when the face of a candidate is visible during an episode based on the given video
    by the Parser Configuration file. This code is based on the project of mattijn: https://github.com/mattijn/widm
    and uses the https://github.com/ageitgey/face_recognition and https://github.com/skvark/opencv-python projects.
    Update the Parser Configuration file manually before running this code. """

    # Setting the tolerance higher means that faces get detected more earlier
    TOLERANCE = 0.50

    # Every this number of frames progress will be shown of the Video Parser
    PROGRESS_FRAMES_FREQUENCY_PRINT = 500

    @staticmethod
    def parse():
        """ Parse the video given by the Parser Configuration file into a set of frames in for every player in which
        that player occurs and save that data plus the player that are still alive during that episode and the
        FRAME_SKIP value into a file. """
        all_players = list(FACE_IMAGE_LOCATIONS.keys())
        face_encodings = VideoParser.__load_faces_encodings(all_players)
        player_occurrences = VideoParser.__get_player_occurrences(all_players, face_encodings)
        VideoParser.__save_parsed_video(player_occurrences)

    @staticmethod
    def has_parsed_video(season: int, episode: int) -> bool:
        """ Check if a certain video has been parsed.

        Parameters:
            season (int): The season number of which we check if the video has been parsed.
            episode (int): The episode number of which we check if the video has been parsed.

        Returns:
            True if the video has been parsed, false if the video has not (yet) been parsed.
        """
        file_path = VideoParser.__get_parsed_video_file_path(season, episode)
        return os.path.isfile(file_path)

    @staticmethod
    def load_parsed_video(season: int, episode: int) -> Union[ParsedVideo, None]:
        """ Load the Parsed Video data which includes the player occurrences, that is a dictionary with a set of frames
        per player in which that player occurs, the alive players, which are all the players that are still there in
        that episode, and the FRAME_SKIP value used.

        Parameters:
            season (int): The season number from which the Parsed Video data gets extracted.
            episode (int): The episode number from which the Parsed Video data gets extracted.

        Returns:
            None if this video has not yet been parsed (so the data is not available). Returns the Parsed Video of the
            episode if it has been parsed.
        """
        file_path = VideoParser.__get_parsed_video_file_path(season, episode)
        if not os.path.isfile(file_path):
            return None

        with open(file_path, 'rb') as file:
            video_parsing = pickle.load(file)

        parsed_video = ParsedVideo(*video_parsing)
        player_occurrences = {player: sorted(occurrences) for player, occurrences in parsed_video.player_occurrences.items()}
        return ParsedVideo(player_occurrences, parsed_video.alive_players, parsed_video.frame_skip)

    @staticmethod
    def __load_faces_encodings(all_players: List[Player]) -> List:
        """ Load the face encodings of all players.

        Parameters:
            all_players (List[Player]): A list with all players that participated in this season.

        Returns:
            A list of face encodings of the players in the same order as the all_players list.
        """
        face_encodings = []
        for player in all_players:
            image = fr.load_image_file(FACE_IMAGE_LOCATIONS[player])
            face_encodings.append(fr.face_encodings(image)[0])

        return face_encodings

    @staticmethod
    def __get_player_occurrences(all_players: List[Player], face_encodings: List) -> Dict[Player, Set[int]]:
        """ Determine for every player at which moments his/her face is visible during the episode.

        Parameters:
            all_players (List[Player]): A list with all players that participated in this season.
            face_encodings (List): A list of face encodings of the players in the same order as the all_players list.

        Returns:
            Dict[Player, Set[int]]: A dictionary with as key the players and as value a set which contains all frames
            numbers in which the player occurs.
        """
        occurrences = dict()
        for player in all_players:
            occurrences[player] = set()

        video_capture = cv2.VideoCapture(EPISODE_VIDEO_LOCATION)
        length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_index = 0
        while video_capture.isOpened():
            continues, frame = video_capture.read()
            if not continues:  # If this is the last frame then stop
                video_capture.release()
                break
            frame_index += 1
            if frame_index % VideoParser.PROGRESS_FRAMES_FREQUENCY_PRINT == 0: # Prints the progress
                print('{}/{}'.format(frame_index, length))
            if frame_index % FRAME_SKIP == 0:  # Only analyse every FRAME_SKIP frame
                player_occurrence = VideoParser.__get_player_occurrence_in_frame(frame, all_players, face_encodings)
                for player in player_occurrence:
                    occurrences[player] = occurrences[player].union({frame_index})

        return occurrences

    @staticmethod
    def __get_player_occurrence_in_frame(frame, all_players: List[Player], face_encodings: List) -> Set[Player]:
        """ Find all player faces in this frame of the video.

        Parameters:
            frame: The frame which gets analysed on the occurrence of faces of players.
            all_players (List[Player]): A list with all players that participated in this season.
            face_encodings (List): A list of face encodings of the players in the same order as the all_players list.
        """
        player_occurrence = set()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame = frame[:, :, ::-1]
        face_locations = fr.face_locations(rgb_frame)
        found_faces = fr.face_encodings(rgb_frame, face_locations)
        for ff in found_faces:
            # Check which candidate face matches with the founded face
            match = fr.compare_faces(face_encodings, ff, tolerance=VideoParser.TOLERANCE)
            for i, player in enumerate(all_players):
                if match[i]:
                    player_occurrence.add(player)
                    break

        return player_occurrence

    @staticmethod
    def __save_parsed_video(player_occurrences: Dict[Player, Set[int]]):
        """ Save the player occurrences, alive players and FRAME_SKIP value to a file.

        Parameters:
            player_occurrences (Dict[Player, Set[int]]): A dictionary with as key the players and as value a set which
            contains all frames numbers in which the player occurs.
        """
        file_path = VideoParser.__get_parsed_video_file_path(SEASON_NUMBER, EPISODE_NUMBER)
        with open(file_path, 'wb') as file:
            pickle.dump((player_occurrences, ALIVE_PLAYERS, FRAME_SKIP), file)

    @staticmethod
    def __get_parsed_video_file_path(season: int, episode: int) -> str:
        """ Get the file path where the parsed video is/will be stored.

        Parameters:
            season (int): The season number of the parsed video.
            episode (int): The episode number of the parsed video.

        Returns:
            The file path where the parsed video is/will be stored.
        """
        return rootpath.detect() + "/" + SAVE_FOLDER + "s" + str(season) + "e" + str(episode) + ".data"

if __name__ == "__main__":
    vp = VideoParser()
    vp.parse()