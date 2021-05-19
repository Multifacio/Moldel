from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

# Aflevering 1 (afvaller: Tina)
# Vragen:
# 3 - Waar bevond de Mol zich bij aanvang van de opdracht 'Spiegelbeeld':
# 1: Jeroen, Nikkie, Patrick, Peggy, Tina; 2: Ellie, Horace, Nadja, Ron, Tygo;
# 7 - Vond de Mol de spiegel met daarop 'Trust Nobody' tijdens de opdracht 'Spiegelbeeld':
# 1: Ron; 2: Ellie, Horace, Jeroen, Nadja, Nikkie, Patrick, Peggie, Tina, Tygo;
# 13 - Welke rol had de Mol tijdens de opdracht 'Gastenlijst':
# 1: Ellie, Patrick; 2: Horace, Jeroen, Nadja, Nikkie, Peggy, Ron, Tina, Tygo;
# 18 - Tegenover welke oud-Mol stond de Mol tijdens de opdracht 'Achter je Rug?':
# 1: Peggy, Tygo; 2: Horace, Jeroen; 3: Nadja, Nikkie; 4: Ron, Tina; 5: Ellie, Patrick;
# 20 - Wie is de Mol:
# 1: Ellie; 2: Horace; 3: Jeroen; 4: Nadja; 5: Nikkie; 6: Patrick; 7: Peggy; 8: Ron; 9: Tina; 10: Tygo;
# Antwoorden: Jeroen (3, 1), Ron (1 joker), Nikkie (7, 2), Tygo (20, 1), Tina (18, 3), Peggy (13, 1), Ellie (20, 6)
players1 = [Player.ELLIE_21, Player.HORACE_21, Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21, Player.PATRICK_21,
            Player.PEGGY_21, Player.RON_21, Player.TINA_21, Player.TYGO_21]
question1_3 = Question({1: [Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21, Player.TINA_21],
                        2: [Player.ELLIE_21, Player.HORACE_21, Player.NADJA_21, Player.RON_21, Player.TYGO_21]})
question1_7 = Question({1: [Player.RON_21],
                        2: [Player.ELLIE_21, Player.HORACE_21, Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21,
                            Player.PATRICK_21, Player.PEGGY_21, Player.TINA_21, Player.TYGO_21]})
question1_13 = Question({1: [Player.ELLIE_21, Player.PATRICK_21],
                         2: [Player.HORACE_21, Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21, Player.PEGGY_21,
                             Player.RON_21, Player.TINA_21, Player.TYGO_21]})
question1_18 = Question({1: [Player.PEGGY_21, Player.TYGO_21],
                         2: [Player.HORACE_21, Player.JEROEN_21],
                         3: [Player.NADJA_21, Player.NIKKIE_21],
                         4: [Player.RON_21, Player.TINA_21],
                         5: [Player.ELLIE_21, Player.PATRICK_21]})
question1_20 = Question({1: [Player.ELLIE_21], 2: [Player.HORACE_21], 3: [Player.JEROEN_21], 4: [Player.NADJA_21],
                         5: [Player.NIKKIE_21], 6: [Player.PATRICK_21], 7: [Player.PEGGY_21], 8: [Player.RON_21],
                         9: [Player.TINA_21], 10: [Player.TYGO_21]})
result1 = Result(DropType.EXECUTION_DROP, [Player.TINA_21])
episode1 = Episode(players1, result1,
                   {Player.HORACE_21: TestInput(mentions = {Player.NADJA_21, Player.TINA_21}),
                    Player.JEROEN_21: TestInput({3: 1}, mentions = {Player.NIKKIE_21}),
                    Player.RON_21: TestInput(mentions = {Player.HORACE_21, Player.NIKKIE_21, Player.PEGGY_21,
                                            Player.TINA_21, Player.TYGO_21}, jokers = 1),
                    Player.NIKKIE_21: TestInput({7: 2}, mentions = {Player.TYGO_21}),
                    Player.TYGO_21: TestInput({20: 1}),
                    Player.TINA_21: TestInput({18: 3}),
                    Player.PEGGY_21: TestInput({13: 1}, mentions = {Player.ELLIE_21, Player.HORACE_21, Player.TINA_21}),
                    Player.ELLIE_21: TestInput({20: 6})},
                   {3: question1_3, 7: question1_7, 13: question1_13, 18: question1_18, 20: question1_20})

