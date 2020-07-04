from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import DelayedAnswer, TestInput

# Aflevering 1 - First (Rood scherm, maar niet afgevallen: Daphne) (10 vragen test)
# Vragen:
# 1 - De Mol is een:
# 1: Freek, Jan-Willem, Maurice, Owen, Tygo; 2: Aaf, Daphne, Jennifer, Sofie, Susan;
# 5 - Waar woont de Mol:
# 1: Aaf, Daphne, Freek, Jennifer, Maurice, Owen, Susan, Tygo; 2: Sofie; 3: Jan-Willem;
# 8 - Wat is de burgerlijke staat van de Mol:
# 1: Maurice, Tygo; 2: Aaf, Daphne, Freek, Jennifer, Owen; 3: Jan-Willem, Sofie; 4: Susan;
# 10 - Wie is de Mol:
# 1: Aaf; 2: Daphne; 3: Freek; 4: Jan-Willem; 5: Jennifer; 6: Maurice; 7: Owen; 8: Sofie; 9: Susan; 10: Tygo;
# Antwoorden: Sofie (1, 1), Jan-Willem (5, 1) (10, 6), Freek (8, 3), Susan (10, 10)
players1 = [Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14,
            Player.MAURICE_14, Player.OWEN_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14]
question1f_1 = Question({1: [Player.FREEK_14, Player.JAN_WILLEM_14, Player.MAURICE_14, Player.OWEN_14, Player.TYGO_14],
                         2: [Player.AAF_14, Player.DAPHNE_14, Player.JENNIFER_14, Player.SOFIE_14, Player.SUSAN_14]})
question1f_5 = Question({1: [Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JENNIFER_14, Player.MAURICE_14,
                             Player.OWEN_14, Player.SUSAN_14, Player.TYGO_14],
                         2: [Player.SOFIE_14],
                         3: [Player.JAN_WILLEM_14]})
question1f_8 = Question({1: [Player.MAURICE_14, Player.TYGO_14],
                         2: [Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JENNIFER_14, Player.OWEN_14],
                         3: [Player.JAN_WILLEM_14, Player.SOFIE_14],
                         4: [Player.SUSAN_14]})
question1f_10 = Question({1: [Player.AAF_14], 2: [Player.DAPHNE_14], 3: [Player.FREEK_14], 4: [Player.JAN_WILLEM_14],
                          5: [Player.JENNIFER_14], 6: [Player.MAURICE_14], 7: [Player.OWEN_14], 8: [Player.SOFIE_14],
                          9: [Player.SUSAN_14], 10: [Player.TYGO_14]})
result1f = Result(DropType.EXECUTION_DROP, [Player.DAPHNE_14])
episode1f = Episode(players1, result1f,
                   {Player.SOFIE_14: TestInput({1: 1}), Player.JAN_WILLEM_14: TestInput({5: 1, 10: 6}),
                    Player.FREEK_14: TestInput({8: 3}), Player.SUSAN_14: TestInput({10: 10})},
                   {1: question1f_1, 5: question1f_5, 8: question1f_8, 10: question1f_10}, 10, skip_regression = True)

