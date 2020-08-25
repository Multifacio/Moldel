from Data.Player import Player
from Data.PlayerData import get_name
from iteround import saferound
from Printers.Printer import Printer
from typing import Dict

class TextSortedPrinter(Printer):
    """ The Text Sorted Printer is the most basic printer that prints the Mol likelihood score for every player. The
    results are sorted from the highest score to lowest score. This class can also be used to determine how many points
    should be put on every player in the "Wie is de Mol" app. """

    def __init__(self, precision: int, multiplier: float = 1.0):
        """ Constructor of the Text Sorted Printer.

        Parameters:
            precision (int): Up to how many decimals the scores will be rounded before printing them (if you do not
                round the likelihoods then the results are not readable).
            multiplier (float): By which value all likelihoods are multiplied to obtain the likelihood score.
        """
        self.__precision = precision
        self.__multiplier = multiplier

    def print(self, distribution: Dict[Player, float]):
        distribution = {player: value * self.__multiplier for player, value in distribution.items()}
        distribution = saferound(distribution, self.__precision)
        sorted_distribution = []
        for player, likelihood in distribution.items():
            sorted_distribution.append((get_name(player), likelihood))

        sorted_distribution.sort(key=lambda x: x[1], reverse=True)
        for row in sorted_distribution:
            player_name = row[0]
            likelihood = row[1]
            print(player_name + ": " + str(likelihood))