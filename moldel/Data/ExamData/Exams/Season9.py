from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Vera)
# 2 - Wanneer liep de Mol naar de laptop bij de vier Mollen:
# 1: Vera; 2: Anniek; 3: Sebastiaan; 4: Paula; 5: Vivienne; 6: Froukje; 7: Jon; 8: Dennis; 9: Rick; 10 Hans;
# 5 - Droeg de Mol een helm met een camera op het hoofd tijdens de Fabrieksopdracht:
# 1: Dennis, Froukje, Sebastiaan; 2: Anniek, Hans, Jon, Paula, Rick, Vera, Vivienne;
# 7 - In welk team zat de Mol tijdens het Vrijstellingsspel:
# 1: Paula, Vera; 2: Froukje, Rick; 3: Dennis, Jon; 4: Anniek, Vivienne; 5: Hans, Sebastiaan;
# 10 - Heeft de Mol zijn topito afgegeven tijdens het Vrijstellingsspel:
# 1: Anniek, Froukje, Vera, Vivienne; 2: Dennis, Jon, Paula, Rick; 3: Hans, Sebastiaan;
# 14 - Stond de Mol in de finale van het Vrijstellingsspel:
# 1: Paula, Rick; 2: Anniek, Dennis, Froukje, Hans, Jon, Sebastiaan, Vera, Vivienne;
# 20 - Wie is de Mol:
# 1: Anniek; 2: Dennis; 3: Froukje; 4: Hans; 5: Jon; 6: Paula; 7: Rick; 8: Sebastiaan; 9: Vera; 10: Vivienne;
# Antwoorden: Paula (10, 2), Vivienne (5, 2), Hans (20, 3), Froukje (2, 10), Jon (7, 5), Anniek (14, 1)
players1 = [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.HANS_9, Player.JON_9, Player.PAULA_9,
            Player.RICK_9, Player.SEBASTIAAN_9, Player.VERA_9, Player.VIVIENNE_9]
question1_2 = Question({1: [Player.VERA_9], 2: [Player.ANNIEK_9], 3: [Player.SEBASTIAAN_9], 4: [Player.PAULA_9],
                        5: [Player.VIVIENNE_9], 6: [Player.FROUKJE_9], 7: [Player.JON_9], 8: [Player.DENNIS_9],
                        9: [Player.RICK_9], 10: [Player.HANS_9]})
question1_5 = Question({1: [Player.DENNIS_9, Player.FROUKJE_9, Player.SEBASTIAAN_9],
                        2: [Player.ANNIEK_9, Player.HANS_9, Player.JON_9, Player.PAULA_9, Player.RICK_9, Player.VERA_9,
                            Player.VIVIENNE_9]})
question1_7 = Question({1: [Player.PAULA_9, Player.VERA_9],
                        2: [Player.FROUKJE_9, Player.RICK_9],
                        3: [Player.DENNIS_9, Player.JON_9],
                        4: [Player.ANNIEK_9, Player.VIVIENNE_9],
                        5: [Player.HANS_9, Player.SEBASTIAAN_9]})
question1_10 = Question({1: [Player.ANNIEK_9, Player.FROUKJE_9, Player.VERA_9, Player.VIVIENNE_9],
                         2: [Player.DENNIS_9, Player.JON_9, Player.PAULA_9, Player.RICK_9],
                         3: [Player.HANS_9, Player.SEBASTIAAN_9]})
question1_14 = Question({1: [Player.PAULA_9, Player.RICK_9],
                         2: [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.HANS_9, Player.JON_9,
                             Player.SEBASTIAAN_9, Player.VERA_9, Player.VIVIENNE_9]})
question1_20 = Question({1: [Player.ANNIEK_9], 2: [Player.DENNIS_9], 3: [Player.FROUKJE_9], 4: [Player.HANS_9],
                         5: [Player.JON_9], 6: [Player.PAULA_9], 7: [Player.RICK_9], 8: [Player.SEBASTIAAN_9],
                         9: [Player.VERA_9], 10: [Player.VIVIENNE_9]})
