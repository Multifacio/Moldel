from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Loretta)
# 1 - De Mol is een:
# 1: Arjen, Erik, Frits, Manuel, Tim; 2: Barbara, Hind, Kim, Loretta, Sanne;
# 4 - Wat kocht de Mol om zichzelf te symboliseren:
# 1: Barbara; 2: Arjen; 3: Hind; 4: Sanne; 5: Frits; 6: Kim; 7: Tim; 8: Erik; 9: Loretta, Manuel;
# 9 - Waar was de Mol tijdens de Boot-Brug-Helikopter opdracht:
# 1: Arjen, Hind, Kim, Sanne; 2: Barbara, Frits, Loretta, Manuel; 3: Erik, Tim;
# 15 - Gaf George op Schiphol een envelop aan de Mol:
# 1: Sanne; 2: Arjen, Barbara, Erik, Frits, Hind, Kim, Loretta, Manuel, Tim;
# 20 - Wie is de Mol:
# 1: Arjen; 2: Barbara; 3: Erik; 4: Frits; 5: Hind; 6: Kim; 7: Loretta; 8: Manuel; 9: Sanne; 10: Tim;
# Antwoorden: Hind (1, 1), Tim (4, 1), Sanne (9, 3), Manuel (15, 1), Barbara (20, 3)
players1 = [Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10,
            Player.LORETTA_10, Player.MANUEL_10, Player.SANNE_10, Player.TIM_10]
question1_1 = Question({1: [Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10, Player.MANUEL_10, Player.TIM_10],
                        2: [Player.BARBARA_10, Player.HIND_10, Player.KIM_10, Player.LORETTA_10, Player.SANNE_10]})
question1_4 = Question({1: [Player.BARBARA_10], 2: [Player.ARJEN_10], 3: [Player.HIND_10], 4: [Player.SANNE_10],
                        5: [Player.FRITS_10], 6: [Player.KIM_10], 7: [Player.TIM_10], 8: [Player.ERIK_10],
                        9: [Player.LORETTA_10, Player.MANUEL_10]})
question1_9 = Question({1: [Player.ARJEN_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10],
                        2: [Player.BARBARA_10, Player.FRITS_10, Player.LORETTA_10, Player.MANUEL_10],
                        3: [Player.ERIK_10, Player.TIM_10]})
question1_15 = Question({1: [Player.SANNE_10],
                         2: [Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10,
                             Player.KIM_10, Player.LORETTA_10, Player.MANUEL_10, Player.TIM_10]})
question1_20 = Question({1: [Player.ARJEN_10], 2: [Player.BARBARA_10], 3: [Player.ERIK_10], 4: [Player.FRITS_10],
                         5: [Player.HIND_10], 6: [Player.KIM_10], 7: [Player.LORETTA_10], 8: [Player.MANUEL_10],
                         9: [Player.SANNE_10], 10: [Player.TIM_10]})
result1 = Result(DropType.EXECUTION_DROP, [Player.LORETTA_10])
episode1 = Episode(players1, result1,
                   {Player.HIND_10: TestInput({1: 1}), Player.TIM_10: TestInput({4: 1}),
                    Player.SANNE_10: TestInput({9: 3}), Player.MANUEL_10: TestInput({15: 1}),
                    Player.BARBARA_10: TestInput({20: 3})},
                   {1: question1_1, 4: question1_4, 9: question1_9, 15: question1_15, 20: question1_20})

