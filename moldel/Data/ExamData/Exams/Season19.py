from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

# Aflevering 1 (geen afvaller, alleen Niels, Jamie, Robert en Rick-Paul kregen hun scherm te zien)
# Vragen:
# 1 - De Mol is:
# 1: Niels, Rick-Paul, Robert, Sinan, Jamie; 2: Evi, Evelien, Merel, Nikkie, Sarah;
# 4 - Trok de Mol helemaal alleen een kist omhoog tijdens de opdracht 'Over Bruggen'?
# 1: Jamie; 2: Evi, Evelien, Merel, Niels, Nikkie, Rick-Paul, Robert, Sarah, Sinan;
# 10 - Bij welke groep werd de Mol ten dans gevraagd tijdens de opdracht 'In Zicht'?
# 1: Jamie, Rick-Paul, Sarah; 2: Merel, Nikkie, Niels, Evi; 3: Sinan, Robert, Evelien;
# 11 - Heeft de Mol op blote voeten gedanst bij de opdracht 'In Zicht'?
# 1: Jamie, 2: Evi, Evelien, Merel, Niels, Nikkie, Rick-Paul, Robert, Sarah, Sinan;
# 12 - Pakte de Mol geld aan van Rik aan het einde van de opdracht 'In Zicht'?
# 1: Evelien; 2: Evi, Jamie, Merel, Niels, Nikkie, Rick-Paul, Robert, Sarah, Sinan
# 16 - Wat was de kleur van de fiets van de Mol bij de opdracht 'Rondje om de Kerk'?
# 1 (Rood): Evi, Robert, Nikkie, Merel, Sarah; 2 (Groen): Evelien, Niels, Sinan; 3 (Blauw): Jamie, Rick-Paul
# Antwoorden: Niels (4, 2), Evelien (11, 1) (Geen Scherm), Jamie (1, 1), Robert (10, 1), Merel (Geen Scherm),
# Nikkie (16, 2) (Geen Scherm), Rick-Paul (12, 1), Evi: (Geen Scherm)
players1 = [Player.EVI_19, Player.EVELIEN_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19,
            Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19]
question1_1 = Question({1: [Player.NIELS_19, Player.RICK_PAUL_19, Player.ROBERT_19, Player.SINAN_19, Player.JAMIE_19],
                        2: [Player.EVI_19, Player.EVELIEN_19, Player.MEREL_19, Player.NIKKIE_19, Player.SARAH_19]})
question1_4 = Question({1: [Player.JAMIE_19],
                        2: [Player.EVI_19, Player.EVELIEN_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19,
                            Player.RICK_PAUL_19, Player.ROBERT_19, Player.SINAN_19, Player.SARAH_19]})
question1_10 = Question({1: [Player.JAMIE_19, Player.RICK_PAUL_19, Player.SARAH_19],
                         2: [Player.MEREL_19, Player.NIKKIE_19, Player.NIELS_19, Player.EVI_19],
                         3: [Player.SINAN_19, Player.ROBERT_19, Player.EVELIEN_19]})
question1_11 = Question({1: [Player.JAMIE_19],
                         2: [Player.EVI_19, Player.EVELIEN_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19,
                             Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19]})
question1_12 = Question({1: [Player.EVELIEN_19],
                         2: [Player.EVI_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19,
                             Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19]})
question1_16 = Question({1: [Player.EVI_19, Player.ROBERT_19, Player.NIKKIE_19, Player.MEREL_19, Player.SARAH_19],
                         2: [Player.EVELIEN_19, Player.NIELS_19, Player.SINAN_19],
                         3: [Player.JAMIE_19, Player.RICK_PAUL_19]})
result1 = Result(DropType.POSSIBLE_DROP, [Player.EVELIEN_19, Player.ROBERT_19, Player.NIKKIE_19, Player.EVI_19])
episode1 = Episode(players1, result1,
                   {Player.NIELS_19: TestInput({4: 2}), Player.EVELIEN_19: TestInput({11: 1}),
                    Player.JAMIE_19: TestInput({1: 1}), Player.ROBERT_19: TestInput({10: 1}),
                    Player.NIKKIE_19: TestInput({16: 2}), Player.RICK_PAUL_19: TestInput({12: 1})},
                   {1: question1_1, 4: question1_4, 10: question1_10, 11: question1_11, 12: question1_12,
                    16: question1_16})

