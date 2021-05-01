from Data.Player import Player
from Data.PlayerData import get_name, get_season, get_age, get_is_mol
from typing import Any, Dict
import json

def json_player(player: Player) -> Dict[str, Any]:
    return {"id": player.value, "name": get_name(player), "season": get_season(player), "is_mol": get_is_mol(player),
            "age": get_age(player)}

FILE_NAME = "PlayerData.json"
data = [json_player(p) for p in Player]

with open("Output/" + FILE_NAME, 'w') as file:
    json.dump(data, file)