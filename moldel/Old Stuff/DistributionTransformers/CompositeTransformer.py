from DistributionTransformers.DistributionTransformer import DistributionTransformer
from DistributionTransformers.NormalizeTransformer import NormalizeTransformer


class CompositeTransformer(DistributionTransformer):
    """ The composite transformer will combine multiple likelihood distributions """

    def transform_distribution(self, distribution, **kwargs):
        res = distribution[0].copy()
        for i in range(1, len(distribution)):
            res = self.combine(res, distribution[i])
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(res)

    def combine(self, res, temp):
        new_distribution = dict()
        for key in res:
            new_distribution[key] = res[key] * temp[key]
        return new_distribution