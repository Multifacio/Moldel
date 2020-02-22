import math

from Data.Player import Player
from Data.WikiWord.Job import Job
from Layers.WikiWord.WikiWordParser import WikiWordData
from typing import Dict, List
import numpy as np

class WikiWordExtractor:
    """ The Wiki Word Extractor excludes and transforms features into a array of floats which can be used by the
    classification algorithm. """

    # How many job features should be used. Only this number of the most frequent job features will be used.
    NUMBER_JOB_FEATURES = 5

    # Which quantile in the list of occurrences of every job will be used to compare all the job features.
    COMPARISON_QUANTILE = 0.8

    # Job frequencies higher than this value will be set to this value in the input extraction to prevent overfitting
    # on outlier data. (Note that after this still the logarithm will be applied)
    JOB_FREQUENCY_CUT_OFF = 10

    def __init__(self, train_data: Dict[Player, WikiWordData]):
        """ Constructor of the Wiki Word Extractor (is used to determine which Job features need to be excluded).

        Parameters:
            train_data (Dict[Player, WikiWordData]): The parsed train data which is used to determine which Job features
            needs to be excluded.
        """
        self.__included_jobs = self.__get_included_jobs(train_data)

    def extract_input(self, player_data: WikiWordData) -> np.array:
        """ Extract the input array for 1 player based on the wiki page data of that player.

        Parameters:
             player_data (WikiWordData): The parsed train data for 1 player which is converted to an array of
             transformed features (floats) used by the classification algorithm.

        Returns:
            An array of transformed features (floats) for that player which is used by the classification algorithm.
        """
        extracted_input = []
        job_frequency, number_words = player_data
        for job in self.__included_jobs:
            log_score = math.log(1 + min(self.JOB_FREQUENCY_CUT_OFF, job_frequency[job]))
            extracted_input.append(log_score)

        log_number_words = math.log(1 + number_words)
        extracted_input.append(log_number_words)
        extracted_input.append(log_number_words ** 2)
        return np.array(extracted_input)

    @staticmethod
    def get_job_occurrences(data: Dict[Player, WikiWordData]) -> Dict[Job, List[int]]:
        """ Compute the number of words for each jobs per player in sorted order (in the number of words).

        Parameters:
            data: The parsed data of which the occurrences of every job get determined.

        Returns:
            Dict[Job, List[int]]: A dictionary with as key the Job and as value a sorted list of occurrences among every
            player for that job.
        """
        job_occurrences = dict()
        for job in Job:
            counts = [player_data.job_frequency[job] for player_data in data.values()]
            counts.sort()
            job_occurrences[job] = counts

        return job_occurrences

    @staticmethod
    def __get_included_jobs(train_data: Dict[Player, WikiWordData]) -> List[Job]:
        """ Determine all jobs that will be included as features.

        Parameters:
            train_data (Dict[Player, WikiWordData]): The parsed train data which will be used to check which jobs should
            be used as features.

        Returns:
            List[Job]: A list with all jobs that should be included.
        """
        job_scores = []
        job_occurrences = WikiWordExtractor.get_job_occurrences(train_data)
        for job, occurrence in job_occurrences.items():
            job_score = WikiWordExtractor.__compute_job_score(np.array(occurrence))
            job_scores.append((job, job_score))

        job_scores.sort(key=lambda item: item[1], reverse=True)
        return [job for job, _ in job_scores[:WikiWordExtractor.NUMBER_JOB_FEATURES]]

    @staticmethod
    def __compute_job_score(occurrences: np.array) -> float:
        """ Compute the score of every job, which is the comparison quantile slightly influenced by the mean of
        occurrences of that jobs.

        Parameters:
            occurrences (np.array): A sorted array of integers which indicates how frequent the job occurs in the wiki
            pages of all players.

        Returns:
            float: The score of that job. The higher the score of the job, the more likely it will be selected as
            feature.
        """
        quantile = np.quantile(occurrences, WikiWordExtractor.COMPARISON_QUANTILE)
        mean = np.mean(occurrences)
        return quantile + 1 / (1 + math.exp(-mean))