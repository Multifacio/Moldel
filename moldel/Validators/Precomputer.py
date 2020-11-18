from Data.Player import Player
from typing import Dict, Tuple, Union
from Validators.Validator import Validator
import os
import pickle
import rootpath

class Precomputer(Validator):
    """ The Precomputer stores the predictions as pickle files which can be used as train data by other layers. """

    MAIN_SAVE_FOLDER = "moldel/Data/Predictions/" # The root folder in which all predictions are stored.

    def __init__(self, save_folder: str):
        """ Constructor of the Precomputer.

        Arguments:
            save_folder (str): The folder inside the MAIN_SAVE_FOLDER where the predictions are stored.
        """
        self.__save_folder = save_folder

    def validate(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]):
        for pair, distribution in distributions.items():
            file_path = self.__get_file_path(*pair)
            with open(file_path, 'wb') as file:
                pickle.dump(distribution, file)

    def load_distribution(self, season: int, episode: int) -> Union[Dict[Player, float], None]:
        """ Load a precomputed distribution for a given season and episode.

        Arguments:
            season (int): The given season.
            episode (int): The given episode.

        Returns:
            The precomputed distribution for this given season and episode. If it does not exist then return None.
        """
        file_path = self.__get_file_path(season, episode)
        if not os.path.isfile(file_path):
            return None

        with open(file_path, 'rb') as file:
            distribution = pickle.load(file)
        return distribution

    def __get_file_path(self, season: int, episode: int) -> str:
        """ Get the file path were a precomputed distribution will be stored.

        Arguments:
            season (int): The season of the distribution.
            episode (int): The episode of the distribution.

        Returns:
            The file path were the precomputed distribution will be stored.
        """
        return rootpath.detect() + "/" + self.MAIN_SAVE_FOLDER + self.__save_folder + "/s" + str(season) + "e" + \
               str(episode) + ".data"
