from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_players_in_season
from Layers.Layer import Layer
from Layers.Special.EqualLayer import EqualLayer
from Layers.Special.NormalizeLayer import NormalizeLayer
from typing import Set, Dict

class InnerExamUniformLayer(Layer):
    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, float]:
        available_seasons = EXAM_DATA.keys()
        if predict_season not in available_seasons:
            return EqualLayer().compute_distribution(predict_season, latest_episode, train_seasons)

        season_players = get_players_in_season(predict_season)
        alive_players = EXAM_DATA[predict_season].get_alive_players(latest_episode)
        return {player: 1.0 if player in alive_players else 0.0 for player in season_players}

class ExamUniformLayer(NormalizeLayer):
    """ The Exam Uniform Layer gives a uniform prediction to all players, excluding the players that have dropped off
    according to the Exam Data. """

    def __init__(self):
        super().__init__(InnerExamUniformLayer())