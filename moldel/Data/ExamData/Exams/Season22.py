from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Remco)
# Vragen:
# 7 - Heeft de Mol geld uit een kistje gepakt tijdens de opdracht 'Vriend of Vijand':
# 1: Charlotte, Joshua, Lakshmi, Renee, Rocky, Splinter; 2: Erik, Florentijn, Marije, Remco;
# 12 - Met wie vormde de Mol een duo tijdens de opdracht 'Moltainbiken':
# 1: Marije; 2: Joshua; 3: Remco; 4: Erik; 5: Splinter; 6: Charlotte; 7: Florentijn; 8: Rocky; 9: Renee; 10: Lakshmi
# Antwoorden: Erik (12, 6), Remco (7, 2), Marije (1 joker), Rocky (1 joker), Renee (1 joker)
players1 = [Player.CHARLOTTE_22, Player.ERIK_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.LAKSHMI_22,
            Player.MARIJE_22, Player.REMCO_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22]
question1_7 = Question({1: [Player.CHARLOTTE_22, Player.JOSHUA_22, Player.LAKSHMI_22, Player.RENEE_22, Player.ROCKY_22,
                            Player.SPLINTER_22],
                        2: [Player.ERIK_22, Player.FLORENTIJN_22, Player.MARIJE_22, Player.REMCO_22]})
question1_12 = Question({1: [Player.MARIJE_22], 2: [Player.JOSHUA_22], 3: [Player.REMCO_22], 4: [Player.ERIK_22],
                         5: [Player.SPLINTER_22], 6: [Player.CHARLOTTE_22], 7: [Player.FLORENTIJN_22],
                         8: [Player.ROCKY_22], 9: [Player.RENEE_22], 10: [Player.LAKSHMI_22]})
result1 = Result(DropType.EXECUTION_DROP, [Player.REMCO_22])
episode1 = Episode(players1, result1,
                   {Player.ERIK_22: TestInput({12: 6}), Player.REMCO_22: TestInput({7: 2}),
                    Player.MARIJE_22: TestInput(jokers = 1), Player.ROCKY_22: TestInput(jokers = 1),
                    Player.RENEE_22: TestInput(jokers = 1)},
                   {7: question1_7, 12: question1_12})

