from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

# Aflevering 1 (afvaller: Pieter)
# Vragen:
# 1 - De Mol is een:
# 1: Ajouad, Chris, Pieter, Rik, Viktor; 2: Carolina, Evelien, Margriet, Marlijn, Martine;
# 18 - Heeft de Mol een rode lijn gevonden tijdens de Schermen-opdracht:
# 1: Ajouad, Marlijn, Evelien, Martine, Viktor, Carolina, Chris; 2: Margriet, Rik, Pieter;
# 20 - Wie is de Mol:
# 1: Ajouad; 2: Carolina; 3: Chris; 4: Evelien; 5: Margriet; 6: Marlijn; 7: Martine; 8: Pieter; 9: Rik; 10: Viktor;
# Antwoorden: Viktor (1, 1), Pieter (18, 1), Margriet (20, 2), Rik (20, 6), Marlijn (20, 10) (1 joker)
players1 = [Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15, Player.EVELIEN_15, Player.MARGRIET_15,
            Player.MARLIJN_15, Player.MARTINE_15, Player.PIETER_15, Player.RIK_15, Player.VIKTOR_15]
question1_1 = Question({1: [Player.AJOUAD_15, Player.CHRIS_15, Player.PIETER_15, Player.RIK_15, Player.VIKTOR_15],
                        2: [Player.CAROLINA_15, Player.EVELIEN_15, Player.MARGRIET_15, Player.MARLIJN_15,
                            Player.MARTINE_15]})
question1_18 = Question({1: [Player.AJOUAD_15, Player.MARLIJN_15, Player.EVELIEN_15, Player.MARTINE_15,
                             Player.VIKTOR_15, Player.CAROLINA_15, Player.CHRIS_15],
                         2: [Player.MARGRIET_15, Player.RIK_15, Player.PIETER_15]})
question1_20 = Question({1: [Player.AJOUAD_15], 2: [Player.CAROLINA_15], 3: [Player.CHRIS_15], 4: [Player.EVELIEN_15],
                         5: [Player.MARGRIET_15], 6: [Player.MARLIJN_15], 7: [Player.MARTINE_15], 8: [Player.PIETER_15],
                         9: [Player.RIK_15], 10: [Player.VIKTOR_15]})
result1 = Result(DropType.EXECUTION_DROP, [Player.PIETER_15])
episode1 = Episode(players1, result1,
                   {Player.VIKTOR_15: TestInput({1: 1}), Player.PIETER_15: TestInput({18: 1}),
                    Player.MARGRIET_15: TestInput({20: 2}), Player.RIK_15: TestInput({20: 6}),
                    Player.MARLIJN_15: TestInput({20: 10}, jokers = 1),
                    Player.AJOUAD_15: TestInput(immunity = True)},
                   {1: question1_1, 18: question1_18, 20: question1_20})

# Aflevering 2 (afvaller: Evelien)
# Vragen:
# 1 - De Mol is een:
# 1: Ajouad, Chris, Rik, Viktor; 2: Carolina, Evelien, Margriet, Marlijn, Martine;
# 10 - Wanneer was het team van de Mol weer compleet in de Bioscoop:
# 1: Chris, Viktor, Martine; 2: Rik, Margriet, Marlijn; 3: Evelien, Ajouad, Carolina;
# 17 - Wanneer arriveerde het team van de Mol bij de vrachtauto van de laden/lossen-opdracht?
# 1: Viktor, Marlijn, Evelien; 2: Rik, Margriet, Carolina; 3: Martine, Ajouad, Chris;
# 20 - Wie is de Mol:
# 1: Ajouad; 2: Carolina; 3: Chris; 4: Evelien; 5: Margriet; 6: Marlijn; 7: Martine; 8: Rik; 9: Viktor;
# Antwoorden: Chris (10, 3), Carolina (17, 3) (1 joker), Viktor (20, 3), Rik (1, 2), Marlijn (1 joker),
# Margriet (1 joker), Martine (2 jokers), Ajouad (Vrijstelling)
players2 = [Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15, Player.EVELIEN_15, Player.MARGRIET_15,
            Player.MARLIJN_15, Player.MARTINE_15, Player.RIK_15, Player.VIKTOR_15]
