from Printers.Printer import Printer

class TextSortedPrinter(Printer):
    """ The Text Sorted Printer is the most basic printer that print how likely every player is the Mol. The results are
        sorted from the highest likelihood to the least likelihood. """

    def __init__(self, precision: int):
        """ Constructor of the Text Sorted Printer.

            Parameters:
                precision (int): Up to how many decimals the likelihoods will be rounded before printing them
                    (if you do not round the likelihoods then the results are not readable).
        """
        self.precision = precision

    def print(self, distribution: dict):
        sorted_distribution = list()
        for player, likelihood in distribution.items():
            likelihood = round(likelihood, self.precision)
            sorted_distribution.append((player.value.name, likelihood))
        sorted_distribution.sort(key=lambda x: x[1], reverse=True)
        for row in sorted_distribution:
            player_name = row[0]
            likelihood = row[1]
            print(player_name + ": " + str(likelihood))