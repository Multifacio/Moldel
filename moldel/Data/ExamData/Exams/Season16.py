from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

# Aflevering 1 (geen afvaller, alleen Klaas, Annemieke en Rop kregen hun scherm te zien)
# Vragen:
# 6 - Stond de Mol zijn geld direct af na de metro opdracht?
# 1: Airen, Annemieke, Cecile, Klaas, Marjolein, Remy, Rop, Taeke; 2: Tim; 3: Ellie;
# 10 - Waar zat de Mol vanochtend in de bus bij aanvang van de rit?
# 1: Rop, Klaas, Ellie, Tim, Airen 2: Annemieke, Taeke, Cecile, Marjolein, Remy
# 18 - Wat is de favoriete stad in Nederland van de Mol? (Niet Bruikbaar)
# 20 - Wie is de Mol?
# 1: Airen; 2: Annemieke; 3: Cecile; 4: Ellie; 5: Klaas; 6: Marjolein; 7: Remy; 8: Rop; 9: Taeke; 10: Tim
# Antwoorden: Annemieke (20, 5), Klaas (20, 1), Cecile (10, 1) (Geen scherm), Remy (6, 2) (Geen scherm),
# Ellie (20, 8) (Geen scherm), Taeke (20, 6), Airen (Geen scherm), Marjolein (Geen scherm), Rop (Geen scherm),
# Tim (Geen scherm)
players1 = [Player.AIREN_16, Player.ANNEMIEKE_16, Player.CECILE_16, Player.ELLIE_16, Player.KLAAS_16,
            Player.MARJOLEIN_16, Player.REMY_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16]
question1_6 = Question({1: [Player.AIREN_16, Player.ANNEMIEKE_16, Player.CECILE_16, Player.KLAAS_16,
                            Player.MARJOLEIN_16, Player.REMY_16, Player.ROP_16, Player.TAEKE_16],
                        2: [Player.TIM_16],
                        3: [Player.ELLIE_16]})
question1_10 = Question({1: [Player.ROP_16, Player.KLAAS_16, Player.ELLIE_16, Player.TIM_16, Player.AIREN_16],
                         2: [Player.ANNEMIEKE_16, Player.TAEKE_16, Player.CECILE_16, Player.MARJOLEIN_16,
                             Player.REMY_16]})
question1_20 = Question({1: [Player.AIREN_16], 2: [Player.ANNEMIEKE_16], 3: [Player.CECILE_16], 4: [Player.ELLIE_16],
                         5: [Player.KLAAS_16], 6: [Player.MARJOLEIN_16], 7: [Player.REMY_16], 8: [Player.ROP_16],
                         9: [Player.TAEKE_16], 10: [Player.TIM_16]})
result1 = Result(DropType.POSSIBLE_DROP, [Player.CECILE_16, Player.REMY_16, Player.ELLIE_16, Player.AIREN_16,
                                          Player.MARJOLEIN_16, Player.ROP_16, Player.TIM_16])
episode1 = Episode(players1, result1,
                   {Player.ANNEMIEKE_16: TestInput({20: 5}), Player.KLAAS_16: TestInput({20: 1}),
                    Player.CECILE_16: TestInput({10: 1}), Player.REMY_16: TestInput({6: 2}),
                    Player.ELLIE_16: TestInput({20: 8}), Player.TAEKE_16: TestInput({20: 6})},
                   {6: question1_6, 10: question1_10, 20: question1_20})

