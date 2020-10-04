from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Sander)
# 9 - Hoeveel jokers heeft de Mol gisteren verdiend?
# 1: Menno; 2: Inge, Renate; 3: Alex, Dick, Eva, Liesbeth, Nadja, Paul, Sander;
# 15 - Heeft de Mol met een meetlint de afstand van de dieselmotor tot het whiteboard gemeten:
# 1: Inge, Menno; 2: Alex, Dick, Eva, Liesbeth, Nadja, Paul, Renate, Sander;
# 17 - Nam de Mol de telefoon als eerste aan bij de dieselmotor:
# 1: Renate; 2: Alex, Dick, Eva, Inge, Liesbeth, Menno, Nadja, Paul, Sander;
# Antwoorden: Alex (Vrijstelling), Inge (4 jokers), Nadja (15, 1), Renate (17, 2) (4 jokers), Menno (2 jokers),
# Paul (9, 1)
players1 = [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.LIESBETH_7, Player.MENNO_7,
            Player.NADJA_7, Player.PAUL_7, Player.RENATE_7, Player.SANDER_7]
question1_9 = Question({1: [Player.MENNO_7],
                        2: [Player.INGE_7, Player.RENATE_7],
                        3: [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.LIESBETH_7, Player.NADJA_7,
                            Player.PAUL_7, Player.SANDER_7]})
question1_15 = Question({1: [Player.INGE_7, Player.MENNO_7],
                         2: [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.LIESBETH_7, Player.NADJA_7,
                             Player.PAUL_7, Player.RENATE_7, Player.SANDER_7]})
question1_17 = Question({1: [Player.RENATE_7],
                         2: [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.LIESBETH_7,
                             Player.MENNO_7, Player.NADJA_7, Player.PAUL_7, Player.SANDER_7]})
result1 = Result(DropType.EXECUTION_DROP, [Player.SANDER_7])
episode1 = Episode(players1, result1,
                   {Player.ALEX_7: TestInput(immunity = True), Player.INGE_7: TestInput(jokers = 4),
                    Player.NADJA_7: TestInput({15: 1}), Player.RENATE_7: TestInput({17: 2}, jokers = 4),
                    Player.MENNO_7: TestInput(jokers = 2), Player.PAUL_7: TestInput({9: 1})},
                   {9: question1_9, 15: question1_15, 17: question1_17})

# Aflevering 2 (afvaller: Liesbeth)
# 1 - De Mol is een:
# 1: Alex, Dick, Menno, Paul; 2: Eva, Inge, Liesbeth, Nadja, Renate;
# 2 - Wat droeg de Mol tijdens de Chinatown opdracht:
# 1: Alex (Tot knie), Dick (Heel kort), Menno (Tot knie), Sander (Tot knie); 2: Eva (Iets over knieen),
# Liesbeth (Iets over knieen), Nadja (Tot voeten), Paul (Iets over knieen), Renate (Iets over knieen);
# 3: Inge (Duidelijk rok);
# 7 - Wat deed de Mol tijdens de Thaise letters opdracht? De Mol:
# 1: Alex, Inge, Liesbeth, Menno, Paul, Renate; 2: Dick, Eva, Nadja;
# 11 - In welke groep kwam de Mol gisteren aan bij de controlroom (Niet bruikbaar)
# 17 - Als hoeveelste ging de Mol naar beneden bij het abseilen:
# 1: Dick; 2: Nadja; 3: Inge; 4: Menno; 5: Liesbeth; 6: Paul; 7: Eva; 8: Alex, Renate;
# Antwoorden: Menno (2, 1), Liesbeth (7, 2), Renate (1, 2) (2 jokers), Nadja (17, 8)
players2 = [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.LIESBETH_7, Player.MENNO_7,
            Player.NADJA_7, Player.PAUL_7, Player.RENATE_7]
question2_1 = Question({1: [Player.ALEX_7, Player.DICK_7, Player.MENNO_7, Player.PAUL_7],
                        2: [Player.EVA_7, Player.INGE_7, Player.LIESBETH_7, Player.NADJA_7, Player.RENATE_7]})
