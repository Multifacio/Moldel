from Data.Player import Player
from Data.PlayerData import get_is_mol, get_season
from Data.WikiWord.Linker import LINKER
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.CutLayer import CutLayer
from Layers.WikiWord.WikiWordExtractor import WikiWordExtractor
from Layers.WikiWord.WikiWordParser import WikiWordParser
from sklearn.linear_model import LogisticRegression
from typing import Dict, Set
import numpy as np

class InnerWikiWordLayer(Layer):
    MAX_TRAINING_ITERATIONS = 1000 # For how many iterations the logistic regression has to be trained

    # How strong the regularization will be. Lower values means a stronger regularization, higher values means a weaker
    # regularization. A strong regularization prevents overfitting and will bring the computed distribution more to
    # an uniform distribution.
    REGULARIZATION_PARAMETER = 0.2

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        if predict_season not in self.seasons_with_data():
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        train_data = WikiWordParser.parse(train_seasons)
        extractor = WikiWordExtractor(train_data)
        train_input = []
        train_output = []
        for player, data in train_data.items():
            train_input.append(extractor.extract_input(data))
            train_output.append(1 if get_is_mol(player) else 0)

        classifier = LogisticRegression(solver='lbfgs', max_iter=self.MAX_TRAINING_ITERATIONS, penalty='l2',
                                        C=self.REGULARIZATION_PARAMETER)
        classifier.fit(np.array(train_input), np.array(train_output))

        distribution = dict()
        predict_data = WikiWordParser.parse({predict_season})
        for player, data in predict_data.items():
            predict_input = extractor.extract_input(data)
            distribution[player] = classifier.predict_proba(np.array([predict_input]))[0][1]

        return distribution

    @staticmethod
    def seasons_with_data() -> Set[int]:
        return {get_season(player) for player in LINKER}

class WikiWordLayer(CutLayer):
    """ The Wiki Word Layer predicts which candidate is the Mol based on their wikipedia pages. """

    def __init__(self):
        super().__init__(InnerWikiWordLayer(), 1.0)