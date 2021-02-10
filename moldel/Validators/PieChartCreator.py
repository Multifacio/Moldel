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

    def __init__(self, name: str):
        """ Constructor of the Pie Chart Creator.

        Arguments:
            name (str): The name of the subfolder where the results will be stored.
        """
        self.__name = name

    def validate(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]):
        folder = rootpath.detect() + self.RESULT_FOLDER + self.__name
        os.mkdir(folder)

        seasons = {pair[0] for pair in distributions.keys()}
        for season in seasons:
            os.mkdir(folder + "/Season " + str(season))

        for pair, distribution in distributions.items():
            season, latest_episode = pair
            file_name = self.get_file_name(folder, season, latest_episode)
            printer = PieChartPrinter(file_name)
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