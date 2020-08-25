from Data.Player import Player
from Data.PlayerData import get_mol_in_season
from typing import Dict, Tuple
from Validators.Validator import Validator
import math

class TotalLogLikelihood(Validator):
    """ Compute the total log likelihood for every season and the total log likelihood of everything. """

    def validate(self, distributions: Dict[Tuple[int, int], Dict[Player, float]]):
        log_likelihoods = dict()
        for pair, distribution in distributions.items():
            season = pair[0]
            likelihood = distribution[get_mol_in_season(season)]
            log_likelihoods[season] = log_likelihoods.get(season, 0.0) + math.log(likelihood)

        print()
        print("Season Log Likelihoods:")
        print(log_likelihoods)

        print()
        print("Total Log Likelihood:")
        print(sum(log_likelihoods.values()))