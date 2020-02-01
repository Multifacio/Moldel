from DistributionTransformers.DistributionTransformer import DistributionTransformer
from DistributionTransformers.NormalizeTransformer import NormalizeTransformer


class ScaleTransformer(DistributionTransformer):
    """ The scale transformer will make a distribution less/more extreme (by raising a distribution to a certain power).
    If the exponent is 1 then the likelihood distribution will remain the same, lower than 1 means that it will
    converge more to an uniform distribution and higher than 1.0 means that it will converge more to
    a likelihood distribution where the highest likelihood is 1.0 and the others are 0.0 """

    def transform_distribution(self, distribution, **kwargs):
        exp = kwargs["exp"]
        new_distribution = dict()
        for key in distribution:
            new_distribution[key] = pow(distribution[key], exp)
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(new_distribution)