# Aflevering 2 (afvaller: Evi)
# Vragen:
# 2 - Hoeveel zwemdiploma's heeft de Mol:
# 1 (0 diploma's): Evi; 2 (1 diploma): Sinan;  3 (2 diploma's): Merel, Niels, Rick-Paul, Robert;
# 4 (3 diploma's): Evelien, Sarah, Jamie; 5 (6 diploma's): Nikkie;
# 4 - Waar bevond de Mol zich tijdens de opdracht 'Ver Tellen':
# 1: Evelien, Evi, Jamie, Merel, Niels, Robert, Sarah, Sinan; 2: Nikkie, Rick-Paul;
# 10 - Als hoeveelste ging de Mol het veld in tijdens de opdracht 'Uit Stralen':
# 1: Sinan; 2: Merel; 3: Niels; 4: Nikkie; 5: Sarah; 6: Jamie; 7: Evelien; 8: Rick-Paul; 9: Robert; 10: Evi;
# 20 - Wie is de Mol:
# 1: Evelien; 2: Evi; 3: Jamie; 4: Merel; 5: Niels; 6: Nikkie; 7: Rick-Paul; 8: Robert; 9: Sarah; 10: Sinan;
# Antwoorden: Rick-Paul (2, 4), Nikkie (4, 1), Merel (20, 1), Robert (1 joker), Jamie (10, 1)
players2 = [Player.EVI_19, Player.EVELIEN_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19,
            Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19]
question2_2 = Question({1: [Player.EVI_19],
                        2: [Player.SINAN_19],
                        3: [Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.ROBERT_19],
                        4: [Player.EVELIEN_19, Player.SARAH_19, Player.JAMIE_19],
                        5: [Player.NIKKIE_19]})
question2_4 = Question({1: [Player.EVELIEN_19, Player.EVI_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19,
                            Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19],
                        2: [Player.NIKKIE_19, Player.RICK_PAUL_19]})
question2_10 = Question({1: [Player.SINAN_19], 2: [Player.MEREL_19], 3: [Player.NIELS_19], 4: [Player.NIKKIE_19],
                         5: [Player.SARAH_19], 6: [Player.JAMIE_19], 7: [Player.EVELIEN_19], 8: [Player.RICK_PAUL_19],
                         9: [Player.ROBERT_19], 10: [Player.EVI_19]})
question2_20 = Question({1: [Player.EVELIEN_19], 2: [Player.EVI_19], 3: [Player.JAMIE_19], 4: [Player.MEREL_19],
                         5: [Player.NIELS_19], 6: [Player.NIKKIE_19], 7: [Player.RICK_PAUL_19], 8: [Player.ROBERT_19],
                         9: [Player.SARAH_19], 10: [Player.SINAN_19]})
result2 = Result(DropType.EXECUTION_DROP, [Player.EVI_19])
episode2 = Episode(players2, result2,
                   {Player.RICK_PAUL_19: TestInput({2: 4}), Player.NIKKIE_19: TestInput({4: 1}),
                    Player.MEREL_19: TestInput({20: 2}), Player.ROBERT_19: TestInput(jokers = 1),
                    Player.JAMIE_19: TestInput({10: 1})},
                   {2: question2_2, 4: question2_4, 10: question2_10, 20: question2_20})

