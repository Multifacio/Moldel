from Data.Player import Player
from Layers.Layer import Layer
from typing import Dict, Set
from Validators.Precomputer import Precomputer

class MemoryLayer(Layer):
    """ The Memory Layer returns back a precomputed distribution. """

    def __init__(self, save_folder: str):
        """ Constructor of the Memory Layer.

        Arguments:
            save_folder (str): The folder inside the MAIN_SAVE_FOLDER from which we load the precomputed distributions.
        """
        self.__save_folder = save_folder

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        precomputer = Precomputer(self.__save_folder)
        return precomputer.load_distribution(predict_season, latest_episode)