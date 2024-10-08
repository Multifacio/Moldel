from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.Appearance.AppearanceExtractor import AppearanceExtractor
from Layers.Appearance.VideoParser import VideoParser
from Layers.MultiLayer.EmptyMultiLayer import EmptyMultiLayer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.MultiLayer.MultiplyAggregateLayer import MultiplyAggregateLayer
from Layers.Special.CutLayer import CutLayer
from Layers.Special.PotentialMolLayer import PotentialMolLayer
from Tools.Classifiers.Classifier import Classifier
from Tools.Classifiers.NaiveKDEClassifier import NaiveKDEClassifier
from scipy.stats import gaussian_kde
from statistics import mean
from typing import Dict, Set
import numpy as np

class InnerAppearanceLayer(MultiLayer):
    def __init__(self, first_season: int, aug_num_cuts: int, aug_min_cuts_on: int, cdf_cutoff: float):
        self.__first_season = first_season
        self.__aug_num_cuts = aug_num_cuts
        self.__aug_min_cuts_on = aug_min_cuts_on
        self.__cdf_cutoff = cdf_cutoff

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, np.array]:
        train_seasons = {season for season in train_seasons if season >= self.__first_season}
        max_episode = self.__latest_available_episode(predict_season, latest_episode)
        if max_episode == 0 or predict_season < self.__first_season:
            return EmptyMultiLayer().predict(predict_season, latest_episode, train_seasons)

        extractor = AppearanceExtractor(predict_season, max_episode, train_seasons, self.__aug_num_cuts,
                                        self.__aug_min_cuts_on)
        classifier = self.__training(extractor)
        return self.__prediction(extractor, classifier, predict_season)

    def __latest_available_episode(self, predict_season: int, latest_episode: int) -> int:
        """ Determine the latest episode that is available and can be used in the prediction season.

        Arguments:
            predict_season (int): The season for which the prediction is made.
            latest_episode (int): The latest episode of the prediction season which may be used as data.

        Returns:
            The latest available and usable episode of the prediction season.
        """
        max_episode = 0
        for i in range(1, latest_episode + 1):
            if VideoParser.has_parsed_video(predict_season, i):
                max_episode = i
            else:
                return max_episode
        return max_episode

    def __training(self, extractor: AppearanceExtractor) -> Classifier:
        """ Execute the training phase of the Appearance Layer.

        Arguments:
            extractor (AppearanceExtractor): The extractor which delivers the training data.

        Returns:
            A classifier which classifies players as either Mol or non-Mol based on how often they appear.
        """
        train_input, train_output = extractor.get_train_data()
        classifier = NaiveKDEClassifier(cdf_cutoff = self.__cdf_cutoff)
        classifier.train(train_input, train_output)
        return classifier

    def __prediction(self, extractor: AppearanceExtractor, classifier: Classifier, predict_season: int) -> \
            Dict[Player, MultiLayerResult]:
        """ Execute the prediction phase of the Appearance Layer.

        Arguments:
            extractor (AppearanceExtractor): The extractor which delivers the prediction data.
            classifier (Classifier): A classifier which classifies players as either Mol or non-Mol based on how often
                they appear.
            predict_season (int): For which season we make the prediction.

        Returns:
            A dictionary with as key the players that participated in the prediction season and as value a
            MultiLayerResult which contains the predictions.
        """
        all_predictions = dict()
        predict_data = extractor.get_predict_data()
        if not predict_data:
            return EmptyMultiLayer().predict(predict_season, 0, set())

        for player in get_players_in_season(predict_season):
            if player in predict_data:
                predictions = []
                for data in predict_data[player]:
                    predictions.append(classifier.predict_proba([data]))
                all_predictions[player] = MultiLayerResult(np.array(predictions), False)
            else:
                all_predictions[player] = MultiLayerResult(np.array([]), True)

        return all_predictions

class AppearanceLayer(PotentialMolLayer):
    """ The Appearance Layer predict which player is the Mol based on how often this player appears during the episode.
    This code is based on the project of mattijn: https://github.com/mattijn/widm """

    def __init__(self, predict_lowerbound: float, first_season: int, aug_num_cuts: int, aug_min_cuts_on: int,
                 cdf_cutoff: float):
        """ Constructor of the Appearance Layer.

        Arguments:
            predict_lowerbound (float): The relative lowerbound with respect to the highest likelihood. All predictions
                with a lower likelihood than this lowerbound will be set equal to the lowerbound (after that the
                likelihoods will be normalized).
            first_season (int): The first season for which the Appearance Layer can do predictions. So on earlier
                seasons it will give an uniform prediction back. Note however that earlier seasons are still used as
                training data.
            aug_num_cuts (int): In how many cuts the episodes get divided. All cuts are turned on/off, where the
                appearance value is computed over only the cuts that are turned on. This is done to create more data.
            aug_min_cuts_on (int): How many cuts should be turned on at least.
            cdf_cutoff (float): This is the total cumulative density which is cutoff from both sides of the
                distributions (mol and non-mol distribution). All appearance values that lie in the cutoff zone of both
                distributions are changed to the closest value that lies in the range of at least one of the
                distributions.
        """
        super().__init__(CutLayer(MultiplyAggregateLayer(InnerAppearanceLayer(first_season, aug_num_cuts,
                            aug_min_cuts_on, cdf_cutoff)), mean, 1.0, predict_lowerbound))