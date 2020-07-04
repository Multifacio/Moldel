from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

# Aflevering 1 (afvaller: Marion)
# Vragen:
# 1 - De Mol is een:
# 1: Dio, Frits, Maarten, Tim, William; 2: Anne-Marie, Hadewych, Liesbeth, Marion, Marit;
# 12 - Heeft de Mol de vrijstellingen gevonden tijdens het eerste deel van de gletsjer opdracht:
# 1: Frits; 2: Anne-Marie, Dio, Hadewych, Liesbeth, Maarten, Marion, Marit, Tim, William;
# 13 - Werd de Mol een vrijstelling voor aflevering 3 gegund?
# 1: Marit; 2: Anne-Marie, Dio, Frits, Hadewych, Liesbeth, Maarten, Marion, Tim, William;
# Antwoorden: Liesbeth (12, 1), Maarten (1, 2), Marion (13, 2), Frits (Vrijstelling)
players1 = [Player.ANNE_MARIE_12, Player.DIO_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12,
            Player.MAARTEN_12, Player.MARION_12, Player.MARIT_12, Player.TIM_12, Player.WILLIAM_12]
question1_1 = Question({1: [Player.DIO_12, Player.FRITS_12, Player.MAARTEN_12, Player.TIM_12, Player.WILLIAM_12],
                        2: [Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARION_12,
                            Player.MARIT_12]})
question1_12 = Question({1: [Player.FRITS_12],
                         2: [Player.ANNE_MARIE_12, Player.DIO_12, Player.HADEWYCH_12, Player.LIESBETH_12,
                             Player.MAARTEN_12, Player.MARION_12, Player.MARIT_12, Player.TIM_12, Player.WILLIAM_12]})
question1_13 = Question({1: [Player.MARIT_12],
                         2: [Player.ANNE_MARIE_12, Player.DIO_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12,
                             Player.MAARTEN_12, Player.MARION_12, Player.TIM_12, Player.WILLIAM_12]})
result1 = Result(DropType.EXECUTION_DROP, [Player.MARION_12])
episode1 = Episode(players1, result1,
                   {Player.LIESBETH_12: TestInput({12: 1}), Player.MAARTEN_12: TestInput({1: 2}),
                    Player.MARION_12: TestInput({13: 2}), Player.FRITS_12: TestInput(immunity = True)},
                   {1: question1_1, 12: question1_12, 13: question1_13})

# Aflevering 2 (afvaller: Dio)
# Vragen:
# 5 - Beantwoordde de Mol de vragen over zichzelf goed tijdens de Trapopdracht (Niet bruikbaar)
# 6 - In welke kamer sliep de Mol vannacht (Niet bruikbaar)
# 14 - Wat was het nummerbord van de auto waarin de Mol zat tijdens de Jeepopdracht: (Maarten 2)
# 1: Anne-Marie, Marit, William; 2: Hadewych, Liesbeth, Maarten, Tim; 3: Dio, Frits;
# Antwoorden: Maarten (14, 2), Tim (Vrijstelling)
players2 = [Player.ANNE_MARIE_12, Player.DIO_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12,
            Player.MAARTEN_12, Player.MARIT_12, Player.TIM_12, Player.WILLIAM_12]
question2_14 = Question({1: [Player.ANNE_MARIE_12, Player.MARIT_12, Player.WILLIAM_12],
                         2: [Player.HADEWYCH_12, Player.LIESBETH_12, Player.MAARTEN_12, Player.TIM_12],
                         3: [Player.DIO_12, Player.FRITS_12]})
result2 = Result(DropType.EXECUTION_DROP, [Player.DIO_12])
episode2 = Episode(players2, result2,
                   {Player.MAARTEN_12: TestInput({14: 2}), Player.TIM_12: TestInput(immunity = True)},
                   {14: question2_14})

# Aflevering 3 (afvaller: Maarten)
# Vragen:
# 1 - De Mol is een:
# 1: Frits, Maarten, Tim, William; 2: Anne-Marie, Hadewych, Liesbeth, Marit;
# 4 - In welk team zat de Mol tijdens de Riverjetopdracht:
# 1: Anne-Marie, Maarten, Tim; 2: Frits, Liesbeth, William; 3: Hadewych, Marit;
# 10 - Wat pakte de Mol tijdens de Jokeropdracht:
# 1: Anne-Marie, Hadewych, Liesbeth, Maarten; 2: Frits; 3: Marit, Tim; 4: William;
# 15 - Tijdens de rondleidingsopdracht zat de Mol in een groep van:
# 1: Maarten, Marit; 2: Anne-Marie, Frits, Hadewych, Liesbeth, Tim, William;
# Antwoorden: Marit (vrijstelling), Tim (4, 2), Hadewych (15, 2) (1 joker), Frits (10, 1), Liesbeth (1, 2) (1 joker),
# Maarten (1 joker)
players3 = [Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MAARTEN_12,
            Player.MARIT_12, Player.TIM_12, Player.WILLIAM_12]