# Aflevering 1 - Second (afvaller: Maurice) (vervolg op vorige test)
# Vragen:
# 1 - De Mol is een:
# 1: Freek, Jan-Willem, Maurice, Owen, Tygo; 2: Aaf, Daphne, Jennifer, Sofie, Susan;
# 5 - Waar woont de Mol:
# 1: Aaf, Daphne, Freek, Jennifer, Maurice, Owen, Susan, Tygo; 2: Sofie; 3: Jan-Willem;
# 8 - Wat is de burgerlijke staat van de Mol:
# 1: Maurice, Tygo; 2: Aaf, Daphne, Freek, Jennifer, Owen; 3: Jan-Willem, Sofie; 4: Susan;
# 10 - Wie is de Mol:
# 1: Aaf; 2: Daphne; 3: Freek; 4: Jennifer; 5: Jan-Willem; 6: Maurice; 7: Owen; 8: Sofie; 9: Susan; 10: Tygo;
# 12: Als hoeveelste maakte de Mol de eerste 10 vragen van de test:
# 1: Sofie; 2: Jan-Willem; 3: Jennifer; 4: Freek; 5: Daphne; 6: Maurice; 7: Aaf; 8: Susan; 9: Tygo; 10: Owen;
# 14 - Houdt de Mol er van in de schijnwerpers te staan (Niet bruikbaar)
# 15 - Met wie vormde de Mol een duo tijdens de Chinees Spreken-opdracht:
# 1: Sofie; 2: Freek; 3: Daphne; 4: Susan; 5: Maurice; 6: Jan-Willem; 7: Tygo; 8: Aaf; 9: Jennifer; 10: Owen;
# 16 - Wat zocht de Mol tijdens de Chinees Spreken-opdracht:
# 1: Maurice, Jan-Willem; 2: Daphne, Freek; 3: Susan, Jennifer; 4: Owen, Tygo; 5: Sofie, Aaf;
# 20 - Wie is de Mol:
# 1: Aaf; 2: Daphne; 3: Freek; 4: Jan-Willem; 5: Jennifer; 6: Maurice; 7: Owen; 8: Sofie; 9: Susan; 10: Tygo;
# Antwoorden: Sofie (1, 1) (12, 5), Jan-Willem (5, 1) (10, 6) (20, 6), Freek (8, 3) (20, 10), Susan (10, 10) (15, 3),
# Maurice (16, 5), Tygo (20, 7)
question1s_12 = Question({1: [Player.SOFIE_14], 2: [Player.JAN_WILLEM_14], 3: [Player.JENNIFER_14],
                          4: [Player.FREEK_14], 5: [Player.DAPHNE_14], 6: [Player.MAURICE_14], 7: [Player.AAF_14],
                          8: [Player.SUSAN_14], 9: [Player.TYGO_14], 10: [Player.OWEN_14]})
question1s_15 = Question({1: [Player.SOFIE_14], 2: [Player.FREEK_14], 3: [Player.DAPHNE_14], 4: [Player.SUSAN_14],
                          5: [Player.MAURICE_14], 6: [Player.JAN_WILLEM_14], 7: [Player.TYGO_14], 8: [Player.AAF_14],
                          9: [Player.JENNIFER_14], 10: [Player.OWEN_14]})
question1s_16 = Question({1: [Player.MAURICE_14, Player.JAN_WILLEM_14],
                          2: [Player.DAPHNE_14, Player.FREEK_14],
                          3: [Player.SUSAN_14, Player.JENNIFER_14],
                          4: [Player.OWEN_14, Player.TYGO_14],
                          5: [Player.SOFIE_14, Player.AAF_14]})
question1s_20 = Question({1: [Player.AAF_14], 2: [Player.DAPHNE_14], 3: [Player.FREEK_14], 4: [Player.JAN_WILLEM_14],
                          5: [Player.JENNIFER_14], 6: [Player.MAURICE_14], 7: [Player.OWEN_14], 8: [Player.SOFIE_14],
                          9: [Player.SUSAN_14], 10: [Player.TYGO_14]})
result1s = Result(DropType.EXECUTION_DROP, [Player.MAURICE_14])
episode1s = Episode(players1, result1s,
                   {Player.SOFIE_14: TestInput({1: 1, 12: 5}),
                    Player.JAN_WILLEM_14: TestInput({5: 1, 10: 6, 20: 6}),
                    Player.FREEK_14: TestInput({8: 3, 20: 10}), Player.SUSAN_14: TestInput({10: 10, 15: 3}),
                    Player.MAURICE_14: TestInput({16: 5}), Player.TYGO_14: TestInput({20: 7})},
                   {1: question1f_1, 5: question1f_5, 8: question1f_8, 10: question1f_10, 12: question1s_12,
                    15: question1s_15, 16: question1s_16, 20: question1s_20})