question2_1 = Question({1: [Player.AJOUAD_15, Player.CHRIS_15, Player.RIK_15, Player.VIKTOR_15],
                        2: [Player.CAROLINA_15, Player.EVELIEN_15, Player.MARGRIET_15, Player.MARLIJN_15,
                            Player.MARTINE_15]})
question2_10 = Question({1: [Player.CHRIS_15, Player.VIKTOR_15, Player.MARTINE_15],
                         2: [Player.RIK_15, Player.MARGRIET_15, Player.MARLIJN_15],
                         3: [Player.EVELIEN_15, Player.AJOUAD_15, Player.CAROLINA_15]})
question2_17 = Question({1: [Player.VIKTOR_15, Player.MARLIJN_15, Player.EVELIEN_15],
                         2: [Player.RIK_15, Player.MARGRIET_15, Player.CAROLINA_15],
                         3: [Player.MARTINE_15, Player.AJOUAD_15, Player.CHRIS_15]})
question2_20 = Question({1: [Player.AJOUAD_15], 2: [Player.CAROLINA_15], 3: [Player.CHRIS_15], 4: [Player.EVELIEN_15],
                         5: [Player.MARGRIET_15], 6: [Player.MARLIJN_15], 7: [Player.MARTINE_15], 8: [Player.RIK_15],
                         9: [Player.VIKTOR_15]})
result2 = Result(DropType.EXECUTION_DROP, [Player.EVELIEN_15])
episode2 = Episode(players2, result2,
                   {Player.CHRIS_15: TestInput({10: 3}), Player.CAROLINA_15: TestInput({17: 3}, jokers = 1),
                    Player.VIKTOR_15: TestInput({20: 3}), Player.RIK_15: TestInput({1: 2}),
                    Player.MARLIJN_15: TestInput(jokers = 1), Player.MARGRIET_15: TestInput(jokers = 1),
                    Player.MARTINE_15: TestInput(jokers = 2), Player.AJOUAD_15: TestInput(immunity = True)},
                   {1: question2_1, 10: question2_10, 17: question2_17, 20: question2_20})

# Aflevering 3 (niemand viel af, alleen Carolina kreeg haar groene scherm te zien)
# Vragen:
# 1 - De Mol is een:
# 1: Ajouad, Chris, Rik, Viktor; 2: Carolina, Margriet, Marlijn, Martine;
# 6 - Met wie vormde de Mol een team tijdens de Laser-opdracht:
# 1: Viktor; 2: Rik; 3: Marlijn; 4: Martine; 5: Chris; 6: Margriet; 7: Carolina; 8: Ajouad
# 7 - Wanneer betrad het team van de Mol het parcours van de Laser-opdracht:
# 1: Rik, Carolina; 2: Chris, Marlijn; 3: Martine, Margriet; 4: Ajouad, Viktor;
# 9 - Is de Mol geraakt door een boobytrap tijdens de Laser-opdracht:
# 1: Rik, Marlijn; 2: Viktor, Martine, Chris, Margriet, Carolina, Ajouad;
# 13 - Wat was de Molactie tijdens de Watervliegtuig-opdracht:
# 1: Ajouad, Viktor, Marlijn, Martine, Margriet, Carolina; 2: Rik, Chris;
# 20 - Wie is de Mol:
# 1: Ajouad; 2: Carolina; 3: Chris; 4: Margriet; 5: Marlijn; 6: Martine; 7: Rik; 8: Viktor;
# Antwoorden: Carolina (6, 6) (20, 4), Martine (7, 2), Viktor (9, 1), Margriet (13, 2), Ajouad (1, 2), Marlijn (9, 2)
players3 = [Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15,
            Player.MARTINE_15, Player.RIK_15, Player.VIKTOR_15]
question3_1 = Question({1: [Player.AJOUAD_15, Player.CHRIS_15, Player.RIK_15, Player.VIKTOR_15],
                        2: [Player.CAROLINA_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15]})
question3_6 = Question({1: [Player.VIKTOR_15], 2: [Player.RIK_15], 3: [Player.MARLIJN_15], 4: [Player.MARTINE_15],
                        5: [Player.CHRIS_15], 6: [Player.MARGRIET_15], 7: [Player.CAROLINA_15], 8: [Player.AJOUAD_15]})
