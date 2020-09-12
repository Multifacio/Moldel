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

# Aflevering 2 (afvaller: Annette)
# 6 - Tijdens de Seinopdracht zat de Mol in:
# 1: Edo, Regina; 2: Dennis, Patrick; 3: Coen, Dunya, Georgina, Joris; 4: Annette;
# Antwoorden: Patrick (6, 3), Regina (2 jokers)
players2 = [Player.ANNETTE_8, Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.GEORGINA_8,
            Player.JORIS_8, Player.PATRICK_8, Player.REGINA_8]
question2_6 = Question({1: [Player.EDO_8, Player.REGINA_8],
                        2: [Player.DENNIS_8, Player.PATRICK_8],
                        3: [Player.COEN_8, Player.DUNYA_8, Player.GEORGINA_8, Player.JORIS_8],
                        4: [Player.ANNETTE_8]})
result2 = Result(DropType.EXECUTION_DROP, [Player.ANNETTE_8])
episode2 = Episode(players2, result2,
                   {Player.PATRICK_8: TestInput({6: 3}), Player.REGINA_8: TestInput(jokers = 2)},
                   {6: question2_6})

# Aflevering 3 (afvaller: Georgina)
# 13 - Is de Mol tijdens de Maisveldopdracht gevangen door een jager:
# 1: Coen, Dennis, Dunya, Regina; 2: Edo, Georgina, Joris, Patrick;
# Antwoorden: Edo (13, 1), Regina (1 joker), Joris (2 jokers)
players3 = [Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.GEORGINA_8, Player.JORIS_8,
            Player.PATRICK_8, Player.REGINA_8]
question3_13 = Question({1: [Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.REGINA_8],
                         2: [Player.EDO_8, Player.GEORGINA_8, Player.JORIS_8, Player.PATRICK_8]})
result3 = Result(DropType.EXECUTION_DROP, [Player.GEORGINA_8])
episode3 = Episode(players3, result3,
                   {Player.EDO_8: TestInput({13: 1}), Player.REGINA_8: TestInput(jokers = 1),
                    Player.JORIS_8: TestInput(jokers = 2)},
                   {13: question3_13})

# Aflevering 4 (afvaller: Coen)
players4 = [Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.JORIS_8, Player.PATRICK_8,
            Player.REGINA_8]
result4 = Result(DropType.EXECUTION_DROP, [Player.COEN_8])
episode4 = Episode(players4, result4, dict(), dict())

# Aflevering 5 (afvaller: Joris)
# 20 - Wie is de Mol:
# 1: Dennis; 2: Dunya; 3: Edo; 4: Joris; 5: Patrick; 6: Regina;
# Antwoorden: Patrick (20, 2), Dunya (20, 5), Dennis (20, 5), Edo (20, 5), Regina (20, 3)
players5 = [Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.JORIS_8, Player.PATRICK_8, Player.REGINA_8]
result5 = Result(DropType.EXECUTION_DROP, [Player.JORIS_8])
question5_20 = Question({1: [Player.DENNIS_8], 2: [Player.DUNYA_8], 3: [Player.EDO_8], 4: [Player.JORIS_8],
                         5: [Player.PATRICK_8], 6: [Player.REGINA_8]})
episode5 = Episode(players5, result5,
                   {Player.PATRICK_8: TestInput({20: 2}), Player.DUNYA_8: TestInput({20: 5}),
                    Player.DENNIS_8: TestInput({20: 5}), Player.EDO_8: TestInput({20: 5}),
                    Player.REGINA_8: TestInput({20: 3})},
                   {20: question5_20})

# Aflevering 6 (afvaller: Joris)
# 20 - Wie is de Mol:
# 1: Dennis; 2: Dunya; 3: Edo; 4: Joris; 5: Patrick; 6: Regina;
# Antwoorden: Edo (20, 5)
players6 = [Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.JORIS_8, Player.PATRICK_8, Player.REGINA_8]
result6 = Result(DropType.EXECUTION_DROP, [Player.JORIS_8])
question6_20 = Question({1: [Player.DENNIS_8], 2: [Player.DUNYA_8], 3: [Player.EDO_8], 4: [Player.JORIS_8],
                         5: [Player.PATRICK_8], 6: [Player.REGINA_8]})
episode6 = Episode(players6, result6,
                   {Player.EDO_8: TestInput({20: 5})},
                   {20: question6_20})

# Aflevering 7 (afvaller: Dunya)
# 20 - Wie is de Mol:
# 1: Dennis; 2: Dunya; 3: Edo; 4: Patrick; 5: Regina;
# Antwoorden: Patrick (Vrijstelling), Dunya (20, 4)
players7 = [Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.PATRICK_8, Player.REGINA_8]
result7 = Result(DropType.EXECUTION_DROP, [Player.DUNYA_8])
question7_20 = Question({1: [Player.DENNIS_8], 2: [Player.DUNYA_8], 3: [Player.EDO_8], 4: [Player.PATRICK_8],
                         5: [Player.REGINA_8]})
episode7 = Episode(players7, result7,
                   {Player.DUNYA_8: TestInput({20: 4})},
                   {20: question7_20})

# Aflevering 8 (afvaller: Patrick)
# 20 - Wie is de Mol:
# 1: Dennis; 2: Edo; 3: Patrick; 4: Regina;
# Antwoorden: Edo (20, 3)
players8 = [Player.DENNIS_8, Player.EDO_8, Player.PATRICK_8, Player.REGINA_8]
result8 = Result(DropType.EXECUTION_DROP, [Player.PATRICK_8])
question8_20 = Question({1: [Player.DENNIS_8], 2: [Player.EDO_8], 3: [Player.PATRICK_8], 4: [Player.REGINA_8]})
episode8 = Episode(players8, result8,
                   {Player.EDO_8: TestInput({20: 3})},
                   {20: question8_20})

# Aflevering 9 (afvaller: Regina) (pas in de reunie bekend)
players9 = [Player.DENNIS_8, Player.EDO_8, Player.REGINA_8]
result9 = Result(DropType.EXECUTION_DROP, [Player.REGINA_8])
episode9 = Episode(players9, result9, dict(), dict(), num_questions = 40)

season8 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                            8: episode8, 10: episode9})