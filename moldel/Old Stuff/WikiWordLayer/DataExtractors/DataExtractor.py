class DataExtractor:
    """ The Data Extractor interface """

    def extract(self, parsed_data):
        """ Extract numberic vectors out of the candidate data.
        Arguments:
            parsed_data (dict): More information can be found in DataParser

        Returns: A dictionary with candidates as key and a list of floats (numberic vectors) as values. """
        pass
