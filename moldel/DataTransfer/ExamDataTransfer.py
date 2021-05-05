from Data.ExamData.Dataclasses.DropType import DropType
from Data.ExamData.Dataclasses.Episode import Episode
from Data.ExamData.Dataclasses.Question import Question
from Data.ExamData.Dataclasses.Result import Result
from Data.ExamData.Dataclasses.TestInput import TestInput, DelayedAnswer
from Data.ExamData.Exams.All import EXAM_DATA
from Data.Player import Player
from Data.PlayerData import get_name, get_season, get_age, get_is_mol
from typing import Any, Dict, List, Union
import json
import math

def json_player(player: Player, drop_mapping: Dict[Player, List[Any]]) -> Dict[str, Any]:
    return {"id": player.value, "name": get_name(player), "season": get_season(player), "is_mol": get_is_mol(player),
            "age": get_age(player), "drops": drop_mapping.get(player, [])}

def json_test_result(result: Result, drop_mapping: Dict[Player, List[Dict[str, Any]]]) -> Dict[str, Any]:
    return {"drop_type": result.drop.name,
            "players": [json_player(p, drop_mapping) for p in result.players]}

def json_question(question_num: int, question: Question, drop_mapping: Dict[Player, List[Dict[str, Any]]]) \
        -> Dict[str, Any]:
    return {"num": question_num,
            "options": [[json_player(p, drop_mapping) for p in question.answers[qid]]
                        for qid in sorted(question.answers)]}

def json_answer(question_num: int, answer: Union[int, DelayedAnswer], episode: Episode,
                drop_mapping: Dict[Player, List[Dict[str, Any]]]) -> Dict[str, Any]:
    question = episode.questions[question_num]
    known_from = answer.known_from if isinstance(answer, DelayedAnswer) else episode.id
    answer = question.answers[answer.answer] if isinstance(answer, DelayedAnswer) else question.answers[answer]
    return {"question": json_question(question_num, question, drop_mapping),
            "answer": [json_player(p, drop_mapping) for p in answer],
            "known_from": known_from}

def json_test_input(player: Player, test_input: TestInput, episode: Episode,
                    drop_mapping: Dict[Player, List[Dict[str, Any]]]) -> Dict[str, Any]:
    return {"player": json_player(player, drop_mapping),
            "answers": [json_answer(qid, answer, episode, drop_mapping) for qid, answer in test_input.answers.items()],
            "immunity": test_input.immunity,
            "jokers": test_input.jokers}

def json_drop_mapping():
    execution_drops = dict()
    voluntary_drops = dict()
    for season in EXAM_DATA.values():
        execution_drops.update(season.get_drop_mapping(DropType.EXECUTION_DROP, math.inf))
        voluntary_drops.update(season.get_drop_mapping(DropType.VOLUNTARY_DROP, math.inf))

    drop_mapping = {player: [{"drop_type": "EXECUTION_DROP", "episode": episode.id} for episode in episodes]
                    for player, episodes in execution_drops.items()}
    for player, episodes in voluntary_drops.items():
        drop_mapping[player] = drop_mapping.get(player, []) + [{"drop_type": "VOLUNTARY_DROP", "episode": episode.id}
                                                                for episode in episodes]
    return drop_mapping

FILE_NAME = "ExamData.json"

drop_mapping = json_drop_mapping()
data = [{"season": sid,
         "episode": eid,
         "season_players": [json_player(p, drop_mapping) for p in season.players],
         "participants": [json_player(p, drop_mapping) for p in episode.players],
         "result": json_test_result(episode.result, drop_mapping),
         "input": [json_test_input(p, ti, episode, drop_mapping) for p, ti in episode.input.items()],
         "questions": [json_question(qid, question, drop_mapping) for qid, question in episode.questions.items()],
         "num_questions": episode.num_questions
         }
            for sid, season in EXAM_DATA.items() for eid, episode in season.episodes.items()]

with open("Output/" + FILE_NAME, 'w') as file:
    json.dump(data, file)