# Aflevering 2 (afvaller: Airen)
# Vragen:
# 1 - De Mol is:
# 1: Klaas, Remy, Rop, Taeke, Tim; 2: Airen, Annemieke, Cecile, Ellie, Marjolein
# 5 - Heeft de Mol een kar bij het eindpunt afgeleverd tijdens de Zoutmijnen-opdracht?
# 1: Remy, Marjolein, Cecile; 2: Airen, Annemiek, Ellie, Klaas, Rop, Taeke, Tim
# 8 - Wat bestelde de Mol tijdens de lunch voor de Trappen-opdracht? (Niet bruikbaar)
# 10 - Waar stond de Mol tijdens de Trappen-opdracht?
# 1: Taeke, Marjolein, Rop; 2: Ellie, Remy, Annemieke; 3: Cecile, Airen, Tim; 4: Klaas
# 12 - Waar stond de Mol op de groepsfoto van aflevering 2?
# 1: Ellie, Airen, Taeke, Marjolein, Cecille, Annemieke; 2: Tim, Klaas, Rop, Remy
# 16 - Als hoeveelste kwam het duo van de Mol aan bij de Klooster-opdracht:
# 1: Tim, Taeke; 2: Klaas, Cecile; 3: Annemieke, Rop; 4: Ellie, Marjolein; 5: Remy, Airen;
# 20 - Wie is de Mol?
# 1: Airen; 2: Annemieke; 3: Cecile; 4: Ellie; 5: Klaas; 6: Marjolein; 7: Remy; 8: Rop; 9: Taeke; 10: Tim
# Antwoorden: Tim (5, 2) (1 joker), Annemieke (20, 7), Remy (12, 1) (1 joker), Cecille (10, 1), Marjolein (1 joker),
# Taeke (1, 1), Rop (16, 5) (1 joker)
players2 = [Player.AIREN_16, Player.ANNEMIEKE_16, Player.CECILE_16, Player.ELLIE_16, Player.KLAAS_16,
            Player.MARJOLEIN_16, Player.REMY_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16]
question2_1 = Question({1: [Player.KLAAS_16, Player.REMY_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16],
                        2: [Player.AIREN_16, Player.ANNEMIEKE_16, Player.CECILE_16, Player.ELLIE_16,
                            Player.MARJOLEIN_16]})
question2_5 = Question({1: [Player.REMY_16, Player.MARJOLEIN_16, Player.CECILE_16],
                        2: [Player.AIREN_16, Player.ANNEMIEKE_16, Player.ELLIE_16, Player.KLAAS_16, Player.ROP_16,
                            Player.TAEKE_16, Player.TIM_16]})
question2_10 = Question({1: [Player.TAEKE_16, Player.MARJOLEIN_16, Player.ROP_16],
                         2: [Player.ELLIE_16, Player.REMY_16, Player.ANNEMIEKE_16],
                         3: [Player.CECILE_16, Player.AIREN_16, Player.TIM_16],
                         4: [Player.KLAAS_16]})
question2_12 = Question({1: [Player.ELLIE_16, Player.AIREN_16, Player.TAEKE_16, Player.MARJOLEIN_16,
                             Player.CECILE_16, Player.ANNEMIEKE_16],
                         2: [Player.TIM_16, Player.KLAAS_16, Player.ROP_16, Player.REMY_16]})
question2_16 = Question({1: [Player.TIM_16, Player.TAEKE_16],
                         2: [Player.KLAAS_16, Player.CECILE_16],
                         3: [Player.ANNEMIEKE_16, Player.ROP_16],
                         4: [Player.ELLIE_16, Player.MARJOLEIN_16],
                         5: [Player.REMY_16, Player.AIREN_16]})
question2_20 = Question({1: [Player.AIREN_16], 2: [Player.ANNEMIEKE_16], 3: [Player.CECILE_16], 4: [Player.ELLIE_16],
                         5: [Player.KLAAS_16], 6: [Player.MARJOLEIN_16], 7: [Player.REMY_16], 8: [Player.ROP_16],
                         9: [Player.TAEKE_16], 10: [Player.TIM_16]})
result2 = Result(DropType.EXECUTION_DROP, [Player.AIREN_16])
episode2 = Episode(players2, result2,
                   {Player.TIM_16: TestInput({5: 2}, jokers = 1), Player.ANNEMIEKE_16: TestInput({20: 7}),
                    Player.REMY_16: TestInput({12: 1}, jokers = 1), Player.CECILE_16: TestInput({10: 1}),
                    Player.MARJOLEIN_16: TestInput(jokers = 1), Player.TAEKE_16: TestInput({1: 1}),
                    Player.ROP_16: TestInput({16: 5}, jokers = 1)},
                   {1: question2_1, 5: question2_5, 10: question2_10, 12: question2_12, 16: question2_16,
                    20: question2_20})

