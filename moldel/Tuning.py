from Data.LastEpisodes import get_last_episode
from Layers.ExamDrop.ExamDropLayer import ExamDropLayer
from Layers.Layer import Layer
from Validators.ValidationMetrics import ValidationMetrics
from progress.bar import Bar
from queue import PriorityQueue
from typing import List, Dict, Any
import math
import numpy as np

VALIDATE_SEASONS = {9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}
TRAIN_SEASONS = {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21}

def params_options() -> List[Dict[str, Any]]:
    regularization = [math.exp(x) for x in np.linspace(-math.log(100), math.log(100), 50)]
    return [{"feature_significance": 1e-2, "regularization": r, "max_splits": 40} for r in regularization]

ranking = PriorityQueue()
options = params_options()

total_tasks = sum([get_last_episode(season) + 1 for season in VALIDATE_SEASONS])
progress_bar = Bar("Distributions Computed:", max = len(options) * total_tasks)
progress_bar.start()
for params in options:
    model = ExamDropLayer(**params)
    distributions = dict()
    for season in VALIDATE_SEASONS:
        train_seasons = TRAIN_SEASONS.difference({season})
        for episode in range(get_last_episode(season) + 1):
            distributions[(season, episode)] = model.compute_distribution(season, episode, train_seasons)
            progress_bar.next()
    score = ValidationMetrics.log_loss(distributions)
    ranking.put((score, params))
progress_bar.finish()

for score, params in list(ranking.queue):
    print(params)
    print("Log Loss: " + str(score))
    print()


