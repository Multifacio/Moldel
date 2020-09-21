from Layers.ExamDrop.ExamDropLayer import ExamDropLayer
from Layers.ExamUniformLayer import ExamUniformLayer
from Layers.FaceVisibility.FaceVisibilityLayer import FaceVisibilityLayer
from Layers.SocialMediaLayer import SocialMediaLayer
from Layers.Special.CompositeLayer import CompositeLayer
from Layers.Special.ManualExclusionLayer import ManualExclusionLayer
from Layers.WikiWord.WikiWordLayer import WikiWordLayer
from numpy.random import RandomState

class InnerMoldel(CompositeLayer):
    #  1.175
    def __init__(self, random_generator: RandomState):
        super().__init__([ExamDropLayer(1e-2, 0.95, 4), WikiWordLayer(6, 1.0, 2, random_generator), SocialMediaLayer(),
                          FaceVisibilityLayer(1/5, 0.95, 14, 5.0)])

class Moldel(ManualExclusionLayer):
    """ The Moldel is a combination of multiple layers used to do the total prediction of the Mol. """

    def __init__(self, random_generator: RandomState):
        """ Constructor of the Moldel.

        Arguments:
            random_generator (RandomState): The random generator used to generate random values.
        """
        super().__init__(InnerMoldel(random_generator))