# Aflevering 3 (afvaller: Remy)
# Vragen:
# 1 - De Mol is:
# 1: Klaas, Remy, Rop, Taeke, Tim; 2: Annemieke, Cecile, Ellie, Marjolein
# 4 - Welk bedrag was de Mol bij aanvang van de Laser-opdracht "waard":
# 1: Rop, Tim; 2: Klaas, Cecille, Remy; 3: Annemieke, Ellie, Marjolein; 4: Taeke
# 6 - Als hoeveelste duo ging de Mol over het parcours tijdens de Laser-opdracht:
# 1: Annemieke, Klaas; 2: Remy, Taeke; 3: Ellie, Rop; 4: Cecile, Marjolein; 5: Tim;
# 7 - Werd de Mol afgeschoten tijdens de Laser-opdracht:
# 1: Tim, Annemieke, Rop, Marjolein, Ellie; 2: Klaas, Remy, Taeke, Cecille;
# 8 - Pakte de Mol een verdubbelaar bij de Laser-opdracht? (Te twijfelachtig om te gebruiken)
# 1: Annemieke, Klaas, Taeke, Cecile 2: Tim, Remy, Rop, Ellie, Marjolein
# 12 - Het team van de Mol kreeg bij aanvang van de Geld Matchen-opdracht:
# 1: Rop, Ellie 2: Klaas, Tim; 3: Remy, Cecille, Marjolein 4: Taeke, Annemieke
# 16 - Maakte de Mol samen met twee andere kandidaten een heel biljet:
# 1: Annemieke, Taeke, Rop, Remy, Cecille, Marjolein; 2: Klaas, Tim, Ellie;
# 19 - Ging de Mol als eerste bieden tijdens de Macht over de Test:
# 1: Ellie; 2: Annemieke, Cecile, Klaas, Marjolein, Remy, Rop, Taeke, Tim;
# 20 - Wie is de Mol?
# 1: Annemieke; 2: Cecile; 3: Ellie; 4: Klaas; 5: Marjolein; 6: Remy; 7: Rop; 8: Taeke; 9: Tim
# Antwoorden: Ellie (12, 2), Rop (16, 1), Taeke (7, 2), Marjolein (19, 1), Klaas (6, 5), Cecile (20, 3), Tim (4, 3),
# Annemieke (1, 1)
players3 = [Player.ANNEMIEKE_16, Player.CECILE_16, Player.ELLIE_16, Player.KLAAS_16, Player.MARJOLEIN_16,
            Player.REMY_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16]
question3_1 = Question({1: [Player.KLAAS_16, Player.REMY_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16],
                        2: [Player.ANNEMIEKE_16, Player.CECILE_16, Player.ELLIE_16, Player.MARJOLEIN_16]})
question3_4 = Question({1: [Player.ROP_16, Player.TIM_16],
                        2: [Player.KLAAS_16, Player.CECILE_16, Player.REMY_16],
                        3: [Player.ANNEMIEKE_16, Player.ELLIE_16, Player.MARJOLEIN_16],
                        4: [Player.TAEKE_16]})
question3_6 = Question({1: [Player.ANNEMIEKE_16, Player.KLAAS_16],
                        2: [Player.REMY_16, Player.TAEKE_16],
                        3: [Player.ELLIE_16, Player.ROP_16],
                        4: [Player.CECILE_16, Player.MARJOLEIN_16],
                        5: [Player.TIM_16]})
question3_7 = Question({1: [Player.TIM_16, Player.ANNEMIEKE_16, Player.ROP_16, Player.MARJOLEIN_16, Player.ELLIE_16],
                        2: [Player.KLAAS_16, Player.REMY_16, Player.TAEKE_16, Player.CECILE_16]})