# Aflevering 2 (afvaller: Erik)
# 1 - De Mol is een:
# 1: Erik, Florentijn, Joshua, Splinter; 2: Charlotte, Lakshmi, Marije, Renee, Rocky;
# 2 - Wat was de rol van de Mol tijdens de opdracht 'Rondleiding' (Vraagnummer onbekend):
# 1: Joshua, Lakshmi; 2: Florentijn, Renee; 3: Erik, Marije, Rocky; 4: Charlotte, Splinter;
# 3 - Wat droeg de Mol op de groepsfoto van aflevering 2 (Vraagnummer onbekend):
# 1: Charlotte, Lakshmi, Marije, Renee (Jurk); 2: Erik, Splinter (Lange Broek); 3: Florentijn, Joshua, Rocky (Korte Broek);
# 6 - De Mol was tijdens de opdracht 'Om de tuin leiden':
# 1: Joshua, Lakshmi; 2: Erik, Marije, Renee, Splinter; 3: Charlotte, Florentijn, Rocky;
# 8 - Is de Mol de huidige penningmeester:
# 1: Erik; 2: Charlotte, Florentijn, Joshua, Lakshmi, Marije, Renee, Rocky, Splinter;
# 10 - Wat was de rol van de Mol tijdens de opdracht met de 'De Dans Ontspringen':
# 1: Charlotte, Joshua, Lakshmi, Marije; 2: Erik, Florentijn, Renee, Rocky, Splinter;
# 12 - Is de Mol afgeschoten tijdens de opdracht met de 'De Dans Ontspringen':
# 1: Charlotte, Erik, Florentijn, Joshua, Marije, Renee, Splinter; 2: Lakshmi, Rocky;
# 16 - Wat was de rol van de Mol tijdens de opdracht 'Symbolisch Bedrag':
# 1: Charlotte, Joshua, Renee, Rocky; 2: Erik, Lakshmi; 3: Marije, Splinter; 4: Florentijn;
# 20 - Wie is de Mol?
# 1: Charlotte; 2: Erik; 3: Florentijn; 4: Joshua; 5: Lakshmi; 6: Marije; 7: Renee; 8: Rocky; 9: Splinter;
# Antwoorden:
# Charlotte (12, 1) (20, 7 pas bekend vanaf aflevering 3) (2, 3 pas bekend vanaf aflevering 3) (6, 2 pas bekend vanaf aflevering 3)
# (16, 1 pas bekend vanaf aflevering 3) (3, 3 pas bekend vanaf aflevering 3),
# Florentijn (2, 3 pas bekend vanaf aflevering 3) (6, 2 pas bekend vanaf aflevering 3) (16, 1 pas bekend vanaf aflevering 3)
# (3, 2 pas bekend vanaf aflevering 3),
# Joshua (10, 2) (6, 3 pas bekend vanaf aflevering 3) (16, 1 pas bekend vanaf aflevering 3) (3, 1 pas bekend vanaf aflevering 3),
# Lakshmi (2, 3 pas bekend vanaf aflevering 3) (6, 2 pas bekend vanaf aflevering 3) (16, 1 pas bekend vanaf aflevering 3)
# (3, 1 pas bekend vanaf aflevering 3),
# Marije (6, 3) (20, 1 pas bekend vanaf aflevering 3) (2, 4 pas bekend vanaf aflevering 3) (16, 1 pas bekend vanaf aflevering 3)
# (3, 3 pas bekend vanaf aflevering 3),
# Renee (8, 2) (20, 6 pas bekend vanaf aflevering 3) (2, 3 pas bekend vanaf aflevering 3) (6, 2 pas bekend vanaf aflevering 3)
# (16, 2 pas bekend vanaf aflevering 3) (3, 1 pas bekend vanaf aflevering 3),
# Rocky (16, 3) (2, 1 pas bekend vanaf aflevering 3) (6, 3 pas bekend vanaf aflevering 3) (3, 3 pas bekend vanaf aflevering 3),
# Splinter (1, 2) (20, 7 pas bekend vanaf aflevering 3) (2, 3 pas bekend vanaf aflevering 3) (16, 1 pas bekend vanaf aflevering 3),
players2 = [Player.CHARLOTTE_22, Player.ERIK_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.LAKSHMI_22,
            Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22]
question2_1 = Question({1: [Player.ERIK_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.SPLINTER_22],
                        2: [Player.CHARLOTTE_22, Player.LAKSHMI_22, Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22]})
question2_2 = Question({1: [Player.JOSHUA_22, Player.LAKSHMI_22],
                        2: [Player.FLORENTIJN_22, Player.RENEE_22],
                        3: [Player.ERIK_22, Player.MARIJE_22, Player.ROCKY_22],
                        4: [Player.CHARLOTTE_22, Player.SPLINTER_22]})
question2_3 = Question({1: [Player.CHARLOTTE_22, Player.LAKSHMI_22, Player.MARIJE_22, Player.RENEE_22],
                        2: [Player.ERIK_22, Player.SPLINTER_22],
                        3: [Player.FLORENTIJN_22, Player.JOSHUA_22, Player.ROCKY_22]})
question2_6 = Question({1: [Player.JOSHUA_22, Player.LAKSHMI_22],
                        2: [Player.ERIK_22, Player.MARIJE_22, Player.RENEE_22, Player.SPLINTER_22],
                        3: [Player.CHARLOTTE_22, Player.FLORENTIJN_22, Player.ROCKY_22]})
question2_8 = Question({1: [Player.ERIK_22],
                        2: [Player.CHARLOTTE_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.LAKSHMI_22,
                            Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22]})
question2_10 = Question({1: [Player.CHARLOTTE_22, Player.JOSHUA_22, Player.LAKSHMI_22, Player.MARIJE_22],
                         2: [Player.ERIK_22, Player.FLORENTIJN_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22]})
