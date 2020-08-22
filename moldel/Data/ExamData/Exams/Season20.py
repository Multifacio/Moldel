from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

# Aflevering 1 (afvaller: Anita)
# Vragen:
# 1 - De Mol is een:
# 1: Buddy, Claes, Johan, Nathan, Rob; 2: Anita, Jaike, Leonie, Miljuschka, Tina;
# 2 - Waar stond de Mol op de groepsfoto van aflevering 1:
# 1: Anita, Buddy, Claes, Jaike, Miljuschka, Tina; 2: Johan, Leonie, Nathan, Rob;
# 4 - Welke keuze maakte de Mol tijdens de opdracht 'Wijsheid & Geluk':
# 1: Jaike, Leonie, Rob, Tina; 2: Anita, Buddy, Claes, Johan, Miljuschka, Nathan;
# 11 - Is de Mol de huidige penningmeester:
# 1: Johan; 2: Anita, Buddy, Claes, Jaike, Leonie, Miljuschka, Nathan, Rob, Tina;
# 13 - Welke escape room had de Mol tijdens de opdracht 'Parkeertarief':
# 1: Leonie, Rob; 2: Claes, Tina; 3: Miljuschka, Nathan; 4: Jaike, Johan; 5: Anita, Buddy;
# 18 - Welk teken had de vrachtwagen van de Mol tijdens de opdracht 'Parkeertarief':
# 1: Miljuschka, Nathan; 2: Jaike, Johan; 3: Leonie, Rob; 4: Anita, Buddy, Claes, Tina;
# 20 - Wie is de Mol:
# 1: Anita; 2: Buddy; 3: Claes; 4: Jaike; 5: Johan; 6: Leonie; 7: Miljuschka; 8: Nathan; 9: Rob; 10: Tina;
# Antwoorden: Leonie (4, 2) (Zwarte vrijstelling), Rob (18, 2), Buddy (Vrijstelling), Anita (Vrijstelling), Tina (11, 1),
# Johan (20, 1) (Vrijstelling), Jaike (2, 1) (Zwarte vrijstelling), Nathan (1, 1) (Vrijstelling),
# Claes (13, 2) (Vrijstelling), Miljuschka (Vrijstelling)
players1 = [Player.ANITA_20, Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.JOHAN_20, Player.LEONIE_20,
            Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20, Player.TINA_20]
question1_1 = Question({1: [Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20, Player.NATHAN_20, Player.ROB_20],
                        2: [Player.ANITA_20, Player.JAIKE_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.TINA_20]})
question1_2 = Question({1: [Player.ANITA_20, Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.MILJUSCHKA_20,
                            Player.TINA_20],
                        2: [Player.JOHAN_20, Player.LEONIE_20, Player.NATHAN_20, Player.ROB_20]})
question1_4 = Question({1: [Player.JAIKE_20, Player.LEONIE_20, Player.ROB_20, Player.TINA_20],
                        2: [Player.ANITA_20, Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20, Player.MILJUSCHKA_20,
                            Player.NATHAN_20]})
question1_11 = Question({1: [Player.JOHAN_20],
                         2: [Player.ANITA_20, Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.LEONIE_20,
                             Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20, Player.TINA_20]})
question1_13 = Question({1: [Player.LEONIE_20, Player.ROB_20],
                         2: [Player.CLAES_20, Player.TINA_20],
                         3: [Player.MILJUSCHKA_20, Player.NATHAN_20],
                         4: [Player.JAIKE_20, Player.JOHAN_20],
                         5: [Player.ANITA_20, Player.BUDDY_20]})
question1_18 = Question({1: [Player.MILJUSCHKA_20, Player.NATHAN_20],
                         2: [Player.JAIKE_20, Player.JOHAN_20],
                         3: [Player.LEONIE_20, Player.ROB_20],
                         4: [Player.ANITA_20, Player.BUDDY_20, Player.CLAES_20, Player.TINA_20]})
question1_20 = Question({1: [Player.ANITA_20], 2: [Player.BUDDY_20], 3: [Player.CLAES_20], 4: [Player.JAIKE_20],
                         5: [Player.JOHAN_20], 6: [Player.LEONIE_20], 7: [Player.MILJUSCHKA_20], 8: [Player.NATHAN_20],
                         9: [Player.ROB_20], 10: [Player.TINA_20]})
