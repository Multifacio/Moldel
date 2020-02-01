from DistributionTransformers.DistributionTransformer import DistributionTransformer
from DistributionTransformers.NormalizeTransformer import NormalizeTransformer

class LowerRemovalTransformer(DistributionTransformer):
    """ Change likelihoods below a certain threshold to 0.0. """

    def transform_distribution(self, distribution, **kwargs):
        new_distribution = dict()
        for candidate, value in distribution.items():
            if value < kwargs["threshold"]:
                new_distribution[candidate] = 0.0
            else:
                new_distribution[candidate] = value
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(new_distribution)
