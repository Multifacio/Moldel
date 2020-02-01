from WikiWordLayer.DataExtractors.DataExtractor import DataExtractor

class Output_Extractor(DataExtractor):
    """ The output extractor will add a 1 if the player is the Mol and a 0 if the player is not the Mol. """

    def extract(self, parsed_data):
        numberic_output = dict()
        for candidate in parsed_data:
            if parsed_data[candidate]["mol"]:
                numberic_output[candidate] = 1
            else:
                numberic_output[candidate] = 0
        return numberic_output