from collections import Counter as counter
from Data.Player import Player
from Data.PlayerData import get_players_in_season, get_season
from Data.Wikipedia import Linker
from Data.Wikipedia.Job import Job
from typing import Counter, List
from typing import Dict, NamedTuple, Set
import enchant
import math
import numpy as np
import re
import rootpath

WikipediaSample = NamedTuple("WikipediaSample", [("job_features", np.array), ("word_feature", float)])
WikipediaData = NamedTuple("WikipediaData", [("job_counts", Counter[Job]), ("number_words", int)])
class WikipediaParser:
    """ The Wikipedia Parser reads all wiki files of all players in the given seasons and converts it to interpretable
    and understandable features. """

    STANDARD_DICTIONARY = "nl_NL" # The standard dictionary used to check if something is a sub word

    def __init__(self, seasons: Set[int], min_subword_length: int, min_word_occurrence: int):
        self.__seasons = seasons
        self.__min_subword_length = min_subword_length
        self.__min_word_occurrence = min_word_occurrence

    def extract_features(self) -> Dict[Player, np.array]:
        dictionary = self.get_standard_dictionary()
        players = set()
        for season in self.__seasons:
            players.update(get_players_in_season(season))

        player_counts = {p: self.full_wiki_parse(p, dictionary, self.__min_subword_length) for p in players}
        player_occurrences = {p: self.get_word_occurrences(player_counts[p]) for p in players}
        occurrences = sum(player_occurrences.values(), counter())
        self.selected_words = [word for word, c in occurrences.items() if c >= self.__min_word_occurrence]
        player_counts = {p: np.array([counts[word] for word in self.selected_words]) for p, counts in player_counts.items()}
        total_words = {p: sum(features) for p, features in player_counts.items()}
        return {p: features / max(total_words[p], 1) for p, features in player_counts.items()}

    @classmethod
    def get_standard_dictionary(self) -> enchant.Dict:
        """ Get the standard dictionary used to check if something is a word.

        Returns:
            The standard dictionary.
        """
        return enchant.Dict(self.STANDARD_DICTIONARY)

    @staticmethod
    def get_word_occurrences(count: Counter[str]) -> Counter[str]:
        """ Convert a counter of words to a counter of 1's indicating that a word occurs.

        Arguments:
            count (Counter[str]): A counter of words.

        Returns:
            A counter of 1's indicating that a word occurs.
        """
        occurrences = counter()
        for word in count.keys():
            occurrences[word] = 1
        return occurrences

    @classmethod
    def full_wiki_parse(self, player: Player, dictionary: enchant.Dict, min_length: int) -> Counter[str]:
        """ Count all the sub word occurrences for a given player.

        Parameters:
            player (Player): The player for which we count the sub word occurrences.
            dictionary (enchant.Dict): The dictionary instance which checks if something is a word.
            min_length (int): The minimum length of a sub word before it is taken into account.

        Returns:
            Counter[str]: A counter which counted all sub word occurrences in his/her Wikipedia file.
        """
        sub_count = counter()
        for word, c in self.wiki_parse(player).items():
            sub_words = self.get_all_sub_words(word, dictionary, min_length)
            for sub_word in sub_words:
                sub_count[sub_word] += c
        return sub_count

    @staticmethod
    def wiki_parse(player: Player) -> Counter[str]:
        """ Count the word occurrences for a given player.

        Parameters:
            player (Player): The player for which we count the word occurrences.

        Returns:
            Counter[str]: A counter which counted all word occurrences in his/her Wikipedia file.
        """
        file_path = rootpath.detect() + "/" + Linker.WIKI_FILES_PATH + Linker.LINKER[player]
        file = open(file_path, "r", encoding = "utf8")
        count = counter()
        for line in file.readlines():
            line = WikipediaParser.__line_filter(line)
            tokens = line.split(" ")
            for token in tokens:
                if token != "":
                    count[token] += 1
        return count

    @staticmethod
    def get_all_sub_words(word: str, dictionary: enchant.Dict, min_length: int) -> Set[str]:
        """ Get all words included in a larger word, including that larger word.

        Arguments:
            word (str): The word of which we extract all sub words.
            dictionary (enchant.Dict): The dictionary instance which checks if something is a word.
            min_length (int): The minimum length of a sub word before it is taken into account.
        """
        all_sub_words = {word}
        for i in range(len(word)):
            for j in range(i + min_length, len(word) + 1):
                sub_word = word[i:j]
                if dictionary.check(sub_word):
                    all_sub_words.add(sub_word)
        return all_sub_words

    @staticmethod
    def __line_filter(line: str) -> str:
        """ Filter unwanted symbols/characters from a read line in the wiki file.

        Arguments:
            line (str): The line that is being filtered.

        Returns:
            A filtered version of that line.
        """
        return re.sub('[^a-z0-9]', ' ', line.lower())