# Deze vraag heb ik niet gebruikt, vanwege teveel twijfel over waar de antwoorden naar linken.
question3_8 = Question({1: [Player.ANNEMIEKE_16, Player.KLAAS_16, Player.TAEKE_16, Player.CECILE_16],
                        2: [Player.TIM_16, Player.REMY_16, Player.ROP_16, Player.ELLIE_16, Player.MARJOLEIN_16]})
question3_12 = Question({1: [Player.ROP_16, Player.ELLIE_16],
                         2: [Player.KLAAS_16, Player.TIM_16],
                         3: [Player.REMY_16, Player.CECILE_16, Player.MARJOLEIN_16],
                         4: [Player.TAEKE_16, Player.ANNEMIEKE_16]})
question3_16 = Question({1: [Player.ANNEMIEKE_16, Player.TAEKE_16, Player.ROP_16, Player.REMY_16, Player.CECILE_16,
                             Player.MARJOLEIN_16],
                         2: [Player.KLAAS_16, Player.TIM_16, Player.ELLIE_16]})
question3_19 = Question({1: [Player.ELLIE_16],
                         2: [Player.ANNEMIEKE_16, Player.CECILE_16, Player.KLAAS_16, Player.MARJOLEIN_16,
                             Player.REMY_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16]})
question3_20 = Question({1: [Player.ANNEMIEKE_16], 2: [Player.CECILE_16], 3: [Player.ELLIE_16], 4: [Player.KLAAS_16],
                         5: [Player.MARJOLEIN_16], 6: [Player.REMY_16], 7: [Player.ROP_16], 8: [Player.TAEKE_16],
                         9: [Player.TIM_16]})
result3 = Result(DropType.EXECUTION_DROP, [Player.REMY_16])
episode3 = Episode(players3, result3,
                   {Player.ELLIE_16: TestInput({12: 2}), Player.ROP_16: TestInput({16: 1}),
                    Player.TAEKE_16: TestInput({7: 2}), Player.MARJOLEIN_16: TestInput({19: 1}),
                    Player.KLAAS_16: TestInput({6: 5}), Player.CECILE_16: TestInput({20: 3}),
                    Player.TIM_16: TestInput({4: 3}), Player.ANNEMIEKE_16: TestInput({1: 1})},
                   {1: question3_1, 4: question3_4, 6: question3_6, 7: question3_7, 12: question3_12, 16: question3_16,
                    19: question3_19, 20: question3_20})

# Aflevering 4 (afvaller: Ellie)
# Vragen:
# 1 - De Mol is:
# 1: Klaas, Rop, Taeke, Tim; 2: Annemieke, Cecile, Ellie, Marjolein
# 4 - Wat was de kleur van de kajak waar de Mol in zat tijdens de Ondiep Water-opdracht?
# 1: Rop, Tim, Klaas, Taeke; 2: Cecille, Ellie, Annemieke, Marjolein;
# 5 - Hoeveel kokers leverde de Mol in op het strand tijdens de Ondiep Water-opdracht?
# 1: Annemieke, Marjolein; 2: Rop, Ellie; 3: Cecille, Tim, Klaas, Taeke;
# 17: Kreeg de Mol een passende sleutel tijdens de Sleutelroute-opdracht:
# 1: Ellie, Taeke 2: Tim, Klaas, Marjolein, Annemieke; 3: Cecile, Rop;
# 20 - Wie is de Mol:
# 1: Annemieke; 2: Cecile; 3: Ellie; 4: Klaas; 5: Marjolein; 6: Rop; 7: Taeke; 8: Tim
# Antwoorden: Taeke (1, 1), Annemieke (20, 8) (3 jokers), Cecille (17, 1), Ellie (5, 2), Klaas (20, 8) (1 joker)
players4 = [Player.ANNEMIEKE_16, Player.CECILE_16, Player.ELLIE_16, Player.KLAAS_16, Player.MARJOLEIN_16, Player.ROP_16,
            Player.TAEKE_16, Player.TIM_16]
