from DistributionTransformers.DistributionTransformer import DistributionTransformer

class ReverseTransformer(DistributionTransformer):
    """ The Reverse Transformer will make low likelihoods high and high likelihoods low """
    def transform_distribution(self, distribution, **kwargs):
        total_weight = 0.0
        new_distribution = dict()
        for value in distribution.values():
            total_weight += 1 / value
        for key in distribution:
            weight = 1 / distribution[key]
            new_distribution[key] =  weight / total_weight
        return new_distribution