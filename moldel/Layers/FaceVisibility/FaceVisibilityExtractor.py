from Data.Player import Player
from Layers.FaceVisibility.VideoParser import ParsedVideo, VideoParser
from scipy import stats
from typing import Dict, List, Tuple, Set, NamedTuple
import itertools
import math
import matplotlib.pyplot as plt
import numpy as np

TrainSample = NamedTuple("TrainSample", [("season", int), ("relative_occurrence", float), ("is_mol", bool)])
class FaceVisibilityExtractor:
    SAMPLE_SIZE = 100000
    SMALL_LOG_ADDITION = 0.0001

    def __init__(self, predict_season: int, predict_episode: int, train_seasons: Set[int], dec_season_weight: float):
        self.__predict_season = predict_season
        self.__predict_episode = predict_episode
        self.__train_seasons = train_seasons
        self.__dec_season_weight = dec_season_weight

    def get_train_data(self) -> Tuple[np.array, np.array]:
        train_data = []
        for season in self.__train_seasons:
            parsed_videos = self.__get_parsed_videos(season)
            player_episodes = self.__get_players_with_episodes(season, parsed_videos)
            for player, episodes in player_episodes.items():
                for episode in episodes:
                    relative_occurrence = self.__get_relative_occurrence(player, parsed_videos[episode])
                    train_data.append(TrainSample(season, relative_occurrence, player.value.is_mol))
        train_input = [ts.relative_occurrence for ts in train_data if ts.season >= 13]
        train_output = [1.0 if ts.is_mol else 0.0 for ts in train_data if ts.season >= 13]
        print(len(train_input))
        plt.scatter(train_input, train_output, s = 5)
        plt.xlabel('Relative Occurrence')
        plt.ylabel('Is Mol')
        plt.show()
        train_data = self.__resample(train_data)
        train_input = np.array([[ts.relative_occurrence] for ts in train_data])
        train_output = np.array([1.0 if ts.is_mol else 0.0 for ts in train_data])
        return train_input, train_output

    def get_predict_data(self) -> Dict[Player, List[np.array]]:
        parsed_videos = self.__get_parsed_videos(self.__predict_season)
        predict_data = dict()
        for player in parsed_videos[self.__predict_episode].alive_players:
            for episode in range(1, self.__predict_episode + 1):
                relative_occurrence = self.__get_relative_occurrence(player, parsed_videos[episode])
                predict_data[player] = predict_data.get(player, []) + [np.array([relative_occurrence])]
        return predict_data

    def __resample(self, train_data: List[TrainSample]) -> List[TrainSample]:
        probabilities = np.array([self.__dec_season_weight ** abs(ts.season - self.__predict_season) for ts in train_data])
        probabilities /= sum(probabilities)
        selection = np.random.choice(len(train_data), self.SAMPLE_SIZE, True, probabilities)
        return [train_data[i] for i in selection]

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
            A dictionary with as key the episodes and as value a set of video parsed episodes in which that player occurs.
        """
        player_episodes = dict()
        season_players = [player for player in Player if player.value.season == season]
        for player in season_players:
            episode_occurrences = {episode for episode, data in parsed_videos.items() if player in data.alive_players}
            player_episodes[player] = episode_occurrences
        return player_episodes

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