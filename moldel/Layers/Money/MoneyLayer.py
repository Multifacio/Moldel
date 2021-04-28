from Data.MoneyData.Earnings.All import MONEY_DATA
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.Money.MoneyExtractor import MoneyExtractor
from Layers.MultiLayer.EmptyMultiLayer import EmptyMultiLayer
from Layers.MultiLayer.MultiLayer import MultiLayer, MultiLayerResult
from Layers.MultiLayer.MultiplyAggregateLayer import MultiplyAggregateLayer
from Layers.Special.PotentialMolLayer import PotentialMolLayer
from numpy.random import RandomState
from sklearn.linear_model import LogisticRegression
from typing import Dict, List, Set
import numpy as np

class InnerMoneyLayer(MultiLayer):
    def __init__(self, pca_explain: float, spline_clusters: int, num_other_money_quantiles: int,
                 random_generator: RandomState):
        self.__pca_explain = pca_explain
        self.__spline_clusters = spline_clusters
        self.__num_other_money_quantiles = num_other_money_quantiles
        self.__random_generator = random_generator

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        available_seasons = MONEY_DATA.keys()
        train_seasons = train_seasons.intersection(available_seasons)
        if predict_season not in available_seasons:
            return EmptyMultiLayer().predict(predict_season, latest_episode, train_seasons)

        extractor = MoneyExtractor(predict_season, latest_episode, train_seasons, self.__pca_explain,
                                   self.__spline_clusters, self.__num_other_money_quantiles, self.__random_generator)
        classifier = self.__training(extractor)
        predict_data = extractor.get_predict_data()
        if not predict_data:
            return EmptyMultiLayer().predict(predict_season, latest_episode, train_seasons)

        return self.__predict(predict_season, latest_episode, predict_data, classifier)

    def __training(self, extractor: MoneyExtractor) -> LogisticRegression:
        """ Execute the training phase of the Money Layer.

        Arguments:
            extractor (MoneyExtractor): The extractor which delivers the training data.

        Returns:
            The trained machine learning model used to make predictions.
        """
        train_input, train_output = extractor.get_train_data()
        classifier = LogisticRegression(solver = "lbfgs")
        classifier.fit(train_input, train_output)
        return classifier

    def __predict(self, predict_season: int, latest_episode: int, predict_data: Dict[Player, List[np.array]],
                  classifier: LogisticRegression) -> Dict[Player, MultiLayerResult]:
        """ Execute the prediction phase of the Money Layer.

        Arguments:
            predict_season (int): The season for which the predictions are made.
            latest_episode (int): The latest episode useable in the predict season.
            predict_data (List[PredictSample]): The prediction data with features used to make predictions.
            classifier (LogisticRegression): The machine learning model used to make predictions.

        Returns:
            A dictionary with as key the players that participated in the prediction season and as value a
            MultiLayerResult which contains the predictions.
        """
        all_predictions = dict()
        season_players = get_players_in_season(predict_season)
        for player in season_players:
            all_predictions[player] = []

        alive_players = MONEY_DATA[predict_season].get_alive(latest_episode)
        for player, all_rows in predict_data.items():
            for row in all_rows:
                likelihood = classifier.predict_proba(np.array([row]))[0][1]
                all_predictions[player] = all_predictions[player] + [likelihood]

        return {player: MultiLayerResult(np.array(predictions), player not in alive_players) for player, predictions in \
                all_predictions.items()}

class MoneyLayer(PotentialMolLayer):
    """ The Money Layer predicts whether you are the Mol based on what you have earned during exercises. """

    def __init__(self, pca_explain: float, spline_clusters: int, num_other_money_quantiles: int,
                 random_generator: RandomState):
        """ Constructor of the Money Layer.

        Arguments:
            pca_explain (float): PCA will select the least number of components that at least explain this amount
                of variance in the features.
            spline_clusters (int): The number of KMeans clusters used in the Semi Rank Transformation and in the
                Spline Encoding to estimate how likely a player is the Mol based on how many money that player earned.
            num_other_likelihood_quantiles (int): The number of quantiles used to extract features from the likelihoods
                based on what others earn.
            random_generator (RandomState): The random generator used to generate random values.
        """
        super().__init__(MultiplyAggregateLayer(InnerMoneyLayer(pca_explain, spline_clusters, num_other_money_quantiles,
                                                                random_generator), False))