result1 = Result(DropType.EXECUTION_DROP, [Player.VERA_9])
episode1 = Episode(players1, result1,
                   {Player.PAULA_9: TestInput({10: 2}), Player.VIVIENNE_9: TestInput({5: 2}),
                    Player.HANS_9: TestInput({20: 3}), Player.FROUKJE_9: TestInput({2: 10}),
                    Player.JON_9: TestInput({7: 5}), Player.ANNIEK_9: TestInput({14: 1})},
                   {2: question1_2, 5: question1_5, 7: question1_7, 10: question1_10, 14: question1_14,
                    20: question1_20})

# Aflevering 2 (afvaller: Anniek)
# 3 - Had de Mol bij aanvang van de Bagagebus-opdracht een van de twee lichtste koffers:
# 1: Anniek, Hans; 2: Dennis, Froukje, Jon, Paula, Rick, Sebastiaan, Vivienne;
# 9 - Hoe vaak stond de Mol onderaan het reuzenrad:
# 1: Jon, Sebastiaan; 2: Anniek, Dennis, Paula; 3: Rick; 4: Froukje, Hans, Vivienne;
# 12 - Hoeveel enveloppes vond de Mol in het grote gebouw (Niet helemaal zeker over de antwoorden):
# 1: Froukje, Paula; 2: Anniek, Hans, Rick; 3: Dennis; 4: Vivienne; 5: Sebastiaan; 6: Jon;
# 15 - Bij welke halte wachtte de Mol op de bus:
# 1: Dennis; 2: Froukje; 3: Vivienne; 4: Rick; 5: Jon; 6: Paula; 7: Sebastiaan; 8: Anniek, Hans;
# Antwoorden: Vivienne (3, 1), Rick (9, 1), Hans (12, 1), Paula (15, 1)
players2 = [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.HANS_9, Player.JON_9, Player.PAULA_9,
            Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9]
question2_3 = Question({1: [Player.ANNIEK_9, Player.HANS_9],
                        2: [Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9, Player.PAULA_9, Player.RICK_9,
                            Player.SEBASTIAAN_9, Player.VIVIENNE_9]})
question2_9 = Question({1: [Player.JON_9, Player.SEBASTIAAN_9],
                        2: [Player.ANNIEK_9, Player.DENNIS_9, Player.PAULA_9],
                        3: [Player.RICK_9],
                        4: [Player.FROUKJE_9, Player.HANS_9, Player.VIVIENNE_9]})
question2_12 = Question({1: [Player.FROUKJE_9, Player.PAULA_9],
                         2: [Player.ANNIEK_9, Player.HANS_9, Player.RICK_9],
                         3: [Player.DENNIS_9],
                         4: [Player.VIVIENNE_9],
                         5: [Player.SEBASTIAAN_9],
                         6: [Player.JON_9]})
question2_15 = Question({1: [Player.DENNIS_9], 2: [Player.FROUKJE_9], 3: [Player.VIVIENNE_9], 4: [Player.RICK_9],
                         5: [Player.JON_9], 6: [Player.PAULA_9], 7: [Player.SEBASTIAAN_9],
                         8: [Player.ANNIEK_9, Player.HANS_9]})
result2 = Result(DropType.EXECUTION_DROP, [Player.ANNIEK_9])
episode2 = Episode(players2, result2,
                   {Player.VIVIENNE_9: TestInput({3: 1}), Player.RICK_9: TestInput({9: 1}),
                    Player.HANS_9: TestInput({12: 1}), Player.PAULA_9: TestInput({15: 1})},
                   {3: question2_3, 9: question2_9, 12: question2_12, 15: question2_15})

# Aflevering 3 (afvaller: Hans)
# 11 - Stond de Mol op het podium in het theater:
# 1: Jon; 2: Anniek, Dennis, Froukje, Hans, Paula, Rick, Sebastiaan, Vivienne;
# 16 - Tijdens de opdracht op het autokerkhof was de Mol:
# 1: Jon, Hans, Sebastiaan; 2: Dennis, Paula, Rick; 3: Anniek, Froukje, Vivienne;
# Antwoorden: Paula (16, 2), Jon (11, 2)
players3 = [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.HANS_9, Player.JON_9, Player.PAULA_9,
            Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9]
question3_11 = Question({1: [Player.JON_9],
                         2: [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.HANS_9, Player.PAULA_9,
                             Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9]})