result1 = Result(DropType.EXECUTION_DROP, [Player.ANITA_20])
episode1 = Episode(players1, result1,
                   {Player.LEONIE_20: TestInput({4: 2}), Player.ROB_20: TestInput({18: 2}),
                    Player.TINA_20: TestInput({11: 1}), Player.JOHAN_20: TestInput({20: 1}),
                    Player.JAIKE_20: TestInput({2: 1}), Player.NATHAN_20: TestInput({1: 1}),
                    Player.CLAES_20: TestInput({13: 2})},
                   {1: question1_1, 2: question1_2, 4: question1_4, 11: question1_11, 13: question1_13,
                    18: question1_18, 20: question1_20})

# Aflevering 2 (afvaller: Tina)
# 1 - De Mol is een:
# 1: Buddy, Claes, Johan, Nathan, Rob; 2: Jaike, Leonie, Miljuschka, Tina;
# 5 - Welke kleur had het station van de Mol tijdens de opdracht 'Kleurwerk':
# 1: Buddy, Jaike; 2: Claes, Rob; 3: Johan, Tina; 4: Leonie, Miljuschka, Nathan;
# 9 - Is het kleurkanon van de Mol afgegaan tijdens de opdracht 'Kleurwerk':
# 1: Buddy, Claes, Jaike, Johan, Rob, Tina; 2: Leonie, Miljuschka, Nathan;
# 14 - In welke taxi stapte de Mol bij aanvang van de opdracht 'Afhaalchinees':
# 1: Nathan, Rob; 2: Tina; 3: Buddy, Leonie; 4: Claes, Jaike; 5: Johan, Miljuschka;
# 18 - Wat was de positie van de Mol tijdens de opdracht 'Wereldbeeld':
# 1: Johan, Leonie; 2: Buddy, Claes, Jaike, Miljuschka, Nathan, Rob, Tina;
# Antwoorden: Miljuschka (1, 2), Buddy (5, 3), Johan (9, 2), Jaike (14, 5), Claes (18, 1), Tina (Zwarte vrijstelling)
players2 = [Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.JOHAN_20, Player.LEONIE_20, Player.MILJUSCHKA_20,
            Player.NATHAN_20, Player.ROB_20, Player.TINA_20]
question2_1 = Question({1: [Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20, Player.NATHAN_20, Player.ROB_20],
                        2: [Player.JAIKE_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.TINA_20]})
question2_5 = Question({1: [Player.BUDDY_20, Player.JAIKE_20],
                        2: [Player.CLAES_20, Player.ROB_20],
                        3: [Player.JOHAN_20, Player.TINA_20],
                        4: [Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20]})
question2_9 = Question({1: [Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.JOHAN_20, Player.ROB_20,
                            Player.TINA_20],
                        2: [Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20]})
question2_14 = Question({1: [Player.NATHAN_20, Player.ROB_20],
                         2: [Player.TINA_20],
                         3: [Player.BUDDY_20, Player.LEONIE_20],
                         4: [Player.CLAES_20, Player.JAIKE_20],
                         5: [Player.JOHAN_20, Player.MILJUSCHKA_20]})
question2_18 = Question({1: [Player.JOHAN_20, Player.LEONIE_20],
                         2: [Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.MILJUSCHKA_20, Player.NATHAN_20,
                             Player.ROB_20, Player.TINA_20]})
result2 = Result(DropType.EXECUTION_DROP, [Player.TINA_20])
episode2 = Episode(players2, result2,
                   {Player.MILJUSCHKA_20: TestInput({1: 2}), Player.BUDDY_20: TestInput({5: 3}),
                    Player.JOHAN_20: TestInput({9: 2}), Player.JAIKE_20: TestInput({14: 5}),
                    Player.CLAES_20: TestInput({18: 1})},
                   {1: question2_1, 5: question2_5, 9: question2_9, 14: question2_14, 18: question2_18})