question3_1 = Question({1: [Player.FRITS_12, Player.MAARTEN_12, Player.TIM_12, Player.WILLIAM_12],
                        2: [Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12]})
question3_4 = Question({1: [Player.ANNE_MARIE_12, Player.MAARTEN_12, Player.TIM_12],
                        2: [Player.FRITS_12, Player.LIESBETH_12, Player.WILLIAM_12],
                        3: [Player.HADEWYCH_12, Player.MARIT_12]})
question3_10 = Question({1: [Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MAARTEN_12],
                         2: [Player.FRITS_12],
                         3: [Player.MARIT_12, Player.TIM_12],
                         4: [Player.WILLIAM_12]})
question3_15 = Question({1: [Player.MAARTEN_12, Player.MARIT_12],
                         2: [Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12,
                             Player.TIM_12, Player.WILLIAM_12]})
result3 = Result(DropType.EXECUTION_DROP, [Player.MAARTEN_12])
episode3 = Episode(players3, result3,
                   {Player.MARIT_12: TestInput(immunity = True), Player.TIM_12: TestInput({4: 2}),
                    Player.HADEWYCH_12: TestInput({15: 2}, jokers = 1), Player.FRITS_12: TestInput({10: 1}),
                    Player.LIESBETH_12: TestInput({1: 2}, jokers = 1), Player.MAARTEN_12: TestInput(jokers = 1)},
                   {1: question3_1, 4: question3_4, 10: question3_10, 15: question3_15})

# Aflevering 4 (geen afvaller, alleen Anne-Marie, Hadewych, Liesbeth, Tim en Frits kregen hun scherm te zien)
# Vragen:
# 2 - Had de Mol voor aanvang van deze test nog een joker in bezit:
# 1: Anne-Marie, Frits; 2: Hadewych, Liesbeth, Marit, Tim, William;
# 5 - Waar stond de Mol op de groepsfoto van aflevering 3:
# 1: Anne-Marie, Hadewych, Liesbeth, Tim; 2: Frits, Marit, William;
# 7 - Hoe vaak zat de Mol op de tandem tijdens de munitie-opdracht:
# 1: Anne-Marie, Hadewych, Liesbeth, Tim; 2: Frits, Marit, William; 3: -;
# 10 - Is de Mol eigenaar van een huis? (Niet bruikbaar)
# Antwoorden: William (5, 1), Liesbeth (7, 1), Marit (2, 2)
players4 = [Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12,
            Player.TIM_12, Player.WILLIAM_12]
question4_2 = Question({1: [Player.ANNE_MARIE_12, Player.FRITS_12],
                        2: [Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12, Player.TIM_12, Player.WILLIAM_12]})
question4_5 = Question({1: [Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.TIM_12],
                        2: [Player.FRITS_12, Player.MARIT_12, Player.WILLIAM_12]})
question4_7 = Question({1: [Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.TIM_12],
                        2: [Player.FRITS_12, Player.MARIT_12, Player.WILLIAM_12],
                        3: []})
result4 = Result(DropType.POSSIBLE_DROP, [Player.MARIT_12, Player.WILLIAM_12])
episode4 = Episode(players4, result4,
                   {Player.WILLIAM_12: TestInput({5: 1}), Player.LIESBETH_12: TestInput({7: 1}),
                    Player.MARIT_12: TestInput({2: 2})},
                   {2: question4_2, 5: question4_5, 7: question4_7})

