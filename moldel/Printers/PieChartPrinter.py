from Data.PlayerData import get_name
from Data.Player import Player
from Printers.Printer import Printer
from typing import Dict
import matplotlib.pyplot as plt
import seaborn as sns

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

    def print(self, distribution: Dict[Player, float]):
        palette = sns.color_palette(None, len(distribution))
        labels = []
        sizes = []
        colors = []

        i = 0
        for player in sorted(distribution.keys(), key=lambda item: item.value):
            likelihood = round(distribution[player], self.precision)
            if likelihood >= self.include_threshold:
                labels.append(get_name(player))
                sizes.append(likelihood)
                colors.append(palette[i])
            i += 1

        sizes_sum = sum(sizes)
        sizes = [size / sizes_sum for size in sizes]
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.axis('equal')
        plt.show()