question4_1 = Question({1: [Player.KLAAS_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16],
                        2: [Player.ANNEMIEKE_16, Player.CECILE_16, Player.ELLIE_16, Player.MARJOLEIN_16]})
question4_4 = Question({1: [Player.ROP_16, Player.TIM_16, Player.KLAAS_16, Player.TAEKE_16],
                        2: [Player.CECILE_16, Player.ELLIE_16, Player.ANNEMIEKE_16, Player.MARJOLEIN_16]})
question4_5 = Question({1: [Player.ANNEMIEKE_16, Player.MARJOLEIN_16],
                        2: [Player.ROP_16, Player.ELLIE_16],
                        3: [Player.CECILE_16, Player.TIM_16, Player.KLAAS_16, Player.TAEKE_16]})
question4_17 = Question({1: [Player.ELLIE_16, Player.TAEKE_16],
                         2: [Player.TIM_16, Player.KLAAS_16, Player.MARJOLEIN_16, Player.ANNEMIEKE_16],
                         3: [Player.CECILE_16, Player.ROP_16]})
question4_20 = Question({1: [Player.ANNEMIEKE_16], 2: [Player.CECILE_16], 3: [Player.ELLIE_16], 4: [Player.KLAAS_16],
                         5: [Player.MARJOLEIN_16], 6: [Player.ROP_16], 7: [Player.TAEKE_16], 8: [Player.TIM_16]})
result4 = Result(DropType.EXECUTION_DROP, [Player.ELLIE_16])
episode4 = Episode(players4, result4,
                   {Player.TAEKE_16: TestInput({1: 1}), Player.ANNEMIEKE_16: TestInput({20: 8}, jokers = 3),
                    Player.CECILE_16: TestInput({17: 1}), Player.ELLIE_16: TestInput({5: 2}),
                    Player.KLAAS_16: TestInput({20: 8}, jokers = 1), Player.MARJOLEIN_16: TestInput({4: 2})},
                   {1: question4_1, 4: question4_4, 5: question4_5, 17: question4_17, 20: question4_20})

# Aflevering 5 (afvaller: Marjolein)
# Vragen:
# 1 - De Mol is:
# 1: Klaas, Rop, Taeke, Tim; 2: Annemieke, Cecile, Marjolein
# 2 - Verloor de Mol de porto tijdens de Tijdrit-opdracht:
# 1: Marjolein; 2: Annemieke, Cecile, Klaas, Rop, Taeke, Tim;
# 4 - Hoeveel tekens nam de boot van de Mol mee tijdens de Taino Tekens-opdracht:
# 1: Annemieke, Rop, Marjolein; 2: Tim, Taeke; 3: Cecile, Klaas;
# 5 - Wat was het nummer van de boot waarin de Mol zat tijdens de Taino Tekens-opdracht:
# 1: Annemieke, Rop, Marjolein; 2: Cecile, Klaas;  3: Tim, Taeke;
# 10 - Als hoeveelste vertrok de Mol bij het startpunt van de Tijdrit-opdracht:
# 1: Taeke; 2: Tim; 3: Annemieke; 4: Rop; 5: Klaas; 6: Marjolein; 7: Cecile;
# 20 - Wie is de Mol:
# 1: Annemieke; 2: Cecile; 3: Klaas; 4: Marjolein; 5: Rop; 6: Taeke; 7: Tim
# Antwoorden: Rop (2, 2), Annemieke (1, 1), Klaas (20, 7), Taeke (5, 3), Cecile (10, 2), Tim (4, 3)
players5 = [Player.ANNEMIEKE_16, Player.CECILE_16, Player.KLAAS_16, Player.MARJOLEIN_16, Player.ROP_16, Player.TAEKE_16,
            Player.TIM_16]
question5_1 = Question({1: [Player.KLAAS_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16],
                        2: [Player.ANNEMIEKE_16, Player.CECILE_16, Player.MARJOLEIN_16]})