# Aflevering 5 (afvaller: Marit)
# Vragen:
# 5 - Als de stewardess in het vliegtuig met haar rug tegen de cockpit aanstond, zag zij de Mol:
# 1: Hadewych, Marit, Tim; 2: Anne-Marie, Frits, Liesbeth, William;
# 7 - Heeft de Mol meerdere molboekjes (Niet bruikbaar)
# 11 - Wat verdiende de Mol bij de Western-opdracht:
# 1: Hadewych; 2: William; 3: Frits; 4: Anne-Marie, Liesbeth, Marit, Tim;
# 12 - Kreeg de Mol een herkansing bij de Western-opdracht:
# 1: Anne-Marie; 2: Frits, Hadewych, Liesbeth, Marit, Tim; 3: William;
# 18 - Heeft het team van de Mol een testvraag gevonden tijdens de Kasteel-opdracht:
# 1: Frits, Marit, William; 2: Anne-Marie, Tim; 3: Hadewych, Liesbeth;
# Antwoorden: William (5, 1), Anne-Marie (11, 4), Tim (12, 1), Hadewych (1 joker), Liesbeth (18, 2), Frits (11, 4) (1 joker)
players5 = [Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12,
            Player.TIM_12, Player.WILLIAM_12]
question5_5 = Question({1: [Player.HADEWYCH_12, Player.MARIT_12, Player.TIM_12],
                        2: [Player.ANNE_MARIE_12, Player.FRITS_12, Player.LIESBETH_12, Player.WILLIAM_12]})
question5_11 = Question({1: [Player.HADEWYCH_12],
                         2: [Player.WILLIAM_12],
                         3: [Player.FRITS_12],
                         4: [Player.ANNE_MARIE_12, Player.LIESBETH_12, Player.MARIT_12, Player.TIM_12]})
question5_12 = Question({1: [Player.ANNE_MARIE_12],
                         2: [Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12, Player.TIM_12],
                         3: [Player.WILLIAM_12]})
question5_18 = Question({1: [Player.FRITS_12, Player.MARIT_12, Player.WILLIAM_12],
                         2: [Player.ANNE_MARIE_12, Player.TIM_12],
                         3: [Player.HADEWYCH_12, Player.LIESBETH_12]})
result5 = Result(DropType.EXECUTION_DROP, [Player.MARIT_12])
episode5 = Episode(players5, result5,
                   {Player.WILLIAM_12: TestInput({5: 1}), Player.ANNE_MARIE_12: TestInput({11: 4}),
                    Player.TIM_12: TestInput({12: 1}), Player.HADEWYCH_12: TestInput(jokers = 1),
                    Player.LIESBETH_12: TestInput({18: 2}), Player.FRITS_12: TestInput({11: 4}, jokers = 1)},
                   {5: question5_5, 11: question5_11, 12: question5_12, 18: question5_18})

# Aflevering 6 (afvaller: Frits)
# Vragen:
# 1 - Wie is de Mol:
# 1: Anne-Marie; 2: Frits; 3: Hadewych; 4: Liesbeth; 5: Tim; 6: William;
# 2 - Wat is de voornaam van de moeder van de Mol? (Niet bruikbaar)
# 6 - Tijdens de Boogschiet-opdracht zat de Mol in het:
# 1: Anne-Marie, Hadewych, Tim, William; 2: Frits, Liesbeth;
# 11 - Is de Mol de penningmeester:
# 1: Frits; 2: Anne-Marie, Hadewych, Liesbeth, Tim, William;
# 12 - Bediende de Mol de porto vanuit de controlroom tijdens de Lichtopdracht:
# 1: Frits, Hadewych; 2: Anne-Marie, Liesbeth, Tim, William;
# 20 - Wie is de Mol:
# 1: Anne-Marie; 2: Frits; 3: Hadewych; 4: Liesbeth; 5: Tim; 6: William;
# Antwoorden: Hadewych (1, 4), Frits (11, 2), Anne-Marie (20, 5), William (12, 1), Tim (6, 2)
players6 = [Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.TIM_12,
            Player.WILLIAM_12]
question6_1 = Question({1: [Player.ANNE_MARIE_12], 2: [Player.FRITS_12], 3: [Player.HADEWYCH_12],
                        4: [Player.LIESBETH_12], 5: [Player.TIM_12], 6: [Player.WILLIAM_12]})
question6_6 = Question({1: [Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.TIM_12, Player.WILLIAM_12],
                        2: [Player.FRITS_12, Player.LIESBETH_12]})
question6_11 = Question({1: [Player.FRITS_12],
                         2: [Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.TIM_12,
                             Player.WILLIAM_12]})
question6_12 = Question({1: [Player.FRITS_12, Player.HADEWYCH_12],
                         2: [Player.ANNE_MARIE_12, Player.LIESBETH_12, Player.TIM_12, Player.WILLIAM_12]})