# Aflevering 2 (afvaller: Tim)
# 1 - De Mol is een:
# 1: Arjen, Erik, Frits, Manuel, Tim; 2: Barbara, Hind, Kim, Sanne;
# 5 - Hoeveel kokers vond de Mol tijdens de Tramopdracht:
# 1: Manuel; 2: Barbara, Erik; 3: Arjen, Frits, Hind, Kim, Sanne, Tim;
# 8 - In welke groep zat de Mol tijdens de Tramopdracht:
# 1: Barbara, Frits, Hind; 2: Arjen, Erik, Kim; 3: Manuel, Sanne, Tim;
# 14 - Hoeveel jokers pakte de Mol bij Pieter Jan:
# 1: Frits, Kim, Tim; 2: Erik, Hind, Sanne; 3: Barbara; 4: Arjen, Manuel;
# 18 - Met wie liep de Mol door Holland Village:
# 1: Sanne; 2: Erik; 3: Barbara; 4: Manuel; 5: Tim; 6: Hind; 7: Arjen; 8: Kim; 9: Frits;
# 19 - Was de Mol als laatste aan de beurt in Holland Village:
# 1: Frits; 2: Arjen, Barbara, Erik, Hind, Kim, Manuel, Sanne, Tim;
# Antwoorden: Barbara (1, 2) (2 jokers), Arjen (5, 2), Tim (8, 1) (1 joker), Sanne (14, 1) (2 jokers), Manuel (18, 1),
# Kim (14, 2) (1 joker), Erik (1 joker), Frits (8, 2) (2 jokers), Hind (19, 1) (2 jokers)
players2 = [Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10,
            Player.MANUEL_10, Player.SANNE_10, Player.TIM_10]
question2_1 = Question({1: [Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10, Player.MANUEL_10, Player.TIM_10],
                        2: [Player.BARBARA_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10]})
question2_5 = Question({1: [Player.MANUEL_10],
                        2: [Player.BARBARA_10, Player.ERIK_10],
                        3: [Player.ARJEN_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10, Player.TIM_10]})
question2_8 = Question({1: [Player.BARBARA_10, Player.FRITS_10, Player.HIND_10],
                        2: [Player.ARJEN_10, Player.ERIK_10, Player.KIM_10],
                        3: [Player.MANUEL_10, Player.SANNE_10, Player.TIM_10]})
question2_14 = Question({1: [Player.FRITS_10, Player.KIM_10, Player.TIM_10],
                         2: [Player.ERIK_10, Player.HIND_10, Player.SANNE_10],
                         3: [Player.BARBARA_10],
                         4: [Player.ARJEN_10, Player.MANUEL_10]})
question2_18 = Question({1: [Player.SANNE_10], 2: [Player.ERIK_10], 3: [Player.BARBARA_10], 4: [Player.MANUEL_10],
                         5: [Player.TIM_10], 6: [Player.HIND_10], 7: [Player.ARJEN_10], 8: [Player.KIM_10],
                         9: [Player.FRITS_10]})
question2_19 = Question({1: [Player.FRITS_10],
                         2: [Player.ARJEN_10,Player.BARBARA_10, Player.ERIK_10, Player.HIND_10, Player.KIM_10,
                             Player.MANUEL_10, Player.SANNE_10, Player.TIM_10]})
result2 = Result(DropType.EXECUTION_DROP, [Player.TIM_10])
episode2 = Episode(players2, result2,
                   {Player.BARBARA_10: TestInput({1: 2}, jokers = 2), Player.ARJEN_10: TestInput({5: 2}),
                    Player.TIM_10: TestInput({8: 1}, jokers = 1), Player.SANNE_10: TestInput({14: 1}, jokers = 2),
                    Player.MANUEL_10: TestInput({18: 1}), Player.KIM_10: TestInput({14: 2}, jokers = 1),
                    Player.ERIK_10: TestInput(jokers = 1), Player.FRITS_10: TestInput({8: 2}, jokers = 2),
                    Player.HIND_10: TestInput({19: 1}, jokers = 2)},
                   {1: question2_1, 5: question2_5, 8: question2_8, 14: question2_14, 18: question2_18,
                    19: question2_19})

# Aflevering 3 - First (afvaller: Manuel, door ziekte vrijwillig afgevallen. Dit werd pas meegedeeld tijdens de test.)
players3f = [Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10,
             Player.MANUEL_10, Player.SANNE_10]
