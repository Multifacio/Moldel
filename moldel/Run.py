from Layers.Moldel import Moldel
from numpy.random import RandomState
from Printers.PieChartPrinter import PieChartPrinter
from Printers.TextSortedPrinter import TextSortedPrinter
import sys

RANDOM_SEED = 949019755
TRAIN_SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
PREDICT_SEASON = 20
LATEST_EPISODE = sys.maxsize
TRAIN_SEASONS.discard(PREDICT_SEASON)

random_generator = RandomState(RANDOM_SEED)
moldel = Moldel(random_generator)
distribution = moldel.compute_distribution(PREDICT_SEASON, LATEST_EPISODE, TRAIN_SEASONS)
printer = PieChartPrinter(2, 0.015)
printer.print(distribution)