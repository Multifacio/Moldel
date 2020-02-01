from WikiWordLayer.DataSelectors.DataSelector import DataSelector

class Strict_Train_Selector(DataSelector):
    """ Only selects data that occurs before that season """

    def include(self, candidate_season, current_season):
        return candidate_season < current_season