question5_2 = Question({1: [Player.MARJOLEIN_16],
                        2: [Player.ANNEMIEKE_16, Player.CECILE_16, Player.KLAAS_16, Player.ROP_16, Player.TAEKE_16,
                            Player.TIM_16]})
question5_4 = Question({1: [Player.ANNEMIEKE_16, Player.ROP_16, Player.MARJOLEIN_16],
                        2: [Player.TIM_16, Player.TAEKE_16],
                        3: [Player.CECILE_16, Player.KLAAS_16]})
question5_5 = Question({1: [Player.ANNEMIEKE_16, Player.ROP_16, Player.MARJOLEIN_16],
                        2: [Player.CECILE_16, Player.KLAAS_16],
                        3: [Player.TIM_16, Player.TAEKE_16]})
question5_10 = Question({1: [Player.TAEKE_16], 2: [Player.TIM_16], 3: [Player.ANNEMIEKE_16], 4: [Player.ROP_16],
                         5: [Player.KLAAS_16], 6: [Player.MARJOLEIN_16], 7: [Player.CECILE_16]})
question5_20 = Question({1: [Player.ANNEMIEKE_16], 2: [Player.CECILE_16], 3: [Player.KLAAS_16],
                         4: [Player.MARJOLEIN_16], 5: [Player.ROP_16], 6: [Player.TAEKE_16], 7: [Player.TIM_16]})
result5 = Result(DropType.EXECUTION_DROP, [Player.MARJOLEIN_16])
episode5 = Episode(players5, result5,
                   {Player.ROP_16: TestInput({2: 2}), Player.ANNEMIEKE_16: TestInput({1: 1}),
                    Player.KLAAS_16: TestInput({20: 7}), Player.TAEKE_16: TestInput({5: 3}),
                    Player.CECILE_16: TestInput({10: 2}), Player.TIM_16: TestInput({4: 3})},
                   {1: question5_1, 2: question5_2, 4: question5_4, 5: question5_5, 10: question5_10, 20: question5_20})

# Aflevering 6 (afvaller: Cecile)
# 2 - Welk woord stond er op de foto van de Mol tijdens de Kandidaten Weg-Opdracht:
# 1: Taeke; 2: Annemieke; 3: Klaas; 4: Cecile; 5: Tim; 6: Rop
# 7 - Hoeveel jokers pakte de Mol tijdens de Zoek Geen Verschillen-opdracht?
# 1: Annemieke, Cecile, Klaas; 2: Taeke, Rop; 3: Tim;
# 11 - Wat was de taak van de Mol bij aanvang van de Spaanse Les-opdracht:
# 1: Tim, Taeke; 2: Rop, Annemieke 3: Klaas, Cecille;
# 18 - Als hoeveelste werd de foto van de Mol gevonden tijdens de Kandidaten Weg-opdracht:
# 1: Taeke; 2: Annemieke; 3: Cecile; 4: Klaas; 5: Tim; 6: Rop;
# 20 - Wie is de Mol:
# 1: Annemieke; 2: Cecile; 3: Klaas; 4: Rop; 5: Taeke; 6: Tim
# Antwoorden: Cecile (2, 3), Klaas (20, 1), Annemieke (7, 3), Tim (11, 3), Rop (18, 2) (1 joker)
players6 = [Player.ANNEMIEKE_16, Player.CECILE_16, Player.KLAAS_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16]
question6_2 = Question({1: [Player.TAEKE_16], 2: [Player.ANNEMIEKE_16], 3: [Player.KLAAS_16], 4: [Player.CECILE_16],
                        5: [Player.TIM_16], 6: [Player.ROP_16]})
question6_7 = Question({1: [Player.ANNEMIEKE_16, Player.CECILE_16, Player.KLAAS_16],
                        2: [Player.TAEKE_16, Player.ROP_16],
                        3: [Player.TIM_16]})
question6_11 = Question({1: [Player.TIM_16, Player.TAEKE_16],
                         2: [Player.ROP_16, Player.ANNEMIEKE_16],
                         3: [Player.KLAAS_16, Player.CECILE_16]})
