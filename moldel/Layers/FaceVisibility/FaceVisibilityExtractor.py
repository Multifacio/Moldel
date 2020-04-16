from Data.Player import Player
from Layers.FaceVisibility.VideoParser import ParsedVideo, VideoParser
from scipy import stats
from sklearn.feature_selection import f_classif
from sklearn.linear_model import LinearRegression
from typing import Dict, List, NamedTuple, Tuple, Set, Union
import itertools
import math
import numpy as np

Encoding = NamedTuple("Encoding", [("season", int), ("occurrences", List[float]), ("is_mol", Union[bool, None])])
class FaceVisibilityExtractor:
    SMALL_LOG_ADDITION = 0.0001 # Small value that is added to prevent that the logarithm of 0.0 is taken.

    def __init__(self, predict_season: int, train_seasons: Set[int], upto_episode: int, z_score_cut: float):
        """ Constructor of the Face Visibility Extractor.

        Parameters:
            predict_season (int): The season for which we want to make predictions.
            train_seasons (Set[int]): A set of season numbers (int) which are used for training.
            upto_episode (int): The last episode up to (and including) which we use the FaceVisibility data in the
            prediction season.
        """
        self.predict_season = predict_season
        self.train_seasons = train_seasons
        self.upto_episode = upto_episode
        self.z_score_cut = z_score_cut

    def get_train_data(self) -> Tuple[np.array, np.array]:
        """ Get all the fully processed train data.

        Returns:
            A tuple where the first output is a 2 dimensional matrix of all fully processed train input and the second
            output is an array of all fully processed train output.
        """
        all_train_data = []
        for season in self.train_seasons:
            all_train_data.extend(self.__get_season_train_data(season))

        # Detrend the data by removing the regression between the season and the occurrences
        self.time_regressions = []
        train_input = []
        for i in range(len(all_train_data[0].occurrences)):
            X = np.array([np.array([d.season]) for d in all_train_data if d.is_mol])
            y = np.array([d.occurrences[i] for d in all_train_data if d.is_mol])
            regression = LinearRegression()
            regression.fit(X, y)
            occurrences = np.array([d.occurrences[i] for d in all_train_data])
            predictions = regression.predict(np.array([[d.season] for d in all_train_data]))
            train_input.append(occurrences - predictions)
            self.time_regressions.append(regression)

        train_input = np.array(train_input).T
        train_output = np.array([1 if data_point.is_mol else 0 for data_point in all_train_data])
        for input, label in zip(train_input, train_output):
            if label == 1.0:
                print("Mol")
                print(input)
            else:
                pass
                # print("Not Mol")
                # print(input)

        # Maximize and minimize all outliers for the prediction data by using z-scores
        occurrences = train_input.flatten()
        z_scores = stats.zscore(occurrences)
        self.outlier_minimum = min([occ for occ, z in zip(occurrences, z_scores) if z >= -self.z_score_cut])
        self.outlier_maximum = max([occ for occ, z in zip(occurrences, z_scores) if z <= self.z_score_cut])

        # Take a weighted sum over all occurrences based on the ANOVA scores
        self.weights = np.ones(len(train_input[0])) - f_classif(train_input, train_output)[1]
        self.weights /= sum(self.weights)
        train_input = np.expand_dims(np.matmul(train_input, self.weights), axis = 1)
        print(train_input)

        return train_input, train_output

    def get_predict_data(self) -> Dict[Player, np.array]:
        predict_data = self.__get_season_predict_data()
        predictions = np.array([tr.predict(np.array([[self.predict_season]]))[0] for tr in self.time_regressions])
        for player, encoding in predict_data.items():
            features = np.array(encoding.occurrences) - predictions
            features = np.maximum(features, np.full(features.shape, self.outlier_minimum))
            features = np.minimum(features, np.full(features.shape, self.outlier_maximum))
            predict_data[player] = np.expand_dims(np.inner(features, self.weights), axis = 0)
        return predict_data

    def __get_season_train_data(self, season: int) -> List[Encoding]:
        """ Get all non-fully processed train data from a given season.

        Parameters:
            season (int): The season from which the train data will be obtained.

        Returns:
            A list of all train data non-fully processed encodings
        """
        parsed_videos = self.__get_parsed_videos(season)
        player_episodes = self.__get_players_with_episodes(season, parsed_videos)
        train_data = []
        for player, episodes in player_episodes.items():
            for selected_episodes in itertools.combinations(episodes, self.upto_episode):
                encoding = self.__get_input_data(player, season, selected_episodes, parsed_videos, player.value.is_mol)
                train_data.append(encoding)
        return train_data

    def __get_season_predict_data(self) -> Dict[Player, Encoding]:
        """ Get all non-fully processed data from the predict season, i.e. the season in which we make a prediction.

        Parameters:
            season (int): The season for which we want to make predictions.

        A dictionary with the non-fully processed feature encoding for every player in that given season
        """
        parsed_videos = self.__get_parsed_videos(self.predict_season)
        predict_data = dict()
        for player in parsed_videos[self.upto_episode].alive_players:
            predict_data[player] = self.__get_input_data(player, self.predict_season,
                                                         tuple(range(1, self.upto_episode + 1)), parsed_videos, None)
        return predict_data

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