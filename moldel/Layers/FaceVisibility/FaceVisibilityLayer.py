from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.FaceVisibility.FaceVisibilityExtractor import FaceVisibilityExtractor
from Layers.FaceVisibility.VideoParser import VideoParser
from Layers.Layer import Layer
from Layers.Special.CutLayer import CutLayer
from Layers.Special.EqualLayer import EqualLayer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import KBinsDiscretizer
from typing import Dict, Set, Tuple
import numpy as np

class InnerFaceVisibilityLayer(Layer):
    def __init__(self, dec_season_weight: float, first_season: int, num_bins: int):
        self.__dec_season_weight = dec_season_weight
        self.__first_season = first_season
        self.__num_bins = num_bins

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        max_episode = self.__latest_available_episode(predict_season, latest_episode)
        if max_episode == 0 or predict_season < self.__first_season:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        extractor = FaceVisibilityExtractor(predict_season, max_episode, train_seasons, self.__dec_season_weight, True)
        classifier, discretizer = self.__training(extractor)
        return self.__prediction(extractor, classifier, discretizer, predict_season)

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
    
    def __training(self, extractor: FaceVisibilityExtractor) -> Tuple[LogisticRegression, KBinsDiscretizer]:
        """ Execute the training phase of the Face Visibility Layer.

        Arguments:
            extractor (FaceVisibilityExtractor): The extractor which delivers the training data.

        Returns:
            The classifier model and the discretizer model (discretize data into bins).
        """
        train_input, train_output = extractor.get_train_data()
        discretizer = KBinsDiscretizer(self.__num_bins, encode="onehot-dense", strategy="quantile")
        train_input = discretizer.fit_transform(train_input)
        classifier = LogisticRegression(solver="lbfgs")
        classifier.fit(train_input, train_output)
        return classifier, discretizer

    def __prediction(self, extractor: FaceVisibilityExtractor, classifier: LogisticRegression,
                     discretizer: KBinsDiscretizer, predict_season: int):
        """ Execute the prediction phase of the Face Visibility Layer.

        Arguments:
            extractor (FaceVisibilityExtractor): The extractor which delivers the prediction data.
            classifier (LogisticRegression): The trained machine learning model used to classify instances.
            discretizer (KBinsDiscretizer): The trained discretizer used to discetize the data into bins.
            predict_season (int): For which season we make the prediction.

        Returns:
            A dictionary with as key the players that participated in the prediction season and as value a float which
            represents how likely that player is the Mol according to the Face Visibility Layer.
        """
        distribution = dict()
        predict_data = extractor.get_predict_data()
        for player in get_players_in_season(predict_season):
            if player in predict_data:
                likelihood = 1.0
                for data in predict_data[player]:
                    data = discretizer.transform(np.array([data]))
                    likelihood *= classifier.predict_proba(data)[0][1]
                distribution[player] = likelihood
            else:
                distribution[player] = 0.0

        return distribution

class FaceVisibilityLayer(CutLayer):
    """ The Face Visibility Layer predict which candidate is the Mol based on how often this candidate appears during
    the episode. This code is based on the project of mattijn: https://github.com/mattijn/widm """

    def __init__(self, predict_lowerbound: float, dec_season_weight: float, first_season: int, num_bins: int):
        """ Constructor of the Face Visibility Layer.

        Arguments:
            predict_lowerbound (float): The relative lowerbound with respect to the uniform likelihood. All predictions
                with a lower likelihood than this lowerbound will be set equal to the lowerbound (after that the
                likelihoods will be normalized).
            dec_season_weight (float): The exponential decrease in weight when the absolute difference between the train
                season and predict season becomes larger. This value is used to give closer seasons a higher weight and
                0.0 < dec_season_weight <= 1.0 should hold. If dec_season_weight is larger then seasons further away
                will have more influence on the prediction.
            first_season (int): The first season for which the Face Visibility Layer can do predictions. So on earlier
                seasons it will give an uniform prediction back. Note however that earlier seasons are still used as
                training data.
            num_bins (int): Into how much bins the relative occurrence data get discretized.
        """
        super().__init__(InnerFaceVisibilityLayer(dec_season_weight, first_season, num_bins), 1.0, predict_lowerbound)