question3_7 = Question({1: [Player.RIK_15, Player.CAROLINA_15],
                        2: [Player.CHRIS_15, Player.MARLIJN_15],
                        3: [Player.MARTINE_15, Player.MARGRIET_15],
                        4: [Player.AJOUAD_15, Player.VIKTOR_15]})
question3_9 = Question({1: [Player.RIK_15, Player.MARLIJN_15],
                        2: [Player.VIKTOR_15, Player.MARTINE_15, Player.CHRIS_15, Player.MARGRIET_15,
                            Player.CAROLINA_15, Player.AJOUAD_15]})
question3_13 = Question({1: [Player.AJOUAD_15, Player.VIKTOR_15, Player.MARLIJN_15, Player.MARTINE_15,
                             Player.MARGRIET_15, Player.CAROLINA_15],
                         2: [Player.RIK_15, Player.CHRIS_15]})
question3_20 = Question({1: [Player.AJOUAD_15], 2: [Player.CAROLINA_15], 3: [Player.CHRIS_15], 4: [Player.MARGRIET_15],
                         5: [Player.MARLIJN_15], 6: [Player.MARTINE_15], 7: [Player.RIK_15], 8: [Player.VIKTOR_15]})
result3 = Result(DropType.POSSIBLE_DROP, [Player.AJOUAD_15, Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15,
                                          Player.MARTINE_15, Player.RIK_15, Player.VIKTOR_15])
episode3 = Episode(players3, result3,
                   {Player.CAROLINA_15: TestInput({6: 6, 20: 4}), Player.MARTINE_15: TestInput({7: 2}),
                    Player.VIKTOR_15: TestInput({9: 1}), Player.MARGRIET_15: TestInput({13: 2}),
                    Player.AJOUAD_15: TestInput({1: 2}), Player.MARLIJN_15: TestInput({9: 2})},
                   {1: question3_1, 6: question3_6, 7: question3_7, 9: question3_9, 13: question3_13, 20: question3_20})

# Aflevering 4 (afvaller: Ajouad)
# Vragen:
# 1 - De Mol is een:
# 1: Ajouad, Chris, Rik, Viktor; 2: Carolina, Margriet, Marlijn, Martine;
# 3 - Wat was de samenstelling van het team van de Mol bij de Vakantiekiekjes-opdracht?
# 1: Marlijn, Viktor; 2: Rik, Carolina, Ajouad; 3: Chris, Martine, Margriet;
# 11 - Heeft de Mol een zwarte vrijstelling in het bezit bij aanvang van deze test:
# 1: Margriet; 2: Ajouad, Carolina, Chris, Martine, Marlijn, Rik, Viktor;
# 17 - Wanneer betrad de Mol de Dagoba tijdens de Russisch Roulette-opdracht:
# 1: Martine; 2: Ajouad; 3: Carolina; 4: Viktor; 5: Rik; 6: Margriet; 7: Marlijn; 8: Chris;
# 20 - Wie is de Mol:
# 1: Ajouad; 2: Carolina; 3: Chris; 4: Margriet; 5: Marlijn; 6: Martine; 7: Rik; 8: Viktor;
# Antwoorden (Zwarte vrijstelling ingezet): Chris (3, 3), Marlijn (20, 7) (1 joker), Rik (11, 2) (1 joker),
# Martine (20, 4) (2 jokers), Viktor (17, 8), Carolina (2 jokers), Ajouad (1, 2) (1 joker), Margriet (11, 2)
players4 = [Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15,
            Player.MARTINE_15, Player.RIK_15, Player.VIKTOR_15]
question4_1 = Question({1: [Player.AJOUAD_15, Player.CHRIS_15, Player.RIK_15, Player.VIKTOR_15],
                        2: [Player.CAROLINA_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15]})
question4_3 = Question({1: [Player.MARLIJN_15, Player.VIKTOR_15],
                        2: [Player.RIK_15, Player.CAROLINA_15, Player.AJOUAD_15],
                        3: [Player.CHRIS_15, Player.MARTINE_15, Player.MARGRIET_15]})