# Aflevering 2 (afvaller: Owen)
# Vragen:
# 1 - De Mol is een:
# 1: Freek, Jan-Willem, Owen, Tygo; 2: Aaf, Daphne, Jennifer, Sofie, Susan;
# 3 - Nam Art de Mol mee voor een cultureel uitje:
# 1: Owen, Susan; 2: Aaf, Daphne, Freek, Jennifer, Jan-Willem, Sofie, Tygo
# 5 - Waar zat de Mol tijdens de Cantonese opera:
# 1: Freek, Sofie, Jennifer, Daphne; 2: Tygo, Jan-Willem, Aaf; 3: Owen, Susan;
# 13 - Heeft de Mol de porto in handen gehad in de controlekamer tijdens de TV-station opdracht:
# 1: Owen, Sofie, Freek, Aaf; 2: Daphne, Jennifer, Jan-Willem, Susan, Tygo;
# 19 - Heeft de Mol een tatoeage:
# 1: Sofie, Tygo; 2: Aaf, Daphne, Jennifer, Susan, Owen, Jan-Willem, Freek;
# 20 - Wie is de Mol:
# 1: Aaf; 2: Daphne; 3: Freek; 4: Jan-Willem; 5: Jennifer; 6: Owen; 7: Sofie; 8: Susan; 9: Tygo;
# Antwoorden (Zwarte vrijstelling ingezet): Aaf (1, 2), Daphne (Vrijstelling), Freek (3, 2), Jan-Willem (Vrijstelling),
# Jennifer (5, 1), Owen (13, 2) (19, 1) (2 jokers), Susan (20, 7), Tygo (2 jokers)
players2 = [Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.OWEN_14,
            Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14]
question2_1 = Question({1: [Player.FREEK_14, Player.JAN_WILLEM_14, Player.OWEN_14, Player.TYGO_14],
                        2: [Player.AAF_14, Player.DAPHNE_14, Player.JENNIFER_14, Player.SOFIE_14, Player.SUSAN_14]})
question2_3 = Question({1: [Player.OWEN_14, Player.SUSAN_14],
                        2: [Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JENNIFER_14, Player.JAN_WILLEM_14,
                            Player.SOFIE_14, Player.TYGO_14]})
question2_5 = Question({1: [Player.FREEK_14, Player.SOFIE_14, Player.JENNIFER_14, Player.DAPHNE_14],
                        2: [Player.TYGO_14, Player.JAN_WILLEM_14, Player.AAF_14],
                        3: [Player.OWEN_14, Player.SUSAN_14]})
question2_13 = Question({1: [Player.OWEN_14, Player.SOFIE_14, Player.FREEK_14, Player.AAF_14],
                         2: [Player.DAPHNE_14, Player.JENNIFER_14, Player.JAN_WILLEM_14, Player.SUSAN_14,
                             Player.TYGO_14]})
question2_19 = Question({1: [Player.SOFIE_14, Player.TYGO_14],
                         2: [Player.AAF_14, Player.DAPHNE_14, Player.JENNIFER_14, Player.SUSAN_14, Player.OWEN_14,
                             Player.JAN_WILLEM_14, Player.FREEK_14]})
question2_20 = Question({1: [Player.AAF_14], 2: [Player.DAPHNE_14], 3: [Player.FREEK_14], 4: [Player.JAN_WILLEM_14],
                         5: [Player.JENNIFER_14], 6: [Player.OWEN_14], 7: [Player.SOFIE_14], 8: [Player.SUSAN_14],
                         9: [Player.TYGO_14]})
result2 = Result(DropType.EXECUTION_DROP, [Player.OWEN_14])
episode2 = Episode(players2, result2,
                   {Player.AAF_14: TestInput({1: 2}), Player.FREEK_14: TestInput({3: 2}),
                    Player.JENNIFER_14: TestInput({5: 1}), Player.OWEN_14: TestInput({13: 2, 19: 1}),
                    Player.SUSAN_14: TestInput({20: 7})},
                   {1: question2_1, 3: question2_3, 5: question2_5, 13: question2_13, 19: question2_19,
                    20: question2_20})

