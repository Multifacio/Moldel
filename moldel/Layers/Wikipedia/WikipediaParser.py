from collections import Counter
from Data.Player import Player
from Data.PlayerData import get_players_in_season, get_season
from Data.Wikipedia import Linker
from Data.Wikipedia.Job import Job
from typing import Counter as CounterType
from typing import Dict, NamedTuple, Set
import enchant
import math
import numpy as np
import re
import rootpath

WikipediaSample = NamedTuple("WikipediaSample", [("job_features", np.array), ("word_feature", float)])
WikipediaData = NamedTuple("WikipediaData", [("job_counts", CounterType[Job]), ("number_words", int)])
class WikipediaParser:
    """ The Wikipedia Parser reads all wiki files of all players in the given seasons and converts it to interpretable
    and understandable features. """

    MIN_LENGTH_COMPOUND_WORD = 4 # The minimum length of the sub words that get extracted out of a larger compound word
    STANDARD_DICTIONARY = "nl_NL" # The standard dictionary used to check if something is a sub word

    @classmethod
    def parse(self, seasons: Set[int]) -> Dict[Player, WikipediaSample]:
        """ Parse the Wikipedia files of all players that participated in these seasons to features.

        Parameters:
            seasons (Set[int]): The seasons for which we want to compute all features of the players that participated
                in it.

        Returns:
            Dict[Player, WikipediaSample]: A dictionary with as key the players and as value a Wikipedia Sample tuple
                with as first value all job features and as second value the feature related to the total number of
                words in the players Wikipedia page.
        """
        feature_data = dict()
        min_job_features = dict()
        dictionary = self.get_standard_dictionary()
        for season in seasons:
            raw_data = self.parse_raw(season, dictionary)
            job_counts = dict()
            sum_words = sum(data.number_words for data in raw_data.values())
            for player, data in raw_data.items():
                for job in Job:
                    job_counts[(player, job)] = 0.0 if data.number_words == 0 else data.job_counts[job] / data.number_words

            for job in Job:
                job_sum = sum(job_counts[(player, job)] for player in raw_data)
                for player, data in raw_data.items():
                    job_count = job_counts[(player, job)]
                    if job_count > 0.0:
                        job_count = math.log(job_count / job_sum)
                        job_counts[(player, job)] = job_count
                        min_job_features[job] = min(job_count, min_job_features.get(job, math.inf))
                    else:
                        job_counts[(player, job)] = None

            for player, data in raw_data.items():
                job_features = {job: job_counts[(player, job)] for job in Job}
                word_feature = math.log(max(data.number_words, 1) / sum_words)
                feature_data[player] = (job_features, word_feature)

        for player, data in feature_data.items():
            job_features, word_feature = feature_data[player]
            job_features = [min_job_features[job] if count is None else count for job, count in job_features.items()]
            feature_data[player] = WikipediaSample(job_features, word_feature)

        return feature_data

    @classmethod
    def get_standard_dictionary(self) -> enchant.Dict:
        """ Get the standard dictionary used to check if something is a word.

        Returns:
            The standard dictionary.
        """
        return enchant.Dict(self.STANDARD_DICTIONARY)

    @classmethod
    def parse_raw(self, season: int, dictionary: enchant.Dict) -> Dict[Player, WikipediaData]:
        """ Parse the Wikipedia files of all players that participated in this season to counts.

        Parameters:
            season (int): The season for which we want to compute all counts of the players that participated in it.
            dictionary (enchant.Dict): The dictionary instance which checks if something is a word.

        Returns:
            Dict[Player, WikipediaData]: A dictionary with as key the players and as value a Wikipedia Data tuple with
                as first value a counter of all job for this player and as second value the total number of words in the
                players Wikipedia page.
        """
        raw_data = dict()
        for player in get_players_in_season(season):
            raw_data[player] = WikipediaParser.extract_player_features(player, dictionary)
        return raw_data

    @classmethod
    def extract_player_features(self, player: Player, dictionary: enchant.Dict) -> WikipediaData:
        """ Computes the features for a given player which are the frequencies of every Job and a total number of words
        in the players Wikipedia page.

        Parameters:
            player (Player): The player for which we want to compute the features.
            dictionary (enchant.Dict): The dictionary instance which checks if something is a word.

        Returns:
            WikipediaData: Which is a tuple with two values. The first value is a dictionary with Job as key and as value
            the total number of times each of the Job word occurs in the wiki page. The second value is the total number
            of words in the players Wikipedia page.
        """
        word_counts = WikipediaParser.wiki_file_parse(player)
        job_counts = Counter()
        for word, count in word_counts.items():
            related_jobs = self.get_related_jobs(word, dictionary)
            for job in related_jobs:
                job_counts[job] += count / len(related_jobs)

        return WikipediaData(job_counts, sum(job_counts.values()))

    @classmethod
    def get_related_jobs(self, word: str, dictionary: enchant.Dict) -> Set[Job]:
        """ Get all jobs related to a word.

        Arguments:
            word (str): The word for which we determine all related jobs.
            dictionary (enchant.Dict): The dictionary instance which checks if something is a word.

        Returns:
            The set of all related jobs, which can also be an empty set.
        """
        related_jobs = set()
        min_words = 1
        min_length = 0
        sub_words = self.get_all_sub_words(word, dictionary, self.MIN_LENGTH_COMPOUND_WORD)
        for job in Job:
            intersection = sub_words.intersection(job.value)
            new_words = len(intersection)
            new_length = max(len(w) for w in intersection) if intersection else 0
            if new_words > min_words or (new_words == min_words and new_length > min_length):
                min_words = new_words
                min_length = new_length
                related_jobs = {job}
            elif new_words == min_words and new_length == min_length:
                related_jobs.add(job)
        return related_jobs

    @staticmethod
    def wiki_file_parse(player: Player) -> CounterType[str]:
        """ Count the word occurrences for a given player.

        Parameters:
            player (Player): The player for which we count the word occurrences.

        Returns:
            Counter[str]: A counter which counted all word occurrences in the file.
        """
        file_path = rootpath.detect() + "/" + Linker.WIKI_FILES_PATH + Linker.LINKER[player]
        file = open(file_path, "r", encoding = "utf8")
        counter = Counter()
        for line in file.readlines():
            line = WikipediaParser.line_filter(line)
            tokens = line.split(" ")
            for token in tokens:
                if token != "":
                    counter[token] += 1
        return counter

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
    def line_filter(line: str) -> str:
        """ Filter unwanted symbols/characters from a read line in the wiki file. """
        return re.sub('[^a-z0-9]', ' ', line.lower())
