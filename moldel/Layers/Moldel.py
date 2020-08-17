from Layers.ExamDrop.ExamDropLayer import ExamDropLayer
from Layers.FaceVisibility.FaceVisibilityLayer import FaceVisibilityLayer
from Layers.MultiLayer.GeneralStackingLayer import GeneralStackingLayer
from Layers.MultiLayer.LayersIntoMulti import LayersIntoMulti
from Layers.SocialMediaLayer import SocialMediaLayer
from Layers.Special.CompositeLayer import CompositeLayer
from Layers.Special.ManualExclusionLayer import ManualExclusionLayer
from Layers.WikiWord.WikiWordLayer import WikiWordLayer
from numpy.random import RandomState

class InnerMoldel(LayersIntoMulti):
    def __init__(self, random_generator: RandomState):
        super().__init__([ExamDropLayer(1e-2, 0.99, 2), WikiWordLayer(6, 1.0, 2, random_generator),
                          FaceVisibilityLayer(1/3, 0.9, 14, 2)])

class Moldel(ManualExclusionLayer):
    """ The Moldel is a combination of multiple layers used to do the total prediction of the Mol. """

    def __init__(self, random_generator: RandomState):
        """ Constructor of the Moldel.

        Arguments:
            random_generator (RandomState): The random generator used to generate random values.
        """
        super().__init__(CompositeLayer([GeneralStackingLayer(InnerMoldel(random_generator), 0.5, 8, 9),
                                         SocialMediaLayer()]))