question6_20 = Question({1: [Player.ANNE_MARIE_12], 2: [Player.FRITS_12], 3: [Player.HADEWYCH_12],
                         4: [Player.LIESBETH_12], 5: [Player.TIM_12], 6: [Player.WILLIAM_12]})
result6 = Result(DropType.EXECUTION_DROP, [Player.FRITS_12])
episode6 = Episode(players6, result6,
                   {Player.HADEWYCH_12: TestInput({1: 4}), Player.FRITS_12: TestInput({11: 2}),
                    Player.ANNE_MARIE_12: TestInput({20: 5}), Player.WILLIAM_12: TestInput({12: 1}),
                    Player.TIM_12: TestInput({6: 2})},
                   {1: question6_1, 6: question6_6, 11: question6_11, 12: question6_12, 20: question6_20})

# Aflevering 7 (afvaller: William)
# Vragen:
# 1 - Wie is de Mol:
# 1: Anne-Marie; 2: Hadewych; 3: Liesbeth; 4: Tim; 5: William;
# 2 - Heeft de Mol een joker met potgeld betaald:
# 1: Hadewych; 2: Anne-Marie, Liesbeth, Tim, William;
# 18 - Van welk kunstwerk maakte de Mol een 3d-variant:
# 1: Anne-Marie, William; 2: Hadewych, Liesbeth; 3: Tim;
# Antwoorden: Liesbeth (1, 1), William (2, 2), Anne-Marie (18, 3), Tim (1, 1)
players7 = [Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.TIM_12, Player.WILLIAM_12]
question7_1 = Question({1: [Player.ANNE_MARIE_12], 2: [Player.HADEWYCH_12], 3: [Player.LIESBETH_12],
                        4: [Player.TIM_12], 5: [Player.WILLIAM_12]})
question7_2 = Question({1: [Player.HADEWYCH_12],
                        2: [Player.ANNE_MARIE_12, Player.LIESBETH_12, Player.TIM_12, Player.WILLIAM_12]})
question7_18 = Question({1: [Player.ANNE_MARIE_12, Player.WILLIAM_12],
                         2: [Player.HADEWYCH_12, Player.LIESBETH_12],
                         3: [Player.TIM_12]})
result7 = Result(DropType.EXECUTION_DROP, [Player.WILLIAM_12])
episode7 = Episode(players7, result7,
                   {Player.LIESBETH_12: TestInput({1: 1}), Player.WILLIAM_12: TestInput({2: 2}),
                    Player.ANNE_MARIE_12: TestInput({18: 3}), Player.TIM_12: TestInput({1: 1})},
                   {1: question7_1, 2: question7_2, 18: question7_18})

# Aflevering 8 (afvaller: Tim)
# Vragen:
# 6 - Wat droeg de Mol tijdens de Plaza de Espana opdracht:
# 1: Anne-Marie, Tim; 2: Hadewych; 3: Liesbeth;
# 11 - Hoeveel geld bracht de Mol in de pot tijdens aflevering 8:
# 1: Anne-Marie, Liesbeth; 2: Hadewych; 3: Tim;
# 18 - Als hoeveelste ging de Mol tijdens het Labyrintspel:
# 1: Tim; 2: Liesbeth; 3: Hadewych; 4: Anne-Marie;
# Antwoorden: Anne-Marie (Vrijstelling), Tim (11, 1), Hadewych (6, 1), Liesbeth (18, 4)
players8 = [Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.TIM_12]
question8_6 = Question({1: [Player.ANNE_MARIE_12, Player.TIM_12],
                        2: [Player.HADEWYCH_12],
                        3: [Player.LIESBETH_12]})
question8_11 = Question({1: [Player.ANNE_MARIE_12, Player.LIESBETH_12],
                         2: [Player.HADEWYCH_12],
                         3: [Player.TIM_12]})
question8_18 = Question({1: [Player.TIM_12], 2: [Player.LIESBETH_12], 3: [Player.HADEWYCH_12],
                         4: [Player.ANNE_MARIE_12]})
result8 = Result(DropType.EXECUTION_DROP, [Player.TIM_12])
episode8 = Episode(players8, result8,
                   {Player.ANNE_MARIE_12: TestInput(immunity = True), Player.TIM_12: TestInput({11: 1}),
                    Player.HADEWYCH_12: TestInput({6: 1}), Player.LIESBETH_12: TestInput({18: 4})},
                   {6: question8_6, 11: question8_11, 18: question8_18})

season12 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                             8: episode8})