import numpy as np
from Candidates import Candidates
from ExamLayer.Data.Data import EXAM_DATA
from ExamLayer.Regression.MLE_Gradient import MLE_Gradient

class GuessRegression:
    """ The Guess Regression predicts how likely a candidate answers a random question correctly. """

    def train(self, season, strict):
        train_seasons = self.get_train_season(season, strict)
        mol_dict = self.get_mol_dict()
        data_points = self.get_data_points(train_seasons, mol_dict)
        known_points = self.filter_data(data_points, True)
        unknown_points = self.filter_data(data_points, False)
        mle_grad = MLE_Gradient()
        self.knownreg_episode, self.knownreg_questprob, self.knownreg_const = mle_grad.gradient_ascend(known_points)
        self.unknownreg_episode, self.unknownreg_candidates, self.unknownreg_const = mle_grad.gradient_ascend(unknown_points)

    def get_train_season(self, predict_season, strict):
        all_seasons = set(EXAM_DATA.keys())
        train_seasons = set()
        for s in all_seasons:
            if strict and s < predict_season:
                train_seasons.add(s)
            elif not strict and s != predict_season:
                train_seasons.add(s)
        return train_seasons

    def predict_known(self, episode_num, episode_data, question_num):
        return self.knownreg_episode * episode_num + self.knownreg_questprob * \
               self.get_question_probability(episode_data, question_num) +  self.knownreg_const

    def predict_unknown(self, episode_num, episode_data):
        return self.unknownreg_episode * episode_num + self.unknownreg_candidates * len(episode_data.players) + \
               self.unknownreg_const

    def filter_data(self, data_points, filter_known_data):
        if filter_known_data:
            return [((tuple[0][0], tuple[0][2], tuple[0][3]), tuple[1]) for tuple in data_points]
        else:
            return [((tuple[0][0], tuple[0][1], tuple[0][3]), tuple[1]) for tuple in data_points]

    def get_data_points(self, train_seasons, mol_dict):
        data_points = []
        for s in train_seasons:
            for e, episode_data in EXAM_DATA[s][1].items():
                if not episode_data.skip_regression:
                    data_points += self.get_episode_data_points(e, episode_data, mol_dict[s])
        return data_points

    def get_episode_data_points(self, e, episode_data, mol):
        data_points = []
        for candidate, test_input in episode_data.test_inputs.items():
            if candidate != mol:
                for question, answer in test_input.answered_questions.items():
                    data_points.append(self.add_data_point(e, episode_data, mol, question, answer))
        return data_points

    def add_data_point(self, e, episode_data, mol, question, answer):
        episode_num = e
        candidate_prob = 1 / (len(episode_data.players) - 1)
        question_prob = self.get_question_probability(episode_data, question)
        answered_correctly = self.answered_correctly(question, answer, episode_data.visible_questions, mol)
        return ((episode_num, candidate_prob, question_prob, 1), answered_correctly)

    def get_question_probability(self, episode_data, question_num):
        prob = 0
        num_players = len(episode_data.players)
        for players in episode_data.visible_questions[question_num].options.values():
            prob += np.math.pow(len(players) / num_players, 2.0)
        return prob

    def answered_correctly(self, question_num, answer, all_questions, mol):
        return mol in all_questions[question_num].options[answer]

    def get_mol_dict(self):
        mol_dict = dict()
        for candidate in Candidates:
            if candidate.value.is_mol:
                mol_dict[candidate.value.season] = candidate
        return mol_dict