# Aflevering 3 (geen afvaller, alleen Aaf, Jan-Willem, Jennifer en Susan kregen hun scherm te zien)
# Vragen:
# 5 - Heeft de Mol een envelop naar Ellis Island gestuurd:
# 1: Sofie, Freek; 2: Aaf, Daphne, Jennifer, Jan-Willem, Susan, Tygo;
# 8 - Met hoeveel andere personen zat de Mol in het team tijdens de Kamer zoeken opdracht:
# 1: Aaf, Daphne; 2: Jan-Willem, Sofie, Freek, Jennifer, Susan, Tygo;
# 20 - Wie is de Mol:
# 1: Aaf; 2: Daphne; 3: Freek; 4: Jan-Willem; 5: Jennifer; 6: Sofie; 7: Susan; 8: Tygo;
# Antwoorden: Daphne (20, 1), Freek (5, 2), Jennifer (20, 2), Jan-Willem (8, 1), Susan (20, 6) (Vrijstelling)
players3 = [Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.SOFIE_14,
            Player.SUSAN_14, Player.TYGO_14]
question3_5 = Question({1: [Player.SOFIE_14, Player.FREEK_14],
                        2: [Player.AAF_14, Player.DAPHNE_14, Player.JENNIFER_14, Player.JAN_WILLEM_14, Player.SUSAN_14,
                            Player.TYGO_14]})
question3_8 = Question({1: [Player.AAF_14, Player.DAPHNE_14],
                        2: [Player.JAN_WILLEM_14, Player.SOFIE_14, Player.FREEK_14, Player.JENNIFER_14, Player.SUSAN_14,
                            Player.TYGO_14]})
question3_20 = Question({1: [Player.AAF_14], 2: [Player.DAPHNE_14], 3: [Player.FREEK_14], 4: [Player.JAN_WILLEM_14],
                         5: [Player.JENNIFER_14], 6: [Player.SOFIE_14], 7: [Player.SUSAN_14], 8: [Player.TYGO_14]})
result3 = Result(DropType.POSSIBLE_DROP, [Player.DAPHNE_14, Player.FREEK_14, Player.SOFIE_14, Player.TYGO_14])
episode3 = Episode(players3, result3,
                   {Player.DAPHNE_14: TestInput({20: 1}), Player.FREEK_14: TestInput({5: 2}),
                    Player.JENNIFER_14: TestInput({20: 2}), Player.JAN_WILLEM_14: TestInput({8: 1}),
                    Player.SUSAN_14: TestInput({20: 6}, immunity = True)},
                   {5: question3_5, 8: question3_8, 20: question3_20})

# Aflevering 4 (afvaller: Daphne)
# Vragen:
# 1 - De Mol is een:
# 1: Freek, Jan-Willem, Tygo; 2: Aaf, Daphne, Jennifer, Sofie, Susan;
# 5 - Hoe ontving de Mol de woorden tijdens de Roltrappen-opdracht:
# 1: Susan, Sofie, Jennifer, Freek, Daphne, Aaf; 2: Tygo; 3: Jan-Willem;
# 7 - Heeft de Mol hoogtevrees (Niet bruikbaar)
# 20 - Wie is de Mol:
# 1: Aaf; 2: Daphne; 3: Freek; 4: Jan-Willem; 5: Jennifer; 6: Sofie; 7: Susan; 8: Tygo;
# Antwoorden: Tygo (20, 6) (3 jokers), Aaf (20, 7) (1 joker), Jan-Willem (1, 2), Daphne (1 joker),
# Susan (5, 1) (1 joker), Jennifer (2 jokers)
players4 = [Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.SOFIE_14,
            Player.SUSAN_14, Player.TYGO_14]
question4_1 = Question({1: [Player.FREEK_14, Player.JAN_WILLEM_14, Player.TYGO_14],
                        2: [Player.AAF_14, Player.DAPHNE_14, Player.JENNIFER_14, Player.SOFIE_14, Player.SUSAN_14]})
