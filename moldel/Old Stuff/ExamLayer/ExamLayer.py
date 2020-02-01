import math
import random
import numpy
from DistributionTransformers.NormalizeTransformer import NormalizeTransformer
from ExamLayer.Data.Data import EXAM_DATA
from ExamLayer.Regression.GuessRegression import GuessRegression
from Layer import Layer, DataError

class ExamLayer(Layer):
    """ A Probability Distribution that is based on what the candidates answer on the 'Test' and how much 'Jokers' they use
     or whether they use a 'Vrijstelling'. Then a prediction about the 'Mol' is made based on which candidate dropped off. """

    def __init__(self, num_runs, strict, enable_guess_regression):
        """ Create an Exam Layer class.
        Arguments:
            num_runs (int): How often a Monte-Carlo simulation is executed (a higher number means a higher accuracy,
            but also a higher running time)
        """
        self.num_runs = num_runs
        self.strict = strict
        self.enable_guess_regression = enable_guess_regression

    def compute_distribution(self, season, episode):
        """ Performs a simulation based on how the questions are filled in """
        if season not in EXAM_DATA:
            raise DataError("Exam Layer - Missing data season " + str(season))
        players = EXAM_DATA[season][0]
        episodes = self.load_episodes(season, episode)
        dropped = self.dropped_off(episodes) # Compute the list of players dropped of so far for efficiency
        guess_reg = GuessRegression()
        guess_reg.train(season, self.strict)
        mol_prob = dict()
        for mol in players:
            if mol in dropped:
                prob = 0.0
            else:
                prob = 1.0
                for e, episode_data in episodes:
                    prob *= self.episode_simulate(e, episode_data, guess_reg, mol)
            mol_prob[mol] = prob
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(mol_prob)

    def load_episodes(self, season, episode):
        if episode is None:
            episode = max(EXAM_DATA[season][1].keys())
        episodes = list()
        for e, data in EXAM_DATA[season][1].items():
            if e <= episode:
                episodes.append((e, data))
        return episodes

    def dropped_off(self, episodes):
        """ Compute the list of players that dropped off """
        dropped = list()
        for _, episode in episodes:
            result = episode.result
            if result.drop:
                dropped.extend(result.players)
        return dropped

    def episode_simulate(self, episode_num, episode_data, guess_reg, mol):
        """ Simulate the episode and determine the probability that the drop condition is satisfied """
        precomp = self.episode_precomputation(episode_num, episode_data, guess_reg, mol)
        immunity = self.get_immunity(episode_data, mol)

        good_runs = 0
        for _ in range(self.num_runs):
            good_runs += self.single_simulate_episode(episode_data, immunity, precomp)
        return good_runs / self.num_runs

    def episode_precomputation(self, episode_num, episode_data, guess_reg, mol):
        """ Do the precomputations used for the simulation (to make the simulations run faster). This method will
        precompute the score (number of questions already answered correctly + number of jokers used) and the
        answer_probs (the probabilities for the players to answer the visible question correctly by doing a random
        guess) for every candidate. It will return a dictionary with as key the candidates and as value a tuple
        consisting of a score (integer) and the list of answer_probabilities (floats). """
        precomp = dict()
        questions = episode_data.visible_questions
        for p in episode_data.players:
            if p == mol:
                continue
            score = episode_data.test_inputs[p].jokers
            answer_probs = []
            answered_questions = episode_data.test_inputs[p].answered_questions
            for qid, question in questions.items():
                if qid in answered_questions:
                    # In case the player answered the question, check whether the Mol is covered by the answer
                    option = answered_questions[qid]
                    covered = question.options[option]
                    if mol in covered:
                        score += 1
                else:
                    # In case the player did not answer the question, then check how likely the player will pick the
                    # answer according to the guess regression if the guess regression is enabled. Otherwise the
                    # probability is equal to a random pick.
                    option = question.option_for_player(mol)
                    covered = question.options[option][:]
                    if p in covered:
                        covered.remove(p)
                    if self.enable_guess_regression:
                        answer_probs.append(guess_reg.predict_known(episode_num, episode_data, qid))
                    else:
                        answer_probs.append(len(covered) / (len(episode_data.players) - 1))
            if self.enable_guess_regression:
                unknown_guess_prob = guess_reg.predict_unknown(episode_num, episode_data)
            else:
                unknown_guess_prob = 1 / (len(episode_data.players) - 1)
            precomp[p] = (score, answer_probs, unknown_guess_prob)
        return precomp

    def get_immunity(self, episode, mol):
        """ Get the set of all players that have immunity during the exam of an episode (either the Mol or someone
        with a "Vrijstelling"). """
        immunity = {mol}
        for p, ti in episode.test_inputs.items():
            if ti.immunity:
                immunity.add(p)
        return immunity

    def single_simulate_episode(self, episode, immunity, precomp):
        """ Do a single simulation of the episode and return 1 if the drop condition is satisfied and 0 if not. """
        player_score = self.simulate_player_score(episode, immunity, precomp)
        player_score.sort(key=lambda x: x[1])
        r = episode.result
        if r.drop:
            # In case player(s) have not survived the test then these player(s) should have the lowest score
            for i in range(len(r.players)):
                drop = player_score[i][0]
                if drop not in r.players:
                    return 0
            return 1
        else:
            # In case all players have survived, because some did not seen their screen. Then the lowest score must
            # occur in the list of player that did not see their screen
            drop = player_score[0][0]
            return 1 if drop in r.players else 0

    def simulate_player_score(self, episode, immunity, precomp):
        """ Do a single simulation of the player scores for the test """
        player_score = list()
        for p in episode.test_inputs:
            # The mol and candidates with a "Vrijstelling" never has to leave the game, so his score is maximal
            if p in immunity:
                player_score.append((p, math.inf))
                continue
            score = precomp[p][0] # The score start with the jokers + already correctly answered questions
            # Simulate the other visible questions with their corresponding probabilities of answering these questions
            # correctly.
            answer_probs = precomp[p][1]
            for prob in answer_probs:
                if random.random() < prob:
                    score += 1
            # The remaining questions (invisible) will be modelled as questions with a seperate answer for each
            # candidate. And can therefore be simulated with a binomial distribution.
            score += numpy.random.binomial(episode.num_invisible_questions, 1 / (len(episode.players) - 1))
            # Score can never exceed the number of questions and will therefore be maximal the number of questions
            score = min(score, episode.num_questions)
            # Influence the score with a random value between 0.0 and 1.0 (so that the order of people with the same
            # score is random) and timing matters when multiple candidates together had the lowest score, so this
            # random values simulates timing
            score += random.random()
            player_score.append((p, score))
        return player_score