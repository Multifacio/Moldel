from Data.LastEpisodes import get_last_episode
from Layers.Moldel import Moldel
from numpy.random.mtrand import RandomState
from progress.bar import Bar
from Validators.PieChartCreator import PieChartCreator
from Validators.Precomputer import Precomputer
from Validators.TotalLogLikelihood import TotalLogLikelihood

RANDOM_SEED = 949019755
VALIDATE_SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
TRAIN_SEASONS = {7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

distributions = dict()
random_generator = RandomState(RANDOM_SEED)
moldel = Moldel(random_generator)

total_tasks = sum([get_last_episode(season) + 1 for season in VALIDATE_SEASONS])
progress_bar = Bar("Distributions Computed:", max = total_tasks)
for season in VALIDATE_SEASONS:
    train_seasons = TRAIN_SEASONS.difference({season})
    for episode in range(get_last_episode(season) + 1):
        distributions[(season, episode)] = moldel.compute_distribution(season, episode, train_seasons)
        progress_bar.next()
progress_bar.finish()

# validator = Precomputer("ForExamPass")
# validator = PieChartCreator("Full Moldel: Season 14-20 (2020-08-25)", 2, 0.015)
validator = TotalLogLikelihood()
validator.validate(distributions)