from DistributionTransformers.DistributionTransformer import DistributionTransformer

class RoundTransformer(DistributionTransformer):
    """ The round transformer will round all likelihood with a certain precision """

    def transform_distribution(self, distribution, **kwargs):
        precision = kwargs["precision"]
        new_distribution = dict()
        for key in distribution:
            new_distribution[key] = round(distribution[key], precision)
        return new_distribution