# Aflevering 3 (afvaller: Jaike)
# 1 - De Mol is een:
# 1: Buddy, Claes, Johan, Nathan, Rob; 2: Jaike, Leonie, Miljuschka;
# 3 - Waar was de Mol bij aanvang van de opdracht 'Lijn(ver)diensten':
# 1: Buddy, Miljuschka; 2: Claes, Jaike, Johan, Leonie, Nathan, Rob;
# 7 - In welke LIJN zat de Mol aan het einde van de opdracht 'Lijn(ver)diensten':
# 1: Miljuschka, Rob; 2: Nathan; 3: Buddy, Claes, Jaike, Johan, Leonie;
# 18 - Plaatste het team van de Mol als eerste een serviesstuk tijdens de opdracht 'Theepot':
# 1: Johan, Miljuschka; 2: Buddy, Claes, Jaike, Leonie, Nathan, Rob;
# 20 - Wie is de Mol:
# 1: Buddy; 2: Claes; 3: Jaike; 4: Johan; 5: Leonie; 6: Miljuschka; 7: Nathan; 8: Rob;
# Antwoorden: Jaike (3, 1), Johan (7, 3), Miljuschka (18, 1), Claes (20, 1), Rob (1, 1), Buddy (20, 5)
players3 = [Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.JOHAN_20, Player.LEONIE_20, Player.MILJUSCHKA_20,
            Player.NATHAN_20, Player.ROB_20]
question3_1 = Question({1: [Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20, Player.NATHAN_20, Player.ROB_20],
                        2: [Player.JAIKE_20, Player.LEONIE_20, Player.MILJUSCHKA_20]})
question3_3 = Question({1: [Player.BUDDY_20, Player.MILJUSCHKA_20],
                        2: [Player.CLAES_20, Player.JAIKE_20, Player.JOHAN_20, Player.LEONIE_20, Player.NATHAN_20,
                            Player.ROB_20]})
question3_7 = Question({1: [Player.MILJUSCHKA_20, Player.ROB_20],
                        2: [Player.NATHAN_20],
                        3: [Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.JOHAN_20, Player.LEONIE_20]})
question3_18 = Question({1: [Player.JOHAN_20, Player.MILJUSCHKA_20],
                         2: [Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.LEONIE_20, Player.NATHAN_20,
                             Player.ROB_20]})
question3_20 = Question({1: [Player.BUDDY_20], 2: [Player.CLAES_20], 3: [Player.JAIKE_20], 4: [Player.JOHAN_20],
                         5: [Player.LEONIE_20], 6: [Player.MILJUSCHKA_20], 7: [Player.NATHAN_20], 8: [Player.ROB_20]})
result3 = Result(DropType.EXECUTION_DROP, [Player.JAIKE_20])
episode3 = Episode(players3, result3,
                   {Player.JAIKE_20: TestInput({3: 1}), Player.JOHAN_20: TestInput({7: 3}),
                    Player.MILJUSCHKA_20: TestInput({18: 1}), Player.CLAES_20: TestInput({20: 1}),
                    Player.ROB_20: TestInput({1: 1}), Player.BUDDY_20: TestInput({20: 5})},
                   {1: question3_1, 3: question3_3, 7: question3_7, 18: question3_18, 20: question3_20})

# Aflevering 4 (geen afvaller en geen informatie, maar wel data ingevoerd voor de regressie)
# 1 - De Mol is een:
# 1: Buddy, Claes, Johan, Nathan, Rob; 2: Leonie, Miljuschka;
# 5 - Met wie ging de Mol door het parcours tijdens de opdracht 'Porseleinen Kamer':
# 1: Johan; 2: Claes; 3: Nathan; 4: Rob; 5: Leonie; 6: Miljuschka; 7: Buddy;
# 7 - Welke waarde had de stok van de Mol tijdens de opdracht 'Porseleinen Kamer':
# 1: Leonie, Nathan; 2: Claes, Johan; 3: Miljuschka, Rob; 4: Buddy;
# 14 - Wat was de taak van de Mol tijdens de opdracht 'Verkeer(d)':
# 1: Johan, Rob; 2: Buddy, Claes, Leonie, Nathan; 3: Miljuschka;
# 20 - Wie is de Mol:
# 1: Buddy; 2: Claes; 3: Johan; 4: Leonie; 5: Miljuschka; 6: Nathan; 7: Rob;
# Antwoorden: Claes (1, 1), Rob (5, 7), Nathan (7, 3), Johan (14, 2), Leonie (20, 5), Miljuschka (20, 6)
players4 = [Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20,
            Player.ROB_20]
question4_1 = Question({1: [Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20, Player.NATHAN_20, Player.ROB_20],
                        2: [Player.LEONIE_20, Player.MILJUSCHKA_20]})