# Aflevering 2 (afvaller: Nadja)
# Vragen:
# 1 - De Mol is een:
# 1: Jeroen, Horace, Patrick, Ron, Tygo; 2: Ellie, Nadja, Nikkie, Peggy;
# 5 - Tijdens de opdracht 'Steen Rijk' zat de Mol in een:
# 1: Ellie, Horace, Patrick, Ron; 2: Jeroen, Nadja, Nikkie, Peggy, Tygo;
# 9 - In welke run betrad de Mol het parcours tijdens de opdracht 'Meeslepend':
# 1: Nikkie, Ron; 2: Patrick, Peggy; 3: Horace, Tygo; 4: Nadja; 5: Ellie, Jeroen;
# 16 - Wat was de rol van de Mol tijdens de opdracht 'Vragenvuur':
# 1: Jeroen, Nadja, Nikkie, Peggy; 2: Ellie, Horace, Ron, Tygo; 3: Patrick;
# 20 - Wie is de Mol:
# 1: Ellie; 2: Horace; 3: Jeroen; 4: Nadja; 5: Nikkie; 6: Patrick; 7: Peggy; 8: Ron; 9: Tygo;
# Antwoorden: Ellie (Vrijstelling), Ron (1, 1), Peggy (9, 4), Horace (5, 2) (1 joker), Nikkie (16, 1), Nadja (1 joker),
# Tygo (20, 2), Patrick (20, 4) (1 joker)
players2 = [Player.ELLIE_21, Player.HORACE_21, Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21, Player.PATRICK_21,
            Player.PEGGY_21, Player.RON_21, Player.TYGO_21]
question2_1 = Question({1: [Player.JEROEN_21, Player.HORACE_21, Player.PATRICK_21, Player.RON_21, Player.TYGO_21],
                        2: [Player.ELLIE_21, Player.NADJA_21, Player.NIKKIE_21, Player.PEGGY_21]})
question2_5 = Question({1: [Player.ELLIE_21, Player.HORACE_21, Player.PATRICK_21, Player.RON_21],
                        2: [Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21, Player.PEGGY_21, Player.TYGO_21]})
question2_9 = Question({1: [Player.NIKKIE_21, Player.RON_21],
                        2: [Player.PATRICK_21, Player.PEGGY_21],
                        3: [Player.HORACE_21, Player.TYGO_21],
                        4: [Player.NADJA_21],
                        5: [Player.ELLIE_21, Player.JEROEN_21]})
question2_16 = Question({1: [Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21, Player.PEGGY_21],
                         2: [Player.ELLIE_21, Player.HORACE_21, Player.RON_21, Player.TYGO_21],
                         3: [Player.PATRICK_21]})
question2_20 = Question({1: [Player.ELLIE_21], 2: [Player.HORACE_21], 3: [Player.JEROEN_21], 4: [Player.NADJA_21],
                         5: [Player.NIKKIE_21], 6: [Player.PATRICK_21], 7: [Player.PEGGY_21], 8: [Player.RON_21],
                         9: [Player.TYGO_21]})
result2 = Result(DropType.EXECUTION_DROP, [Player.NADJA_21])
episode2 = Episode(players2, result2,
                   {Player.ELLIE_21: TestInput(immunity = True),
                    Player.RON_21: TestInput({1: 1}, mentions = {Player.ELLIE_21, Player.HORACE_21, Player.NIKKIE_21,
                                            Player.PEGGY_21, Player.TYGO_21}),
                    Player.PEGGY_21: TestInput({9: 4}, mentions = {Player.ELLIE_21, Player.NADJA_21}),
                    Player.HORACE_21: TestInput({5: 2}, jokers = 1),
                    Player.NIKKIE_21: TestInput({16: 1}, mentions = {Player.NADJA_21}),
                    Player.NADJA_21: TestInput(jokers = 1),
                    Player.JEROEN_21: TestInput(mentions = {Player.TYGO_21}),
                    Player.TYGO_21: TestInput({20: 2}, mentions = {Player.HORACE_21}),
                    Player.PATRICK_21: TestInput({20: 4}, mentions = {Player.NADJA_21, Player.PEGGY_21}, jokers = 1)},
                   {1: question2_1, 5: question2_5, 9: question2_9, 16: question2_16, 20: question2_20})