# Aflevering 3 (afvaller: Nikkie, wordt pas bekend aan het begin van aflevering 4)
# Vragen:
# 4 - Welk Spaanse woord kreeg de Mol bij aanvang van de opdracht 'Vlag Uithangen':
# 1: Evelien, 2: Jamie, 3: Merel, 4: Sinan, 5: Niels, 6: Nikkie, 7: Rick, 8: Robert, 9: Sarah (Niet Accuraat)
# 7 - Kreeg de Mol de taak om de was op te hangen bij aanvang van de opdracht 'Vlag Uithangen':
# 1: Rick, 2: Evelien, Jamie, Merel, Niels, Nikkie, Robert, Sarah, Sinan
# 12 - Won de Mol het duel bij de opdracht 'Stapelgek':
# 1: Robert, Sarah, Rick, Evelien; 2: Jamie, Merel, Nikkie, Sinan; 3: Niels
# 16 - Waarvoor stemde de Mol tijdens de opdracht 'Op Treden':
# 1: Evelien, Jamie, Niels, Robert, Sarah; 2: Sinan, Rick, Merel, Nikkie
# 19 - Pakte de Mol het geld aan het einde van de opdracht 'Op Treden':
# 1: Sarah; 2: Evelien, Jamie, Merel, Niels, Nikie, Rick, Robert, Sinan
# 20 - Wie is de Mol:
# 1: Evelien; 2: Jamie; 3: Merel; 4: Niels; 5: Nikkie; 6: Rick-Paul; 7: Robert; 8: Sarah; 9: Sinan
# Antwoorden: Rick-Paul (4, 4), Niels (16, 1), Nikkie (12, 1), Robert (1 Joker), Merel (Vrijstelling), Jamie (7, 1),
# Sarah (19, 2) (1 Joker), Evelien (20, 9) (2 Jokers)
players3 = [Player.EVELIEN_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19, Player.RICK_PAUL_19,
            Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19]
question3_4 = Question({1: [Player.EVELIEN_19], 2: [Player.JAMIE_19], 3: [Player.MEREL_19], 4: [Player.SINAN_19],
                        5: [Player.NIELS_19], 6: [Player.NIKKIE_19], 7: [Player.RICK_PAUL_19], 8: [Player.ROBERT_19],
                        9: [Player.SARAH_19]})
question3_7 = Question({1: [Player.RICK_PAUL_19],
                        2: [Player.EVELIEN_19, Player.JAMIE_19, Player.MEREL_19, Player.SINAN_19, Player.NIELS_19,
                            Player.NIKKIE_19, Player.ROBERT_19, Player.SARAH_19]})
question3_12 = Question({1: [Player.ROBERT_19, Player.SARAH_19, Player.RICK_PAUL_19, Player.EVELIEN_19],
                         2: [Player.JAMIE_19, Player.MEREL_19, Player.NIKKIE_19, Player.SINAN_19],
                         3: [Player.NIELS_19]})
question3_16 = Question({1: [Player.EVELIEN_19, Player.JAMIE_19, Player.NIELS_19, Player.ROBERT_19, Player.SARAH_19],
                         2: [Player.SINAN_19, Player.RICK_PAUL_19, Player.MEREL_19, Player.NIKKIE_19]})
question3_19 = Question({1: [Player.SARAH_19],
                         2: [Player.EVELIEN_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19,
                             Player.RICK_PAUL_19, Player.ROBERT_19, Player.SINAN_19]})
question3_20 = Question({1: [Player.EVELIEN_19], 2: [Player.JAMIE_19], 3: [Player.MEREL_19], 4: [Player.NIELS_19],
                         5: [Player.NIKKIE_19], 6: [Player.RICK_PAUL_19], 7: [Player.ROBERT_19], 8: [Player.SARAH_19],
                         9: [Player.SINAN_19]})
result3 = Result(DropType.EXECUTION_DROP, [Player.NIKKIE_19])
episode3 = Episode(players3, result3,
                   {Player.RICK_PAUL_19: TestInput({4: 4}), Player.NIELS_19: TestInput({16: 1}),
                    Player.NIKKIE_19: TestInput({12: 1}), Player.ROBERT_19: TestInput(jokers = 1),
                    Player.MEREL_19: TestInput(immunity = True), Player.JAMIE_19: TestInput({7: 1}),
                    Player.SARAH_19: TestInput({19: 2}, jokers = 1), Player.EVELIEN_19: TestInput({20: 9}, jokers = 2)},
                   {4: question3_4, 7: question3_7, 12: question3_12, 16: question3_16, 19: question3_19,
                    20: question3_20})