question2_12 = Question({1: [Player.CHARLOTTE_22, Player.ERIK_22, Player.FLORENTIJN_22, Player.JOSHUA_22,
                             Player.MARIJE_22, Player.RENEE_22, Player.SPLINTER_22],
                         2: [Player.LAKSHMI_22, Player.ROCKY_22]})
question2_16 = Question({1: [Player.CHARLOTTE_22, Player.JOSHUA_22, Player.RENEE_22, Player.ROCKY_22],
                         2: [Player.ERIK_22, Player.LAKSHMI_22],
                         3: [Player.MARIJE_22, Player.SPLINTER_22],
                         4: [Player.FLORENTIJN_22]})
question2_20 = Question({1: [Player.CHARLOTTE_22], 2: [Player.ERIK_22], 3: [Player.FLORENTIJN_22], 4: [Player.JOSHUA_22],
                         5: [Player.LAKSHMI_22], 6: [Player.MARIJE_22], 7: [Player.RENEE_22], 8: [Player.ROCKY_22],
                         9: [Player.SPLINTER_22]})
result2 = Result(DropType.EXECUTION_DROP, [Player.ERIK_22])
episode2 = Episode(players2, result2,
                   {Player.CHARLOTTE_22: TestInput({2: DelayedAnswer(3, 3), 3: DelayedAnswer(3, 3), 6: DelayedAnswer(2, 3),
                                                    12: 1, 16: DelayedAnswer(1, 3), 20: DelayedAnswer(7, 3)}),
                    Player.FLORENTIJN_22: TestInput({2: DelayedAnswer(3, 3), 3: DelayedAnswer(2, 3), 6: DelayedAnswer(2, 3),
                                                     16: DelayedAnswer(1, 3)}),
                    Player.JOSHUA_22: TestInput({3: DelayedAnswer(1, 3), 6: DelayedAnswer(3, 3), 10: 2, 16: DelayedAnswer(1, 3)}),
                    Player.LAKSHMI_22: TestInput({2: DelayedAnswer(3, 3), 3: DelayedAnswer(1, 3), 6: DelayedAnswer(2, 3),
                                                  16: DelayedAnswer(1, 3)}),
                    Player.MARIJE_22: TestInput({2: DelayedAnswer(4, 3), 3: DelayedAnswer(3, 3), 6: 3, 16: DelayedAnswer(1, 3),
                                                 20: DelayedAnswer(1, 3)}),
                    Player.RENEE_22: TestInput({2: DelayedAnswer(3, 3), 3: DelayedAnswer(1, 3), 6: DelayedAnswer(2, 3),
                                                8: 2, 16: DelayedAnswer(2, 3), 20: DelayedAnswer(6, 3)}),
                    Player.ROCKY_22: TestInput({2: DelayedAnswer(1, 3), 3: DelayedAnswer(3, 3), 6: DelayedAnswer(3, 3),
                                                16: 3}),
                    Player.SPLINTER_22: TestInput({1: 2, 2: DelayedAnswer(3, 3), 16: DelayedAnswer(1, 3), 20: DelayedAnswer(7, 3)})},
                   {1: question2_1, 2: question2_2, 3: question2_3, 6: question2_6, 8: question2_8, 10: question2_10,
                    12: question2_12, 16: question2_16, 20: question2_20})

# Aflevering 3 (afvaller: Florentijn)
# 4 - Hoeveel aanwijzingen heeft het duo van de Mol ontvangen tijdens de opdracht 'Kameraad':
# 1: Rocky, Splinter; 2: Joshua, Marije; 3: Florentijn, Lakshmi; 4: Charlotte, Renee;
# 5 - Heeft de Mol gelogen over minstens één test-antwoord tijdens de opdracht 'Kameraad':
# 1: Florentijn, Joshua, Lakshmi, Rocky, Splinter; 2: Charlotte, Marije, Renee;
# 12 - Wat deed de Mol deze aflevering:
# 1: Joshua, Lakshmi, Rocky, Splinter; 2: Charlotte, Florentijn, Marije, Renee;
# 14 - Welke kokers heeft de Mol gepakt tijdens het abseilen:
# 1: Joshua, Lakshmi, Rocky; 2: Splinter; 3: Charlotte, Florentijn, Marije, Renee;
# 20 - Wie is de Mol:
# 1: Charlotte; 2: Florentijn; 3: Joshua; 4: Lakshmi; 5: Marije; 6: Renee; 7: Rocky; 8: Splinter;
# Antwoorden: Marije (4, 2) (1 joker), Lakshmi (1 joker), Florentijn (5, 2) (2 jokers), Splinter (12, 2) (1 joker)
# Charlotte (14, 1) (1 joker), Renee (1 joker), Joshua (20, 7), Rocky (2 jokers)
players3 = [Player.CHARLOTTE_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.LAKSHMI_22, Player.MARIJE_22,
            Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22]
