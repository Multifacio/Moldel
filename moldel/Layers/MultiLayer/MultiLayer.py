from Data.Player import Player
from typing import Dict, NamedTuple, Set
import numpy as np

MultiLayerResult = NamedTuple("MultiLayerResult", [("predictions", np.array), ("exclusion", bool)])
class MultiLayer:
    """ A Multi Layer does multiple predictions how likely someone is the 'Mol'. """

    def predict(self, predict_season: int, latest_episode: int, train_seasons: Set[int]) -> Dict[Player, MultiLayerResult]:
        """ Do multiple predictions about how likely a player is the 'Mol'.

        Parameters:
            predict_season (int): The season number for which the predictions are made (the season started at
                19 november 1999 is considered as season number 1).
            latest_episode (int): From the predict_season we only use episode data from episodes with numbers until the
                latest_episode number as observation data. This also includes the entire episode data from the episode
                with the latest_episode number. <br>
                - Set this value to sys.maxsize if you want to use all episodes from the predict_season as observation
                    data.
                - Set this value to 0 if you want to use no episodes from the predict_season as observation data.
                    (Which can be used to check the performance of only the pre-layers)
            train_seasons (Set[int]): A set of season numbers (int) which are used for training this layer.

        Returns:
            Dict[Player, MultiLayerResult]: A dictionary that contains the predictions for each player how likely they
                are the 'Mol'. The key of this dictionary is the Player for which the predictions are made and the value
                is a MultiLayerResult which consists of an array of floats that indicates how likely the player is the
                'Mol' and an exclusion value which is True if this MultiLayer determined that that player cannot be the
                'Mol' anymore and False if there is still a posibility that the player is the 'Mol'. In case the
                MultiLayer cannot say something about any participant then an empty dictionary is returned.
        """
        pass