result3f = Result(DropType.VOLUNTARY_DROP, [Player.MANUEL_10])
episode3f = Episode(players3f, result3f, dict(), dict())

# Aflevering 3 - Second (afvaller: Barbara)
# 1 - De Mol is een:
# 1: Arjen, Erik, Frits, Manuel; 2: Barbara, Hind, Kim, Sanne;
# 8 - Werd de Mol aangewezen door Karel en Angela na het diner:
# 1: Frits; 2: Arjen, Barbara, Erik, Hind, Manuel, Kim, Sanne;
# 12 - Tijdens de rijles was de Mol:
# 1: Arjen, Erik, Hind, Kim; 2: Barbara, Frits, Sanne; 3: Manuel;
# Antwoorden: Arjen (1, 1), Hind (8, 1), Barbara (12, 2)
players3s = [Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10,
             Player.SANNE_10]
question3_1 = Question({1: [Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10],
                        2: [Player.BARBARA_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10]})
question3_8 = Question({1: [Player.FRITS_10],
                        2: [Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.HIND_10, Player.KIM_10,
                            Player.SANNE_10]})
question3_12 = Question({1: [Player.ARJEN_10, Player.ERIK_10, Player.HIND_10, Player.KIM_10],
                         2: [Player.BARBARA_10, Player.FRITS_10, Player.SANNE_10]})
result3s = Result(DropType.EXECUTION_DROP, [Player.BARBARA_10])
episode3s = Episode(players3s, result3s,
                    {Player.ARJEN_10: TestInput({1: 1}), Player.HIND_10: TestInput({8: 1}),
                     Player.BARBARA_10: TestInput({12: 2})},
                    {1: question3_1, 8: question3_8, 12: question3_12})

# Aflevering 4 (afvaller: Barbara)
# 1 - De Mol is een:
# 1: Arjen, Erik, Frits; 2: Barbara, Hind, Kim, Sanne;
# 5 - Wanneer pakte de Mol de sleutel bij het Ketting-Sleutelspel:
# 1: Sanne; 2: Arjen; 3: Barbara; 4: Erik; 5: Kim; 6: Hind; 7: Frits;
# 12 - Hoeveel vragen kreeg de Mol in de school:
# 1: Arjen, Hind, Sanne; 2: Frits; 3: Erik, Kim; 4: Barbara;
# Antwoorden: Frits (Vrijstelling), Sanne (5, 2), Erik (12, 3), Barbara (1, 1)
players4 = [Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10,
            Player.SANNE_10]
question4_1 = Question({1: [Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10],
                        2: [Player.BARBARA_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10]})
question4_5 = Question({1: [Player.SANNE_10], 2: [Player.ARJEN_10], 3: [Player.BARBARA_10], 4: [Player.ERIK_10],
                        5: [Player.KIM_10], 6: [Player.HIND_10], 7: [Player.FRITS_10]})
question4_12 = Question({1: [Player.ARJEN_10, Player.HIND_10, Player.SANNE_10],
                         2: [Player.FRITS_10],
                         3: [Player.ERIK_10, Player.KIM_10],
                         4: [Player.BARBARA_10]})
result4 = Result(DropType.EXECUTION_DROP, [Player.BARBARA_10])
episode4 = Episode(players4, result4,
                    {Player.FRITS_10: TestInput(immunity = True), Player.SANNE_10: TestInput({5: 2}),
                     Player.ERIK_10: TestInput({12: 3}), Player.BARBARA_10: TestInput({1: 1})},
                    {1: question4_1, 5: question4_5, 12: question4_12})

# Aflevering 5 (afvaller: Hind)
# 5 - Hoe vaak peddelde de Mol in de boot:
# 1: Arjen; 2: Frits, Hind, Kim, Sanne; 3: Erik;
# 11 - In welke bioscoopzaal stond de Mol:
# 1: Erik, Frits, Hind; 2: Arjen, Kim, Sanne;
# 17 - De Mol startte de tempelopdracht op:
# 1: Arjen, Sanne; 2: Erik, Kim; 3: Frits, Hind;
# Antwoorden: Sanne (5, 2), Arjen (11, 1), Kim (17, 1)
players5 = [Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10]
question5_5 = Question({1: [Player.ARJEN_10],
                        2: [Player.FRITS_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10],
                        3: [Player.ERIK_10]})