question4_11 = Question({1: [Player.MARGRIET_15],
                         2: [Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15, Player.MARTINE_15,
                             Player.MARLIJN_15, Player.RIK_15, Player.VIKTOR_15]})
question4_17 = Question({1: [Player.MARTINE_15], 2: [Player.AJOUAD_15], 3: [Player.CAROLINA_15], 4: [Player.VIKTOR_15],
                         5: [Player.RIK_15], 6: [Player.MARGRIET_15], 7: [Player.MARLIJN_15], 8: [Player.CHRIS_15]})
question4_20 = Question({1: [Player.AJOUAD_15], 2: [Player.CAROLINA_15], 3: [Player.CHRIS_15], 4: [Player.MARGRIET_15],
                         5: [Player.MARLIJN_15], 6: [Player.MARTINE_15], 7: [Player.RIK_15], 8: [Player.VIKTOR_15]})
result4 = Result(DropType.EXECUTION_DROP, [Player.AJOUAD_15])
episode4 = Episode(players4, result4,
                   {Player.CHRIS_15: TestInput({3: 3}), Player.MARLIJN_15: TestInput({20: 7}),
                    Player.RIK_15: TestInput({11: 2}), Player.MARTINE_15: TestInput({20: 4}),
                    Player.VIKTOR_15: TestInput({17: 8}), Player.AJOUAD_15: TestInput({1: 2}),
                    Player.MARGRIET_15: TestInput({11: 2})},
                   {1: question4_1, 3: question4_3, 11: question4_11, 17: question4_17, 20: question4_20})

# Aflevering 5 (afvaller: Viktor)
# Vragen:
# 4 - Heeft de Mol een joker aangenomen in ruil voor beloftes rond de Zwarte Vrijstelling:
# 1: Rik; 2: Carolina, Chris, Margriet, Marlijn, Martine, Viktor;
# 6 - Is de Mol de huidige penningmeester:
# 1: Rik; 2: Carolina, Chris, Margriet, Marlijn, Martine, Viktor;
# 7 - Tijdens de opdracht in de tempel:
# 1: Marlijn, Carolina; 2: Viktor, Rik, Margriet, Martine, Chris;
# 15 - Op de groepsfoto van de aflevering staat de Mol:
# 1: Martine, Rik, Carolina, Marlijn; 2: Margriet, Viktor, Chris;
# 17 - Met wie vormde de Mol een duo tijdens de Koeriers-opdracht:
# 1: Viktor; 2: Rik; 3: Martine; 4: Marlijn; 5: Margriet; 6: Carolina; 7: Chris;
# 18 - Wat was de eerste bezorgplaats van de Mol tijdens de Koeriersopdracht:
# 1: Viktor, Carolina; 2: Rik, Margriet; 3: Martine, Marlijn; 4: Chris;
# 20 - Wie is de Mol:
# 1: Carolina; 2: Chris; 3: Margriet; 4: Marlijn; 5: Martine; 6: Rik; 7: Viktor;
# Antwoorden: Rik (18, 4), Marlijn (20, 2), Viktor (7, 2), Margriet (15, 2), Carolina (6, 1), Martine (4, 2)
players5 = [Player.CAROLINA_15, Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15,
            Player.RIK_15, Player.VIKTOR_15]
question5_4 = Question({1: [Player.RIK_15],
                        2: [Player.CAROLINA_15, Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15,
                            Player.MARTINE_15, Player.VIKTOR_15]})
question5_6 = Question({1: [Player.RIK_15],
                        2: [Player.CAROLINA_15, Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15,
                            Player.MARTINE_15, Player.VIKTOR_15]})
question5_7 = Question({1: [Player.MARLIJN_15, Player.CAROLINA_15],
                        2: [Player.VIKTOR_15, Player.RIK_15, Player.MARGRIET_15, Player.MARTINE_15, Player.CHRIS_15]})
question5_15 = Question({1: [Player.MARTINE_15, Player.RIK_15, Player.CAROLINA_15, Player.MARLIJN_15],
                         2: [Player.MARGRIET_15, Player.VIKTOR_15, Player.CHRIS_15]})
question5_17 = Question({1: [Player.VIKTOR_15], 2: [Player.RIK_15], 3: [Player.MARTINE_15], 4: [Player.MARLIJN_15],
                         5: [Player.MARGRIET_15], 6: [Player.CAROLINA_15], 7: [Player.CHRIS_15]})
