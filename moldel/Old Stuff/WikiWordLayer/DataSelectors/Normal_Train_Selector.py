from WikiWordLayer.DataSelectors.DataSelector import DataSelector

class Normal_Train_Selector(DataSelector):
    """ Only selects data that does not occur in that season """

    def include(self, candidate_season, current_season):
        return not candidate_season == current_season