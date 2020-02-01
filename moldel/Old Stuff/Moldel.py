from itertools import compress

from DistributionTransformers.CompositeTransformer import CompositeTransformer
from DistributionTransformers.LowerRemovalTransformer import LowerRemovalTransformer
from DistributionTransformers.ManualExclusions import ManualExclusions
from DistributionTransformers.RoundTransformer import RoundTransformer
from EarlyActivityLayer.EarlyActivityLayer import EarlyActivityLayer
from Layers.ExamLayer import ExamLayer
from FaceVisibilityLayers.FaceVisibilityLayer import FaceVisibilityLayer
from Printers.PiechartPrinter import PiechartPrinter
from WikiWordLayer.DataExtractors.Job_Extractor import Job_Extractor
from WikiWordLayer.DataPredictors.Cossim_Predictor import Cossim_Predictor
from WikiWordLayer.WikiWordLayer import WikiWordLayer

LAYERS = [ExamLayer(10000),
          WikiWordLayer(Job_Extractor(), Cossim_Predictor(10, 2, 0.02), False),
          EarlyActivityLayer(),
          FaceVisibilityLayer(False, {1: 2.0, 2: 20.0, 3: 50.0, 4: 100.0})]
PRINTER = PiechartPrinter()

# All frequently changed constants. The episode value is inclusive, meaning that also the result of the test of that
# episode is also included as data. If you set episode to 0 as value then no episodes are used as data at all. If you
# set episode to None then all known information about that season is used.
EXAM_ACTIVATED = True
WIKIWORD_ACTIVATED = True
EARLYACTIVITY_ACTIVATED = True
FACEVISIBILITY_ACTIVATED = True
SEASON = 18
EPISODE = 1

# Start of the code
include = [EXAM_ACTIVATED, WIKIWORD_ACTIVATED, EARLYACTIVITY_ACTIVATED, FACEVISIBILITY_ACTIVATED]
included_layers = list(compress(LAYERS, include))
results = []
for l in included_layers:
    results.append(l.compute_distribution(SEASON, EPISODE))
composite = CompositeTransformer()
results = composite.transform_distribution(results)
excluder = ManualExclusions()
results = excluder.transform_distribution(results, season = SEASON, episode = EPISODE)
rounder = RoundTransformer()
results = rounder.transform_distribution(results, precision = 3)
remover = LowerRemovalTransformer()
results = remover.transform_distribution(results, threshold = 0.015)
PRINTER.do_print(results)