question2_2 = Question({1: [Player.ALEX_7, Player.DICK_7, Player.MENNO_7, Player.SANDER_7],
                        2: [Player.EVA_7, Player.LIESBETH_7, Player.NADJA_7, Player.PAUL_7, Player.RENATE_7],
                        3: [Player.INGE_7]})
question2_7 = Question({1: [Player.ALEX_7, Player.INGE_7, Player.LIESBETH_7, Player.MENNO_7, Player.PAUL_7,
                            Player.RENATE_7],
                        2: [Player.DICK_7, Player.EVA_7, Player.NADJA_7]})
question2_17 = Question({1: [Player.DICK_7], 2: [Player.NADJA_7], 3: [Player.INGE_7], 4: [Player.MENNO_7],
                         5: [Player.LIESBETH_7], 6: [Player.PAUL_7], 7: [Player.EVA_7],
                         8: [Player.ALEX_7, Player.RENATE_7]})
result2 = Result(DropType.EXECUTION_DROP, [Player.LIESBETH_7])
episode2 = Episode(players2, result2,
                   {Player.MENNO_7: TestInput({2: 1}), Player.LIESBETH_7: TestInput({7: 2}),
                    Player.RENATE_7: TestInput({1: 2}, jokers = 2), Player.NADJA_7: TestInput({17: 8})},
                   {1: question2_1, 2: question2_2, 7: question2_7, 17: question2_17})

# Aflevering 3 (afvaller: Paul)
# 1 - De Mol is een:
# 1: Alex, Dick, Menno, Paul; 2: Eva, Inge, Nadja, Renate;
# 14 - Gaf de Mol vanaf de boot aanwijzingen aan de lopers bij het tempelcomplex:
# 1: Menno, Paul; 2: Alex, Dick, Eva, Inge, Nadja, Renate;
# 18 - Heeft de Mol een joker verdiend in het tempelcomplex in Ayutthaya:
# 1: Alex, Dick, Renate; 2: Eva, Inge, Menno, Nadja, Paul;
# Antwoorden: Alex (18, 1) (1 joker), Renate (1, 2), Paul (14, 1)
players3 = [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.MENNO_7, Player.NADJA_7,
            Player.PAUL_7, Player.RENATE_7]
question3_1 = Question({1: [Player.ALEX_7, Player.DICK_7, Player.MENNO_7, Player.PAUL_7],
                        2: [Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.RENATE_7]})
question3_14 = Question({1: [Player.MENNO_7, Player.PAUL_7],
                         2: [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.RENATE_7]})
question3_18 = Question({1: [Player.ALEX_7, Player.DICK_7, Player.RENATE_7],
                         2: [Player.EVA_7, Player.INGE_7, Player.MENNO_7, Player.NADJA_7, Player.PAUL_7]})
result3 = Result(DropType.EXECUTION_DROP, [Player.PAUL_7])
episode3 = Episode(players3, result3,
                   {Player.ALEX_7: TestInput({18: 1}, jokers = 1), Player.RENATE_7: TestInput({1: 2}),
                    Player.PAUL_7: TestInput({14: 1})},
                   {1: question3_1, 14: question3_14, 18: question3_18})

# Aflevering 4 (afvaller: Menno)
# 1 - De Mol is een:
# 1: Alex, Dick, Menno, Paul; 2: Eva, Inge, Nadja, Renate;
# 4 - Had de Mol zijn molboekje nog na de treinopdracht:
# 1: Alex, Menno, Paul, Renate; 2: Dick, Eva, Inge, Nadja;
# 14 - Met wie zat de Mol in een buggy tijdens de buggyhunt:
# 1: Renate; 2: Menno; 3: Nadja; 4: Dick; 5: Inge; 6: Alex; 7: Eva; 8: Paul;
# 15 - Hoeveel geld werd er in de buggy van de Mol verdiend:
# 1: Inge, Nadja; 2: Alex, Renate; 3: Dick, Menno; 4: Eva; 5: Paul;
# 16 - Heeft de Mol een vrijstelling verdiend na de buggyhunt:
# 1: Nadja; 2: Alex, Dick, Eva, Inge, Menno, Paul, Renate;
# 18 - Wat was de Molactie tijdens de buggyhunt:
# 1: Alex, Inge, Nadja, Renate; 2: Dick, Menno; 3: Eva; 4: Paul;
# 20 - Wie is de Mol:
# 1: Alex; 2: Dick; 3: Eva; 4: Inge; 5: Menno; 6: Nadja; 7: Paul; 8: Renate;
# Antwoorden: Nadja (Vrijstelling), Paul (4, 2), Alex (14, 7) (1 joker), Eva (15, 1) (2 jokers), Inge (18, 1),
# Renate (1, 2), Dick (20, 8), Menno (16, 1)
players4 = [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.MENNO_7, Player.NADJA_7, Player.PAUL_7,
            Player.RENATE_7]