question6_18 = Question({1: [Player.TAEKE_16], 2: [Player.ANNEMIEKE_16], 3: [Player.CECILE_16], 4: [Player.KLAAS_16],
                         5: [Player.TIM_16], 6: [Player.ROP_16]})
question6_20 = Question({1: [Player.ANNEMIEKE_16], 2: [Player.CECILE_16], 3: [Player.KLAAS_16], 4: [Player.ROP_16],
                         5: [Player.TAEKE_16], 6: [Player.TIM_16]})
result6 = Result(DropType.EXECUTION_DROP, [Player.CECILE_16])
episode6 = Episode(players6, result6,
                   {Player.CECILE_16: TestInput({2: 3}), Player.KLAAS_16: TestInput({20: 1}),
                    Player.ANNEMIEKE_16: TestInput({7: 3}), Player.TIM_16: TestInput({11: 3}),
                    Player.ROP_16: TestInput({18: 2}, jokers = 1)},
                   {2: question6_2, 7: question6_7, 11: question6_11, 18: question6_18, 20: question6_20})

# Aflevering 7 (afvaller: Rop)
# 3 - Als hoeveelste ging de Mol op zoek naar z'n koffer tijdens de Verlaten Resort - opdracht:
# 1: Rop; 2: Taeke; 3: Klaas; 4: Tim; 5: Annemieke;
# 6 - Waar stond de koffer van de Mol tijdens de Verlaten Resort - opdracht (Niet bruikbaar)
# 13 - Wat won de Mol uiteindelijk bij de Vier op een Rij - opdracht:
# 1: Taeke, Rop; 2: Tim; 3: Annemieke; 4: Klaas;
# 18 - Welke rol had de Mol voornamelijk tijdens de Pop-up Restaurant opdracht:
# 1: Rop; 2: Taeke; 3: Annemieke; 4: Klaas, Tim;
# 20 - Wie is de Mol:
# 1: Annemieke; 2: Klaas; 3: Rop; 4: Taeke; 5: Tim
# Antwoorden (Zwarte vrijstelling ingezet): Taeke (2 jokers), Tim (20, 1) (3 jokers),
# Klaas (13, 3) (Zwarte vrijstelling), Annemieke (18, 4) (5 jokers), Rop (3, 4) (2 jokers)
players7 = [Player.ANNEMIEKE_16, Player.KLAAS_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16]
question7_3 = Question({1: [Player.ROP_16], 2: [Player.TAEKE_16], 3: [Player.KLAAS_16], 4: [Player.TIM_16],
                        5: [Player.ANNEMIEKE_16]})
question7_13 = Question({1: [Player.TAEKE_16, Player.ROP_16],
                         2: [Player.TIM_16],
                         3: [Player.ANNEMIEKE_16],
                         4: [Player.KLAAS_16]})
question7_18 = Question({1: [Player.ROP_16],
                         2: [Player.TAEKE_16],
                         3: [Player.ANNEMIEKE_16],
                         4: [Player.KLAAS_16, Player.TIM_16]})
question7_20 = Question({1: [Player.ANNEMIEKE_16], 2: [Player.KLAAS_16], 3: [Player.ROP_16], 4: [Player.TAEKE_16],
                         5: [Player.TIM_16]})
result7 = Result(DropType.EXECUTION_DROP, [Player.ROP_16])
episode7 = Episode(players7, result7,
                   {Player.TIM_16: TestInput({20: 1}), Player.KLAAS_16: TestInput({13: 3}),
                    Player.ANNEMIEKE_16: TestInput({18: 4}), Player.ROP_16: TestInput({3: 4})},
                   {3: question7_3, 13: question7_13, 18: question7_18, 20: question7_20})

