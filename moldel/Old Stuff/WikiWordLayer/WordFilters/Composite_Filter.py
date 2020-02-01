from WikiWordLayer.WordFilters.WordFilter import WordFilter

class Composite_Filter(WordFilter):
    def __init__(self):
        self.filters = []

    def add(self, filter):
        self.filters.append(filter)

    def filter(self, all_words, parsed_data):
        important_words = all_words
        for f in self.filters:
            important_words = f.filter(important_words, parsed_data)
        return important_words