# Aflevering 4 (afvaller: Evelien)
# Vragen:
# 5 - Als hoeveelste werd de kooi van de Mol geopend tijdens de opdracht 'Min of Meer':
# 1: Niels, Evelien; 2: Sarah, Robert; 3: Rick-Paul, Merel; 4: Jamie, Sinan
# 7 - Op welk bedrag had het duo van de Mol de geldklok stilgezet, tijdens de opdracht 'Min of Meer':
# 1 (-100): Niels, Evelien; 2 (-150): Robert, Sarah; 3 (-250): Merel, Rick-Paul; 4 (geen klok): Jamie, Sinan
# 18 - Voerde de Mol het laatste foute antwoord in tijdens de opdracht 'Koffiepedia':
# 1: Sarah; 2: Evelien, Jamie, Merel, Niels, Rick-Paul, Robert, Sinan;
# Antwoorden: Jamie (5, 1), Robert (7, 2), Niels (1 Joker), Evelien (18, 2)
players4 = [Player.EVELIEN_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.ROBERT_19,
            Player.SARAH_19, Player.SINAN_19]
question4_5 = Question({1: [Player.NIELS_19, Player.EVELIEN_19],
                        2: [Player.SARAH_19, Player.ROBERT_19],
                        3: [Player.RICK_PAUL_19, Player.MEREL_19],
                        4: [Player.JAMIE_19, Player.SINAN_19]})
question4_7 = Question({1: [Player.NIELS_19, Player.EVELIEN_19],
                        2: [Player.ROBERT_19, Player.SARAH_19],
                        3: [Player.RICK_PAUL_19, Player.MEREL_19],
                        4: [Player.JAMIE_19, Player.SINAN_19]})
question4_18 = Question({1: [Player.SARAH_19],
                         2: [Player.EVELIEN_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19,
                             Player.ROBERT_19, Player.SINAN_19]})
result4 = Result(DropType.EXECUTION_DROP, [Player.EVELIEN_19])
episode4 = Episode(players4, result4,
                   {Player.JAMIE_19: TestInput({5: 1}), Player.ROBERT_19: TestInput({7: 2}),
                    Player.NIELS_19: TestInput(jokers = 1), Player.EVELIEN_19: TestInput({18: 2})},
                   {5: question4_5, 7: question4_7, 18: question4_18})

# Aflevering 5 (afvaller: Robert)
# Vragen:
# 6 - Hield de Mol een foto in zijn hand tijdens de afronding van de opdracht 'Pittoresk'
# 1: Jamie; 2: Merel, Niels, Rick-Paul, Robert, Sinan
# 12 - Wat was de kleur van de auto waar de Mol in reed tijdens de opdracht 'Parkeergeld'
# 1: Jamie; 2: Rick-Paul; 3: Merel, Sarah, Niels, Sinan, Robert
# 17 - Welke abseil-lijn nam de Mol vanaf beneden gezien tijdens 'Sleutelhanger'
# 1: Sarah, Merel, Rick-Paul; 2: Jamie, Robert, Niels; 3: Sinan
# 20 - Wie is de Mol:
# 1: Jamie; 2: Merel; 3: Niels; 4: Rick-Paul; 5: Robert; 6: Sarah; 7: Sinan
# Antwoorden: Sarah (6, 2), Rick-Paul (17, 2), Sinan (12, 3), Jamie (20, 4)
players5 = [Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19,
            Player.SINAN_19]
question5_6 = Question({1: [Player.JAMIE_19],
                        2: [Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19,
                            Player.SINAN_19]})
question5_12 = Question({1: [Player.JAMIE_19],
                         2: [Player.RICK_PAUL_19],
                         3: [Player.MEREL_19, Player.SARAH_19, Player.NIELS_19, Player.ROBERT_19, Player.SINAN_19]})
question5_17 = Question({1: [Player.SARAH_19, Player.MEREL_19, Player.RICK_PAUL_19],
                         2: [Player.JAMIE_19, Player.ROBERT_19, Player.NIELS_19],
                         3: [Player.SINAN_19]})
question5_20 = Question({1: [Player.JAMIE_19], 2: [Player.MEREL_19], 3: [Player.NIELS_19], 4: [Player.RICK_PAUL_19],
                         5: [Player.ROBERT_19], 6: [Player.SARAH_19], 7: [Player.SINAN_19]})
result5 = Result(DropType.EXECUTION_DROP, [Player.ROBERT_19])
episode5 = Episode(players5, result5,
                   {Player.SARAH_19: TestInput({6: 2}), Player.RICK_PAUL_19: TestInput({17: 2}),
                    Player.SINAN_19: TestInput({12: 3}), Player.JAMIE_19: TestInput({20: 4})},
                    {6: question5_6, 12: question5_12, 17: question5_17, 20: question5_20})

