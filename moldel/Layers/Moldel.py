from Layers.AgeLayer.AgeLayer import AgeLayer
from Layers.ExamDrop.ExamDropLayer import ExamDropLayer
from Layers.ExamPass.ExamPassLayer import ExamPassLayer
from Layers.ExamUniformLayer import ExamUniformLayer
from Layers.FaceVisibility.FaceVisibilityLayer import FaceVisibilityLayer
from Layers.MultiLayer.CombineLayer import CombineLayer
from Layers.MultiLayer.StackLayer import StackLayer
from Layers.SocialMediaLayer import SocialMediaLayer
from Layers.Special.CompositeLayer import CompositeLayer
from Layers.Special.ManualExclusionLayer import ManualExclusionLayer
from Layers.Special.MemoryLayer import MemoryLayer
from Layers.Wikipedia.WikipediaLayer import WikipediaLayer
from numpy.random import RandomState

class MoldelStacker(StackLayer):
    SPLITS = [{2, 3, 4}, {5, 6}, {7, 8}, {9, 10, 11}]

    def __init__(self, random_generator: RandomState):
        predict_layers = [ExamDropLayer(1e-2, 0.95, 40), WikipediaLayer(-0.524, 0.417, 5, random_generator),
                          FaceVisibilityLayer(1/5, 13, 4, 2, 0.01, 0.01), ExamPassLayer(), AgeLayer(0.02)]
        train_layers = [MemoryLayer("Exam Drop Stacker"), MemoryLayer("Wikipedia Stacker"),
                        MemoryLayer("Appearance Stacker"), MemoryLayer("Exam Pass Stacker"), MemoryLayer("Age Stacker")]
        super().__init__(CombineLayer(predict_layers, True), CombineLayer(train_layers, True), self.SPLITS)

class Moldel(CompositeLayer):
    """ The Moldel is a combination of multiple layers used to do the total prediction of the Mol. """

    def __init__(self, random_generator: RandomState):
        """ Constructor of the Moldel.

        Arguments:
            random_generator (RandomState): The random generator used to generate random values.
        """
        super().__init__([MoldelStacker(random_generator), SocialMediaLayer(), ManualExclusionLayer()])