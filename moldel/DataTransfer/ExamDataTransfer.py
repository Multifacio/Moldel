from Data.ExamData.Dataclasses.Episode import Episode
from Data.ExamData.Dataclasses.Question import Question
from Data.ExamData.Dataclasses.Result import Result
from Data.ExamData.Dataclasses.TestInput import TestInput, DelayedAnswer
from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from DataTransfer.PlayerDataTransfer import json_player
from Data.PlayerData import get_name, get_season, get_age, get_is_mol
from typing import Any, Dict, List, Union
import json

def json_test_result(result: Result) -> Dict[str, Any]:
    return {"drop_type": result.drop.name,
            "players": [json_player(p) for p in result.players]}

def json_question(question_num: int, question: Question) -> Dict[str, Any]:
    return {"num": question_num,
            "options": [[json_player(p) for p in question.answers[qid]] for qid in sorted(question.answers)]}

def json_answer(question_num: int, answer: Union[int, DelayedAnswer], episode: Episode) -> Dict[str, Any]:
    question = episode.questions[question_num]
    known_from = answer.known_from if isinstance(answer, DelayedAnswer) else episode.id
    answer = question.answers[answer.answer] if isinstance(answer, DelayedAnswer) else question.answers[answer]
    return {"question": json_question(question_num, question),
            "answer": [json_player(p) for p in answer],
            "known_from": known_from}

def json_test_input(player: Player, test_input: TestInput, episode: Episode) -> Dict[str, Any]:
    return {"player": json_player(player),
            "answers": [json_answer(qid, answer, episode) for qid, answer in test_input.answers.items()],
            "immunity": test_input.immunity,
            "jokers": test_input.jokers}

FILE_NAME = "ExamData.json"
data = [{"season": sid,
         "episode": eid,
         "season_players": [json_player(p) for p in season.players],
         "participants": [json_player(p) for p in episode.players],
         "result": json_test_result(episode.result),
         "input": [json_test_input(p, ti, episode) for p, ti in episode.input.items()],
         "questions": [json_question(qid, question) for qid, question in episode.questions.items()],
         "num_questions": episode.num_questions
         }
            for sid, season in EXAM_DATA.items() for eid, episode in season.episodes.items()]

with open("Output/" + FILE_NAME, 'w') as file:
    json.dump(data, file)