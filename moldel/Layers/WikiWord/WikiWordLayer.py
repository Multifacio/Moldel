from Data.Player import Player
from Layers.Layer import Layer
from Layers.Special.NormalizeLayer import NormalizeLayer
from Layers.WikiWord.WikiWordExtractor import WikiWordExtractor
from Layers.WikiWord.WikiWordParser import WikiWordParser
from sklearn.linear_model import LogisticRegression
from typing import Dict, Set
import numpy as np

class InnerWikiWordLayer(Layer):
    """ The Wiki Word Layer predicts which candidate is the Mol based on their wikipedia pages. """

    MAX_TRAINING_ITERATIONS = 1000 # For how many iterations the logistic regression has to be trained

    # How strong the regularization will be. Lower values means a stronger regularization, higher values means a weaker
    # regularization. A strong regularization prevents overfitting and will bring the computed distribution more to
    # an uniform distribution.
    REGULARIZATION_PARAMETER = 0.2

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        train_data = WikiWordParser.parse(train_seasons)

        extractor = WikiWordExtractor(train_data)
        train_input = []
        train_output = []
        for player, data in train_data.items():
            train_input.append(extractor.extract_input(data))
            train_output.append(1 if player.value.is_mol else 0)

        classifier = LogisticRegression(solver='lbfgs', max_iter=self.MAX_TRAINING_ITERATIONS, penalty='l2',
                                        C=self.REGULARIZATION_PARAMETER)
        classifier.fit(np.array(train_input), np.array(train_output))

        distribution = dict()
        predict_data = WikiWordParser.parse({predict_season})
        for player, data in predict_data.items():
            predict_input = extractor.extract_input(data)
            distribution[player] = classifier.predict_proba(np.array([predict_input]))[0][1]

        return distribution

class WikiWordLayer(NormalizeLayer):
    def __init__(self):
        super().__init__(InnerWikiWordLayer())