question4_5 = Question({1: [Player.SUSAN_14, Player.SOFIE_14, Player.JENNIFER_14, Player.FREEK_14, Player.DAPHNE_14,
                            Player.AAF_14],
                        2: [Player.TYGO_14],
                        3: [Player.JAN_WILLEM_14]})
question4_20 = Question({1: [Player.AAF_14], 2: [Player.DAPHNE_14], 3: [Player.FREEK_14], 4: [Player.JAN_WILLEM_14],
                         5: [Player.JENNIFER_14], 6: [Player.SOFIE_14], 7: [Player.SUSAN_14], 8: [Player.TYGO_14]})
result4 = Result(DropType.EXECUTION_DROP, [Player.DAPHNE_14])
episode4 = Episode(players4, result4,
                   {Player.TYGO_14: TestInput({20: 6}, jokers = 3), Player.AAF_14: TestInput({20: 7}, jokers = 1),
                    Player.JAN_WILLEM_14: TestInput({1: 2}), Player.DAPHNE_14: TestInput(jokers = 1),
                    Player.SUSAN_14: TestInput({5: 1}, jokers = 1), Player.JENNIFER_14: TestInput(jokers = 2)},
                   {1: question4_1, 5: question4_5, 20: question4_20})

# Aflevering 5 (afvaller: Jennifer)
# Vragen:
# 1 - De Mol is een:
# 1: Freek, Jan-Willem, Tygo; 2: Aaf, Jennifer, Sofie, Susan;
# 2 (vraag nummer onbekend) - Raakt de Mol niet snel de weg kwijt:
# 1: Freek, Sofie, Tygo; 2: Aaf, Jan-Willem, Jennifer, Susan;
# 3 - Had de Mol oog voor detail tijdens de 10.000 Boedha's opdracht:
# 1: Aaf, Sofie; 2: Jennifer, Freek, Jan-Willem, Susan, Tygo;
# 6 - Bestuurde de Mol een speedboot in de haven van Hongkong:
# 1: Jennifer, Tygo; 2: Aaf, Freek, Jan-Willem, Sofie, Susan;
# 14 - Met hoeveel personen zat de Mol in het team tijdens de Snake-opdracht:
# 1: Susan, Jennifer, Jan-Willem, Aaf; 2: Tygo, Freek, Sofie;
# 17 - Heeft de Mol deze aflevering geld gepost naar Ellis Island:
# 1: Jennifer, Tygo; 2: Aaf, Freek, Jan-Willem, Sofie, Susan;
# 20 - Wie is de Mol:
# 1: Aaf; 2: Freek; 3: Jan-Willem; 4: Jennifer; 5: Sofie; 6: Susan; 7: Tygo;
# Antwoorden (Zwarte vrijstelling ingezet): Jan-Willem (20, 4) (2, 1 pas bekend vanaf aflevering 6),
# Jennifer (6, 2) (1 joker), Aaf (17, 2), Freek (1, 1) (14, 1 pas bekend vanaf aflevering 6) (Vrijstelling),
# Sofie (3, 2), Susan (20, 5) (3, 2 pas bekend vanaf aflevering 6), Tygo (14, 1) (1, 2 pas bekend vanaf aflevering 6)
players5 = [Player.AAF_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.SOFIE_14, Player.SUSAN_14,
            Player.TYGO_14]
question5_1 = Question({1: [Player.FREEK_14, Player.JAN_WILLEM_14, Player.TYGO_14],
                        2: [Player.AAF_14, Player.JENNIFER_14, Player.SOFIE_14, Player.SUSAN_14]})
question5_3 = Question({1: [Player.AAF_14, Player.SOFIE_14],
                        2: [Player.JENNIFER_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.SUSAN_14,
                            Player.TYGO_14]})
question5_6 = Question({1: [Player.JENNIFER_14, Player.TYGO_14],
                        2: [Player.AAF_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.SOFIE_14, Player.SUSAN_14]})
