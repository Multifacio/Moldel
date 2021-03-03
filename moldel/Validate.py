from Data.LastEpisodes import get_last_episode
from Layers.ExamDrop.ExamDropLayer import ExamDropLayer
from Layers.Moldel import Moldel
from numpy.random.mtrand import RandomState
from progress.bar import Bar
from Validators.PieChartCreator import PieChartCreator
from Validators.Precomputer import Precomputer
from Validators.TotalLogLoss import TotalLogLoss
from Validators.ValidationMetrics import ValidationMetrics

RANDOM_SEED = 949019755
VALIDATE_SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
TRAIN_SEASONS = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

distributions = dict()
random_generator = RandomState(RANDOM_SEED)
moldel = ExamDropLayer(2e-2, 0.95, 24)

total_tasks = sum([get_last_episode(season) + 1 for season in VALIDATE_SEASONS])
progress_bar = Bar("Distributions Computed:", max = total_tasks)
for season in VALIDATE_SEASONS:
    train_seasons = TRAIN_SEASONS.difference({season})
    for episode in range(get_last_episode(season) + 1):
        distributions[(season, episode)] = moldel.compute_distribution(season, episode, train_seasons)
        progress_bar.next()
progress_bar.finish()

# validator = Precomputer("Stacker")
# validator = PieChartCreator("Appearance (9-21)")
# validator = ValidationMetrics(9, [2, 3, 4, 5, 6, 7, 8, 9, 10])
validator = TotalLogLoss()
validator.validate(distributions)