question4_1 = Question({1: [Player.ALEX_7, Player.DICK_7, Player.MENNO_7, Player.PAUL_7],
                        2: [Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.RENATE_7]})
question4_4 = Question({1: [Player.ALEX_7, Player.MENNO_7, Player.PAUL_7, Player.RENATE_7],
                        2: [Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.NADJA_7]})
question4_14 = Question({1: [Player.RENATE_7], 2: [Player.MENNO_7], 3: [Player.NADJA_7], 4: [Player.DICK_7],
                         5: [Player.INGE_7], 6: [Player.ALEX_7], 7: [Player.EVA_7], 8: [Player.PAUL_7]})
question4_15 = Question({1: [Player.INGE_7, Player.NADJA_7],
                         2: [Player.ALEX_7, Player.RENATE_7],
                         3: [Player.DICK_7, Player.MENNO_7],
                         4: [Player.EVA_7],
                         5: [Player.PAUL_7]})
question4_16 = Question({1: [Player.NADJA_7],
                         2: [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.MENNO_7, Player.PAUL_7,
                             Player.RENATE_7]})
question4_18 = Question({1: [Player.ALEX_7, Player.INGE_7, Player.NADJA_7, Player.RENATE_7],
                         2: [Player.DICK_7, Player.MENNO_7],
                         3: [Player.EVA_7],
                         4: [Player.PAUL_7]})
question4_20 = Question({1: [Player.ALEX_7], 2: [Player.DICK_7], 3: [Player.EVA_7], 4: [Player.INGE_7],
                         5: [Player.MENNO_7], 6: [Player.NADJA_7], 7: [Player.PAUL_7], 8: [Player.RENATE_7]})
result4 = Result(DropType.EXECUTION_DROP, [Player.MENNO_7])
episode4 = Episode(players4, result4,
                   {Player.NADJA_7: TestInput(immunity = True), Player.PAUL_7: TestInput({4: 2}),
                    Player.ALEX_7: TestInput({14: 7}, jokers = 1), Player.EVA_7: TestInput({15: 1}, jokers = 2),
                    Player.INGE_7: TestInput({18: 1}), Player.RENATE_7: TestInput({1: 2}),
                    Player.DICK_7: TestInput({20: 8}), Player.MENNO_7: TestInput({16: 1})},
                   {1: question4_1, 4: question4_4, 14: question4_14, 15: question4_15, 16: question4_16,
                    18: question4_18, 20: question4_20})

# Aflevering 5 (afvaller: Alex)
# 1 - De Mol is een:
# 1: Alex, Dick, Paul; 2: Eva, Inge, Nadja, Renate;
# 11 - Heeft de Mol op een olifant gezeten tijdens de olifantenopdracht:
# 1: Nadja; 2: Alex, Dick, Eva, Inge, Paul, Renate;
# 17 - Las de Mol de tekst voor uit de fles bij het Zwembad:
# 1: Renate; 2: Alex, Dick, Eva, Inge, Nadja, Paul;
# Antwoorden: Dick (1, 2), Nadja (17, 1) (4 jokers), Eva (11, 1) (1 joker)
players5 = [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.PAUL_7, Player.RENATE_7]
question5_1 = Question({1: [Player.ALEX_7, Player.DICK_7, Player.PAUL_7],
                        2: [Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.RENATE_7]})
