from Data.Player import Player
from Layers.FaceVisibility.VideoParser import ParsedVideo, VideoParser
from sklearn.preprocessing import StandardScaler
from typing import Dict, List, NamedTuple, Tuple, Set, Union
import itertools
import math
import numpy as np

Encoding = NamedTuple("Encoding", [("season", int), ("occurrences", List[float]), ("is_mol", Union[bool, None])])
class FaceVisibilityExtractor:
    SMALL_LOG_ADDITION = 0.0001 # Small value that is added to prevent that the logarithm of 0.0 is taken.

    @classmethod
    def get_train_data(self, seasons: Set[int], upto_episode: int) -> List[Encoding]:
        """ Get all non-fully processed train data from a given season.

        Parameters:
            season (int): The season from which the train data will be obtained.
            upto_episode (int): The last episode up to (and including) for which we use the FaceVisibility data in the
                prediction season.

        Returns:
            A list of all train data non-fully processed encodings.
        """
        train_data = []
        for season in seasons:
            parsed_videos = self.__get_parsed_videos(season)
            player_episodes = self.__get_players_with_episodes(season, parsed_videos)
            for player, episodes in player_episodes.items():
                for selected_episodes in itertools.combinations(episodes, upto_episode):
                    encoding = self.__get_input_data(player, season, selected_episodes, parsed_videos,
                                                     player.value.is_mol)
                    train_data.append(encoding)
        return train_data

    @classmethod
    def get_predict_data(self, season: int, upto_episode: int) -> Dict[Player, Encoding]:
        """ Get all non-fully processed data from the predict season, i.e. the season in which we make a prediction.

        Parameters:
            season (int): The season for which we want to make predictions.
            upto_episode (int): The last episode up to (and including) for which we use the FaceVisibility data in the
                prediction season.

        Returns:
            A dictionary with the non-fully processed feature encoding for every player in that given season.
        """
        parsed_videos = self.__get_parsed_videos(season)
        predict_data = dict()
        for player in parsed_videos[upto_episode].alive_players:
            predict_data[player] = self.__get_input_data(player, season, tuple(range(1, upto_episode + 1)),
                                                         parsed_videos, None)
        return predict_data

    @classmethod
    def __get_parsed_videos(self, season: int) -> Dict[int, ParsedVideo]:
        """ Load the parsed videos for the given season.

        Parameters:
            season (int): The season for which we load the parsed videos.

        Returns:
            The parsed video data for this season. The key represent the episode numbers and the value is the parsed
            video data for that episode.
        """
        parsed_videos = dict()
        for episode in itertools.count(1):
            parsed_video = VideoParser.load_parsed_video(season, episode)
            if parsed_video is None:
                break
            else:
                parsed_videos[episode] = parsed_video
        return parsed_videos

    @classmethod
    def __get_players_with_episodes(self, season: int, parsed_videos: Dict[int, ParsedVideo]) -> Dict[Player, Set[int]]:
        """ Get the players that participated in this season with the corresponding episodes in which these players
        participated.

        Parameters:
            season (int): The season from which we get the players.
            parsed_videos (Dict[int, ParsedVideo]): All the parsed videos from the episodes of that season.

        Returns:
            A dictionary with as key the players and as value a set of video parsed episodes in which that player occurs.
        """
        player_episodes = dict()
        season_players = [player for player in Player if player.value.season == season]
        for player in season_players:
            episode_occurrences = {episode for episode, data in parsed_videos.items() if player in data.alive_players}
            player_episodes[player] = episode_occurrences
        return player_episodes

    @classmethod
    def __get_input_data(self, player: Player, season: int, selected_episodes: Tuple[int],
                         parsed_videos: Dict[int, ParsedVideo], is_mol: Union[bool, None]) -> np.array:
        """ Get the input/feature encoding for a player for a combination of selected episodes.

        Parameters:
            player (Player): The player for which we get the input/feature encoding.
            season (int): The season in which this player participated.
            selected_episodes (Tuple[int]): The selected combination of episodes from which the features get extracted.
            parsed_videos (Dict[int, ParsedVideo]): The parsed video data of the episodes in this season.
            is_mol (Union[bool, None]): True if that player is the Mol, false if that player is not the Mol. None if it
                is unknown whether that player is the Mol.
        Returns:
            The input/feature encoding for the given player with this combination of episodes.
        """
        occurrences = []
        for episode in selected_episodes:
            occurrences.append(self.__get_relative_occurrence(player, parsed_videos[episode]))
        occurrences.sort()
        return Encoding(season, occurrences, is_mol)

    @classmethod
    def __get_relative_occurrence(self, player: Player, parsed_video: ParsedVideo) -> float:
        """ Get the relative occurrence of a player in a given episode compared to the total occurrence of all players.

        Parameters:
            player (Player): The player of which we determine the relative occurrence.
            parsed_video (ParsedVideo): The parsed video data about the episode.

        Returns:
            The relative occurrence of the player in the given episode.
        """
        total_occurrence = 0
        for p in parsed_video.alive_players:
            total_occurrence += len(parsed_video.player_occurrences[p])
        own_occurrence = len(parsed_video.player_occurrences[player]) * len(parsed_video.alive_players)
        return math.log(self.SMALL_LOG_ADDITION + own_occurrence / total_occurrence)