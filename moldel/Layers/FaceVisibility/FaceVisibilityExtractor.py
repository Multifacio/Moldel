from Data.Player import Player
from Data.PlayerData import get_is_mol, get_players_in_season
from Layers.FaceVisibility.VideoParser import ParsedVideo, VideoParser
from numpy.random.mtrand import RandomState
from typing import Dict, List, Tuple, Set, NamedTuple
import bisect
import itertools
import math
import numpy as np

TrainSample = NamedTuple("TrainSample", [("season", int), ("relative_occurrence", float), ("is_mol", bool)])
class FaceVisibilityExtractor:
    """ The Face Visibility Extractor deals with obtaining the train data and predict data. For this feature encoding
    and extraction techniques are used. Likewise train data gets resampled such that closer seasons have more influence
    in the training process than seasons further aways. """

    # The size of the resampled train data list. Higher sample sizes will decrease the variance in the results (with
    # resampling the results you obtain when re-running the layer might be different), but will increase the running
    # time of the Face Visibility layer.
    SAMPLE_SIZE = 100000

    # A small log addition constant used to prevent situations where the log is taken of zero.
    SMALL_LOG_ADDITION = 0.0001

    def __init__(self, predict_season: int, predict_episode: int, train_seasons: Set[int], dec_season_weight: float,
                 aug_num_cuts: int, aug_min_cuts_on: int, outlier_cutoff: float):
        """ Constructor of the Face Visibility Extractor.

        Arguments:
            predict_season (int): The season for which we make the prediction.
            predict_episode (int): The latest episode in the predict season that could be used.
            train_seasons (Set[int]): The seasons which are used as train data.
            dec_season_weight (float): The exponential decrease in weight when the absolute difference between the train
                season and predict season becomes larger. This value is used to give closer seasons a higher weight and
                0.0 < dec_season_weight <= 1.0 should hold. If dec_season_weight is larger then seasons further away
                will have more influence on the prediction.
            aug_num_cuts (int): In how many cuts the episodes get divided. All cuts are turned on/off, where the
                appearance value is computed over only the cuts that are turned on. This is done to create more data.
            aug_min_cuts_on (int): How many cuts should be turned on at least.
            outlier_cutoff (float): This is the relative amount of highest and lowest appearance values that get removed.
        """
        self.__predict_season = predict_season
        self.__predict_episode = predict_episode
        self.__train_seasons = train_seasons
        self.__dec_season_weight = dec_season_weight
        self.__aug_num_cuts = aug_num_cuts
        self.__aug_min_cuts_on = aug_min_cuts_on
        self.__outlier_cutoff = outlier_cutoff

    def get_train_data(self) -> Tuple[np.array, np.array, np.array]:
        """ Get the formatted and sampled train data with train weights useable for machine learning algorithms.

        Returns:
            The train input, train output and train weights in this order. The train input is a 2d array where each row
            represents a different train element. The train output is 1d array of labels, such that the ith row of the
            train input corresponds to the ith element of the train output.
        """
        train_data = []
        for season in self.__train_seasons:
            parsed_videos = self.__get_parsed_videos(season)
            player_episodes = self.__get_players_with_episodes(season, parsed_videos)
            for player, episodes in player_episodes.items():
                for episode in episodes:
                    # Do the Data Augmentation by turning cuts on/off.
                    for selection in itertools.product([False, True], repeat = self.__aug_num_cuts):
                        if sum(selection) >= self.__aug_min_cuts_on:
                            relative_occurrence = self.get_relative_occurrence(player, parsed_videos[episode], selection)
                            train_data.append(TrainSample(season, relative_occurrence, get_is_mol(player)))

        train_data = self.__filter_outliers(train_data)
        train_input = np.array([[ts.relative_occurrence] for ts in train_data])
        train_output = np.array([1.0 if ts.is_mol else 0.0 for ts in train_data])
        train_weights = np.array([self.__dec_season_weight ** abs(ts.season - self.__predict_season) for ts in train_data])
        return train_input, train_output, train_weights

    def get_predict_data(self) -> Dict[Player, List[np.array]]:
        """ Get all formatted predict data useable for the machine learning algorithms to do a prediction.

        Returns:
            A dictionary with as key the players that are still present in the predict episode and as value a list of
            the predict input for every episode up to (and including) the predict episode.
        """
        parsed_videos = self.__get_parsed_videos(self.__predict_season)
        predict_data = dict()
        alive_players = parsed_videos[self.__predict_episode].alive_players
        for player in alive_players:
            for episode in range(1, self.__predict_episode + 1):
                relative_occurrence = self.get_relative_occurrence(player, parsed_videos[episode], (True,))
                predict_data[player] = predict_data.get(player, []) + [np.array([relative_occurrence])]
        return predict_data

    def __filter_outliers(self, train_data: List[TrainSample]) -> List[TrainSample]:
        """ Remove the outliers from a list of train data.

        Arguments:
            train_data (List[TrainSample]): The train data from which the outliers are removed.

        Returns:
            The train data without outliers.
        """
        appearances = [td.relative_occurrence for td in train_data]
        quantiles = np.quantile(appearances, [self.__outlier_cutoff / 2, 1 - self.__outlier_cutoff / 2])
        return [td for td in train_data if quantiles[0] <= td.relative_occurrence <= quantiles[1]]

    @staticmethod
    def get_relative_occurrence(player: Player, parsed_video: ParsedVideo, selection: Tuple[bool, ...]) -> float:
        """ Get the relative occurrence of a player in a given episode for the enabled cuts compared to the total
        occurrence of all players. This relative occurrence is already log transformed and we also normalized this value
        by the number of players that participated in that episode.

        Parameters:
            player (Player): The player of which we determine the relative occurrence.
            parsed_video (ParsedVideo): The parsed video data about the episode.
            selection (Tuple[bool, ...]): The length of this list is the number of cuts and the boolean values indicate
                which cuts are turned on (True) and which are turned off (False).

        Returns:
            The relative occurrence of the player in the given episode for the enabled cuts.
        """
        all_occurrences = list(itertools.chain(*parsed_video.player_occurrences.values()))
        quantiles = [q for q in np.linspace(0.0, 1.0, len(selection) + 1)]
        quantiles = np.quantile(all_occurrences, quantiles)

        frame_count = dict()
        for select, q1, q2 in zip(selection, quantiles, quantiles[1:]):
            if select:
                for p in parsed_video.alive_players:
                    occurrences = parsed_video.player_occurrences[p]
                    frame_count[p] = bisect.bisect_right(occurrences, q2) - bisect.bisect_left(occurrences, q1) + \
                        frame_count.get(p, 0)

        total_occurrence = sum(frame_count.values())
        own_occurrence = frame_count.get(player, 0) * len(parsed_video.alive_players)
        return math.log(FaceVisibilityExtractor.SMALL_LOG_ADDITION + own_occurrence / total_occurrence)

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
                player_occurrences = {player: sorted(occurrences) for player, occurrences in parsed_video.player_occurrences.items()}
                parsed_videos[episode] = ParsedVideo(player_occurrences, parsed_video.alive_players, parsed_video.frame_skip)
        return parsed_videos

    @classmethod
    def __get_players_with_episodes(self, season: int, parsed_videos: Dict[int, ParsedVideo]) -> Dict[Player, Set[int]]:
        """ Get a dictionary of players that participated in this season with the corresponding episodes in which these
        players participated.

        Parameters:
            season (int): The season for which we compute this.
            parsed_videos (Dict[int, ParsedVideo]): All the parsed videos from the episodes of that season.

        Returns:
            A dictionary with as key the players of that season and as value a set of episodes in which they
            participated.
        """
        player_episodes = dict()
        for player in get_players_in_season(season):
            episode_occurrences = {episode for episode, data in parsed_videos.items() if player in data.alive_players}
            player_episodes[player] = episode_occurrences
        return player_episodes