question4_5 = Question({1: [Player.JOHAN_20], 2: [Player.CLAES_20], 3: [Player.NATHAN_20], 4: [Player.ROB_20],
                        5: [Player.LEONIE_20], 6: [Player.MILJUSCHKA_20], 7: [Player.BUDDY_20]})
question4_7 = Question({1: [Player.LEONIE_20, Player.NATHAN_20],
                        2: [Player.CLAES_20, Player.JOHAN_20],
                        3: [Player.MILJUSCHKA_20, Player.ROB_20],
                        4: [Player.BUDDY_20]})
question4_14 = Question({1: [Player.JOHAN_20, Player.ROB_20],
                         2: [Player.BUDDY_20, Player.CLAES_20, Player.LEONIE_20, Player.NATHAN_20],
                         3: [Player.MILJUSCHKA_20]})
question4_20 = Question({1: [Player.BUDDY_20], 2: [Player.CLAES_20], 3: [Player.JOHAN_20], 4: [Player.LEONIE_20],
                         5: [Player.MILJUSCHKA_20], 6: [Player.NATHAN_20], 7: [Player.ROB_20]})
result4 = Result(DropType.NO_DROP_NOR_SCREENS, [])
episode4 = Episode(players4, result4,
                   {Player.CLAES_20: TestInput({1: 1}), Player.ROB_20: TestInput({5: 7}),
                    Player.NATHAN_20: TestInput({7: 3}), Player.JOHAN_20: TestInput({14: 2}),
                    Player.LEONIE_20: TestInput({20: 5}), Player.MILJUSCHKA_20: TestInput({20: 6})},
                   {1: question4_1, 5: question4_5, 7: question4_7, 14: question4_14, 20: question4_20})

# Aflevering 5 (afvaller: Johan)
# 2 - Met welke deelopdracht startte de Mol tijdens 'Beeld en Geluid':
# 1: Buddy; 2: Johan; 3: Leonie; 4: Rob; 5: Nathan; 6: Claes; 7: Miljuschka;
# 3 - Is de Mol uit het spel geraakt tijdens de opdracht 'Beeld en Geluid':
# 1: Johan, Miljuschka, Nathan; 2: Buddy, Claes, Leonie, Rob;
# 6 - Wat is de geboortedatum van de Mol:
# 1: Claes; 2: Leonie; 3: Johan; 4: Nathan; 5: Miljuschka; 6: Rob; 7: Buddy;
# 11 - Welke letters haalde het team van de Mol binnen tijdens de opdracht 'Lettergreep':
# 1: Claes, Leonie, Rob; 2: Buddy, Miljuschka; 3: Johan, Nathan;
# 17 - Als hoeveelste kwam de Mol bij Rik tijdens de opdracht 'Lezen en Schrijven': (Laatste 3 antwoorden niet zeker)
# 1: Claes; 2: Miljuschka; 3: Buddy; 4: Nathan; 5: Rob; 6: Leonie; 7: Johan;
# 20 - Wie is de Mol:
# 1: Buddy; 2: Claes; 3: Johan; 4: Leonie; 5: Miljuschka; 6: Nathan; 7: Rob;
# Antwoorden: Buddy (2, 3), Leonie (20, 5), Miljuschka (6, 2), Johan (17, 3), Claes (3, 2), Nathan (11, 2),
# Rob (20, 1) (Zwarte vrijstelling)
players5 = [Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20,
            Player.ROB_20]
question5_2 = Question({1: [Player.BUDDY_20], 2: [Player.JOHAN_20], 3: [Player.LEONIE_20], 4: [Player.ROB_20],
                        5: [Player.NATHAN_20], 6: [Player.CLAES_20], 7: [Player.MILJUSCHKA_20]})
question5_3 = Question({1: [Player.JOHAN_20, Player.MILJUSCHKA_20, Player.NATHAN_20],
                        2: [Player.BUDDY_20, Player.CLAES_20, Player.LEONIE_20, Player.ROB_20]})
question5_6 = Question({1: [Player.CLAES_20], 2: [Player.LEONIE_20], 3: [Player.JOHAN_20], 4: [Player.NATHAN_20],
                        5: [Player.MILJUSCHKA_20], 6: [Player.ROB_20], 7: [Player.BUDDY_20]})
question5_11 = Question({1: [Player.CLAES_20, Player.LEONIE_20, Player.ROB_20],
                         2: [Player.BUDDY_20, Player.MILJUSCHKA_20],
                         3: [Player.JOHAN_20, Player.NATHAN_20]})
