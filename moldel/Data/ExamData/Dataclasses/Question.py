from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, List

import numpy as np
import scipy as sc
import scipy.stats

@dataclass
class Question:
    """ Representation of a visible question during the test.

    Attributes:
        answers (Dict[int, List[Player]]): All the possible answers for this question. The key (int) is the answer
            number which starts with 1 and are numbered from top to bottom, from left to right. The value is a list of
            players corresponding to this answer. Questions should always be a partitioning, meaning that every player
            is represented by exactly 1 answer.
    """
    answers: Dict[int, List[Player]]

    def entropy(self) -> float:
        """ Compute the entropy (using base log) of this question, which is a measure how hard this question is. If the
        entropy is larger then the question is harder to answer correctly.

        Returns:
            The entropy of this question which is a value >= 0.0.
        """
        probabilities = np.array([len(players) for players in self.answers.values()])
        probabilities = probabilities / sum(probabilities)
        return sc.stats.entropy(probabilities)