question3_16 = Question({1: [Player.JON_9, Player.HANS_9, Player.SEBASTIAAN_9],
                         2: [Player.DENNIS_9, Player.PAULA_9, Player.RICK_9],
                         3: [Player.ANNIEK_9, Player.FROUKJE_9, Player.VIVIENNE_9]})
result3 = Result(DropType.EXECUTION_DROP, [Player.HANS_9])
episode3 = Episode(players3, result3,
                   {Player.PAULA_9: TestInput({16: 2}), Player.JON_9: TestInput({11: 2})},
                   {11: question3_11, 16: question3_16})

# Aflevering 4 (afvaller: Paula) (Paula heeft 1 fout antwoord extra gekregen, wat betekent dat iedereen +1 joker heeft)
# 3 - Hoeveel geld won de Mol bij de flipperkast:
# 1: Anniek, Froukje; 2: Jon; 3: Rick; 4: Vivienne; 5: Paula; 6: Dennis, Sebastiaan;
# 7 - Heeft de Mol ooit gestemd voor het kopen van kampeerspullen:
# 1: Dennis, Froukje, Jon, Sebastiaan, Vivienne; 2: Anniek, Paula, Rick;
# 11 - Opende de Mol de eerste kist tijdens de Kistenopdracht:
# 1: Vivienne; 2: Anniek, Dennis, Froukje, Jon, Paula, Rick, Sebastiaan,
# 14 - Heeft de Mol een deel van het geld uit de pot laten verdwijnen:
# 1: Sebastiaan; 2: Anniek, Dennis, Froukje, Jon, Paula, Rick, Vivienne;
# 20 - Wie is de Mol:
# 1: Anniek; 2: Dennis; 3: Froukje; 4: Jon; 5: Paula; 6: Rick; 7: Sebastiaan; 8: Vivienne;
# Antwoorden: Sebastiaan (3, 1), Paula (7, 1) (-1 joker), Vivienne (11, 2), Froukje (14, 1),
# Dennis (20, 6 pas bekend vanaf aflevering 6)
players4 = [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9, Player.PAULA_9, Player.RICK_9,
            Player.SEBASTIAAN_9, Player.VIVIENNE_9]
question4_3 = Question({1: [Player.ANNIEK_9, Player.FROUKJE_9],
                        2: [Player.JON_9],
                        3: [Player.RICK_9],
                        4: [Player.VIVIENNE_9],
                        5: [Player.PAULA_9],
                        6: [Player.DENNIS_9, Player.SEBASTIAAN_9]})
question4_7 = Question({1: [Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9],
                        2: [Player.ANNIEK_9, Player.PAULA_9, Player.RICK_9]})
question4_11 = Question({1: [Player.VIVIENNE_9],
                         2: [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9, Player.PAULA_9,
                             Player.RICK_9, Player.SEBASTIAAN_9]})
question4_14 = Question({1: [Player.SEBASTIAAN_9],
                         2: [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9, Player.PAULA_9,
                             Player.RICK_9, Player.VIVIENNE_9]})
question4_20 = Question({1: [Player.ANNIEK_9], 2: [Player.DENNIS_9], 3: [Player.FROUKJE_9], 4: [Player.JON_9],
                         5: [Player.PAULA_9], 6: [Player.RICK_9], 7: [Player.SEBASTIAAN_9], 8: [Player.VIVIENNE_9]})
result4 = Result(DropType.EXECUTION_DROP, [Player.PAULA_9])
episode4 = Episode(players4, result4,
                   {Player.ANNIEK_9: TestInput(jokers = 1),
                    Player.DENNIS_9: TestInput({20: DelayedAnswer(6, 6)}, jokers = 1),
                    Player.FROUKJE_9: TestInput({14: 1}, jokers = 1), Player.JON_9: TestInput(jokers = 1),
                    Player.PAULA_9: TestInput({7: 1}), Player.RICK_9: TestInput(jokers = 1),
                    Player.SEBASTIAAN_9: TestInput({3: 1}, jokers = 1), Player.VIVIENNE_9: TestInput({11: 2}, jokers = 1)},
                   {3: question4_3, 7: question4_7, 11: question4_11, 14: question4_14, 20: question4_20})

