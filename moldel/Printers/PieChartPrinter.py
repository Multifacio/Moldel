from Data.PlayerData import get_name
from Data.Player import Player
from iteround import saferound
from Printers.Printer import Printer
from typing import Dict, Union
import matplotlib.pyplot as plt
import seaborn as sns

class PieChartPrinter(Printer):
    """ The Pie Chart Printer prints a pie chart with the likelihoods that players are the Mol. """

    def __init__(self, precision: int, include_threshold: float, file_name: Union[str, None] = None):
        """ Constructor of the Pie Chart Printer.

            Parameters:
                precision (int): Up to how many decimals the likelihoods will be rounded before printing them
                    (if you do not round the likelihoods then the pie chart will be cluttered).
                include_threshold (float): Only players with a likelihood larger or equal than this threshold will be
                    included in the pie chart (if you do not use this then you can have slice where the text is larger
                    than the slice itself which means that the text can overlap with text from other slices).
                file_name (Union[str, None]): If set then instead of showing a Pie Chart, it will save a Pie Chart as
                    this given file name.
        """
        self.__precision = precision
        self.__include_threshold = include_threshold
        self.__file_name = file_name

    def print(self, distribution: Dict[Player, float]):
        palette = sns.color_palette(None, len(distribution))
        labels = []
        sizes = []
        colors = []

        i = 0
        for player in sorted(distribution.keys(), key=lambda item: item.value):
            likelihood = distribution[player]
            if likelihood >= self.__include_threshold:
                labels.append(get_name(player))
                sizes.append(likelihood)
                colors.append(palette[i])
            i += 1

        sizes_sum = sum(sizes)
        sizes = saferound([size / sizes_sum for size in sizes], self.__precision)
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        plt.axis('equal')
        if self.__file_name is None:
            plt.show()
        else:
            plt.savefig(self.__file_name)
            plt.clf()