from Data.Player import Player
from Data.PlayerData import get_players_in_season, get_age, get_is_mol, get_season
from Layers.FaceVisibility.FaceVisibilityLayer import InnerFaceVisibilityLayer
from Layers.Layer import Layer
from Layers.Special.CutLayer import CutLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from scipy.stats import gaussian_kde
from typing import Dict, Set, Tuple
import numpy as np

class InnerAgeLayer(Layer):
    # Values related to determine the boundaries.
    MIN_VALUE = 0.0 # The lowest value used when searching for the boundaries.
    MAX_VALUE = 100.0 # The highest value used when searching for the boundaries.

    def __init__(self, cdf_cutoff: float):
        self.__cdf_cutoff = cdf_cutoff

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        non_mol_kde, mol_kde = self.__training(train_seasons)
        return self.__prediction(predict_season, non_mol_kde, mol_kde)

    def __training(self, train_seasons: Set[int]) -> Tuple[gaussian_kde, gaussian_kde]:
        """ Execute the training phase of the Age Layer.

        Arguments:
             train_seasons (Set[int]):  The season used as training data

        Returns:
            The kernel density estimator for respectively the Mol data and non-Mol data.
        """
        players = [player for player in Player if get_season(player) in train_seasons]
        train_input = [float(get_age(player)) for player in players]
        train_output = [1.0 if get_is_mol(player) else 0.0 for player in players]
        non_mol = np.array([data for data, label in zip(train_input, train_output) if label == 0.0])
        mol = np.array([data for data, label in zip(train_input, train_output) if label == 1.0])
        non_mol_kde = InnerFaceVisibilityLayer.kernel_density_estimation(non_mol)
        mol_kde = InnerFaceVisibilityLayer.kernel_density_estimation(mol)
        return non_mol_kde, mol_kde

    def __prediction(self, predict_season: int, non_mol_kde: gaussian_kde, mol_kde: gaussian_kde) -> Dict[Player, float]:
        """ Execute the prediction phase of the Age Layer.

        Arguments:
            predict_season (int): For which season we make the prediction.
            non_mol_kde (gaussian_kde): The Kernel Density Estimator for non-Mol ages.
            mol_kde (gaussian_kde): The Kernel Density Estimator for Mol ages.

        Returns:
            A dictionary with as key the players that participated in the prediction season and as value their Mol
            likelihood based on their age.
        """
        all_predictions = dict()
        predict_data = {player: float(get_age(player)) for player in get_players_in_season(predict_season)}
        min_value = InnerFaceVisibilityLayer.get_boundary(non_mol_kde, mol_kde, len(predict_data),
                                                          self.__cdf_cutoff / 2, self.MIN_VALUE, self.MAX_VALUE)
        max_value = InnerFaceVisibilityLayer.get_boundary(non_mol_kde, mol_kde, len(predict_data),
                                                          1 - self.__cdf_cutoff / 2, self.MIN_VALUE, self.MAX_VALUE)
        for player, age in predict_data.items():
            age = min(max(age, min_value), max_value)
            non_mol_likelihood = non_mol_kde.pdf(age)[0] * (len(predict_data) - 1) / len(predict_data)
            mol_likelihood = mol_kde.pdf(age)[0] / len(predict_data)
            all_predictions[player] = mol_likelihood / (non_mol_likelihood + mol_likelihood)

        return all_predictions

class AgeLayer(CutLayer):
    """ The Age Layer predict which player is the Mol based on their age. """

    def __init__(self, cdf_cutoff: float):
        """ Constructor of the Age Layer.

        Arguments:
            cdf_cutoff (float): This is the total cumulative density which is cutoff from both sides of the
                distributions (mol and non-mol distribution). All appearance values that lie in the cutoff zone of both
                distributions are changed to the closest value that lies in the range of at least one of the
                distributions.
        """
        super().__init__(InnerAgeLayer(cdf_cutoff), lambda x: 1 / len(x), 1.0, 0.0)