# Aflevering 3 (afvaller: Horace)
# Vragen:
# 4 - Waar stond de Mol op de groepsfoto van aflevering 3:
# 1: Ellie, Horace, Peggy, Ron; 2: Jeroen, Nikkie, Patrick, Tygo;
# 6 - Was de Mol betrokken bij de eerste geldwissel tijdens de opdracht: 'Sleutelbos':
# 1: Peggy, Tygo; 2: Ellie, Horace, Jeroen, Nikkie, Patrick, Ron;
# 10 - Wat was de rol van de Mol tijdens de opdracht 'Meer of Min':
# 1: Ellie, Horace, Ron, Tygo; 2: Jeroen, Nikkie, Patrick, Peggy;
# 12 - Met wie stond de Mol op een uitkijkpunt tijdens de opdracht 'Meer of Min':
# 1: Horace; 2: Ellie; 3: Tygo; 4: Ron; 5: Jeroen, Nikkie, Patrick, Peggy;
# 16 - Aan welke opdrachten heeft de Mol deelgenomen tijdens de opdracht 'Fortuin':
# 1: Jeroen, Nikkie, Ron, Tygo; 2: Ellie, Horace, Patrick, Peggy;
# 18 - Heeft de Mol een schild geraakt tijdens de opdracht 'Fortuin':
# 1: Horace, Jeroen, Nikkie, Patrick, Peggy; 2: Ellie, Ron, Tygo;
# Antwoorden: Tygo (6, 1), Ron (10, 2), Jeroen (12, 5), Patrick (4, 1), Peggy (16, 2), Ellie (18, 1)
players3 = [Player.ELLIE_21, Player.HORACE_21, Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21,
            Player.RON_21, Player.TYGO_21]
question3_4 = Question({1: [Player.ELLIE_21, Player.HORACE_21, Player.PEGGY_21, Player.RON_21],
                        2: [Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.TYGO_21]})
question3_6 = Question({1: [Player.PEGGY_21, Player.TYGO_21],
                        2: [Player.ELLIE_21, Player.HORACE_21, Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21,
                            Player.RON_21]})
question3_10 = Question({1: [Player.ELLIE_21, Player.HORACE_21, Player.RON_21, Player.TYGO_21],
                         2: [Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21]})
question3_12 = Question({1: [Player.HORACE_21],
                         2: [Player.ELLIE_21],
                         3: [Player.TYGO_21],
                         4: [Player.RON_21],
                         5: [Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21]})
question3_16 = Question({1: [Player.JEROEN_21, Player.NIKKIE_21, Player.RON_21, Player.TYGO_21],
                         2: [Player.ELLIE_21, Player.HORACE_21, Player.PATRICK_21, Player.PEGGY_21]})
question3_18 = Question({1: [Player.HORACE_21, Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21],
                         2: [Player.ELLIE_21, Player.RON_21, Player.TYGO_21]})
result3 = Result(DropType.EXECUTION_DROP, [Player.HORACE_21])
episode3 = Episode(players3, result3,
                   {Player.TYGO_21: TestInput({6: 1}, mentions = {Player.ELLIE_21, Player.JEROEN_21}),
                    Player.RON_21: TestInput({10: 2}, mentions = {Player.PEGGY_21}),
                    Player.NIKKIE_21: TestInput(mentions = {Player.JEROEN_21}),
                    Player.JEROEN_21: TestInput({12: 5}, mentions = {Player.PATRICK_21}),
                    Player.PATRICK_21: TestInput({4: 1}, mentions = {Player.PEGGY_21}),
                    Player.PEGGY_21: TestInput({16: 2}, mentions = {Player.ELLIE_21}),
                    Player.ELLIE_21: TestInput({18: 1}, mentions = {Player.HORACE_21, Player.PEGGY_21}),
                    Player.HORACE_21: TestInput(mentions = {Player.ELLIE_21, Player.PATRICK_21, Player.PEGGY_21})},
                   {4: question3_4, 6: question3_6, 10: question3_10, 12: question3_12, 16: question3_16,
                    18: question3_18})

# Aflevering 4 (afvaller: Ellie)
# Vragen:
# 5 - Welk schilderij heeft de Mol nageschilderd tijdens de opdracht 'Meesterwerken':
# 1: Jeroen; 2: Peggy; 3: Nikkie; 4: Tygo; 5: Ellie, Patrick, Ron;
# 10 - Met wie vormde de Mol een team tijdens de opdracht 'Follow the Money':
# 1: Peggy; 2: Ron; 3: Tygo; 4: Ellie; 5: Jeroen; 6: Nikkie; 7: Patrick;
# 14 - Waar stond het kaartenrek van de Mol bij aanvang van de opdracht 'Groeten uit Florence':
# 1: Nikkie, Ron; 2: Ellie, Peggy, Tygo; 3: Jeroen, Patrick;
# 20 - Wie is de Mol:
# 1: Ellie; 2: Jeroen; 3: Nikkie; 4: Patrick; 5: Peggy; 6: Ron; 7: Tygo;
# Antwoorden: Peggy (5, 5), Ron (20, 1), Tygo (14, 2), Nikkie (10, 5), Jeroen (20, 1)
players4 = [Player.ELLIE_21, Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21, Player.RON_21,
            Player.TYGO_21]
