from Printers.Printer import Printer
import matplotlib.pyplot as plt

class PieChartPrinter(Printer):
    """ The Pie Chart Printer prints a pie chart with the likelihoods that players are the Mol. """

    def __init__(self, precision: int, include_threshold: float):
        """ Constructor of the Pie Chart Printer.

            Parameters:
                precision (int): Up to how many decimals the likelihoods will be rounded before printing them
                    (if you do not round the likelihoods then the pie chart will be cluttered).
                include_threshold (float): Only players with a likelihood larger or equal than this threshold will be
                    included in the pie chart (if you do not use this then you can have slice where the text is larger
                    than the slice itself which means that the text can overlap with text from other slices).
        """
        self.precision = precision
        self.include_threshold = include_threshold

    def print(self, distribution: dict):
        labels = list()
        sizes = list()
        for player, likelihood in distribution.items():
            likelihood = round(likelihood, self.precision)
            if likelihood >= self.include_threshold:
                labels.append(player.value.name)
                sizes.append(likelihood)
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()