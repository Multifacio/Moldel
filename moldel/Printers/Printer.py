from Data.Player import Player
from typing import Dict

class Printer:
    """ A printer looks at the distribution how likely players are the 'Mol' and based on this distribution it
     prints/shows/visualizes/stores/etc. something. """

    def print(self, distribution: Dict[Player, float]):
        """ Prints/shows/visualizes/stores/etc. the interpretation.

            Parameters:
                distribution (Dict[Player, float]): A dictionary with as keys the player from that season and with
                    values the likelihood that this player is the 'Mol'.
        """
        pass