question5_14 = Question({1: [Player.SUSAN_14, Player.JENNIFER_14, Player.JAN_WILLEM_14, Player.AAF_14],
                         2: [Player.TYGO_14, Player.FREEK_14, Player.SOFIE_14]})
question5_17 = Question({1: [Player.JENNIFER_14, Player.TYGO_14],
                         2: [Player.AAF_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.SOFIE_14, Player.SUSAN_14]})
question5_20 = Question({1: [Player.AAF_14], 2: [Player.FREEK_14], 3: [Player.JAN_WILLEM_14], 4: [Player.JENNIFER_14],
                         5: [Player.SOFIE_14], 6: [Player.SUSAN_14], 7: [Player.TYGO_14]})
result5 = Result(DropType.EXECUTION_DROP, [Player.JENNIFER_14])
episode5 = Episode(players5, result5,
                   {Player.JAN_WILLEM_14: TestInput({2: DelayedAnswer(1, 6), 20: 4}),
                    Player.JENNIFER_14: TestInput({6: 2}), Player.AAF_14: TestInput({17: 2}),
                    Player.FREEK_14: TestInput({1: 1, 14: DelayedAnswer(1, 6)}), Player.SOFIE_14: TestInput({3: 2}),
                    Player.SUSAN_14: TestInput({3: DelayedAnswer(2, 6), 20: 5}),
                    Player.TYGO_14: TestInput({1: DelayedAnswer(2, 6), 14: 1})},
                   {1: question5_1, 3: question5_3, 6: question5_6, 14: question5_14, 17: question5_17,
                    20: question5_20})

# Aflevering 6 (afvaller: Aaf)
# Vragen:
# 5 - Met wie vormde de Mol een duo tijdens de optocht:
# 1: Sofie; 2: Susan; 3: Aaf; 4: Freek; 5: Jan-Willem, Tygo;
# 6 - Wat ontdekte het team van de Mol tijdens de optocht:
# 1: Freek, Susan; 2: Aaf, Sofie; 3: Jan-Willem, Tygo;
# 11 - Heeft de Mol achter het stuur gezeten tijdens de 4x4 opdracht:
# 1: Jan-Willem, Susan, Sofie; 2: Tygo, Aaf, Freek;
# 12 - Met wie vormde de Mol een duo tijdens de 4x4 opdracht:
# 1: Susan; 2: Jan-Willem; 3: Freek; 4: Tygo; 5: Aaf; 6: Sofie;
# 20 - Wie is de Mol:
# 1: Aaf; 2: Freek; 3: Jan-Willem; 4: Sofie; 5: Susan; 6: Tygo;
# Antwoorden: Freek (20, 1), Sofie (12, 1), Jan-Willem (20, 1) (2 jokers), Aaf (6, 3), Tygo (5, 2), Susan (11, 1)
players6 = [Player.AAF_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14]
question6_5 = Question({1: [Player.SOFIE_14],
                        2: [Player.SUSAN_14],
                        3: [Player.AAF_14],
                        4: [Player.FREEK_14],
                        5: [Player.JAN_WILLEM_14, Player.TYGO_14]})
question6_6 = Question({1: [Player.FREEK_14, Player.SUSAN_14],
                        2: [Player.AAF_14, Player.SOFIE_14],
                        3: [Player.JAN_WILLEM_14, Player.TYGO_14]})
question6_11 = Question({1: [Player.JAN_WILLEM_14, Player.SUSAN_14, Player.SOFIE_14],
                         2: [Player.TYGO_14, Player.AAF_14, Player.FREEK_14]})
question6_12 = Question({1: [Player.SUSAN_14], 2: [Player.JAN_WILLEM_14], 3: [Player.FREEK_14], 4: [Player.TYGO_14],
                         5: [Player.AAF_14], 6: [Player.SOFIE_14]})
