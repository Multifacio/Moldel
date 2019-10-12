from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Season:
    """ Representation of the episodes in a season and players participating in this episode.

    Attributes:
        players (list): A list of all players that participated in this season (which also includes early drop offs and
            which includes the Mol).
        episodes (dict): The execution/test/drop off moments during a season. The key (float) is an episode number,
            if multiple executions/test/drop off moments happen then the keys should be different values in the range
            e - 1 < key <= e where e is the episode number of that episode in which these moments happen. The order of
            the moments matters: the earliest moment should get the lowest key and the latest moment should get the key
            value e. The values of this dict are Episode instances.
    """
    players: list
    episodes: dict