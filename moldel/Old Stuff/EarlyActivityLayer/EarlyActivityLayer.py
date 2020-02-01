from EarlyActivityLayer.Data import SUSPICION_DATA
from ManualLayer import ManualLayer

class EarlyActivityLayer(ManualLayer):
    """ The Early Activity Layer checks whether someone was active during the recording of "Wie is de Mol" which
    indicates that this candidate dropped of earlier and did not reach the finals (so this candidate cannot be the Mol).
    Suspicion Levels for each candidate should be manually inserted in the Data file. """

    def __init__(self):
        parsed_data = dict()
        for season, season_data in SUSPICION_DATA.items():
            inner_parse = dict()
            for candidate, suspicion in season_data.items():
                inner_parse[candidate] = suspicion.value
            parsed_data[season] = inner_parse
        super().__init__("Early Activity Layer", parsed_data)

