from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Nicolette)
# 1 - De Mol is een:
# 1: Coen, Dennis, Edo, Joris, Patrick; 2: Annette, Dunya, Georgina, Nicolette, Regina;
# Antwoorden: Patrick (1, 2), Regina (3 jokers), Joris (2 jokers)
players1 = [Player.ANNETTE_8, Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.GEORGINA_8,
            Player.JORIS_8, Player.NICOLETTE_8, Player.PATRICK_8, Player.REGINA_8]
question1_1 = Question({1: [Player.COEN_8, Player.DENNIS_8, Player.EDO_8, Player.JORIS_8, Player.PATRICK_8],
                        2: [Player.ANNETTE_8, Player.DUNYA_8, Player.GEORGINA_8, Player.NICOLETTE_8, Player.REGINA_8]})
result1 = Result(DropType.EXECUTION_DROP, [Player.NICOLETTE_8])
episode1 = Episode(players1, result1,
                   {Player.PATRICK_8: TestInput({1: 2}), Player.REGINA_8: TestInput(jokers = 3),
                    Player.JORIS_8: TestInput(jokers = 2)},
                   {1: question1_1})

season8 = Season(players1, {1: episode1})