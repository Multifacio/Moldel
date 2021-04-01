from Data.Player import Player
from typing import Dict, Tuple
from Validators.ValidationMetrics import ValidationMetrics
from Validators.Validator import Validator

class TotalLogLoss(Validator):
    """ Computes the total log loss over all predictions. """

    def validate(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]):
        print("Total Log Loss: " + str(ValidationMetrics.log_loss(distributions)))