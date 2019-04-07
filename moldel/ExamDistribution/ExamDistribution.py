import math
import random
from ProbabilityDistribution import ProbabilityDistribution, DataError

class ExamDistribution(ProbabilityDistribution):
    """ A Probability Distribution that is based on what the candidates answer on the 'Test' and how much 'Jokers' they use
     or whether they use a 'Vrijstelling'. Then a prediction about the 'Mol' is made based on which candidate dropped off. """

    def __init__(self, data, num_runs, precision):
        """ Performs a simulation based on how the questions are filled in """
        self.data = data
        self.num_runs = num_runs
        self.precision = precision

    def compute_distribution(self, season, episode):
        if season not in self.data:
            raise DataError("Exam Distribution - Missing data season " + str(season))
        players = self.data[season][0]
        episodes = self.load_episodes(season, episode)
        dropped = self.dropped_off(episodes) # Compute the list of players dropped of so far for efficiency
        mol_prob = dict()
        for mol in players:
            if mol in dropped:
                prob = 0.0
            else:
                prob = 1.0
                for e in episodes:
                    prob *= self.episode_simulate(e, mol)
            mol_prob[mol] = prob
        self.normalize(mol_prob, players)
        return mol_prob

    def load_episodes(self, season, episode):
        if episode is None:
            episode = max(self.data[season][1].keys())
        episodes = list()
        for i in range(1, episode + 1):
            if i in self.data[season][1]:
                episodes.append(self.data[season][1][i])
        return episodes

    def dropped_off(self, episodes):
        """ Compute the list of players that dropped off """
        dropped = list()
        for episode in episodes:
            result = episode.result
            if result.drop:
                dropped.extend(result.players)
        return dropped

    def normalize(self, mol_prob, players):
        """ Scale the probabilities such that they sum up to 1.0 """
        total = 0.0
        for p in players:
            total += mol_prob[p]
        for p in players:
            mol_prob[p] = round(mol_prob[p] / total, self.precision)

    def episode_simulate(self, episode, mol):
        """ Simulate the episode and determine the probability that the drop condition is satisfied """
        good_runs = 0
        for i in range(self.num_runs):
            good_runs += self.single_simulate_episode(episode, mol)
        return good_runs / self.num_runs

    def single_simulate_episode(self, episode, mol):
        """ Do a single simulation of the episode and return 1 if the drop condition is satisfied and 0 if not """
        player_score = self.simulate_player_score(episode, mol)
        player_score.sort(key=lambda x: x[1])
        r = episode.result
        if r.drop: # In case player(s) have not survived the test then these player(s) should have the lowest score
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

    def simulate_player_score(self, episode, mol):
        """ Do a single simulation of the player scores for the test """
        player_score = list()
        for p in episode.test_inputs:
            if p == mol: # The mol never has to leave the game, so his score is maximal
                player_score.append((p, math.inf))
                continue
            score = self.simulate_questions(episode, mol, p)
            score += episode.test_inputs[p].jokers
            score = min(score, episode.num_questions)
            # Influence the score with a random value between 0.0 and 1.0 (so that the order of people with the same
            # score is random)
            score += random.random()
            player_score.append((p, score))
        return player_score

    def simulate_questions(self, episode, mol, player):
        """ Simulate the score on the questions for a player """
        score = 0
        questions = episode.questions
        answered_questions = episode.test_inputs[player].answered_questions
        player_choices = episode.players[:] # The other players where the player can fill in a question on
        player_choices.remove(player)
        for q in range(1, len(questions) + 1):
            if q in answered_questions:
                option = answered_questions[q]
            else:
                target = random.choice(player_choices)
                option = questions[q].option_for_player(target)
            covered = questions[q].options[option] # The players that are covered by the option of that question
            if mol in covered:
                score += 1
        return score