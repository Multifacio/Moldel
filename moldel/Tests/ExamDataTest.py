from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Exams.All import EXAM_DATA
import unittest

class MLERegressionTest(unittest.TestCase):
    """ Check the Exam Data for inconsistencies. """

    def test_players_in_correct_season(self):
        """ Check if all players in the exam data are put in the right season. """
        for season, season_data in EXAM_DATA.items():
            self.assertTrue(self.players_from_season(season_data.players, season),
                            "Player of the wrong season included in the player list of season " + str(season))
            for episode, episode_data in season_data.episodes.items():
                self.assertTrue(self.players_from_season(episode_data.players, season),
                                "Player of the wrong season included in the player list of episode "
                                + str(episode) + " season " + str(season))

    def test_questions(self):
        """ Check if every question is a partitioning of the player, which means that:

            - Every player from that episode is included in at least 1 question answer.
            - Every player from that episode is included in at most 1 question answer.
        """
        for season, season_data in EXAM_DATA.items():
            for episode, episode_data in season_data.episodes.items():
                for question, question_data in episode_data.questions.items():
                    self.assertTrue(self.question_is_partition(episode_data.players, question_data),
                                    "Question " + str(question) + " of season " + str(season) + " episode "
                                    + str(episode) + " is not a partition.")

    def test_result(self):
        """ Check if the drop of players from the result are also contained in the episode. Moreover check if the
        number of players in the drop list matches the DropType. """
        for season, season_data in EXAM_DATA.items():
            for episode, episode_data in season_data.episodes.items():
                contains = all([player in episode_data.players for player in episode_data.result.players])
                self.assertTrue(contains, "Season " + str(season) + " episode " + str(episode) + " contains a player"
                                + " in the result list which did not participate in that episode.")
                self.droptype_matches_list(season, episode, episode_data)

    def test_input(self):
        """ Check if the test input of an episode for the following things:

            - Every player in the test input list indeed participated in that episode.
            - No player used both jokers and immunity (which makes no sense to do).
            - Every question in the question list is at least answered by 1 player and players only answered existing
              questions.
            - Every player gave a valid answer on his question (e.g. you can never answer 4 if the question only
              contains 3 answers). """
        for season, season_data in EXAM_DATA.items():
            for episode, episode_data in season_data.episodes.items():
                contains = all([player in episode_data.players for player in episode_data.input])
                self.assertTrue(contains, "Season " + str(season) + " episode " + str(episode) + " contains a player"
                                + " in the result list which did not participate in that episode.")
                self.not_joker_immunity(season, episode, episode_data)
                self.every_question_answered(season, episode, episode_data)
                self.check_valid_answers(season, episode, episode_data)

    def droptype_matches_list(self, season, episode, episode_data):
        dropType = episode_data.result.drop
        dropPlayers = episode_data.result.players
        if dropType == DropType.EXECUTION_DROP or dropType == DropType.POSSIBLE_DROP or \
                dropType == DropType.POSSIBLE_DROP:
            self.assertTrue(len(dropPlayers) > 0, "The result list of players for season " + str(season)
                            + " episode " + str(episode) + " is empty, which does not match with the dropType"
                            + " used.")
        elif dropType == DropType.NO_DROP_NOR_SCREENS:
            self.assertTrue(len(dropPlayers) == 0, "The result list of players for season " + str(season)
                            + " episode " + str(episode) + " should be empty, because nobody dropped off and "
                            + " there is no information about who should have been dropped off.")

    def not_joker_immunity(self, season, episode, episode_data):
        for player, test_input in episode_data.input.items():
            self.assertTrue(test_input.jokers == 0 or not test_input.immunity, "Player " + player.value.name + " in"
                            + " season " + str(season) + " episode " + str(episode) + " had immunity but also used"
                            + " jokers.")

    def every_question_answered(self, season, episode, episode_data):
        included_questions = episode_data.questions.keys()
        answered_questions = set()
        for player, testInput in episode_data.input.items():
            answered_questions.update(testInput.answers.keys())
        self.assertTrue(answered_questions == included_questions, "The questions included in episode " + str(episode)
                        + " of season " + str(season) + "  do not match with the questions that are answered by the"
                        + " players. ")

    def check_valid_answers(self, season, episode, episode_data):
        for player, testInput in episode_data.input.items():
            for question_num, answer_num in testInput.answers.items():
                self.assertTrue(answer_num in episode_data.questions[question_num].answers.keys(),
                                "Player " + player.value.name + " did not give a valid answer on question "
                                + str(question_num) + " in episode " + str(episode) + " of season " + str(season))

    @staticmethod
    def question_is_partition(episode_players, question):
        question_players = []
        for players_in_answer in question.answers.values():
            question_players.extend(players_in_answer)
        question_players_set = set(question_players)
        return set(episode_players) == question_players_set and len(question_players) == len(question_players_set)

    @staticmethod
    def players_from_season(players, season):
        for player in players:
            if player.value.season != season:
                return False
        return True

if __name__ == '__main__':
    unittest.main()

