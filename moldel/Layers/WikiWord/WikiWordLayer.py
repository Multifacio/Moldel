from Data.Player import Player
from Data.PlayerData import get_season
from Data.WikiWord.Linker import LINKER
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.CutLayer import CutLayer
from Layers.WikiWord.WikiWordExtractor import WikiWordExtractor
from numpy.random import RandomState
from sklearn.linear_model import LogisticRegression
from typing import Dict, Set

class InnerWikiWordLayer(Layer):
    MAX_TRAINING_ITERATIONS = 1000 # For how many iterations the logistic regression has to be trained

    def __init__(self, pca_components: int, minimum_log: float, degree_total_count: int, random_generator: RandomState):
        self.__pca_components = pca_components
        self.__minimum_log = minimum_log
        self.__degree_total_count = degree_total_count
        self.__random_generator = random_generator

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        if predict_season not in self.seasons_with_data():
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        extractor = WikiWordExtractor(predict_season, train_seasons, self.__pca_components, self.__minimum_log,
                                      self.__degree_total_count, self.__random_generator)
        train_input, train_output = extractor.get_train_data()
        classifier = LogisticRegression(solver = 'lbfgs', max_iter = self.MAX_TRAINING_ITERATIONS)
        classifier.fit(train_input, train_output)

        distribution = dict()
        predict_data = extractor.get_predict_data()
        for player, data in predict_data.items():
            distribution[player] = classifier.predict_proba(data)[0][1]
        return distribution

    @staticmethod
    def seasons_with_data() -> Set[int]:
        """ Get all seasons that have Wiki Word data. """
        return {get_season(player) for player in LINKER}

class WikiWordLayer(CutLayer):
    """ The Wiki Word Layer predicts which player is the Mol based on their wikipedia pages. It tries to find the
     correlation between the number of words on your Wikipage and the likelihood of being the Mol. Furthermore it tries
     to find a correlation to which job a player belongs and the likelihood of being the Mol. """

    def __init__(self, pca_components: int, minimum_log: float, degree_total_count: int, random_generator: RandomState):
        """ Constructor of the Wiki Word Layer.

        Arguments:
            pca_components (int): How many PCA components should be extracted from the job counts as features.
            minimum_log (float): The lower bound on the job count and total count before applying a logarithm.
            degree_total_count (int): Up to which degree a polynomial transformation should be applied on the log
                of the total word count.
            random_generator (RandomState): The random generator used to generate random values.
        """
        super().__init__(InnerWikiWordLayer(pca_components, minimum_log, degree_total_count, random_generator), 1.0)