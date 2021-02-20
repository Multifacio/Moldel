from Data.PlayerData import get_name
from Data.Player import Player
from iteround import saferound
from Printers.Printer import Printer
from typing import Dict, Union
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class PieChartPrinter(Printer):
    """ The Pie Chart Printer prints a pie chart with the likelihoods that players are the Mol. """

    # Up to how many decimals the likelihoods will be rounded before printing them (if you do not round the likelihoods
    # then the pie chart will be cluttered).
    __PRECISION = 3

    # Players with a likelihood below this threshold are annotated using a line (if you do not use this then you can
    # have slice where the text is larger than the slice itself which means that the text can overlap with text from
    # other slices).
    __THRESHOLD_LIKELIHOOD = 0.015

    # The minimum difference between the previous and next angle
    __THRESHOLD_MIN_ANGLE_INC = 4

    # The relative length of the line with respect to the radius of the circle
    __THRESHOLD_LINE_LENGTH = 0.5

    def __init__(self, file_name: Union[str, None] = None):
        """ Constructor of the Pie Chart Printer.

        Parameters:
            file_name (Union[str, None]): If set then instead of showing a Pie Chart, it will save a Pie Chart as this
                given file name.
        """
        self.__file_name = file_name

    def print(self, distribution: Dict[Player, float]):
        palette = sns.color_palette(None, len(distribution))
        labels = []
        sizes = []
        colors = []

        i = 0
        for player in sorted(distribution.keys(), key=lambda item: item.value):
            likelihood = distribution[player]
            if likelihood != 0:
                labels.append(get_name(player))
                sizes.append(likelihood)
                colors.append(palette[i])
            i += 1

        sizes_sum = sum(sizes)
        sizes = saferound([size / sizes_sum for size in sizes], self.__PRECISION)

        wedges, names, percentages = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
        kw = dict(arrowprops=dict(arrowstyle="-"), zorder=0, va="center")
        previous_angle = None
        for i, it in enumerate(zip(wedges, names, percentages, sizes)):
            wedge, name, percentage, size = it
            if size < self.__THRESHOLD_LIKELIHOOD:
                name.update({'visible': False})
                percentage.update({'visible': False})
                angle = (wedge.theta2 - wedge.theta1) / 2 + wedge.theta1
                text_angle = angle
                if previous_angle is not None and self.__angle_distance(angle, previous_angle) < self.__THRESHOLD_MIN_ANGLE_INC:
                    text_angle = (previous_angle + self.__THRESHOLD_MIN_ANGLE_INC + 360) % 360
                x, y = np.cos(np.deg2rad(angle)), np.sin(np.deg2rad(angle))
                x_text = (1 + self.__THRESHOLD_LINE_LENGTH) * np.cos(np.deg2rad(text_angle))
                y_text = (1 + self.__THRESHOLD_LINE_LENGTH) * np.sin(np.deg2rad(text_angle))
                horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
                plt.annotate(name.get_text() + ": " + percentage.get_text(), xy=(x, y), xytext=(x_text, y_text),
                             horizontalalignment=horizontalalignment, **kw)
                previous_angle = angle

        if self.__file_name is None:
            plt.show()
        else:
            plt.savefig(self.__file_name)
            plt.clf()

    @staticmethod
    def __angle_distance(angle1: float, angle2: float):
        forward_distance = (angle1 - angle2) % 360
        backward_distance = (angle2 - angle1) % 360
        return min(forward_distance, backward_distance)