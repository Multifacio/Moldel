class WordFilter:
    """ The Word Filter interface """

    def filter(self, all_words, parsed_data):
        """ Filter the important words out of all words.
        Arguments:
            all_words (set): A set of all words found in the parsed data
            parsed_data (dict): More information can be found in DataParser

        Returns: A set of all (possible) important words """
        pass