from Data.LastEpisodes import get_last_episode
from Layers.Appearance.AppearanceLayer import AppearanceLayer
from Layers.ExamDrop.ExamDropLayer import ExamDropLayer
from Layers.ExamPass.ExamPassLayer import ExamPassLayer
from Layers.Moldel import Moldel
from numpy.random.mtrand import RandomState
from progress.bar import Bar

from Layers.Special.MemoryLayer import MemoryLayer
from Layers.Special.PotentialMolLayer import PotentialMolLayer
from Layers.Wikipedia.WikipediaLayer import WikipediaLayer
from Validators.PieChartCreator import PieChartCreator
from Validators.Precomputer import Precomputer
from Validators.TotalLogLoss import TotalLogLoss
from Validators.ValidationMetrics import ValidationMetrics

RANDOM_SEED = 949019755
VALIDATE_SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
TRAIN_SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

distributions = dict()
random_generator = RandomState(RANDOM_SEED)
moldel = PotentialMolLayer()

total_tasks = sum([get_last_episode(season) + 1 for season in VALIDATE_SEASONS])
progress_bar = Bar("Distributions Computed:", max = total_tasks)
for season in VALIDATE_SEASONS:
    train_seasons = TRAIN_SEASONS.difference({season})
    for episode in range(get_last_episode(season) + 1):
        distributions[(season, episode)] = moldel.compute_distribution(season, episode, train_seasons)
        progress_bar.next()
progress_bar.finish()

# validator = Precomputer("Full Moldel Predictions")
validator = PieChartCreator("Uniform (9-21)")
# validator = ValidationMetrics(9, [10, 9, 8, 7, 6, 5, 4, 3, 2])
# validator = TotalLogLoss()
validator.validate(distributions)