question5_11 = Question({1: [Player.NADJA_7],
                         2: [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.PAUL_7, Player.RENATE_7]})
question5_17 = Question({1: [Player.RENATE_7],
                         2: [Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.PAUL_7]})
result5 = Result(DropType.EXECUTION_DROP, [Player.ALEX_7])
episode5 = Episode(players5, result5,
                   {Player.DICK_7: TestInput({1: 2}), Player.NADJA_7: TestInput({17: 1}, jokers = 4),
                    Player.EVA_7: TestInput({11: 1}, jokers = 1)},
                   {1: question5_1, 11: question5_11, 17: question5_17})

# Aflevering 6 (afvaller: Dick)
# 1 - De Mol is een:
# 1: Dick, Paul; 2: Eva, Inge, Nadja, Renate;
# 12 - Op welke positie hing de foto van de Mol op het pad tijdens de jungle opdracht:
# 1: Nadja; 2: Dick; 3: Renate; 4: Eva, Inge, Paul;
# 18 - Hoeveel jokers heeft de Mol gekocht bij de veiling:
# 1: Eva; 2: Nadja; 3: Dick, Inge, Paul, Renate;
# 20 - Wie is de Mol:
# 1: Dick; 2: Eva; 3: Inge; 4: Nadja; 5: Paul; 6: Renate;
# Antwoorden: Nadja (12, 3), Renate (18, 2), Dick (1, 2 pas bekend in aflevering 7) (18, 3 pas bekend in aflevering 7)
# (20, 6 pas bekend in aflevering 7)
players6 = [Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.PAUL_7, Player.RENATE_7]
question6_1 = Question({1: [Player.DICK_7, Player.PAUL_7],
                        2: [Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.RENATE_7]})
question6_12 = Question({1: [Player.NADJA_7],
                         2: [Player.DICK_7],
                         3: [Player.RENATE_7],
                         4: [Player.EVA_7, Player.INGE_7, Player.PAUL_7]})
question6_18 = Question({1: [Player.EVA_7],
                         2: [Player.NADJA_7],
                         3: [Player.DICK_7, Player.INGE_7, Player.PAUL_7, Player.RENATE_7]})
question6_20 = Question({1: [Player.DICK_7], 2: [Player.EVA_7], 3: [Player.INGE_7], 4: [Player.NADJA_7],
                         5: [Player.PAUL_7], 6: [Player.RENATE_7]})
result6 = Result(DropType.EXECUTION_DROP, [Player.DICK_7])
episode6 = Episode(players6, result6,
                   {Player.NADJA_7: TestInput({12: 3}), Player.RENATE_7: TestInput({18: 2}),
                    Player.DICK_7: TestInput({1: DelayedAnswer(2, 7), 18: DelayedAnswer(3, 7), 20: DelayedAnswer(6, 7)})},
                   {1: question6_1, 12: question6_12, 18: question6_18, 20: question6_20})

# Aflevering 7 (afvaller: Nadja)
# 7 - Op welke positie zat de Mol in de roeiboot:
# 1: Paul; 2: Eva; 3: Inge; 4: Nadja, Renate;
# 20 - Wie is de Mol:
# 1: Eva; 2: Inge; 3: Nadja; 4: Paul; 5: Renate;
# Antwoorden: Paul (7, 3), Renate (20, 3) (1 joker)
players7 = [Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.PAUL_7, Player.RENATE_7]
question7_7 = Question({1: [Player.PAUL_7],
                        2: [Player.EVA_7],
                        3: [Player.INGE_7],
                        4: [Player.NADJA_7, Player.RENATE_7]})
question7_20 = Question({1: [Player.EVA_7], 2: [Player.INGE_7], 3: [Player.NADJA_7], 4: [Player.PAUL_7],
                         5: [Player.RENATE_7]})
result7 = Result(DropType.EXECUTION_DROP, [Player.NADJA_7])
episode7 = Episode(players7, result7,
                   {Player.PAUL_7: TestInput({7: 3}), Player.RENATE_7: TestInput({20: 3}, jokers = 1)},
                   {7: question7_7, 20: question7_20})