question4_5 = Question({1: [Player.JEROEN_21],
                        2: [Player.PEGGY_21],
                        3: [Player.NIKKIE_21],
                        4: [Player.TYGO_21],
                        5: [Player.ELLIE_21, Player.PATRICK_21, Player.RON_21]})
question4_10 = Question({1: [Player.PEGGY_21], 2: [Player.RON_21], 3: [Player.TYGO_21], 4: [Player.ELLIE_21],
                         5: [Player.JEROEN_21], 6: [Player.NIKKIE_21], 7: [Player.PATRICK_21]})
question4_14 = Question({1: [Player.NIKKIE_21, Player.RON_21],
                         2: [Player.ELLIE_21, Player.PEGGY_21, Player.TYGO_21],
                         3: [Player.JEROEN_21, Player.PATRICK_21]})
question4_20 = Question({1: [Player.ELLIE_21], 2: [Player.JEROEN_21], 3: [Player.NIKKIE_21], 4: [Player.PATRICK_21],
                         5: [Player.PEGGY_21], 6: [Player.RON_21], 7: [Player.TYGO_21]})
result4 = Result(DropType.EXECUTION_DROP, [Player.ELLIE_21])
episode4 = Episode(players4, result4,
                   {Player.PATRICK_21: TestInput(mentions = {Player.PEGGY_21, Player.RON_21}),
                    Player.PEGGY_21: TestInput({5: 5}, mentions = {Player.RON_21}),
                    Player.RON_21: TestInput({20: 1}, mentions = {Player.ELLIE_21, Player.NIKKIE_21, Player.PEGGY_21}),
                    Player.TYGO_21: TestInput({14: 2}, mentions = {Player.ELLIE_21, Player.PEGGY_21}),
                    Player.NIKKIE_21: TestInput({10: 5}, mentions = {Player.ELLIE_21, Player.JEROEN_21, Player.RON_21}),
                    Player.JEROEN_21: TestInput({20: 1})},
                   {5: question4_5, 10: question4_10, 14: question4_14, 20: question4_20})

# Aflevering 6 (afvallers: Patrick, Ron)
# Vragen:
# 10 - Van welk duo kreeg de Mol de routebeschrijving tijdens de opdracht 'Route Beschrijving':
# 1: Patrick, Peggy (Nikkie & Tygo); 2: Nikkie, Tygo (Jeroen & Ron) 3: Jeroen, Ron (Peggy & Patrick)
# 11 - Bestuurde de Mol de Cabrio tijdens de opdracht 'Route Beschrijving':
# 1: Peggy, Ron, Tygo (Ja); 2: Jeroen, Nikkie, Patrick (Nee);
# 16 - De Mol was tijdens aflevering 6:
# 1: Nikkie, Tygo (Opgesloten in een cel); 2: Jeroen, Patrick, Peggy, Ron (Op zoek naar de andere kandidaten);
# 17 - Is de Mol tijdens de zoektocht in de Martello Toren geweest:
# 1: Peggy, Ron (Ja); 2: Jeroen, Patrick (Nee); 3: Nikkie, Tygo (De Mol deed niet mee aan de zoektocht);
# 20 - Wie is de Mol:
# 1: Jeroen; 2: Nikkie; 3: Patrick; 4: Peggy; 5: Ron; 6: Tygo;
# Antwoorden: Tygo (Vrijstelling), Nikkie (Vrijstelling), Patrick (11, 1) (20, 4), Peggy (17, 1) (20, 5), Ron (10, 3),
# Jeroen (16, 1) (20, 2)
players6 = [Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21, Player.RON_21, Player.TYGO_21]
question6_10 = Question({1: [Player.PATRICK_21, Player.PEGGY_21], 2: [Player.NIKKIE_21, Player.TYGO_21],
                         3: [Player.JEROEN_21, Player.RON_21]})
question6_11 = Question({1: [Player.PEGGY_21, Player.RON_21, Player.TYGO_21],
                         2: [Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21]})