question3_4 = Question({1: [Player.ROCKY_22, Player.SPLINTER_22],
                        2: [Player.JOSHUA_22, Player.MARIJE_22],
                        3: [Player.FLORENTIJN_22, Player.LAKSHMI_22],
                        4: [Player.CHARLOTTE_22, Player.RENEE_22]})
question3_5 = Question({1: [Player.FLORENTIJN_22, Player.JOSHUA_22, Player.LAKSHMI_22, Player.ROCKY_22, Player.SPLINTER_22],
                        2: [Player.CHARLOTTE_22, Player.MARIJE_22, Player.RENEE_22]})
question3_12 = Question({1: [Player.JOSHUA_22, Player.LAKSHMI_22, Player.ROCKY_22, Player.SPLINTER_22],
                         2: [Player.CHARLOTTE_22, Player.FLORENTIJN_22, Player.MARIJE_22, Player.RENEE_22]})
question3_14 = Question({1: [Player.JOSHUA_22, Player.LAKSHMI_22, Player.ROCKY_22],
                         2: [Player.SPLINTER_22],
                         3: [Player.CHARLOTTE_22, Player.FLORENTIJN_22, Player.MARIJE_22, Player.RENEE_22]})
question3_20 = Question({1: [Player.CHARLOTTE_22], 2: [Player.FLORENTIJN_22], 3: [Player.JOSHUA_22],
                         4: [Player.LAKSHMI_22], 5: [Player.MARIJE_22], 6: [Player.RENEE_22], 7: [Player.ROCKY_22],
                         8: [Player.SPLINTER_22]})
result3 = Result(DropType.EXECUTION_DROP, [Player.FLORENTIJN_22])
episode3 = Episode(players3, result3,
                   {Player.MARIJE_22: TestInput({4: 2}, jokers = 1), Player.LAKSHMI_22: TestInput(jokers = 1),
                    Player.FLORENTIJN_22: TestInput({5: 2}, jokers = 2), Player.SPLINTER_22: TestInput({12: 2}, jokers = 1),
                    Player.CHARLOTTE_22: TestInput({14: 1}, jokers = 1), Player.RENEE_22: TestInput(jokers = 1),
                    Player.JOSHUA_22: TestInput({20: 7}), Player.ROCKY_22: TestInput(jokers = 2)},
                   {4: question3_4, 5: question3_5, 12: question3_12, 14: question3_14, 20: question3_20})

# Aflevering 4 (afvaller: Lakshmi)
# 4 - Op welke verdieping stond de Mol tijdens de opdracht 'Meeliften':
# 1: Rocky; 2: Splinter; 3: Lakshmi; 4: Charlotte, Joshua, Marije, Renee;
# 8 - Is de Mol de huidige penningmeester:
# 1: Splinter; 2: Charlotte, Joshua, Lakshmi, Marije, Renee, Rocky;
# 9 - Welke rol had de Mol tijdens de opdracht 'Fotogenie(k)':
# 1: Joshua, Lakshmi, Renee, Rocky, Splinter; 2: Charlotte, Marije;
# 12 - Op welk bord stond de foto van de Mol:
# 1: Splinter; 2: Marije; 3: Renee; 4: Charlotte; 5: Rocky; 6: Lakshmi; 7: Joshua;
# 17 - Maakde de Mol als eerste een slot open tijdens de opdracht 'In Vuur en Vlam':
# 1: Charlotte; 2: Joshua, Lakshmi, Marije, Renee, Rocky, Splinter;
# Antwoorden: Rocky (4, 4), Marije (8, 2), Renee (9, 2) (1 joker), Charlotte (12, 1), Splinter (17, 1)
players4 = [Player.CHARLOTTE_22, Player.JOSHUA_22, Player.LAKSHMI_22, Player.MARIJE_22, Player.RENEE_22,
            Player.ROCKY_22, Player.SPLINTER_22]