question5_18 = Question({1: [Player.VIKTOR_15, Player.CAROLINA_15],
                         2: [Player.RIK_15, Player.MARGRIET_15],
                         3: [Player.MARTINE_15, Player.MARLIJN_15],
                         4: [Player.CHRIS_15]})
question5_20 = Question({1: [Player.CAROLINA_15], 2: [Player.CHRIS_15], 3: [Player.MARGRIET_15], 4: [Player.MARLIJN_15],
                         5: [Player.MARTINE_15], 6: [Player.RIK_15], 7: [Player.VIKTOR_15]})
result5 = Result(DropType.EXECUTION_DROP, [Player.VIKTOR_15])
episode5 = Episode(players5, result5,
                   {Player.RIK_15: TestInput({18: 4}), Player.MARLIJN_15: TestInput({20: 2}),
                    Player.VIKTOR_15: TestInput({7: 2}), Player.MARGRIET_15: TestInput({15: 2}),
                    Player.CAROLINA_15: TestInput({6: 1}), Player.MARTINE_15: TestInput({4: 2}),
                    Player.CHRIS_15: TestInput({17: 3})},
                   {4: question5_4, 6: question5_6, 7: question5_7, 15: question5_15, 17: question5_17,
                    18: question5_18, 20: question5_20})

# Aflevering 6 (afvaller: Carolina)
# Vragen:
# 5 - In welke kleur truck reed de Mol bij het achteruit parkeren:
# 1: Carolina, Chris; 2: Margriet; 3: Rik; 4: Marlijn, Martine;
# 7 - Was de Mol de slechtste chauffeur van Hambantota:
# 1: Martine, Rik, Margriet, Marlijn; 2: Carolina, Chris;
# 16 - Hoeveel kokers heeft de Mol ingeleverd aan het eind van de Lijnen-opdracht:
# 1: Chris; 2: Margriet, Rik; 3: Martine, Marlijn; 4: Carolina;
# 20 - Wie is de Mol:
# 1: Carolina; 2: Chris; 3: Margriet; 4: Marlijn; 5: Martine; 6: Rik;
# Antwoorden: Carolina (7, 2), Chris (5, 2), Margriet (20, 2), Martine (16, 2)
players6 = [Player.CAROLINA_15, Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15,
            Player.RIK_15]
question6_5 = Question({1: [Player.CAROLINA_15, Player.CHRIS_15],
                        2: [Player.MARGRIET_15],
                        3: [Player.RIK_15],
                        4: [Player.MARLIJN_15, Player.MARTINE_15]})
question6_7 = Question({1: [Player.MARTINE_15, Player.RIK_15, Player.MARGRIET_15, Player.MARLIJN_15],
                        2: [Player.CAROLINA_15, Player.CHRIS_15]})
question6_16 = Question({1: [Player.CHRIS_15],
                         2: [Player.MARGRIET_15, Player.RIK_15],
                         3: [Player.MARTINE_15, Player.MARLIJN_15],
                         4: [Player.CAROLINA_15]})
question6_20 = Question({1: [Player.CAROLINA_15], 2: [Player.CHRIS_15], 3: [Player.MARGRIET_15], 4: [Player.MARLIJN_15],
                         5: [Player.MARTINE_15], 6: [Player.RIK_15]})
result6 = Result(DropType.EXECUTION_DROP, [Player.CAROLINA_15])
episode6 = Episode(players6, result6,
                   {Player.CAROLINA_15: TestInput({7: 2}), Player.CHRIS_15: TestInput({5: 2}),
                    Player.MARGRIET_15: TestInput({20: 2}), Player.MARTINE_15: TestInput({16: 2})},
                   {5: question6_5, 7: question6_7, 16: question6_16, 20: question6_20})

