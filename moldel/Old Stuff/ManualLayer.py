from DistributionTransformers.NormalizeTransformer import NormalizeTransformer
from Layers.Layer import Layer, DataError

class ManualLayer(Layer):
    """ The Manual Layer will set likelihoods to each candidate manually. """

    def __init__(self, layer_name, likelihoods):
        """ Create a Manual Layer.
        Arguments:
            layer_name (string): The name of the layer
            likelihoods (dict): A dictionary with as key the season (integer) and as value a dictionary with as
            key the candidate (enum) and as value the likelihood (float) """
        self.layer_name = layer_name
        self.likelihoods = likelihoods

    def compute_distribution(self, season, episode):
        if season not in self.likelihoods:
            raise DataError(self.layer_name + " - Missing data season " + str(season))
        distribution = self.likelihoods[season]
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(distribution)