question6_16 = Question({1: [Player.NIKKIE_21, Player.TYGO_21],
                         2: [Player.JEROEN_21, Player.PATRICK_21, Player.PEGGY_21, Player.RON_21]})
question6_17 = Question({1: [Player.PEGGY_21, Player.RON_21],
                         2: [Player.JEROEN_21, Player.PATRICK_21],
                         3: [Player.NIKKIE_21, Player.TYGO_21]})
question6_20 = Question({1: [Player.JEROEN_21], 2: [Player.NIKKIE_21], 3: [Player.PATRICK_21], 4: [Player.PEGGY_21],
                         5: [Player.RON_21], 6: [Player.TYGO_21]})
result6 = Result(DropType.EXECUTION_DROP, [Player.PATRICK_21, Player.RON_21])
episode6 = Episode(players6, result6,
                   {Player.TYGO_21: TestInput(immunity = True),
                    Player.NIKKIE_21: TestInput(immunity = True),
                    Player.PATRICK_21: TestInput({11: 1, 20: 4}, mentions = {Player.PEGGY_21}),
                    Player.PEGGY_21: TestInput({17: 1, 20: 5}, mentions = {Player.RON_21}),
                    Player.JEROEN_21: TestInput({16: 1, 20: 2}, mentions = {Player.NIKKIE_21})},
                   {10: question6_10, 11: question6_11, 16: question6_16, 17: question6_17, 20: question6_20})

# Aflevering 7 - First (afvaller: Peggy)
# Vragen:
# 20 - Wie is de Mol:
# 1: Jeroen; 2: Nikkie; 3: Peggy; 4: Tygo;
# Antwoorden: Jeroen (20, 2), Tygo (20, 3), Peggy (20, 4), Nikkie (20, 1)
players7 = [Player.JEROEN_21, Player.NIKKIE_21, Player.PEGGY_21, Player.TYGO_21]
question7_20 = Question({1: [Player.JEROEN_21], 2: [Player.NIKKIE_21], 3: [Player.PEGGY_21], 4: [Player.TYGO_21]})
result7 = Result(DropType.EXECUTION_DROP, [Player.PEGGY_21])
episode7 = Episode(players7, result7,
                   {Player.JEROEN_21: TestInput({20: 2}, mentions = {Player.NIKKIE_21}),
                    Player.TYGO_21: TestInput({20: 3}, mentions = {Player.PEGGY_21}),
                    Player.PEGGY_21: TestInput({20: 4}),
                    Player.NIKKIE_21: TestInput({20: 1}, mentions = {Player.JEROEN_21})},
                   {20: question7_20})

# Aflevering 7 - Second (afvaller: Tygo)
# Vragen:
# 6 - Met wie vormde de Mol een team tijdens de opdracht 'Gastenlijst':
# 1: Jeroen; 2: Tygo; 3: Nikkie;
# 14 - Was de Mol betrokken bij de eerste geldwissel tijdens de opdracht 'Sleutel Bos':
# 1: Tygo; 2: Jeroen, Nikkie;
# 24 - Tilde de Mol het puzzelstuk met mes en vork naar de verzamelplaats tijdens 'Stuk voor Stuk' (Niet Bruikbaar)
# 40 - Wie is de Mol:
# 1: Jeroen; 2: Nikkie; 3: Tygo;
# Antwoorden: Tygo (6, 3) (40, 2), Nikkie (14, 2) (40, 1), Jeroen (40, 2)
players8 = [Player.JEROEN_21, Player.NIKKIE_21, Player.TYGO_21]
question8_6 = Question({1: [Player.JEROEN_21], 2: [Player.TYGO_21], 3: [Player.NIKKIE_21]})
question8_14 = Question({1: [Player.TYGO_21], 2: [Player.JEROEN_21, Player.NIKKIE_21]})
question8_40 = Question({1: [Player.JEROEN_21], 2: [Player.NIKKIE_21], 3: [Player.TYGO_21]})
result8 = Result(DropType.EXECUTION_DROP, [Player.TYGO_21])
episode8 = Episode(players8, result8,
                   {Player.TYGO_21: TestInput({6: 3, 40: 2}, mentions = {Player.NIKKIE_21}),
                    Player.NIKKIE_21: TestInput({14: 2, 40: 1}, mentions = {Player.JEROEN_21}),
                    Player.JEROEN_21: TestInput({40: 2}, mentions = {Player.NIKKIE_21})},
                   {6: question8_6, 14: question8_14, 40: question8_40})

season21 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 6: episode6, 7: episode7, 8: episode8})