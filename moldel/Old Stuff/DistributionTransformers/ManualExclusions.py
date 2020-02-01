import math

from Candidates import *
from DistributionTransformers.DistributionTransformer import DistributionTransformer
from DistributionTransformers.NormalizeTransformer import NormalizeTransformer

class ManualExclusions(DistributionTransformer):
    """ Exclude persons who cannot be the Mol. For example during the finals of season 14 it was announced that
        Freek is not the Mol. """

    # Exclusions is a dictionary with as keys the season numbers and as values a list of tuples where the first value
    # in the tuple is the candidate and the second value is the episode from which on it is known that this candidate
    # is not the Mol.
    EXCLUSIONS = {14: [(Candidates.FREEK_14, 9)]}

    def transform_distribution(self, distribution, **kwargs):
        if kwargs["episode"] is None:
            kwargs["episode"] = math.inf
        season_exclusions = self.EXCLUSIONS.get(kwargs["season"], [])
        excluded = {candidate for candidate, episode in season_exclusions if episode <= kwargs["episode"]}
        new_distribution = dict()
        for candidate, value in distribution.items():
            if candidate in excluded:
                new_distribution[candidate] = 0.0
            else:
                new_distribution[candidate] = value
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(new_distribution)