# Aflevering 5 (afvaller: Froukje)
# 7 - Waar begon de Mol het spel met de sluipschutters:
# 1: Jon, Vivienne; 2: Anniek, Dennis, Froukje, Rick, Sebastiaan;
# 14 - Gaf de Mol een goed antwoord op het ganzenbord:
# 1: Jon, Vivienne; 2: Anniek, Dennis, Froukje, Rick, Sebastiaan;
# 20 - Wie is de Mol:
# 1: Anniek; 2: Dennis; 3: Froukje; 4: Jon; 5: Rick; 6: Sebastiaan; 7: Vivienne;
# Antwoorden: Dennis (Vrijstelling), Rick (14, 2) (20, 1 pas bekend vanaf aflevering 6),
# Jon (7, 2) (20, 1 pas bekend vanaf aflevering 6), Sebastiaan (20, 5 pas bekend vanaf aflevering 6),
# Anniek (20, 4 pas bekend vanaf aflevering 6), Vivienne (20, 4 pas bekend vanaf aflevering 6)
players5 = [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9, Player.RICK_9, Player.SEBASTIAAN_9,
            Player.VIVIENNE_9]
question5_7 = Question({1: [Player.JON_9, Player.VIVIENNE_9],
                        2: [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.RICK_9, Player.SEBASTIAAN_9]})
question5_14 = Question({1: [Player.JON_9, Player.VIVIENNE_9],
                         2: [Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.RICK_9, Player.SEBASTIAAN_9]})
question5_20 = Question({1: [Player.ANNIEK_9], 2: [Player.DENNIS_9], 3: [Player.FROUKJE_9], 4: [Player.JON_9],
                         5: [Player.RICK_9], 6: [Player.SEBASTIAAN_9], 7: [Player.VIVIENNE_9]})
result5 = Result(DropType.EXECUTION_DROP, [Player.FROUKJE_9])
episode5 = Episode(players5, result5,
                   {Player.DENNIS_9: TestInput(immunity = True),
                    Player.RICK_9: TestInput({14: 2, 20: DelayedAnswer(1, 6)}),
                    Player.JON_9: TestInput({7: 2, 20: DelayedAnswer(1, 6)}),
                    Player.SEBASTIAAN_9: TestInput({20: DelayedAnswer(5, 6)}),
                    Player.ANNIEK_9: TestInput({20: DelayedAnswer(4, 6)}),
                    Player.VIVIENNE_9: TestInput({20: DelayedAnswer(4, 6)})},
                   {7: question5_7, 14: question5_14, 20: question5_20})

# Aflevering 6 (afvaller: Sebastiaan)
# 1 - De Mol is een:
# 1: Dennis, Jon, Rick, Sebastiaan; 2: Anniek, Vivienne;
# 7 - Bij Ben Hur reed de Mol (Foutieve vraag, want Dennis wordt door geen enkel antwoord gecovered)
# 15 - Met wie zat de Mol in een taxi:
# 1: Jon; 2: Rick; 3: Anniek; 4: Dennis; 5: Vivienne; 6: Sebastiaan;
# Antwoorden: Dennis (15, 1), Rick (1, 2)
players6 = [Player.ANNIEK_9, Player.DENNIS_9, Player.JON_9, Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9]
question6_1 = Question({1: [Player.DENNIS_9, Player.JON_9, Player.RICK_9, Player.SEBASTIAAN_9],
                        2: [Player.ANNIEK_9, Player.VIVIENNE_9]})
question6_15 = Question({1: [Player.JON_9], 2: [Player.RICK_9], 3: [Player.ANNIEK_9], 4: [Player.DENNIS_9],
                         5: [Player.VIVIENNE_9], 6: [Player.SEBASTIAAN_9]})
result6 = Result(DropType.EXECUTION_DROP, [Player.SEBASTIAAN_9])
episode6 = Episode(players6, result6,
                   {Player.DENNIS_9: TestInput({15: 1}), Player.RICK_9: TestInput({1: 2})},
                   {1: question6_1, 15: question6_15})

