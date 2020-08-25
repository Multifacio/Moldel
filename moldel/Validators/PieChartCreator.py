from Data.Player import Player
from pathlib import Path
from Printers.PieChartPrinter import PieChartPrinter
from typing import Dict, Tuple
from Validators.Validator import Validator
import os
import rootpath

class PieChartCreator(Validator):
    """ Create a Pie Chart image file for every distribution. """
    RESULT_FOLDER = "/results/"

    def __init__(self, name: str, precision: int, include_threshold: float):
        """ Constructor of the Pie Chart Creator.

        Arguments:
            name (str): The name of the subfolder where the results will be stored.
            precision (int): Up to how many decimals the likelihoods will be rounded before printing them
                    (if you do not round the likelihoods then the pie chart will be cluttered).
            include_threshold (float): Only players with a likelihood larger or equal than this threshold will be
                included in the pie chart (if you do not use this then you can have slice where the text is larger
                than the slice itself which means that the text can overlap with text from other slices).
        """
        self.__name = name
        self.__precision = precision
        self.__include_threshold = include_threshold

    def validate(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]):
        folder = rootpath.detect() + self.RESULT_FOLDER + self.__name
        os.mkdir(folder)

        seasons = {pair[0] for pair in distributions.keys()}
        for season in seasons:
            os.mkdir(folder + "/Season " + str(season))

        for pair, distribution in distributions.items():
            season, latest_episode = pair
            file_name = self.get_file_name(folder, season, latest_episode)
            printer = PieChartPrinter(self.__precision, self.__include_threshold, file_name)
            printer.print(distribution)

    @staticmethod
    def get_file_name(main_folder: str, season: int, latest_episode: int) -> str:
        """ Get the file name where the Pie Chart for a distribution will be stored.

        Arguments:
            main_folder (str): The main folder in which all the results are stored.
            season (int): The season of the distribution which will be stored.
            latest_episode (int): The latest episode used as training data for the distribution.

        Returns:
            The file name for the Pie Chart.
        """
        file_part = "Before Start" if latest_episode == 0 else "After Episode " + str(latest_episode)
        return main_folder + "/Season " + str(season) + "/" + "{0:0=2d}".format(latest_episode) + " - " + file_part + ".png"