# Aflevering 8 (afvaller: Taeke)
# 13 - Voor welk eindbedrag bij de Geldklokken-opdracht is de Mol verantwoordelijk: (Niet Accuraat)
# 1: Klaas; 2: Annemieke; 3: Taeke; 4: Tim;
# 18 - Sprak de Mol het woord 'haremos' uit op tv tijdens de Omroep Santiago-opdracht:
# 1: Klaas; 2: Taeke, Tim; 3: Annemieke;
# Antwoorden: Klaas (13, 4), Tim (18, 1) (3 jokers), Taeke (1 joker), Annemieke (Vrijstelling)
players8 = [Player.ANNEMIEKE_16, Player.KLAAS_16, Player.TAEKE_16, Player.TIM_16]
question8_13 = Question({1: [Player.KLAAS_16], 2: [Player.ANNEMIEKE_16], 3: [Player.TAEKE_16], 4: [Player.TIM_16]})
question8_18 = Question({1: [Player.KLAAS_16],
                         2: [Player.TAEKE_16, Player.TIM_16],
                         3: [Player.ANNEMIEKE_16]})
result8 = Result(DropType.EXECUTION_DROP, [Player.TAEKE_16])
episode8 = Episode(players8, result8,
                   {Player.KLAAS_16: TestInput({13: 4}), Player.TIM_16: TestInput({18: 1}, jokers = 3),
                    Player.TAEKE_16: TestInput(jokers = 1), Player.ANNEMIEKE_16: TestInput(immunity = True)},
                   {13: question8_13, 18: question8_18})

# Aflevering 9 (afvaller: Annemieke) (pas in de reunie bekend)
# 2 - De Mol heeft bij de Zoutmijnen-opdracht:
# 1: Tim; 2: Annemieke; 3: Klaas;
# 7 - Bij de Laser-opdracht:
# 1: Annemieke; 2: Tim; 3: Klaas;
# 19 - Tijdens de Verlaten resort-opdracht heeft de Mol:
# 1: Klaas; 2: Tim; 3: Annemieke;
# 28 - Tijdens de Verhalen-estafette-opdracht heeft de Mol:
# 1: Annemieke; 2: Tim; 3: Klaas;
# 35 - Tijdens de Geldklokken-opdracht heeft de Mol:
# 1: Tim; 2: Klaas; 3: Annemieke;
# 40 - Wie is de Mol:
# 1: Annemieke; 2: Klaas; 3: Tim;
# Antwoorden: Tim (2, 3) (28, 3) (40, 2), Klaas (7, 2) (35, 1) (40, 3), Annemieke (19, 1) (40, 2)
players9 = [Player.ANNEMIEKE_16, Player.KLAAS_16, Player.TIM_16]
question9_2 = Question({1: [Player.TIM_16], 2: [Player.ANNEMIEKE_16], 3: [Player.KLAAS_16]})
question9_7 = Question({1: [Player.ANNEMIEKE_16], 2: [Player.TIM_16], 3: [Player.KLAAS_16]})
question9_19 = Question({1: [Player.KLAAS_16], 2: [Player.TIM_16], 3: [Player.ANNEMIEKE_16]})
question9_28 = Question({1: [Player.ANNEMIEKE_16], 2: [Player.TIM_16], 3: [Player.KLAAS_16]})
question9_35 = Question({1: [Player.TIM_16], 2: [Player.KLAAS_16], 3: [Player.ANNEMIEKE_16]})
question9_40 = Question({1: [Player.ANNEMIEKE_16], 2: [Player.KLAAS_16], 3: [Player.TIM_16]})
result9 = Result(DropType.EXECUTION_DROP, [Player.ANNEMIEKE_16])
episode9 = Episode(players9, result9,
                   {Player.TIM_16: TestInput({2: 3, 28: 3, 40: 2}), Player.KLAAS_16: TestInput({7: 2, 35: 1, 40: 3}),
                    Player.ANNEMIEKE_16: TestInput({19: 1, 40: 2})},
                   {2: question9_2, 7: question9_7, 19: question9_19, 28: question9_28, 35: question9_35,
                    40: question9_40}, num_questions = 40)

season16 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                             8: episode8, 10: episode9})