question5_17 = Question({1: [Player.CLAES_20], 2: [Player.MILJUSCHKA_20], 3: [Player.BUDDY_20], 4: [Player.NATHAN_20],
                         5: [Player.ROB_20], 6: [Player.LEONIE_20], 7: [Player.JOHAN_20]})
question5_20 = Question({1: [Player.BUDDY_20], 2: [Player.CLAES_20], 3: [Player.JOHAN_20], 4: [Player.LEONIE_20],
                         5: [Player.MILJUSCHKA_20], 6: [Player.NATHAN_20], 7: [Player.ROB_20]})
result5 = Result(DropType.EXECUTION_DROP, [Player.JOHAN_20])
episode5 = Episode(players5, result5,
                   {Player.BUDDY_20: TestInput({2: 3}), Player.LEONIE_20: TestInput({20: 5}),
                    Player.MILJUSCHKA_20: TestInput({6: 2}), Player.JOHAN_20: TestInput({17: 3}),
                    Player.CLAES_20: TestInput({3: 2}), Player.NATHAN_20: TestInput({11: 2}),
                    Player.ROB_20: TestInput({20: 1})},
                   {2: question5_2, 3: question5_3, 6: question5_6, 11: question5_11, 17: question5_17,
                    20: question5_20})

# Aflevering 6 (afvaller: Claes)
# 1 - De Mol is een:
# 1: Buddy, Claes, Nathan, Rob; 2: Leonie, Miljuschka;
# 4 - Vond de Mol de derde telefoon tijdens de opdracht 'Voice Mol':
# 1: Nathan; 2: Buddy, Claes, Leonie, Miljuschka, Rob;
# 8 - Welke kleur vlag had het groepje van de Mol tijdens de opdracht 'Vak Werk':
# 1: Claes; 2: Rob; 3: Leonie; 4: Buddy; 5: Miljuschka; 6: Nathan;
# 14 - Als hoeveelste ging de Mol naar binnen tijdens de opdracht: 'Alles Kenners':
# 1: Rob; 2: Buddy; 3: Leonie; 4: Miljuschka; 5: Claes; 6: Nathan;
# 20 - Wie is de Mol:
# 1: Buddy; 2: Claes; 3: Leonie; 4: Miljuschka; 5: Nathan; 6: Rob;
# Antwoorden: Rob (1, 1), Buddy (4, 2), Leonie (8, 5), Claes (14, 2), Miljuschka (20, 3), Nathan (20, 4)
players6 = [Player.BUDDY_20, Player.CLAES_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20]
question6_1 = Question({1: [Player.BUDDY_20, Player.CLAES_20, Player.NATHAN_20, Player.ROB_20],
                        2: [Player.LEONIE_20, Player.MILJUSCHKA_20]})
question6_4 = Question({1: [Player.NATHAN_20],
                        2: [Player.BUDDY_20, Player.CLAES_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.ROB_20]})
question6_8 = Question({1: [Player.CLAES_20], 2: [Player.ROB_20], 3: [Player.LEONIE_20], 4: [Player.BUDDY_20],
                        5: [Player.MILJUSCHKA_20], 6: [Player.NATHAN_20]})
question6_14 = Question({1: [Player.ROB_20], 2: [Player.BUDDY_20], 3: [Player.LEONIE_20], 4: [Player.MILJUSCHKA_20],
                         5: [Player.CLAES_20], 6: [Player.NATHAN_20]})
question6_20 = Question({1: [Player.BUDDY_20], 2: [Player.CLAES_20], 3: [Player.LEONIE_20], 4: [Player.MILJUSCHKA_20],
                         5: [Player.NATHAN_20], 6: [Player.ROB_20]})
result6 = Result(DropType.EXECUTION_DROP, [Player.CLAES_20])
episode6 = Episode(players6, result6,
                   {Player.ROB_20: TestInput({1: 1}), Player.BUDDY_20: TestInput({4: 2}),
                    Player.LEONIE_20: TestInput({8: 5}), Player.CLAES_20: TestInput({14: 2}),
                    Player.MILJUSCHKA_20: TestInput({20: 3}), Player.NATHAN_20: TestInput({20: 4})},
                   {1: question6_1, 4: question6_4, 8: question6_8, 14: question6_14, 20: question6_20})

