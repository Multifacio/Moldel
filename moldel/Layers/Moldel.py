from Layers.FaceVisibility.FaceVisibilityLayer import InnerFaceVisibilityLayer, FaceVisibilityLayer
from Layers.Special.CompositeLayer import CompositeLayer
from Layers.WikiWord.WikiWordLayer import WikiWordLayer

class Moldel(CompositeLayer):
    """ The Moldel is a combination of multiple layers used to do the total prediction of the Mol. """

    def __init__(self):
        super().__init__([FaceVisibilityLayer(1/3, 0.9, 14, 2)])