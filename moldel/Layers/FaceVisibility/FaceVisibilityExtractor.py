from Data.Player import Player
from Layers.FaceVisibility.VideoParser import ParsedVideo, VideoParser
from scipy import stats
from typing import Dict, List, Tuple, Set, NamedTuple
import itertools
import math
import numpy as np

TrainSample = NamedTuple("TrainSample", [("season", int), ("relative_occurrence", float), ("is_mol", bool)])
class FaceVisibilityExtractor:
    SAMPLE_SIZE = 10000
    SMALL_LOG_ADDITION = 0.0001

    def __init__(self, predict_season: int, predict_episode: int, train_seasons: Set[int], z_cutoff: float,
                 dec_season_weight: float):
        self.__predict_season = predict_season
        self.__predict_episode = predict_episode
        self.__train_seasons = train_seasons
        self.__z_cutoff = z_cutoff
        self.__dec_season_weight = dec_season_weight

    def get_train_data(self) -> Tuple[np.array, np.array]:
        train_data = self.__get_raw_train_data()
        train_data = self.__cutoff_outliers(train_data)
        train_data = self.__resample(train_data)
        return np.array([[ts.relative_occurrence] for ts in train_data]), \
               np.array([1.0 if ts.is_mol else 0.0 for ts in train_data])

    def get_predict_data(self) -> Dict[Player, np.array]:
        parsed_videos = self.__get_parsed_videos(self.__predict_season)
        predict_data = dict()
        for player in parsed_videos[self.__predict_episode].alive_players:
            relative_occurrence = self.__get_input_data(player, tuple(range(1, self.__predict_episode + 1)), parsed_videos)
            relative_occurrence = min(max(relative_occurrence, self.lowerbound), self.upperbound)
            predict_data[player] = np.array([relative_occurrence])
        return predict_data

    def __get_raw_train_data(self) -> List[TrainSample]:
        """ Get all train data from a given season.

        Parameters:
            train_seasons (int): The season from which the train data will be obtained.
            predict_episode (int): The latest episode used in the predict season.

        Returns:
            A tuple consisting of a list of input features per case and a list of output results, where both lists have
            the same length and input item i corresponds to the ith output item.
        """
        train_data = []
        for season in self.__train_seasons:
            parsed_videos = self.__get_parsed_videos(season)
            player_episodes = self.__get_players_with_episodes(season, parsed_videos)
            for player, episodes in player_episodes.items():
                for selected_episodes in itertools.combinations(episodes, self.__predict_episode):
                    relative_occurrence = self.__get_input_data(player, selected_episodes, parsed_videos)
                    train_data.append(TrainSample(season, relative_occurrence, player.value.is_mol))
        return train_data

    def __cutoff_outliers(self, train_data: List[TrainSample]) -> List[TrainSample]:
        relative_occurrences = [ts.relative_occurrence for ts in train_data]
        z_scores = stats.zscore(relative_occurrences)
        self.lowerbound = min([occ for occ, z_score in zip(relative_occurrences, z_scores) if z_score >= -self.__z_cutoff])
        self.upperbound = max([occ for occ, z_score in zip(relative_occurrences, z_scores) if z_score <= self.__z_cutoff])
        return [TrainSample(ts.season, min(max(ts.relative_occurrence, self.lowerbound), self.upperbound), ts.is_mol)
                for ts in train_data]

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
            A dictionary with as key the players and as value a set of video parsed episodes in which that player occurs.
        """
        player_episodes = dict()
        season_players = [player for player in Player if player.value.season == season]
        for player in season_players:
            episode_occurrences = {episode for episode, data in parsed_videos.items() if player in data.alive_players}
            player_episodes[player] = episode_occurrences
        return player_episodes

    @classmethod
    def __get_input_data(self, player: Player, selected_episodes: Tuple[int], parsed_videos: Dict[int, ParsedVideo]) \
            -> float:
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
        return relative_occurrence

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