from WikiWordLayer.DataPredictors.DataPredictor import DataPredictor
import math

class Cossim_Predictor(DataPredictor):
    def __init__(self, score_lowerbound, exponent, min_probability):
        """ The Cosine Similarity Predictor predicts which candidate is the Mol based how similar a candidate is to
        the candidates in the train data and then it takes a weighted sum based on the similarity.
        Arguments:
            score_lowerbound (int): If the sum of the numberic vector (number of words from jobs occuring in the
            wiki page of the candidate) of a candidate is lower than this value then it is excluded from the
            training data and for the predict data it gets the lowest likelihood of being the Mol.
            exponent (float): When the exponent is set higher then closer neighbours have a larger weight. If the
            value is set lower then the likelihoods for the candidates of being the Mol are closer to each other.
            min_probability (float): The least possible likelihood of being the Mol. Candidates with a lower
            likelihood will have their likelihood increased to this value. """
        self.score_lowerbound = score_lowerbound
        self.exponent = exponent
        self.min_probability = min_probability

    def train(self, train_input, train_output):
        self.train_input = train_input
        self.train_output = train_output
        self.train_candidates = set()

        for c, numeric in train_input.items():
            if self.satisfies_treshold(numeric):
                self.train_candidates.add(c)

    def predict(self, predict_input):
        # Set the weighted score for every candidate
        predict_output = dict()
        for c, numeric in predict_input.items():
            score = 0
            if self.satisfies_treshold(numeric):
                for c2 in self.train_candidates:
                    similarity = self.cos_sim(numeric, self.train_input[c2])
                    score += pow(similarity, self.exponent) * self.train_output[c2]
            predict_output[c] = score

        # Increase the score of all candidates by the same value such that every candidate has at least min_chance of
        # being the Mole
        lowest = math.inf
        sum = 0
        num_candidates = 0
        for _, score in predict_output.items():
            lowest = min(score, lowest)
            sum += score
            num_candidates += 1

        lowest_chance = lowest / sum
        if lowest_chance < self.min_probability:
            add_val = (lowest - self.min_probability * sum) / (num_candidates * self.min_probability - 1)
            for c in predict_output:
                predict_output[c] += add_val

        return predict_output

    def satisfies_treshold(self, numeric):
        """ Checks whether a numeric value sums up to at least the score lowerbound """
        total = sum(numeric)
        return total >= self.score_lowerbound

    def cos_sim(self, x, y):
        """ Determines the cosinus similarity between vectors x and y. It is equal to 1.0 if the ratio between the
        numbers of both numberic vectors is the same. It is 0.0 if there is no similarity and -1.0 if it has an
        opposite ratio (which does not occur, because all numbers are positive). """
        mixed = 0
        x_sum = 0
        y_sum = 0

        for v, v2 in zip(x, y):
            mixed += v * v2
            x_sum += pow(v, 2)
            y_sum += pow(v2, 2)

        x_sum = math.sqrt(x_sum)
        y_sum = math.sqrt(y_sum)
        return mixed / (x_sum * y_sum)