# Aflevering 6 (geen afvaller en geen informatie, maar wel data ingevoerd voor de regressie)
# Vragen:
# 6 - Werkte de Mol aan de rode draad opdracht tijdens 'Steentje bijdragen':
# 1: Niels, Jamie, Sarah; 2: Merel, Sinan, Rick-Paul;
# 7 - Bestuurde de Mol de wals tijdens de opdracht 'Steentje Bijdragen':
# 1: Sinan; 2: Jamie, Merel, Rick-Paul, Sarah, Niels;
# 8 - Aan welke opdracht werkte de Mol aan het einde van 'Steentje bijdragen':
# 1: Rick-Paul, Sinan, Merel; 2: Jamie, Niels, Sarah;
# 16 - Welke verkeersregel kreeg de Mol toegewezen tijdens de opdracht 'Links/Rechts':
# 1: Jamie, Merel; 2: Sarah, Sinan; 3: Rick-Paul, Niels;
# 18 - Hoe vaak was de Mol op tijd bij Rik tijdens de opdracht 'Links/Rechts':
# 1: Merel, Niels, Jamie, Rick-Paul; 2: Sinan; 3: Sarah;
# 20 - Wie is de Mol:
# 1: Jamie; 2: Merel; 3: Niels; 4: Rick-Paul; 5: Sarah; 6: Sinan;
# Antwoorden: Jamie (6, 2), Rick-Paul (16, 1) (1 joker), Sinan (18, 1), Niels (7, 1), Sarah (20, 1), Merel (8, 1)
players6 = [Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.SARAH_19, Player.SINAN_19]
question6_6 = Question({1: [Player.NIELS_19, Player.JAMIE_19, Player.SARAH_19],
                        2: [Player.MEREL_19, Player.SINAN_19, Player.RICK_PAUL_19]})
question6_7 = Question({1: [Player.SINAN_19],
                        2: [Player.JAMIE_19, Player.MEREL_19, Player.RICK_PAUL_19, Player.SARAH_19, Player.NIELS_19]})
question6_8 = Question({1: [Player.RICK_PAUL_19, Player.SINAN_19, Player.MEREL_19],
                        2: [Player.JAMIE_19, Player.NIELS_19, Player.SARAH_19]})
question6_16 = Question({1: [Player.JAMIE_19, Player.MEREL_19],
                         2: [Player.SARAH_19, Player.SINAN_19],
                         3: [Player.RICK_PAUL_19, Player.NIELS_19]})
question6_18 = Question({1: [Player.MEREL_19, Player.NIELS_19, Player.JAMIE_19, Player.RICK_PAUL_19],
                         2: [Player.SINAN_19],
                         3: [Player.SARAH_19]})
question6_20 = Question({1: [Player.JAMIE_19], 2: [Player.MEREL_19], 3: [Player.NIELS_19], 4: [Player.RICK_PAUL_19],
                         5: [Player.SARAH_19], 6: [Player.SINAN_19]})
result6 = Result(DropType.NO_DROP_NOR_SCREENS, [])
episode6 = Episode(players6, result6,
                   {Player.JAMIE_19: TestInput({6: 2}), Player.RICK_PAUL_19: TestInput({16: 1}, jokers = 1),
                    Player.SINAN_19: TestInput({18: 1}), Player.NIELS_19: TestInput({7: 1}),
                    Player.SARAH_19: TestInput({20: 1}), Player.MEREL_19: TestInput({8: 1})},
                    {6: question6_6, 7: question6_7, 8: question6_8, 16: question6_16, 18: question6_18, 20: question6_20})