question5_11 = Question({1: [Player.ERIK_10, Player.FRITS_10, Player.HIND_10],
                         2: [Player.ARJEN_10, Player.KIM_10, Player.SANNE_10]})
question5_17 = Question({1: [Player.ARJEN_10, Player.SANNE_10],
                         2: [Player.ERIK_10, Player.KIM_10],
                         3: [Player.FRITS_10, Player.HIND_10]})
result5 = Result(DropType.EXECUTION_DROP, [Player.HIND_10])
episode5 = Episode(players5, result5,
                    {Player.SANNE_10: TestInput({5: 2}), Player.ARJEN_10: TestInput({11: 1}),
                     Player.KIM_10: TestInput({17: 1})},
                    {5: question5_5, 11: question5_11, 17: question5_17})

# Aflevering 6 (geen afvaller, alleen Arjen kreeg zijn scherm te zien)
# Antwoorden: Frits (1 joker), Sanne (5 jokers)
players6 = [Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10, Player.KIM_10, Player.SANNE_10]
result6 = Result(DropType.POSSIBLE_DROP, [Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10])
episode6 = Episode(players6, result6,
                    {Player.FRITS_10: TestInput(jokers = 1), Player.SANNE_10: TestInput(jokers = 5)}, dict())

# Aflevering 7 (afvaller: Arjen)
# 8 - Welke letters communiceerde de Mol bij de Webcamopdracht:
# 1: Kim; 2: Sanne; 3: Erik; 4: Arjen, Frits;
# 12 - Heeft de Mol de inhoud van een koffer verdiend op het zebrapad:
# 1: Arjen, Kim; 2: Erik, Frits, Sanne;
# Antwoorden: Arjen (12, 2), Kim (8, 2)
players7 = [Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10, Player.KIM_10, Player.SANNE_10]
question7_8 = Question({1: [Player.KIM_10],
                        2: [Player.SANNE_10],
                        3: [Player.ERIK_10],
                        4: [Player.ARJEN_10, Player.FRITS_10]})
question7_12 = Question({1: [Player.ARJEN_10, Player.KIM_10],
                         2: [Player.ERIK_10, Player.FRITS_10, Player.SANNE_10]})
result7 = Result(DropType.EXECUTION_DROP, [Player.ARJEN_10])
episode7 = Episode(players7, result7,
                   {Player.ARJEN_10: TestInput({12: 2}), Player.KIM_10: TestInput({8: 2})},
                   {8: question7_8, 12: question7_12})

# Aflevering 8 (afvaller: Erik)
# 10 - Heeft de Mol een joker van Arjen gewonnen:
# 1: Kim, Sanne; 2: Erik, Frits;
# Antwoorden: Sanne (Vrijstelling), Frits (10, 1), Kim (2 jokers)
players8 = [Player.ERIK_10, Player.FRITS_10, Player.KIM_10, Player.SANNE_10]
question8_10 = Question({1: [Player.KIM_10, Player.SANNE_10],
                         2: [Player.ERIK_10, Player.FRITS_10]})
result8 = Result(DropType.EXECUTION_DROP, [Player.ERIK_10])
episode8 = Episode(players8, result8,
                   {Player.SANNE_10: TestInput(immunity = True), Player.FRITS_10: TestInput({10: 1}),
                    Player.KIM_10: TestInput(jokers = 2)},
                   {10: question8_10})

season10 = Season(players1, {1: episode1, 2: episode2, 2.5: episode3f, 3: episode3s, 4: episode4, 5: episode5,
                             6: episode6, 7: episode7, 8: episode8})