# Aflevering 7 (geen afvaller, alleen Buddy en Nathan kregen hun scherm te zien)
# 1 - De Mol is een:
# 1: Buddy, Nathan, Rob; 2: Leonie, Miljuschka;
# 3 - Als de Mol een dag iemand anders mocht zijn, wie zou dat dan zijn (Niet bruikbaar)
# 5 - Gaf de Mol de eerste wagenkleur door tijdens de opdracht 'Kleur Rijk':
# 1: Miljuschka; 2: Buddy, Leonie, Nathan, Rob;
# 20 - Wie is de Mol:
# 1: Buddy; 2: Leonie; 3: Miljuschka; 4: Nathan; 5: Rob;
# Antwoorden: Miljuschka (1, 2), Leonie (5, 2), Buddy (20, 2)
players7 = [Player.BUDDY_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20]
question7_1 = Question({1: [Player.BUDDY_20, Player.NATHAN_20, Player.ROB_20],
                        2: [Player.LEONIE_20, Player.MILJUSCHKA_20]})
question7_5 = Question({1: [Player.MILJUSCHKA_20],
                        2: [Player.BUDDY_20, Player.LEONIE_20, Player.NATHAN_20, Player.ROB_20]})
question7_20 = Question({1: [Player.BUDDY_20], 2: [Player.LEONIE_20], 3: [Player.MILJUSCHKA_20], 4: [Player.NATHAN_20],
                         5: [Player.ROB_20]})
result7 = Result(DropType.POSSIBLE_DROP, [Player.LEONIE_20, Player.MILJUSCHKA_20, Player.ROB_20])
episode7 = Episode(players7, result7,
                   {Player.MILJUSCHKA_20: TestInput({1: 2}), Player.LEONIE_20: TestInput({5: 2}),
                    Player.BUDDY_20: TestInput({20: 2})},
                   {1: question7_1, 5: question7_5, 20: question7_20})

# Aflevering 8 (afvaller: Leonie)
# 3 - De Mol begon de opdracht 'Doorzichtig' bij:
# 1: Buddy; 2: Nathan 3: Rob; 4: Leonie; 5: Miljuschka;
# 5 - Op welke fietsen heeft de mol gefietst tijdens de opdracht 'Kettingreacties':
# 1: Buddy; 2: Leonie; 3: Nathan; 4: Miljuschka, Rob;
# 13 - Hoe vaak heeft de Mol de tafel gedraaid tijdens de opdracht 'Je Draai Vinden' (Niet 100% zeker in welk antwoord
# Leonie zich bevindt):
# 1: Buddy, Leonie; 2: Miljuschka, Nathan, Rob;
# 14 - Hoeveel punten had de Mol na vraag 10 tijdens de opdracht 'Je Draai Vinden':
# 1: Leonie; 2: Buddy, Rob; 3: Miljuschka, Nathan;
# 20 - Wie is de Mol:
# 1: Buddy; 2: Leonie; 3: Miljuschka; 4: Nathan; 5: Rob;
# Antwoorden: Rob (3, 4) (20, 2), Buddy (14, 1) (20, 2), Miljuschka (13, 1) (20, 2) (Vrijstelling),
# Nathan (5, 2) (20, 2)
players8 = [Player.BUDDY_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20]
question8_3 = Question({1: [Player.BUDDY_20], 2: [Player.NATHAN_20], 3: [Player.ROB_20], 4: [Player.LEONIE_20],
                        5: [Player.MILJUSCHKA_20]})
question8_5 = Question({1: [Player.BUDDY_20],
                        2: [Player.LEONIE_20],
                        3: [Player.NATHAN_20],
                        4: [Player.MILJUSCHKA_20, Player.ROB_20]})
question8_13 = Question({1: [Player.BUDDY_20, Player.LEONIE_20],
                         2: [Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20]})
question8_14 = Question({1: [Player.LEONIE_20],
                         2: [Player.BUDDY_20, Player.ROB_20],
                         3: [Player.MILJUSCHKA_20, Player.NATHAN_20]})
question8_20 = Question({1: [Player.BUDDY_20], 2: [Player.LEONIE_20], 3: [Player.MILJUSCHKA_20], 4: [Player.NATHAN_20],
                         5: [Player.ROB_20]})
