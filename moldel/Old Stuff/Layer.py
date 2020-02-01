class DataError(Exception):
    def __init__(self, message):
        self.message = message

# Interface used to compute the likelihood distribution which indicates how likely someone is the 'Mol'
class Layer:
    def compute_distribution(self, season, episode):
        """ Compute the likelihood distribution of each candidate that it is the 'Mol'
            Args:
                season (int): The season number for which the likelihoods are computed (19 november 1999 is considered
                as season 1)
                episode (int): Until which episode the data is used, including this entire episode. None means that all
                episodes known so far are used. 0 means that none data of the episodes is used at all.

            Returns:
                dict: A dictionary that contains the likelihood for each candidate that it is the 'Mol'

            Raises:
                DataError: When the model does not have sufficient enough data to compute a distribution
        """
        pass