question4_4 = Question({1: [Player.ROCKY_22],
                        2: [Player.SPLINTER_22],
                        3: [Player.LAKSHMI_22],
                        4: [Player.CHARLOTTE_22, Player.JOSHUA_22, Player.MARIJE_22, Player.RENEE_22]})
question4_8 = Question({1: [Player.SPLINTER_22],
                        2: [Player.CHARLOTTE_22, Player.JOSHUA_22, Player.LAKSHMI_22, Player.MARIJE_22, Player.RENEE_22,
                            Player.ROCKY_22]})
question4_9 = Question({1: [Player.JOSHUA_22, Player.LAKSHMI_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22],
                        2: [Player.CHARLOTTE_22, Player.MARIJE_22]})
question4_12 = Question({1: [Player.SPLINTER_22], 2: [Player.MARIJE_22], 3: [Player.RENEE_22], 4: [Player.CHARLOTTE_22],
                         5: [Player.ROCKY_22], 6: [Player.LAKSHMI_22], 7: [Player.JOSHUA_22]})
question4_17 = Question({1: [Player.CHARLOTTE_22],
                         2: [Player.JOSHUA_22, Player.LAKSHMI_22, Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22,
                             Player.SPLINTER_22]})
result4 = Result(DropType.EXECUTION_DROP, [Player.LAKSHMI_22])
episode4 = Episode(players4, result4,
                   {Player.ROCKY_22: TestInput({4: 4}), Player.MARIJE_22: TestInput({8: 2}),
                    Player.RENEE_22: TestInput({9: 2}, jokers = 1), Player.CHARLOTTE_22: TestInput({12: 1}),
                    Player.SPLINTER_22: TestInput({17: 1})},
                   {4: question4_4, 8: question4_8, 9: question4_9, 12: question4_12, 17: question4_17})

# Aflevering 5 (afvaller: Joshua)
# 6 - Met wie vormde de Mol een duo tijdens de opdracht 'Wie, Wat ... Waar':
# 1: Joshua; 2: Charlotte; 3: Rocky; 4: Splinter; 5: Marije; 6: Renee;
# 14 - Had de Mol beide handen in de zakken op de groepsfoto van aflevering 5:
# 1: Renee; 2: Charlotte, Joshua, Marije, Rocky, Splinter;
# 18 - Wat was de taak van de Mol tijdens de opdracht 'Wie, Wat ... Waar':
# 1: Charlotte, Rocky, Splinter; 2: Joshua, Marije, Renee;
# 20 - Wie is de Mol:
# 1: Charlotte; 2: Joshua; 3: Marije; 4: Renee; 5: Rocky; 6: Splinter;
# Antwoorden: Charlotte (6, 5) (Vrijstelling), Marije (20, 2) (Vrijstelling), Rocky (Vrijstelling), Joshua (14, 2),
# Splinter (18, 2), Renee (20, 2)
players5 = [Player.CHARLOTTE_22, Player.JOSHUA_22, Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22,
            Player.SPLINTER_22]
question5_6 = Question({1: [Player.JOSHUA_22], 2: [Player.CHARLOTTE_22], 3: [Player.ROCKY_22], 4: [Player.SPLINTER_22],
                        5: [Player.MARIJE_22], 6: [Player.RENEE_22]})
question5_14 = Question({1: [Player.RENEE_22],
                         2: [Player.CHARLOTTE_22, Player.JOSHUA_22, Player.MARIJE_22, Player.ROCKY_22, Player.SPLINTER_22]})
question5_18 = Question({1: [Player.CHARLOTTE_22, Player.ROCKY_22, Player.SPLINTER_22],
                         2: [Player.JOSHUA_22, Player.MARIJE_22, Player.RENEE_22]})