question6_20 = Question({1: [Player.AAF_14], 2: [Player.FREEK_14], 3: [Player.JAN_WILLEM_14], 4: [Player.SOFIE_14],
                         5: [Player.SUSAN_14], 6: [Player.TYGO_14]})
result6 = Result(DropType.EXECUTION_DROP, [Player.AAF_14])
episode6 = Episode(players6, result6,
                   {Player.FREEK_14: TestInput({20: 1}), Player.SOFIE_14: TestInput({12: 1}),
                    Player.JAN_WILLEM_14: TestInput({20: 1}, jokers = 2), Player.AAF_14: TestInput({6: 3}),
                    Player.TYGO_14: TestInput({5: 2}), Player.SUSAN_14: TestInput({11: 1})},
                   {5: question6_5, 6: question6_6, 11: question6_11, 12: question6_12, 20: question6_20})

# Aflevering 7 (geen afvaller, alleen Jan-Willem kreeg zijn scherm te zien)
# Vragen:
# 1 - De Mol is een:
# 1: Freek, Jan-Willem, Tygo; 2: Sofie, Susan;
# 8 - Welke windmolen koos de Mol uit om te beklimmen:
# 1: Jan-Willem; 2: Susan; 3: Freek; 4: Sofie, Tygo;
# 11 - Heeft de Mol de top van de windmolen bereikt:
# 1: Freek, Jan-Willem; 2: Susan; 3: Sofie, Tygo;
# 19 - Met welk vervoermiddel verplaatste de Mol zich door de Vigan:
# 1: Freek, Jan-Willem; 2: Sofie, Susan, Tygo;
# 20 - Wie is de Mol:
# 1: Freek; 2: Jan-Willem; 3: Sofie; 4: Susan; 5: Tygo;
# Antwoorden: Freek (8, 4) (19, 1), Tygo (20, 4), Sofie (1, 2), Susan (11, 3), Jan-Willem (20, 3)
players7 = [Player.FREEK_14, Player.JAN_WILLEM_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14]
question7_1 = Question({1: [Player.FREEK_14, Player.JAN_WILLEM_14, Player.TYGO_14],
                        2: [Player.SOFIE_14, Player.SUSAN_14]})
question7_8 = Question({1: [Player.JAN_WILLEM_14],
                        2: [Player.SUSAN_14],
                        3: [Player.FREEK_14],
                        4: [Player.SOFIE_14, Player.TYGO_14]})
question7_11 = Question({1: [Player.FREEK_14, Player.JAN_WILLEM_14],
                         2: [Player.SUSAN_14],
                         3: [Player.SOFIE_14, Player.TYGO_14]})
question7_19 = Question({1: [Player.FREEK_14, Player.JAN_WILLEM_14],
                         2: [Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14]})
question7_20 = Question({1: [Player.FREEK_14], 2: [Player.JAN_WILLEM_14], 3: [Player.SOFIE_14], 4: [Player.SUSAN_14],
                         5: [Player.TYGO_14]})
result7 = Result(DropType.POSSIBLE_DROP, [Player.FREEK_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14])
episode7 = Episode(players7, result7,
                   {Player.FREEK_14: TestInput({8: 4, 19: 1}), Player.TYGO_14: TestInput({20: 4}),
                    Player.SOFIE_14: TestInput({1: 2}), Player.SUSAN_14: TestInput({11: 3}),
                    Player.JAN_WILLEM_14: TestInput({20: 3})},
                   {1: question7_1, 8: question7_8, 11: question7_11, 19: question7_19, 20: question7_20})

# Aflevering 8 (afvaller: Jan-Willem)
# Vragen:
# 20 - Wie is de Mol:
# 1: Freek; 2: Jan-Willem; 3: Sofie; 4: Susan; 5: Tygo;
# Antwoorden: Freek (20, 3), Tygo (20, 4) (1 joker), Sofie (20, 4)
players8 = [Player.FREEK_14, Player.JAN_WILLEM_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14]
question8_20 = Question({1: [Player.FREEK_14], 2: [Player.JAN_WILLEM_14], 3: [Player.SOFIE_14], 4: [Player.SUSAN_14],
                         5: [Player.TYGO_14]})
