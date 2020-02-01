from DistributionTransformers.DistributionTransformer import DistributionTransformer

class NormalizeTransformer(DistributionTransformer):
    """ The normalize transformer will normalize the likelihood distribution such that it sums up to 1.0 """

    def transform_distribution(self, distribution, **kwargs):
        total = 0.0
        new_distribution = dict()
        for value in distribution.values():
            total += value
        for key in distribution:
            new_distribution[key] = distribution[key] / total
        return new_distribution
