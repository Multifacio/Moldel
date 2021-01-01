from Data.Player import Player
from Data.PlayerData import get_season
from Data.Wikipedia.Linker import LINKER
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from Layers.Wikipedia.WikipediaExtractor import WikipediaExtractor
from numpy.random import RandomState
from typing import Dict, Set

class InnerWikipediaLayer(Layer):
    def __init__(self, unlikely_z_score: float, lower_likelihood: float, pca_components: int, random_generator: RandomState):
        self.__unlikely_z_score = unlikely_z_score
        self.__lower_likelihood = lower_likelihood
        self.__pca_components = pca_components
        self.__random_generator = random_generator

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        available_seasons = self.seasons_with_data()
        if predict_season not in available_seasons:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)
        train_seasons = train_seasons.intersection(available_seasons)

        extractor = WikipediaExtractor(predict_season, train_seasons, self.__pca_components, self.__unlikely_z_score,
                                       self.__random_generator)
        extractor.train()
        return self.__predict(extractor)

    def __predict(self, extractor: WikipediaExtractor) -> Dict[Player, float]:
        """ Execute the prediction phase of the Wikipedia Layer.

        Arguments:
            extractor (WikipediaExtractor): The extractor which delivers the prediction data.

        Returns:
            A dictionary with as key the players that participated in the prediction season and as value the likelihood
            of being the Mol.
        """
        predict_input = extractor.get_predict_data()
        predict_output = {p: self.__lower_likelihood if pi else 1.0 for p, pi in predict_input.items()}
        return predict_output

    @staticmethod
    def seasons_with_data() -> Set[int]:
        """ Get all seasons that have Wikipedia data. """
        return {get_season(player) for player in LINKER}

class WikipediaLayer(NormalizeLayer):
    """ The Wikipedia Layer predicts which player is the Mol based on their Wikipedia pages. It tries to find the
    correlation between the number of words on your Wikipedia page and the likelihood of being the Mol. Furthermore it
    tries to find a correlation to which job a player belongs and the likelihood of being the Mol. """

    def __init__(self, unlikely_z_score: float, lower_likelihood: float, pca_components: int, random_generator: RandomState):
        """ Constructor of the Wikipedia Layer.

        Arguments:
            unlikely_z_score (float): All players with a lower z-score than this value get a lower likelihood assigned.
            lower_likelihood (float): The lower likelihood assigned to these players.
            pca_components (int): The number of PCA components extracted from the job features before LDA is applied.
            random_generator (RandomState): The random generator used to generate random values.
        """
        super().__init__(InnerWikipediaLayer(unlikely_z_score, lower_likelihood, pca_components, random_generator))