question5_20 = Question({1: [Player.CHARLOTTE_22], 2: [Player.JOSHUA_22], 3: [Player.MARIJE_22], 4: [Player.RENEE_22],
                         5: [Player.ROCKY_22], 6: [Player.SPLINTER_22]})
result5 = Result(DropType.EXECUTION_DROP, [Player.JOSHUA_22])
episode5 = Episode(players5, result5,
                   {Player.CHARLOTTE_22: TestInput({6: 5}, immunity = True),
                    Player.MARIJE_22: TestInput({20: 2}, immunity = True), Player.ROCKY_22: TestInput(immunity = True),
                    Player.JOSHUA_22: TestInput({14: 2}), Player.SPLINTER_22: TestInput({18: 2}),
                    Player.RENEE_22: TestInput({20: 2})},
                   {6: question5_6, 14: question5_14, 18: question5_18, 20: question5_20})

# Aflevering 6 (geen afvaller, alleen Rocky en Splinter kregen hun scherm te zien)
# 4 - Bij welke haltes is de Mol uit de bus gestapt tijdens de opdracht 'Brieven-bus':
# 1: Rocky; 2: Splinter; 3: Charlotte; 4: Renee; 5: Marije;
# 5 - Is de Mol bij een halte achtergebleven tijdens de opdracht 'Brieven-bus':
# 1: Marije, Splinter (Ja); 2: Charlotte, Renee, Rocky (Nee);
# 10 - Met wie deelde de Mol een vleugel bij aanvang van de opdracht 'Ontsnappen':
# 1: Splinter; 2: Rocky; 3: Renee; 4: Charlotte; 5: Marije;
# 12 - Als hoeveelste ontsnapte de Mol uit eigen cel tijdens de opdracht 'Ontsnappen':
# 1: Charlotte; 2: Rocky; 3: Renee; 4: Splinter; 5: Marije;
# 20 - Wie is de Mol:
# 1: Charlotte; 2: Marije; 3: Renee; 4: Rocky; 5: Splinter;
# Antwoorden: Charlotte (5, 1) (1 joker), Splinter (4, 1), Rocky (10, 3) (1 joker), Renee (12, 5), Marije (20, 1)
players6 = [Player.CHARLOTTE_22, Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22]
question6_4 = Question({1: [Player.ROCKY_22], 2: [Player.SPLINTER_22], 3: [Player.CHARLOTTE_22], 4: [Player.RENEE_22],
                        5: [Player.MARIJE_22]})
question6_5 = Question({1: [Player.MARIJE_22, Player.SPLINTER_22],
                        2: [Player.CHARLOTTE_22, Player.RENEE_22, Player.ROCKY_22]})
question6_10 = Question({1: [Player.SPLINTER_22], 2: [Player.ROCKY_22], 3: [Player.RENEE_22], 4: [Player.CHARLOTTE_22],
                         5: [Player.MARIJE_22]})
question6_12 = Question({1: [Player.CHARLOTTE_22], 2: [Player.ROCKY_22], 3: [Player.RENEE_22], 4: [Player.SPLINTER_22],
                         5: [Player.MARIJE_22]})
question6_20 = Question({1: [Player.CHARLOTTE_22], 2: [Player.MARIJE_22], 3: [Player.RENEE_22], 4: [Player.ROCKY_22],
                         5: [Player.SPLINTER_22]})
result6 = Result(DropType.POSSIBLE_DROP, [Player.CHARLOTTE_22, Player.MARIJE_22, Player.RENEE_22])
episode6 = Episode(players6, result6,
                   {Player.CHARLOTTE_22: TestInput({5: 1}, jokers = 1), Player.SPLINTER_22: TestInput({4: 1}),
                    Player.ROCKY_22: TestInput({10: 3}, jokers = 1), Player.RENEE_22: TestInput({12: 5}),
                    Player.MARIJE_22: TestInput({20: 1})},
                   {4: question6_4, 5: question6_5, 10: question6_10, 12: question6_12, 20: question6_20})

season22 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6})