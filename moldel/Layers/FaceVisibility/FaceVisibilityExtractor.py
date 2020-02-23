from Data.Player import Player
from Layers.FaceVisibility.VideoParser import ParsedVideo, VideoParser
from typing import Dict, List, Tuple, Set
import itertools
import math
import numpy as np

class FaceVisibilityExtractor:
    # The quantiles in which the all occurrences in an episode get split up. These split ups are used to determine the
    # quantile occurrences, which is the relative occurrence of the player in every quantile.
    FRAME_QUANTILES = [0.0, 0.2, 0.4, 0.6, 0.8]

    # The quantile occurrence for every quantile gets upperbounded by this value (so higher values will be made equal
    # to this value).
    QUANTILE_OCCURRENCE_UPPERBOUND = 0.2

    SMALL_LOG_ADDITION = 0.0001

    @classmethod
    def get_train_data(self, season: int, predict_episode: int) -> Tuple[List[np.array], List[int]]:
        """ Get all train data from a given season.

        Parameters:
            season (int): The season from which the train data will be obtained.
            predict_episode (int): The latest episode used in the predict season.

        Returns:
            A tuple consisting of a list of input features per case and a list of output results, where both lists have
            the same length and input item i corresponds to the ith output item.
        """
        parsed_videos = self.__get_parsed_videos(season)
        player_episodes = self.__get_players_with_episodes(season, parsed_videos)

        input = []
        output = []
        for player, episodes in player_episodes.items():
            is_mol = 1 if player.value.is_mol else 0
            for selected_episodes in itertools.combinations(episodes, predict_episode):
                input.append(self.__get_input_data(player, season, selected_episodes, parsed_videos))
                output.append(is_mol)

        return (input, output)

    @classmethod
    def get_predict_data(self, season: int, predict_episode: int) -> Dict[Player, np.array]:
        parsed_videos = self.__get_parsed_videos(season)
        predict_data = dict()
        for player in parsed_videos[predict_episode].alive_players:
            predict_data[player] = self.__get_input_data(player, season, tuple(range(1, predict_episode + 1)),
                                                         parsed_videos)
        return predict_data

    @classmethod
    def __get_parsed_videos(self, season: int) -> Dict[int, ParsedVideo]:
        """ Load the parsed videos for the given season.

        Parameters:
            season (int): The season for which we load the parsed videos.

        Returns:
            The parsed video data for this season.
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
        """ Get the list of players that participated in this season with the corresponding episodes in which these
        players participated.

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
                         parsed_videos: Dict[int, ParsedVideo]) -> np.array:
        """ Get the input/feature encoding for a player with a combination of selected episodes.

        Parameters:
            player (Player): The player for which we get the input/feature encoding.
            season (int): The season in which this player participated.
            selected_episodes (Tuple[int]): The selected episodes from which the features get extracted.
            parsed_videos (Dict[int, ParsedVideo]): The parsed video data of the episodes in this season.

        Returns:
            The input/feature encoding for this player in combination with the selected episodes.
        """
        relative_occurrence = 0
        for episode in selected_episodes:
            relative_occurrence += self.__get_relative_occurrence(player, parsed_videos[episode])

        relative_occurrence /= len(selected_episodes)
        return np.array([relative_occurrence, season])

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