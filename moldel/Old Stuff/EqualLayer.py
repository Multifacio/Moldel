from Candidates import *
from ManualLayer import ManualLayer

class EqualLayer(ManualLayer):
    """ The Equal Layer gives an equal likelihood to all candidates. """

    def __init__(self):
        likelihoods = dict()
        for candidate in Candidates:
            season = candidate.value.season
            if season not in likelihoods:
                likelihoods[season] = dict()
            likelihoods[season][candidate] = 1.0
        super().__init__("Equal Layer", likelihoods)