result8 = Result(DropType.EXECUTION_DROP, [Player.JAN_WILLEM_14])
episode8 = Episode(players8, result8,
                   {Player.FREEK_14: TestInput({20: 3}), Player.TYGO_14: TestInput({20: 4}, jokers = 1),
                    Player.SOFIE_14: TestInput({20: 4})},
                   {20: question8_20})

# Aflevering 9 - First (afvaller: Tygo)
# Vragen:
# 5 - Heeft de Mol ooit een zwarte vrijstelling ingezet:
# 1: Sofie, Tygo; 2: Susan, Freek;
# 12 - Hoeveel enveloppen haalde het team van de Mol op tijdens de Ellis Island opdracht:
# 1: Sofie, Tygo; 2: Freek, Susan;
# 20 - Wie is de Mol:
# 1: Freek; 2: Sofie; 3: Susan; 4: Tygo;
# Antwoorden: Freek (Vrijstelling), Tygo (20, 3), Sofie (5, 2), Susan (12, 1)
players9f = [Player.FREEK_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14]
question9f_5 = Question({1: [Player.SOFIE_14, Player.TYGO_14],
                         2: [Player.SUSAN_14, Player.FREEK_14]})
question9f_12 = Question({1: [Player.SOFIE_14, Player.TYGO_14],
                          2: [Player.FREEK_14, Player.SUSAN_14]})
question9f_20 = Question({1: [Player.FREEK_14], 2: [Player.SOFIE_14], 3: [Player.SUSAN_14], 4: [Player.TYGO_14]})
result9f = Result(DropType.EXECUTION_DROP, [Player.TYGO_14])
episode9f = Episode(players9f, result9f,
                   {Player.FREEK_14: TestInput(immunity = True), Player.TYGO_14: TestInput({20: 3}),
                    Player.SOFIE_14: TestInput({5: 2}), Player.SUSAN_14: TestInput({12: 1})},
                   {5: question9f_5, 12: question9f_12, 20: question9f_20})

# Aflevering 9 - Second (verliezer: Freek of Susan) (20 vragen finale)
# Vragen:
# 6 - Staat de Mol graag in de schijnwerpers (niet bruikbaar)
# 9 - Wanneer stuurde de Mol een envelop naar Ellis Island:
# 1: Freek, Sofie; 2: Susan;
# 17 - Met welk vervoermiddel verplaatste de Mol zich door de Vigan:
# 1: Sofie, Susan; 2: Freek;
# 20 - Wie is de Mol:
# 1: Freek; 2: Sofie; 3: Susan;
# Antwoorden: Sofie (17, 1) (20, 3), Freek (9, 1), Susan (20, 2)
players9s = [Player.FREEK_14, Player.SOFIE_14, Player.SUSAN_14]
question9s_9 = Question({1: [Player.FREEK_14, Player.SOFIE_14],
                         2: [Player.SUSAN_14]})
question9s_17 = Question({1: [Player.SOFIE_14, Player.SUSAN_14],
                          2: [Player.FREEK_14]})
question9s_20 = Question({1: [Player.FREEK_14], 2: [Player.SOFIE_14], 3: [Player.SUSAN_14]})
result9s = Result(DropType.POSSIBLE_DROP, [Player.FREEK_14, Player.SUSAN_14])
episode9s = Episode(players9s, result9s,
                    {Player.SOFIE_14: TestInput({17: 1, 20: 3}), Player.FREEK_14: TestInput({9: 1}),
                     Player.SUSAN_14: TestInput({20: 2})},
                    {9: question9s_9, 17: question9s_17, 20: question9s_20})

season14 = Season(players1, {0.5: episode1f, 1: episode1s, 2: episode2, 3: episode3, 4: episode4, 5: episode5,
                             6: episode6, 7: episode7, 8: episode8, 8.5: episode9f, 9: episode9s})