# Aflevering 7 (geen schermen en geen afvallers maar wel data ingevuld voor regressie)
# Vragen:
# 1 - De Mol is:
# 1: Chris, Rik; 2: Margriet, Marlijn, Martine;
# 13 - Wanneer speechte de Mol in de tempel:
# 1: Martine; 2: Marlijn; 3: Rik; 4: Margriet; 5: Chris;
# 15 - Werd de Mol door de inwoners van Pundaluoya als Mol verkozen:
# 1: Chris; 2: Margriet, Marlijn, Martine, Rik;
# 20 - Wie is de Mol:
# 1: Chris; 2: Margriet; 3: Marlijn; 4: Martine; 5: Rik;
# Antwoorden: Marlijn (13, 2) (1 joker), Martine (15, 1), Chris (1, 2), Margriet (20, 5), Rik (1 joker)
players7 = [Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15, Player.RIK_15]
question7_1 = Question({1: [Player.CHRIS_15, Player.RIK_15],
                        2: [Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15]})
question7_13 = Question({1: [Player.MARTINE_15], 2: [Player.MARLIJN_15], 3: [Player.RIK_15], 4: [Player.MARGRIET_15],
                         5: [Player.CHRIS_15]})
question7_15 = Question({1: [Player.CHRIS_15],
                         2: [Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15, Player.RIK_15]})
question7_20 = Question({1: [Player.CHRIS_15], 2: [Player.MARGRIET_15], 3: [Player.MARLIJN_15], 4: [Player.MARTINE_15],
                         5: [Player.RIK_15]})
result7 = Result(DropType.NO_DROP_NOR_SCREENS, [])
episode7 = Episode(players7, result7,
                   {Player.MARLIJN_15: TestInput({13: 2}, jokers = 1), Player.MARTINE_15: TestInput({15: 1}),
                    Player.CHRIS_15: TestInput({1: 2}), Player.MARGRIET_15: TestInput({20: 5}),
                    Player.RIK_15: TestInput(jokers = 1)},
                   {1: question7_1, 13: question7_13, 15: question7_15, 20: question7_20})

# Aflevering 8 (afvaller: Martine)
# Vragen:
# 1 - De Mol is een:
# 1: Chris, Rik; 2: Margriet, Marlijn, Martine;
# 6 - Wanneer kwam de Mol bij de rekentafel om geld te tellen tijdens de Geld plukken-opdracht:
# 1: Chris; 2: Rik; 3: Martine; 4: Margriet; 5: Marlijn;
# 12 - Was de stift zoek in het team van de Mol tijdens de Straattaal-opdracht:
# 1: Rik, Martine, Chris; 2: Margriet, Marlijn;
# 16 - Wanneer ging de Mol de theefabriek binnen om enveloppen te verzamelen:
# 1: Martine; 2: Margriet; 3: Marlijn; 4: Rik; 5: Chris;
# 18 - Hoeveel enveloppen heeft de Mol gepakt in de theefabriek
# 1: Rik; 2: Margriet, Marlijn; 3: Martine, Chris;
# Antwoorden: Chris (16, 2), Marlijn (6, 4), Rik (12, 2), Margriet (18, 1), Martine (1, 2)
players8 = [Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15, Player.RIK_15]
question8_1 = Question({1: [Player.CHRIS_15, Player.RIK_15],
                        2: [Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15]})
question8_6 = Question({1: [Player.CHRIS_15], 2: [Player.RIK_15], 3: [Player.MARTINE_15], 4: [Player.MARGRIET_15],
                        5: [Player.MARLIJN_15]})
question8_12 = Question({1: [Player.RIK_15, Player.MARTINE_15, Player.CHRIS_15],
                         2: [Player.MARGRIET_15, Player.MARLIJN_15]})
question8_16 = Question({1: [Player.MARTINE_15], 2: [Player.MARGRIET_15], 3: [Player.MARLIJN_15], 4: [Player.RIK_15],
                         5: [Player.CHRIS_15]})
question8_18 = Question({1: [Player.RIK_15],
                         2: [Player.MARGRIET_15, Player.MARLIJN_15],
                         3: [Player.MARTINE_15, Player.CHRIS_15]})
result8 = Result(DropType.EXECUTION_DROP, [Player.MARTINE_15])
episode8 = Episode(players8, result8,
                   {Player.CHRIS_15: TestInput({16: 2}), Player.MARLIJN_15: TestInput({6: 4}),
                    Player.RIK_15: TestInput({12: 2}), Player.MARGRIET_15: TestInput({18: 1}),
                    Player.MARTINE_15: TestInput({1: 2})},
                   {1: question8_1, 6: question8_6, 12: question8_12, 16: question8_16, 18: question8_18})

