from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Earnings.All import MONEY_DATA
from Data.Player import Player
from Data.PlayerData import get_is_mol
from Tools.Encoders.NaturalSplineEncoding import NaturalSplineEncoding
from Tools.Encoders.SemiRankTransformer import SemiRankTransformer, Setting
from numpy.random import RandomState
from scipy.special import logit
from sklearn.linear_model import LogisticRegression
from typing import Counter, List, NamedTuple, Set, Callable
import numpy as np

MoneySample = NamedTuple("MoneySample", [("player", Player), ("num_alive", int), ("major_self", float),
                                         ("major_others", np.array), ("minor_self", float), ("minor_others", np.array)])
class MoneyEncoder:
    """ The Money Encoder deals with the encoding of the features used for the Money Layer. For encoding, the likelihood
    of being the Mol is estimated using Semi Rank Transformation and Natural Spline Encoding combined with a Logistic
    Regression for both the major and minor earned amounts. And as encoding the likelihoods of yourself both major/minor
    are used plus quantiles of the major/minor likelihoods of other players """

    # Which clusters containing these values should be ignored during the Semi Rank Transformation.
    SEMI_RANK_TRANSFORM_IGNORED_VALUES = {0}

    def __init__(self, spline_clusters: int, num_other_likelihood_quantiles: int, random_generator: RandomState):
        """ Constructor of the Money Encoder.

        Arguments:
            spline_clusters (int): The number of KMeans clusters used in the Semi Rank Transformation and in the
                Spline Encoding to estimate how likely a player is the Mol based on how many money that player earned.
            num_other_likelihood_quantiles (int): The number of quantiles used to extract features from the likelihoods
                based on what others earn.
            random_generator (RandomState): The random generator used to generate random values.
        """
        self.__spline_clusters = spline_clusters
        self.__num_other_likelihood_quantiles = num_other_likelihood_quantiles
        self.__random_generator = random_generator

    def get_money_samples(self, seasons: Set[int], latest_episode: float) -> List[MoneySample]:
        """ Get all Money Samples from a range of seasons.

        Arguments:
            seasons (Set[int]): The seasons from which the money samples are extracted.
            latest_episode (float): The latest episode taken into consideration.

        Returns:
            The list of all Money Samples.
        """
        samples = []
        for season in seasons:
            exercises = MONEY_DATA[season].get_exercises(latest_episode)
            for exercise in exercises:
                samples.extend(self.__extract_samples_exercise(exercise))
        return samples

    def extract_features(self, sample: MoneySample, major_likelihood: Callable[[float], float],
                         minor_likelihood: Callable[[float], float]) -> np.array:
        """ Get the feature encoding of a Money Sample.

        Arguments:
            sample (MoneySample): The sample from which the feature encoding is extracted.
            major_likelihood (Callable[[float], float]): Function returning Mol likelihood based on major earned money.
            minor_likelihood (Callable[[float], float]): Function returning Mol likelihood based on minor earned money.

        Returns:
            The feature encoding of this sample.
        """
        quantiles = np.linspace(0, 1, self.__num_other_likelihood_quantiles)
        major_major_likelihoods = np.quantile([major_likelihood(earning) for earning in sample.major_others], quantiles)
        major_minor_likelihoods = np.quantile([minor_likelihood(earning) for earning in sample.major_others], quantiles)
        minor_major_likelihoods = np.quantile([major_likelihood(earning) for earning in sample.minor_others], quantiles)
        minor_minor_likelihoods = np.quantile([minor_likelihood(earning) for earning in sample.minor_others], quantiles)
        features = np.concatenate((np.array([major_likelihood(sample.major_self)]), major_major_likelihoods,
                                   np.array([minor_likelihood(sample.major_self)]), major_minor_likelihoods,
                                   np.array([major_likelihood(sample.minor_self)]), minor_major_likelihoods,
                                   np.array([minor_likelihood(sample.minor_self)]), minor_minor_likelihoods,
                                   np.array([1 / sample.num_alive])))
        return logit(features)

    def major_money_pattern(self, samples: List[MoneySample]) -> Callable[[float], float]:
        """ Learn the likelihood function how likely someone is the Mol based on what that player major earned during a
        single exercise.

        Arguments:
            samples (List[MoneySample): The samples used to train the likelihood function

        Returns:
            A function that returns based on how many money that player major earned how likely that player is the Mol.
        """
        train_input = np.array([[sample.major_self] for sample in samples])
        train_output = np.array([1.0 if get_is_mol(sample.player) else 0.0 for sample in samples])
        return self.__learn_money_pattern(train_input, train_output)

    def minor_money_pattern(self, samples: List[MoneySample]) -> Callable[[float], float]:
        """ Learn the likelihood function how likely someone is the Mol based on what that player minor earned during a
        single exercise.

        Arguments:
            samples (List[MoneySample): The samples used to train the likelihood function

        Returns:
            A function that returns based on how many money that player minor earned how likely that player is the Mol.
        """
        train_input = np.array([[sample.minor_self] for sample in samples])
        train_output = np.array([1.0 if get_is_mol(sample.player) else 0.0 for sample in samples])
        return self.__learn_money_pattern(train_input, train_output)

    def __learn_money_pattern(self, train_input: np.array, train_output: np.array) -> Callable[[float], float]:
        """ Learn the likelihood function how likely someone is the Mol based on what that player major/minor earned
        during a single exercise.

        Arguments:
            train_input (np.array): The major/minor earned money by players.
            train_output (np.array): Whether these major/minor earned money amount where earned by a mol or not.

        Returns:
            A function that returns based on how many money that player major/minor earned how likely that player is the
            Mol.
        """
        transformer = SemiRankTransformer([Setting(self.__spline_clusters, self.SEMI_RANK_TRANSFORM_IGNORED_VALUES)],
                                          self.__random_generator)
        transformer.fit(train_input)
        train_input = transformer.transform(train_input)
        spline_encoder = NaturalSplineEncoding([self.__spline_clusters], self.__random_generator)
        spline_encoder.knots = transformer.rank_splits
        train_input = spline_encoder.transform(train_input)

        regression = LogisticRegression()
        regression.fit(train_input, train_output)
        return lambda money: regression.predict_proba(spline_encoder.transform(transformer.transform(np.array([[money]]))))[0][1]

    def __extract_samples_exercise(self, exercise: Exercise) -> List[MoneySample]:
        """ Extract all Money Samples from a given exercise.

        Arguments:
            exercise (Exercise): The exercise from which all Money Samples are extracted.

        Returns:
            All Money Samples related to the given exercise.
        """
        major_earned = exercise.major_earned()
        minor_earned = exercise.minor_earned()

        # Normalize the earning amounts by multiplying them by the number of players still alive
        for player, earned in major_earned.items():
            major_earned[player] = len(exercise.alive) * earned
        for player, earned in minor_earned.items():
            minor_earned[player] = len(exercise.alive) * earned

        return [self.__extract_single_sample(exercise, player, major_earned, minor_earned) for player in exercise.alive]

    def __extract_single_sample(self, exercise: Exercise, player: Player, major_earned: Counter[Player],
                                minor_earned: Counter[Player]) -> MoneySample:
        """ Extract the Money Sample related to a given player from a given exercise.

        Arguments:
            exercise (Exercise): The exercise from which the Money Sample is extracted.
            player (Player): The player from which the Money Sample is extracted.
            major_earned (Counter[Player]): The normalized major amount of money earned by players.
            minor_earned (Counter[Player]): The normalized minor amount of money earned by players.

        Returns:
            The Money Sample of this player from this exercise.
        """
        major_other_earned = [major_earned[p] for p in exercise.alive if p != player]
        minor_other_earned = [minor_earned[p] for p in exercise.alive if p != player]
        return MoneySample(player, len(exercise.alive), major_earned[player], major_other_earned, minor_earned[player],
                           minor_other_earned)