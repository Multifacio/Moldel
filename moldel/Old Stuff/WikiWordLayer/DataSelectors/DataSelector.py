class DataSelector:
    """ The Data Selector interface """

    def select(self, numberic_data, parsed_data, season):
        """ Selects part of the data out of the numberic_data based on the season.
        Arguments:
            numberic_data (dict): More information can be found in DataExtractor (same data type as return value)
            parsed_data (dict): More information can be found in DataParser
            season (int): The season number on which we will do a prediction about who the Mol is

        Returns: A filtered numberic data where only the numberic data of some candidate remains. """
        selected_data = dict()
        for candidate in parsed_data:
            if self.include(parsed_data[candidate]["season"], season):
                selected_data[candidate] = numberic_data[candidate]
        return selected_data

    def include(self, candidate_season, current_season):
        """ Whether the data should be selected.
        Arguments:
            candidate_season (int): The season number of the candidate of which we wants to decide whether it should be
            included or not.
            current_season (int): The season for which we will do a prediction about who the Mol is

        Returns: True if the candidates data should be selected. False if the candidates data should not be selected."""
        pass