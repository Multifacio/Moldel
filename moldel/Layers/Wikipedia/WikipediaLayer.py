from Data.Player import Player
from Data.PlayerData import get_season
from Data.Wikipedia.Linker import LINKER
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from Layers.Special.PotentialMolLayer import PotentialMolLayer
from Layers.Wikipedia.WikipediaExtractor import WikipediaExtractor
from Tools.Classifiers.Classifier import Classifier
from Tools.Classifiers.NaiveKDEClassifier import NaiveKDEClassifier
from numpy.random import RandomState
from typing import Dict, Set

class InnerWikipediaLayer(Layer):
    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        available_seasons = self.seasons_with_data()
        if predict_season not in available_seasons:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)
        train_seasons = train_seasons.intersection(available_seasons)

        extractor = WikipediaExtractor(predict_season, train_seasons)
        classifier = self.__train(extractor)
        return self.__predict(classifier, extractor)

    def __train(self, extractor: WikipediaExtractor) -> Classifier:
        train_input, train_output, feature_weights = extractor.get_train_data()
        classifier = NaiveKDEClassifier(weights = feature_weights)
        classifier.train(train_input, train_output)
        return classifier

    def __predict(self, classifier: Classifier, extractor: WikipediaExtractor) -> Dict[Player, float]:
        """ Execute the prediction phase of the Wikipedia Layer.

        Arguments:
            classifier (Classifier): The classifier used to check if Wikipedia pages belong to the Mol or not.
            extractor (WikipediaExtractor): The extractor which delivers the prediction data.

        Returns:
            A dictionary with as key the players that participated in the prediction season and as value the likelihood
            of being the Mol.
        """
        predict_input = extractor.get_predict_data()
        return {p: classifier.predict_proba(pi) for p, pi in predict_input.items()}

    @staticmethod
    def seasons_with_data() -> Set[int]:
        """ Get all seasons that have Wikipedia data. """
        return {get_season(player) for player in LINKER}

class WikipediaLayer(PotentialMolLayer):
    """ The Wikipedia Layer predicts which player is the Mol based on their Wikipedia pages. It tries to find the
    correlation between the number of words on your Wikipedia page and the likelihood of being the Mol. Furthermore it
    tries to find a correlation to which job a player belongs and the likelihood of being the Mol. """

    def __init__(self):
        super().__init__(NormalizeLayer(InnerWikipediaLayer()))