# Aflevering 9 - First (afvaller: Chris)
# Vragen:
# 1 - De Mol is een:
# 1: Chris, Rik; 2: Margriet, Marlijn;
# 16 - Wat pakte de Mol aanvankelijk aan de Jokertafel:
# 1: Chris, Margriet; 2: Marlijn; 3: Rik;
# 20 - Wie is de Mol:
# 1: Chris; 2: Margriet; 3: Marlijn; 4: Rik;
# Antwoorden: Marlijn (1 joker), Rik (1, 2) (1 joker), Margriet (16, 3) (2 jokers), Chris (20, 2)
players9f = [Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.RIK_15]
question9f_1 = Question({1: [Player.CHRIS_15, Player.RIK_15],
                        2: [Player.MARGRIET_15, Player.MARLIJN_15]})
question9f_16 = Question({1: [Player.CHRIS_15, Player.MARGRIET_15],
                         2: [Player.MARLIJN_15],
                         3: [Player.RIK_15]})
question9f_20 = Question({1: [Player.CHRIS_15], 2: [Player.MARGRIET_15], 3: [Player.MARLIJN_15], 4: [Player.RIK_15]})
result9f = Result(DropType.EXECUTION_DROP, [Player.CHRIS_15])
episode9f = Episode(players9f, result9f,
                   {Player.MARLIJN_15: TestInput(jokers = 1), Player.RIK_15: TestInput({1: 2}, jokers = 1),
                    Player.MARGRIET_15: TestInput({16: 3}, jokers = 2), Player.CHRIS_15: TestInput({20: 2})},
                   {1: question9f_1, 16: question9f_16, 20: question9f_20})

# Aflevering 9 - Second (afvaller: Marlijn) (pas in de reunie bekend)
# 4 - Bemande de Mol bij aanvang van de Schermen-opdracht de controlroom:
# 1: Margiet; 2: Marlijn, Rik;
# 8 - Wanneer arriveerde het team van de Mol bij de vrachtauto van de Laden/lossen-opdracht:
# 1: Marlijn; 2: Margriet, Rik;
# 14 - Met wie vormde de mol een duo tijdens de Koeriersopdracht:
# 1: Rik; 2: Marlijn; 3: Margriet;
# 18 - Wat was de Molactie tijdens de Watervliegtuig-opdracht:
# 1: Margriet, Marlijn; 2: Rik;
# 40 - Wie is de Mol:
# 1: Margriet; 2: Marlijn; 3: Rik;
# Antwoorden: Marlijn (4, 1) (40, 1), Margriet (14, 1) (18, 2) (40, 3), Rik (8, 2) (40, 1)
players9s = [Player.MARGRIET_15, Player.MARLIJN_15, Player.RIK_15]
question9s_4 = Question({1: [Player.MARGRIET_15],
                         2: [Player.MARLIJN_15, Player.RIK_15]})
question9s_8 = Question({1: [Player.MARLIJN_15],
                         2: [Player.MARGRIET_15, Player.RIK_15]})
question9s_14 = Question({1: [Player.RIK_15], 2: [Player.MARLIJN_15], 3: [Player.MARGRIET_15]})
question9s_18 = Question({1: [Player.MARGRIET_15, Player.MARLIJN_15],
                          2: [Player.RIK_15]})
question9s_40 = Question({1: [Player.MARGRIET_15], 2: [Player.MARLIJN_15], 3: [Player.RIK_15]})
result9s = Result(DropType.EXECUTION_DROP, [Player.MARLIJN_15])
episode9s = Episode(players9s, result9s,
                   {Player.MARLIJN_15: TestInput({4: 1, 40: 1}), Player.MARGRIET_15: TestInput({14: 1, 18: 2, 40: 3}),
                    Player.RIK_15: TestInput({8: 2, 40: 1})},
                   {4: question9s_4, 8: question9s_8, 14: question9s_14, 18: question9s_18, 40: question9s_40},
                    num_questions = 40)
season15 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                             8: episode8, 9: episode9f, 10: episode9s})