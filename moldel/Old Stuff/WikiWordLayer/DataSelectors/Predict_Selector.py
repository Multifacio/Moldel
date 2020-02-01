from WikiWordLayer.DataSelectors.DataSelector import DataSelector

class Predict_Selector(DataSelector):
    """ Only selects data that occurs in that season """

    def include(self, candidate_season, current_season):
        return candidate_season == current_season