result8 = Result(DropType.EXECUTION_DROP, [Player.LEONIE_20])
episode8 = Episode(players8, result8,
                   {Player.ROB_20: TestInput({3: 4, 20: 2}), Player.BUDDY_20: TestInput({14: 1, 20: 2}),
                    Player.MILJUSCHKA_20: TestInput({13: 1, 20: 2}, immunity = True),
                    Player.NATHAN_20: TestInput({5: 2, 20: 2})},
                   {3: question8_3, 5: question8_5, 13: question8_13, 14: question8_14, 20: question8_20})

# Aflevering 9 (afvaller: Miljuschka, Nathan) (pas in de reunie bekend)
# 6 - Was de Mol binnen de tijd terug aan het einde van de opdracht 'Kettingreactie':
# 1: Nathan; 2: Buddy; 3: Miljuschka, Rob;
# 11 - Waar was de Mol bij aanvang van de opdracht 'Lijn(ver)diensten':
# 1: Buddy, Miljuschka; 2: Nathan, Rob;
# 15 - Welke waarde had de stok van de Mol tijdens de opdracht 'Porseleinen Kamer' (Foutieve vraag, want Nathan wordt
# door geen enkel antwoord gecovered)
# 18 - Welk teken had de vrachtwagen van de Mol tijdens de opdracht 'Parkeertarief':
# 1: Miljuschka, Nathan; 2: Rob; 3: Buddy;
# 27 - Als hoeveelste ging de Mol het doolhofje binnen tijdens de opdracht 'Alles kenners':
# 1: Rob; 2: Buddy; 3: Miljuschka; 4: Nathan;
# 35 - Bij welk kistje begon de Mol tijdens de opdracht 'Doorzichtig':
# 1: Buddy; 2: Nathan; 3: Rob; 4: Miljuschka;
# 38 - Met wie was de Mol een duo tijdens de opdracht 'Cijferkunst':
# 1: Miljuschka; 2: Rob; 3: Nathan; 4: Buddy;
# 40 - Wie is de Mol:
# 1: Buddy; 2: Miljuschka; 3: Nathan; 4: Rob;
# Antwoorden: Buddy (18, 3) (27, 1) (40, 4), Rob (6, 2) (11, 1) (40, 1), Nathan (35, 3) (40, 4),
# Miljuschka (38, 2) (40, 4)
players9 = [Player.BUDDY_20, Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20]
question9_6 = Question({1: [Player.NATHAN_20],
                        2: [Player.BUDDY_20],
                        3: [Player.MILJUSCHKA_20, Player.ROB_20]})
question9_11 = Question({1: [Player.BUDDY_20, Player.MILJUSCHKA_20],
                         2: [Player.NATHAN_20, Player.ROB_20]})
question9_18 = Question({1: [Player.MILJUSCHKA_20, Player.NATHAN_20],
                         2: [Player.ROB_20],
                         3: [Player.BUDDY_20]})
question9_27 = Question({1: [Player.ROB_20], 2: [Player.BUDDY_20], 3: [Player.MILJUSCHKA_20], 4: [Player.NATHAN_20]})
question9_35 = Question({1: [Player.BUDDY_20], 2: [Player.NATHAN_20], 3: [Player.ROB_20], 4: [Player.MILJUSCHKA_20]})
question9_38 = Question({1: [Player.MILJUSCHKA_20], 2: [Player.ROB_20], 3: [Player.NATHAN_20], 4: [Player.BUDDY_20]})
question9_40 = Question({1: [Player.BUDDY_20], 2: [Player.MILJUSCHKA_20], 3: [Player.NATHAN_20], 4: [Player.ROB_20]})
result9 = Result(DropType.EXECUTION_DROP, [Player.MILJUSCHKA_20, Player.NATHAN_20])
episode9 = Episode(players9, result9,
                   {Player.BUDDY_20: TestInput({18: 3, 27: 1, 40: 4}), Player.ROB_20: TestInput({6: 2, 11: 1, 40: 1}),
                    Player.NATHAN_20: TestInput({35: 3, 40: 4}), Player.MILJUSCHKA_20: TestInput({38: 2, 40: 4})},
                   {6: question9_6, 11: question9_11, 18: question9_18, 27: question9_27, 35: question9_35,
                    38: question9_38, 40: question9_40}, num_questions = 40)

season20 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                             8: episode8, 10: episode9})