# Aflevering 7 (afvallers: Jamie, Rick-Paul)
# Vragen:
# 6 - Naar wie kon de Mol kisten verplaatsen tijdens de opdracht 'Getouwtrek':
# 1: Rick-Paul; 2: Merel; 3: Sarah; 4: Jamie; 5: Niels; 6: Sinan
# 11 - Als hoeveelste kwam de Mol bij Rik tijdens de opdracht 'Roulette':
# 1: Niels; 2: Jamie; 3: Sinan; 4: Merel; 5: Sarah; 6: Rick-Paul;
# 12 - Wat was de keuze van de Mol tijdens de opdracht 'Roulette':
# 1: Niels, Sinan; 2: Rick-Paul, Jamie, Merel; 3: Sarah
# 18 - Bij welk station begon de Mol tijdens de opdracht 'Geld Oogsten':
# 1: Rick-Paul; 2: Sarah; 3: Sinan; 4: Merel; 5: Niels, Jamie
# 20 - Wie is de Mol:
# 1: Jamie; 2: Merel; 3: Niels; 4: Rick-Paul; 5: Sarah; 6: Sinan
# Antwoorden: Merel (11, 2), Rick-Paul (20, 1) (1 Joker), Sinan (12, 2), Sarah (6, 2), Niels (18, 5) (2 Jokers),
# Jamie (20, 4) (2 Jokers)
players7 = [Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.SARAH_19, Player.SINAN_19]
question7_6 = Question({1: [Player.RICK_PAUL_19], 2: [Player.MEREL_19], 3: [Player.SARAH_19], 4: [Player.JAMIE_19],
                        5: [Player.NIELS_19], 6: [Player.SINAN_19]})
question7_11 = Question({1: [Player.NIELS_19], 2: [Player.JAMIE_19], 3: [Player.SINAN_19], 4: [Player.MEREL_19],
                         5: [Player.SARAH_19], 6: [Player.RICK_PAUL_19]})
question7_12 = Question({1: [Player.NIELS_19, Player.SINAN_19],
                         2: [Player.RICK_PAUL_19, Player.JAMIE_19, Player.MEREL_19],
                         3: [Player.SARAH_19]})
question7_18 = Question({1: [Player.RICK_PAUL_19], 2: [Player.SARAH_19], 3: [Player.SINAN_19], 4: [Player.MEREL_19],
                         5: [Player.NIELS_19, Player.JAMIE_19]})
question7_20 = Question({1: [Player.JAMIE_19], 2: [Player.MEREL_19], 3: [Player.NIELS_19], 4: [Player.RICK_PAUL_19],
                         5: [Player.SARAH_19], 6: [Player.SINAN_19]})
result7 = Result(DropType.EXECUTION_DROP, [Player.JAMIE_19, Player.RICK_PAUL_19])
episode7 = Episode(players7, result7,
                   {Player.MEREL_19: TestInput({11: 2}), Player.RICK_PAUL_19: TestInput({20: 1}, jokers = 1),
                    Player.SINAN_19: TestInput({12: 2}), Player.SARAH_19: TestInput({6: 2}),
                    Player.NIELS_19: TestInput({18: 5}, jokers = 2), Player.JAMIE_19: TestInput({20: 4}, jokers = 2)},
                    {6: question7_6, 11: question7_11, 12: question7_12, 18: question7_18, 20: question7_20})

# Aflevering 8 (afvaller: Sinan)
# Vragen:
# 3 - In welke ronde betrad de Mol het speelveld tijdens de opdracht 'In het vizier'?
# 1: Niels, Merel; 2: Sarah; 3: Sinan
# 4 - Als hoeveelste mocht de Mol een pin pakken tijdens de opdracht 'Ten val brengen'? (Inacurraat)
# 1: Sarah; 2: Merel; 3: Niels; 4: Sinan
# 5 - Met wie vormde de Mol een duo tijdens de opdracht 'Vuurproef'? (Inaccuraat)
# 1: Niels; 2: Merel; 3: Sinan; 4: Sarah
# Antwoord: Merel (4, 1), Sinan (5, 2), Sarah (3, 1), Niels (Vrijstelling)
players8 = [Player.MEREL_19, Player.NIELS_19, Player.SARAH_19, Player.SINAN_19]
question8_3 = Question({1: [Player.NIELS_19, Player.MEREL_19], 2: [Player.SARAH_19], 3: [Player.SINAN_19]})
question8_4 = Question({1: [Player.SARAH_19], 2: [Player.MEREL_19], 3: [Player.NIELS_19], 4: [Player.SINAN_19]})
question8_5 = Question({1: [Player.NIELS_19], 2: [Player.MEREL_19], 3: [Player.SINAN_19], 4: [Player.SARAH_19]})
result8 = Result(DropType.EXECUTION_DROP, [Player.SINAN_19])
episode8 = Episode(players8, result8,
                   {Player.MEREL_19: TestInput({4: 1}), Player.SINAN_19: TestInput({5: 2}),
                    Player.SARAH_19: TestInput({3: 1}), Player.NIELS_19: TestInput(immunity = True)},
                    {3: question8_3, 4: question8_4, 5: question8_5})

