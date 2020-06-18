from Data.Player import Player
from Layers.Layer import Layer
from typing import Dict, Set, List
import itertools as it
import math

class HypertunedLayer(Layer):
    SMALL_LOG_ADDITION = 0.0001

    def __init__(self, hyperparams_options: Dict[str, List[float]]):
        self.hyperparams_options = hyperparams_options

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        all_mol = {p.value.season: p for p in Player if p.value.is_mol}

        best_hyperparams = dict()
        best_score = -math.inf
        for hyperparams in it.product(*self.hyperparams_options.values()):
            hyperparams = dict(zip(self.hyperparams_options, hyperparams))
            score = self.__validate(latest_episode, train_seasons, all_mol, hyperparams)
            if score > best_score:
                best_hyperparams = hyperparams

        print(best_hyperparams)
        return self.compute_distribution2(predict_season, latest_episode, train_seasons, best_hyperparams)

    def compute_distribution2(self, predict_season: int, latest_episode: int, train_seasons: Set[int],
                              hyperparams: Dict[str, float]) -> Dict[Player, float]:
        pass

    def __validate(self, latest_episode: int, train_seasons: Set[int], all_mol: Dict[int, Player],
                   hyperparams: Dict[str, float]) -> float:
        score = 0.0
        for validate_season in train_seasons:
            score += self.__validate_season(validate_season, latest_episode, train_seasons, all_mol[validate_season],
                                            hyperparams)
        return score

    def __validate_season(self, validate_season: int, latest_episode: int, train_seasons: Set[int], mol: Player,
                          hyperparams: Dict[str, float]) -> float:
        distribution = self.compute_distribution2(validate_season, latest_episode, train_seasons, hyperparams)
        return math.log(distribution[mol] + self.SMALL_LOG_ADDITION)
