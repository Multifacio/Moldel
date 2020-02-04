from Layers.Moldel import Moldel
from Printers.PieChartPrinter import PieChartPrinter

train_seasons = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19}
predict_season = 9
train_seasons.remove(predict_season)
moldel = Moldel()
distribution = moldel.compute_distribution(predict_season, 0, train_seasons)
printer = PieChartPrinter(3, 0.015)
printer.print(distribution)