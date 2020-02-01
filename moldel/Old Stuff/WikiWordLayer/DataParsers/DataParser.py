import rootpath
import string

from WikiWordLayer.DataParsers.Linker import LINKER

class DataParser:
    """ The Data Parser will read the Wiki Files and Linker for each candidate and convert it into a variable
    "parsed_data". This variable is a dictionary with 3 keys:
    -"occ": Which is a dictionary where the keys are the words occuring in the wiki page of the candidate and the
    values are ints how often this word occurs in the candidate wiki page.
    -"season": Which is an integer equal to the season in which the candidate participated.
    -"mol": Which is a boolean variable. It is equal to true if this candidate is the Mol.
    the word occurences (occ), season number (season) and whether that person is the Mol or not (mol). """

    WIKI_FILES_FOLDER = "/moldel/WikiWordLayer/WikiFiles/"

    @staticmethod
    def parse():
        """ Will parse all data for all candidates """
        parsed_data = dict()
        for candidate, occ in LINKER.items():
            parsed_data[candidate] = {"occ": DataParser.wiki_file_parse(occ), "season": candidate.value.season,
                                      "mol": candidate.value.is_mol}
        return parsed_data

    @staticmethod
    def get_all_words(parsed_data):
        """ Extract all words from the parsed data """
        all_words = set()
        for candidate in parsed_data:
            candidate_words = parsed_data[candidate]["occ"].keys()
            all_words.update(candidate_words)
        return all_words

    @staticmethod
    def wiki_file_parse(file_name):
        """ Will parse the word occurrences of a single wiki file """
        file = open(rootpath.detect() + DataParser.WIKI_FILES_FOLDER + file_name, "r", encoding="utf8")
        lines = file.readlines()
        word_occurrence = dict()
        for line in lines:
            filtered = DataParser.line_filter(line)
            split = filtered.split(" ")
            for word in split:
                pure_word = DataParser.word_filter(word)
                word_occurrence[pure_word] = word_occurrence.get(pure_word, 0) + 1
        return word_occurrence

    @staticmethod
    def line_filter(line):
        result = line.lower()
        for char in string.punctuation: # Remove symbols from text
            result = result.replace(char, ' ')
        result = result.strip("\n")
        result = result.strip("\t")
        return result

    @staticmethod
    def word_filter(word):
        result = word.strip("\n")
        result = result.strip("\t")
        return result
