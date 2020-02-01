from WikiWordLayer.WordFilters.WordManipulator import WordManipulator
from WikiWordLayer.WordFilters.WordPrinter import WordPrinter

class TO_Printer(WordPrinter):
    """ The TO Printer sorts the words based on total occurrence (sum of occurrences in all pages) and prints out the
    words with their total occurrence value. """
    def __init__(self, decreasing_order):
        """ Create a TO Printer.
        Arguments:
            decreasing_order (bool): If set to true then it will be print in decreasing order, otherwise it will be
            print in increasing order. """
        self.decreasing_order = decreasing_order

    def print(self, important_words, parsed_data):
        ranking = [(w, WordManipulator.get_total_occurrence_word(w, parsed_data)) for w in important_words]
        ranking.sort(key=lambda tup: tup[1])
        if self.decreasing_order:
            ranking.reverse()
        print(ranking)