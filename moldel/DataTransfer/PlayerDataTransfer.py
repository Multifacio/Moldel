from Data.Player import Player
from Data.PlayerData import get_name, get_season, get_age, get_is_mol
import json

FILE_NAME = "data.json"
data = [{"id": p.value, "name": get_name(p), "season": get_season(p), "is_mol": get_is_mol(p), "age": get_age(p)}
            for p in Player]

with open("Output/" + FILE_NAME, 'w') as file:
    json.dump(data, file)