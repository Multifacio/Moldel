from Data.Player import Player
from typing import Dict, Tuple

class Validator:
    """ A Validator interprets the distributions for different episodes and seasons. Based on this it
    prints/shows/visualizes/stores/etc. something. """

    def validate(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]):
        """ Prints/shows/visualizes/stores/etc. the interpretation.

            Parameters:
                distributions (Dict[Tuple[int, int], Dict[Player, float]]): A dictionary with as key a tuple consisting
                    of season and episode and as value the distribution for that season episode combination.
        """
        pass