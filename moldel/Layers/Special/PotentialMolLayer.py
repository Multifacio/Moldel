from Layers.Layer import Layer
from Layers.Special.CompositeLayer import CompositeLayer
from Layers.Special.ExamUniformLayer import ExamUniformLayer
from Layers.Special.ManualExclusionLayer import ManualExclusionLayer

class PotentialMolLayer(CompositeLayer):
    """ The Potential Mol layer excludes all players from a Layer that could not be the Mol anymore, which are all
    players that dropped out, seen a red screen or have been revealed to not be the Mol. """

    def __init__(self, layer: Layer):
        super().__init__([layer, ExamUniformLayer(), ManualExclusionLayer()])