# Aflevering 8 (geen afvaller en geen schermen)
# 14 - Welke envelop haalde de Mol vandaag naar beneden:
# 1: Renate; 2: Inge; 3: Eva, Paul;
# 20 - Wie is de Mol:
# 1: Eva; 2: Inge; 3: Paul; 4: Renate;
# Antwoorden: Renate (14, 3) (20, 3), Paul (14, 2) (20, 2), Inge (20, 1), Eva (20, 3)
players8 = [Player.EVA_7, Player.INGE_7, Player.PAUL_7, Player.RENATE_7]
question8_14 = Question({1: [Player.RENATE_7],
                         2: [Player.INGE_7],
                         3: [Player.EVA_7, Player.PAUL_7]})
question8_20 = Question({1: [Player.EVA_7], 2: [Player.INGE_7], 3: [Player.PAUL_7], 4: [Player.RENATE_7]})
result8 = Result(DropType.NO_DROP_NOR_SCREENS, [Player.EVA_7, Player.INGE_7, Player.PAUL_7, Player.RENATE_7])
episode8 = Episode(players8, result8,
                   {Player.RENATE_7: TestInput({14: 3, 20: 3}), Player.PAUL_7: TestInput({14: 2, 20: 2}),
                    Player.INGE_7: TestInput({20: 1}), Player.EVA_7: TestInput({20: 3})},
                   {14: question8_14, 20: question8_20})

# Aflevering 9 (afvaller: Eva, Renate) (pas in de reunie bekend)
# 2 - Wat was de Molactie tijdens het abseilen:
# 1: Renate; 2: Eva, Paul; 3: Inge;
# 3 - Tijdens de jungle opdracht zat de Mol in het:
# 1: Eva, Inge, Paul; 2: Renate;
# 5 - Hoeveel geld werd er in de buggy van de Mol verdiend:
# 1: Inge; 2: Renate; 3: Eva; 4: Paul;
# 11 - Stelde de Mol aan het zwembad voor de groepsindeling van het vlot te veranderen:
# 1: Inge; 2: Eva, Paul, Renate;
# 21 - Met wie zat de Mol in een team bij aanvang van de zeekano-opdracht:
# 1: Renate; 2: Paul; 3: Inge; 4: Eva;
# 27 - Wat was de Molactie tijdens de boksring opdracht:
# 1: Inge, Paul; 2: Eva; 3: Renate;
# Antwoorden: Eva (2, 2) (5, 4), Inge (3, 2) (11, 2), Renate (21, 2) (27, 1)
players9 = [Player.EVA_7, Player.INGE_7, Player.PAUL_7, Player.RENATE_7]
question9_2 = Question({1: [Player.RENATE_7],
                        2: [Player.EVA_7, Player.PAUL_7],
                        3: [Player.INGE_7]})
question9_3 = Question({1: [Player.EVA_7, Player.INGE_7, Player.PAUL_7],
                        2: [Player.RENATE_7]})
question9_5 = Question({1: [Player.INGE_7], 2: [Player.RENATE_7], 3: [Player.EVA_7], 4: [Player.PAUL_7]})
question9_11 = Question({1: [Player.INGE_7],
                         2: [Player.EVA_7, Player.PAUL_7, Player.RENATE_7]})
question9_21 = Question({1: [Player.RENATE_7], 2: [Player.PAUL_7], 3: [Player.INGE_7], 4: [Player.EVA_7]})
question9_27 = Question({1: [Player.INGE_7, Player.PAUL_7],
                         2: [Player.EVA_7],
                         3: [Player.RENATE_7]})
result9 = Result(DropType.EXECUTION_DROP, [Player.EVA_7, Player.RENATE_7])
episode9 = Episode(players9, result9,
                   {Player.EVA_7: TestInput({2: 2, 5: 4}), Player.INGE_7: TestInput({3: 2, 11: 2}),
                    Player.RENATE_7: TestInput({21: 2, 27: 1})},
                   {2: question9_2, 3: question9_3, 5: question9_5, 11: question9_11, 21: question9_21,
                    27: question9_27}, num_questions = 40)

season7 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                            8: episode8, 10: episode9})