# Aflevering 7 (afvaller: Rick)
# 1 - De Mol is een:
# 1: Dennis, Jon, Rick; 2: Anniek, Vivienne;
# 12 - Heeft de Mol een ijsblok kapot geslagen:
# 1: Dennis, Rick; 2: Anniek, Jon, Vivienne;
# Antwoord: Jon (1, 2), Anniek (12, 2)
players7 = [Player.ANNIEK_9, Player.DENNIS_9, Player.JON_9, Player.RICK_9, Player.VIVIENNE_9]
question7_1 = Question({1: [Player.DENNIS_9, Player.JON_9, Player.RICK_9],
                        2: [Player.ANNIEK_9, Player.VIVIENNE_9]})
question7_12 = Question({1: [Player.DENNIS_9, Player.RICK_9],
                         2: [Player.ANNIEK_9, Player.JON_9, Player.VIVIENNE_9]})
result7 = Result(DropType.EXECUTION_DROP, [Player.RICK_9])
episode7 = Episode(players7, result7,
                   {Player.JON_9: TestInput({1: 2}), Player.ANNIEK_9: TestInput({12: 2})},
                   {1: question7_1, 12: question7_12})

# Aflevering 8 (afvaller: Dennis)
# 4 - Maakte de Mol de foto van de groep voor de schatkamer in Petra:
# 1: Dennis; 2: Anniek, Jon, Vivienne;
# 7 - Hoe lang was het touw van de Mol bij de meetopdracht:
# 1: Anniek, Vivienne; 2: Dennis, Jon;
# 10 - Hoeveel geld verdiende de Mol in de trein:
# 1: Anniek, Dennis; 2: Jon; 3: Vivienne;
# Antwoord: Vivienne (Vrijstelling), Anniek (4, 2), Dennis (10, 2), Jon (7, 1)
players8 = [Player.ANNIEK_9, Player.DENNIS_9, Player.JON_9, Player.VIVIENNE_9]
question8_4 = Question({1: [Player.DENNIS_9],
                        2: [Player.ANNIEK_9, Player.JON_9, Player.VIVIENNE_9]})
question8_7 = Question({1: [Player.ANNIEK_9, Player.VIVIENNE_9],
                        2: [Player.DENNIS_9, Player.JON_9]})
question8_10 = Question({1: [Player.ANNIEK_9, Player.DENNIS_9],
                         2: [Player.JON_9],
                         3: [Player.VIVIENNE_9]})
result8 = Result(DropType.EXECUTION_DROP, [Player.DENNIS_9])
episode8 = Episode(players8, result8,
                   {Player.VIVIENNE_9: TestInput(immunity = True), Player.ANNIEK_9: TestInput({4: 2}),
                    Player.DENNIS_9: TestInput({10: 2}), Player.JON_9: TestInput({7: 1})},
                   {4: question8_4, 7: question8_7, 10: question8_10})

# Aflevering 9 (afvaller: Anniek)
# 23 - Heeft de Mol een vlag omver gereden:
# 1: Vivienne; 2: Anniek, Jon;
# 31 - Stond de Mol op het podium in het theater:
# 1: Jon; 2: Anniek, Vivienne;
# 40 - Wie is de Mol:
# 1: Anniek; 2: Jon; 3: Vivienne;
# Antwoorden: Vivienne (23, 2), Anniek (31, 1), Jon (40, 1)
players9 = [Player.ANNIEK_9, Player.JON_9, Player.VIVIENNE_9]
question9_23 = Question({1: [Player.VIVIENNE_9],
                         2: [Player.ANNIEK_9, Player.JON_9]})
question9_31 = Question({1: [Player.JON_9],
                         2: [Player.ANNIEK_9, Player.VIVIENNE_9]})
question9_40 = Question({1: [Player.ANNIEK_9],
                         2: [Player.JON_9],
                         3: [Player.VIVIENNE_9]})
result9 = Result(DropType.EXECUTION_DROP, [Player.ANNIEK_9])
episode9 = Episode(players9, result9,
                   {Player.VIVIENNE_9: TestInput({23: 2}), Player.ANNIEK_9: TestInput({31: 1}),
                    Player.JON_9: TestInput({40: 1})},
                   {23: question9_23, 31: question9_31, 40: question9_40})

season9 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                            8: episode8, 10: episode9})