# Aflevering 9 (afvaller: Niels) (pas in de reunie bekend)
# 3 - Waarvoor stemde de Mol naar aanleiding van de opdracht 'Over Bruggen':
# 1: Merel, Niels; 2: Sarah;
# 6 - Als hoeveelste ging de Mol het speelveld in tijdens de opdracht 'Uit Stralen':
# 1: Merel; 2: Niels; 3: Sarah;
# 11 - Op welk bedrag had het duo van de Mol de geldklok stopgezet bij de opdracht 'Min of meer':
# 1: Niels; 2: Sarah; 3: Merel;
# 22 - Wat zat er in de envelop van de Mol tijdens de opdracht 'Roulette':
# 1: Niels; 2: Sarah; 3: Merel;
# 28 - Welke rol had de Mol bij aanvang van de opdracht 'Ver Tellen':
# 1: Merel, Sarah; 2: Niels;
# 31 - Welke verkeersregel kreeg de Mol tijdens de opdracht 'Links/Rechts':
# 1: Merel; 2: Sarah; 3: Niels;
# 35 - Wat was de taak van de Mol bij de opdracht 'Parkeergeld':
# 1: Niels; 2: Merel, Sarah;
# 38 - Welke categorie stond er op het pak van de Mol tijdens de opdracht 'Koffiepedia':
# 1: Merel; 2: Sarah; 3: Niels;
# 40 - Wie is de Mol:
# 1: Merel; 2: Niels; 3: Sarah;
# Antwoorden: Merel (6, 3) (22, 2) (35, 2) (40, 3), Sarah (3, 1) (28, 1) (38, 1) (40, 1), Niels (11, 3) (31, 1) (40, 1)
players9 = [Player.MEREL_19, Player.NIELS_19, Player.SARAH_19]
question9_3 = Question({1: [Player.MEREL_19, Player.NIELS_19],
                        2: [Player.SARAH_19]})
question9_6 = Question({1: [Player.MEREL_19], 2: [Player.NIELS_19], 3: [Player.SARAH_19]})
question9_11 = Question({1: [Player.NIELS_19], 2: [Player.SARAH_19], 3: [Player.MEREL_19]})
question9_22 = Question({1: [Player.NIELS_19], 2: [Player.SARAH_19], 3: [Player.MEREL_19]})
question9_28 = Question({1: [Player.MEREL_19, Player.SARAH_19],
                         2: [Player.NIELS_19]})
question9_31 = Question({1: [Player.MEREL_19], 2: [Player.SARAH_19], 3: [Player.NIELS_19]})
question9_35 = Question({1: [Player.NIELS_19], 2: [Player.MEREL_19, Player.SARAH_19]})
question9_38 = Question({1: [Player.MEREL_19], 2: [Player.SARAH_19], 3: [Player.NIELS_19]})
question9_40 = Question({1: [Player.MEREL_19], 2: [Player.NIELS_19], 3: [Player.SARAH_19]})
result9 = Result(DropType.EXECUTION_DROP, [Player.NIELS_19])
episode9 = Episode(players9, result9,
                   {Player.MEREL_19: TestInput({6: 3, 22: 2, 35: 2, 40: 3}),
                    Player.SARAH_19: TestInput({3: 1, 28: 1, 38: 1, 40: 1}),
                    Player.NIELS_19: TestInput({11: 3, 31: 1, 40: 1})},
                    {3: question9_3, 6: question9_6, 11: question9_11, 22: question9_22, 28: question9_28,
                     31: question9_31, 35: question9_35, 38: question9_38, 40: question9_40}, num_questions = 40)
season19 = Season(players1, {1: episode1, 2: episode2, 3.5: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                             8: episode8, 10: episode9})