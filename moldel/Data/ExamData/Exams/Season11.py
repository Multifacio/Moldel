from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (geen afvaller, vanwege een groepsvrijstelling)
# 2 (Vraagnummer onbekend) - Stak de Mol vuurwerk af:
# 1: Anna, Art, Horace, Miryanna, Pepijn, Soundos; 2: Hanna, Jan, Karin, Patrick;
# 3 (Vraagnummer onbekend) - Nam de Mol een vrijstelling mee tijdens de vrijstellingsroute:
# 1: Anna, Hanna, Pepijn; 2: Art, Horace, Jan, Karin, Miryanna, Patrick, Soundos;
# Antwoorden: Jan (3, 2 pas bekend vanaf aflevering 4) (1 joker), Art (2 jokers), Pepijn (vrijstelling),
# Miryanna (2, 1 pas bekend vanaf aflevering 4), Karin (3, 1 pas bekend vanaf aflevering 4),
# Anna (2, 1 pas bekend vanaf aflevering 4) (3, 1 pas bekend vanaf aflevering 4)
players1 = [Player.ANNA_11, Player.ART_11, Player.HANNA_11, Player.HORACE_11, Player.JAN_11, Player.KARIN_11,
            Player.MIRYANNA_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11]
question1_2 = Question({1: [Player.ANNA_11, Player.ART_11, Player.HORACE_11, Player.MIRYANNA_11, Player.PEPIJN_11,
                            Player.SOUNDOS_11],
                        2: [Player.HANNA_11, Player.JAN_11, Player.KARIN_11, Player.PATRICK_11]})
question1_3 = Question({1: [Player.ANNA_11, Player.HANNA_11, Player.PEPIJN_11],
                        2: [Player.ART_11, Player.HORACE_11, Player.JAN_11, Player.KARIN_11, Player.MIRYANNA_11,
                            Player.PATRICK_11, Player.SOUNDOS_11]})
result1 = Result(DropType.POSSIBLE_DROP, [Player.ANNA_11, Player.ART_11, Player.HANNA_11, Player.HORACE_11,
            Player.JAN_11, Player.KARIN_11, Player.MIRYANNA_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11])
episode1 = Episode(players1, result1,
                   {Player.JAN_11: TestInput({3: DelayedAnswer(2, 4)}, jokers = 1), Player.ART_11: TestInput(jokers = 2),
                    Player.PEPIJN_11: TestInput(immunity = True), Player.MIRYANNA_11: TestInput({2: DelayedAnswer(1, 4)}),
                    Player.KARIN_11: TestInput({3: DelayedAnswer(1, 4)}),
                    Player.ANNA_11: TestInput({2: DelayedAnswer(1, 4), 3: DelayedAnswer(1, 4)})},
                   {2: question1_2, 3: question1_3})

# Aflevering 2 (afvaller: Hanna)
# 2 (Vraagnummer onbekend) - Wat was de Mol tijdens de boobytrap opdracht:
# 1: Anna, Hanna, Horace, Karin, Miryanna, Patrick, Pepijn, Soundos; 2: Art, Jan;
# 3 (Vraagnummer onbekend) - Werd de Mol tijdens de boobytrap opdracht gedood door een sluipschutter:
# 1: Hanna, Horace, Karin, Miryanna, Pepijn, Soundos; 2: Anna, Art, Jan, Patrick;
# 11 - Hoe beantwoordde de Mol de vraag tijdens de opdracht met het 'Levend Stilleven':
# 1: Anna, Horace, Patrick, Soundos; 2: Art, Hanna, Jan, Karin, Miryanna, Pepijn;
# Antwoorden: Art (11, 2) (3, 1 pas bekend vanaf aflevering 4), Horace (3 jokers),
# Patrick (11, 2 pas bekend vanaf aflevering 4) (3, 1 pas bekend vanaf aflevering 4),
# Jan (2, 2 pas bekend vanaf aflevering 4), Pepijn (1 joker), Soundos (3, 2 pas bekend vanaf aflevering 4)
players2 = [Player.ANNA_11, Player.ART_11, Player.HANNA_11, Player.HORACE_11, Player.JAN_11, Player.KARIN_11,
            Player.MIRYANNA_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11]
question2_2 = Question({1: [Player.ANNA_11, Player.HANNA_11, Player.HORACE_11, Player.KARIN_11, Player.MIRYANNA_11,
                            Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11],
                        2: [Player.ART_11, Player.JAN_11]})
question2_3 = Question({1: [Player.HANNA_11, Player.HORACE_11, Player.KARIN_11, Player.MIRYANNA_11, Player.PEPIJN_11,
                            Player.SOUNDOS_11],
                        2: [Player.ANNA_11, Player.ART_11, Player.JAN_11, Player.PATRICK_11]})
question2_11 = Question({1: [Player.ANNA_11, Player.HORACE_11, Player.PATRICK_11, Player.SOUNDOS_11],
                         2: [Player.ART_11, Player.HANNA_11, Player.JAN_11, Player.KARIN_11, Player.MIRYANNA_11,
                             Player.PEPIJN_11]})
result2 = Result(DropType.EXECUTION_DROP, [Player.HANNA_11])
episode2 = Episode(players2, result2,
                   {Player.ART_11: TestInput({11: 2, 3: DelayedAnswer(1, 4)}), Player.HORACE_11: TestInput(jokers = 3),
                    Player.PATRICK_11: TestInput({3: DelayedAnswer(1, 4), 11: DelayedAnswer(2, 4)}),
                    Player.JAN_11: TestInput({2: DelayedAnswer(2, 4)}), Player.PEPIJN_11: TestInput(jokers = 1),
                    Player.SOUNDOS_11: TestInput({3: DelayedAnswer(2, 4)})},
                   {2: question2_2, 3: question2_3, 11: question2_11})

# Aflevering 3 (afvaller: Horace)
# 1 - De Mol is een:
# 1: Anna, Karin, Miryanna, Soundos; 2: Art, Horace, Jan, Patrick, Pepijn;
# 2 (Vraagnummer onbekend) - Wat was de rol van de Mol bij de voorstellingsopdracht:
# 1: Art, Karin, Miryanna; 2: Anna, Horace, Patrick, Pepijn, Soundos; 3: Jan;
# 3 (Vraagnummer onbekend) - Was de Mol een plakker of een verver:
# 1: Art, Jan, Karin, Pepijn; 2: Anna, Horace, Miryanna, Patrick, Soundos;
# 4 (Vraagnummer onbekend) - Waar lag de sleutel van de Mol tijdens de hotelopdracht:
# 1: Karin, Miryanna; 2: Anna, Soundos; 3: Horace; 4: Art, Jan; 5: Patrick, Pepijn;
# 16 - Spreekt de Mol Spaans:
# 1: Art, Miryanna, Soundos; 2: Anna, Horace, Jan, Karin, Patrick, Pepijn;
# 20 (Vraagnummer onbekend) - Wie is de Mol:
# 1: Anna; 2: Art; 3: Horace; 4: Jan; 5: Karin; 6: Miryanna; 7: Patrick; 8: Pepijn; 9: Soundos;
# Antwoorden: Horace (1, 2), Jan (16, 1), Miryanna (20, 5 pas bekend vanaf aflevering 4),
# Karin (2, 3 pas bekend vanaf aflevering 4) (20, 3 pas bekend vanaf aflevering 4),
# Patrick (20, 5 pas bekend vanaf aflevering 4), Pepijn (2, 1 pas bekend vanaf aflevering 4) (3, 1 pas bekend vanaf
# aflevering 4), Soundos (16, 1 pas bekend vanaf aflevering 4) (4, 5 pas bekend vanaf aflevering 4)
players3 = [Player.ANNA_11, Player.ART_11, Player.HORACE_11, Player.JAN_11, Player.KARIN_11, Player.MIRYANNA_11,
            Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11]
question3_1 = Question({1: [Player.ANNA_11, Player.KARIN_11, Player.MIRYANNA_11, Player.SOUNDOS_11],
                        2: [Player.ART_11, Player.HORACE_11, Player.JAN_11, Player.PATRICK_11, Player.PEPIJN_11]})
question3_2 = Question({1: [Player.ART_11, Player.KARIN_11, Player.MIRYANNA_11],
                        2: [Player.ANNA_11, Player.HORACE_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11],
                        3: [Player.JAN_11]})
question3_3 = Question({1: [Player.ART_11, Player.JAN_11, Player.KARIN_11, Player.PEPIJN_11],
                        2: [Player.ANNA_11, Player.HORACE_11, Player.MIRYANNA_11, Player.PATRICK_11, Player.SOUNDOS_11]})
question3_4 = Question({1: [Player.KARIN_11, Player.MIRYANNA_11],
                        2: [Player.ANNA_11, Player.SOUNDOS_11],
                        3: [Player.HORACE_11],
                        4: [Player.ART_11, Player.JAN_11],
                        5: [Player.PATRICK_11, Player.PEPIJN_11]})
question3_16 = Question({1: [Player.ART_11, Player.MIRYANNA_11, Player.SOUNDOS_11],
                         2: [Player.ANNA_11, Player.HORACE_11, Player.JAN_11, Player.KARIN_11, Player.PATRICK_11,
                             Player.PEPIJN_11]})
question3_20 = Question({1: [Player.ANNA_11], 2: [Player.ART_11], 3: [Player.HORACE_11], 4: [Player.JAN_11],
                         5: [Player.KARIN_11], 6: [Player.MIRYANNA_11], 7: [Player.PATRICK_11], 8: [Player.PEPIJN_11],
                         9: [Player.SOUNDOS_11]})
result3 = Result(DropType.EXECUTION_DROP, [Player.HORACE_11])
episode3 = Episode(players3, result3,
                   {Player.HORACE_11: TestInput({1: 2}), Player.JAN_11: TestInput({16: 1}),
                    Player.MIRYANNA_11: TestInput({20: DelayedAnswer(5, 4)}),
                    Player.KARIN_11: TestInput({2: DelayedAnswer(3, 4), 20: DelayedAnswer(3, 4)}),
                    Player.PATRICK_11: TestInput({20: DelayedAnswer(5, 4)}),
                    Player.PEPIJN_11: TestInput({2: DelayedAnswer(1, 4), 3: DelayedAnswer(1, 4)}),
                    Player.SOUNDOS_11: TestInput({4: DelayedAnswer(5, 4), 16: DelayedAnswer(1, 4)})},
                   {1: question3_1, 2: question3_2, 3: question3_3, 4: question3_4, 16: question3_16, 20: question3_20})

# Aflevering 4 (afvaller: Miryanna)
# 6 - De Mol zat op de racebaan in:
# 1: Anna, Jan, Karin, Patrick; 2: Art, Miryanna, Pepijn, Soundos;
# 17 - Hoeveel meter legde de Mol af tussen de rotsen van El Diablo:
# 1: Anna, Art, Jan, Karin, Pepijn; 2: Patrick; 3: Miryanna, Soundos;
# Antwoorden: Miryanna (6, 2), Soundos (17, 2), Patrick (2 jokers), Art (2 jokers)
players4 = [Player.ANNA_11, Player.ART_11, Player.JAN_11, Player.KARIN_11, Player.MIRYANNA_11, Player.PATRICK_11,
            Player.PEPIJN_11, Player.SOUNDOS_11]
question4_6 = Question({1: [Player.ANNA_11, Player.JAN_11, Player.KARIN_11, Player.PATRICK_11],
                        2: [Player.ART_11, Player.MIRYANNA_11, Player.PEPIJN_11, Player.SOUNDOS_11]})
question4_17 = Question({1: [Player.ANNA_11, Player.ART_11, Player.JAN_11, Player.KARIN_11, Player.PEPIJN_11],
                         2: [Player.PATRICK_11],
                         3: [Player.MIRYANNA_11, Player.SOUNDOS_11]})
result4 = Result(DropType.EXECUTION_DROP, [Player.MIRYANNA_11])
episode4 = Episode(players4, result4,
                   {Player.MIRYANNA_11: TestInput({6: 2}), Player.SOUNDOS_11: TestInput({17: 2}),
                    Player.PATRICK_11: TestInput(jokers = 2), Player.ART_11: TestInput(jokers = 2)},
                   {6: question4_6, 17: question4_17})

# Aflevering 5 (afvaller: Jan)
# 8 - Waar stond de Mol tijdens de voordracht van het gedicht?
# 1: Anna, Art, Pepijn; 2: Jan, Karin, Patrick, Soundos;
# 11 - De Mol is:
# 1: Anna, Jan, Patrick, Soundos; 2: Art, Karin, Pepijn;
# Antwoorden: Anna (Vrijstelling), Karin (8, 2), Art (11, 2)
players5 = [Player.ANNA_11, Player.ART_11, Player.JAN_11, Player.KARIN_11, Player.PATRICK_11, Player.PEPIJN_11,
            Player.SOUNDOS_11]
question5_8 = Question({1: [Player.ANNA_11, Player.ART_11, Player.PEPIJN_11],
                        2: [Player.JAN_11, Player.KARIN_11, Player.PATRICK_11, Player.SOUNDOS_11]})
question5_11 = Question({1: [Player.ANNA_11, Player.JAN_11, Player.PATRICK_11, Player.SOUNDOS_11],
                         2: [Player.ART_11, Player.KARIN_11, Player.PEPIJN_11]})
result5 = Result(DropType.EXECUTION_DROP, [Player.JAN_11])
episode5 = Episode(players5, result5,
                   {Player.ANNA_11: TestInput(immunity = True), Player.KARIN_11: TestInput({8: 2}),
                    Player.ART_11: TestInput({11: 2})},
                   {8: question5_8, 11: question5_11})

# Aflevering 6 (geen afvaller, alleen Karin, Pepijn en Soundos kregen hun scherm te zien)
# 13 - Tijdens de Woordspooropdracht was de Mol een:
# 1: Anna, Patrick, Karin; 2: Art, Pepijn, Soundos;
# 17 - Heeft de Mol ooit een joker in bezit gehad:
# 1: Art, Patrick, Pepijn; 2: Anna, Karin, Soundos;
# Antwoorden: Soundos (17, 1), Art (13, 1)
players6 = [Player.ANNA_11, Player.ART_11, Player.KARIN_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11]
question6_13 = Question({1: [Player.ANNA_11, Player.KARIN_11, Player.PATRICK_11],
                         2: [Player.ART_11, Player.PEPIJN_11, Player.SOUNDOS_11]})
question6_17 = Question({1: [Player.ART_11, Player.PATRICK_11, Player.PEPIJN_11],
                         2: [Player.ANNA_11, Player.KARIN_11, Player.SOUNDOS_11]})
result6 = Result(DropType.POSSIBLE_DROP, [Player.ANNA_11, Player.ART_11, Player.PATRICK_11])
episode6 = Episode(players6, result6,
                   {Player.ART_11: TestInput({13: 1}), Player.SOUNDOS_11: TestInput({17: 1})},
                   {13: question6_13, 17: question6_17})

# Aflevering 7 (afvaller: Pepijn)
# Vragen:
# 11 - Droeg de Mol een kist op de Cerro Negro:
# 1: Anna, Art, Patrick, Pepijn; 2: Karin, Soundos;
# 20 - Wie is de Mol:
# 1: Anna; 2: Pepijn; 3: Soundos; 4: Art; 5: Karin; 6: Patrick;
# Antwoorden: Karin (2 jokers), Soundos (11, 1) (3 jokers), Anna (1 joker), Art (20, 1) (2 jokers)
players7 = [Player.ANNA_11, Player.ART_11, Player.KARIN_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11]
question7_11 = Question({1: [Player.ANNA_11, Player.ART_11, Player.PATRICK_11, Player.PEPIJN_11],
                         2: [Player.KARIN_11, Player.SOUNDOS_11]})
question7_20 = Question({1: [Player.ANNA_11], 2: [Player.PEPIJN_11], 3: [Player.SOUNDOS_11], 4: [Player.ART_11],
                         5: [Player.KARIN_11], 6: [Player.PATRICK_11]})
result7 = Result(DropType.EXECUTION_DROP, [Player.PEPIJN_11])
episode7 = Episode(players7, result7,
                   {Player.ANNA_11: TestInput(jokers = 1), Player.ART_11: TestInput({20: 1}, jokers = 2),
                    Player.KARIN_11: TestInput(jokers = 2), Player.SOUNDOS_11: TestInput({11: 1}, jokers = 3)},
                   {11: question7_11, 20: question7_20})

# Aflevering 8 (afvaller: Anna)
# Vragen:
# 19 - Hoeveel jokers heeft de Mol nog in bezit:
# 1: Soundos; 2: Anna, Karin; 3: Art; 4: Patrick;
# Antwoorden: Art (19, 2) (1 joker)
# Patrick contact gehad met de Mol, en Karin heeft ook ingezet voor contact
players8 = [Player.ANNA_11, Player.ART_11, Player.KARIN_11, Player.PATRICK_11, Player.SOUNDOS_11]
question8_19 = Question({1: [Player.SOUNDOS_11],
                         2: [Player.ANNA_11, Player.KARIN_11],
                         3: [Player.ART_11],
                         4: [Player.PATRICK_11]})
result8 = Result(DropType.EXECUTION_DROP, [Player.ANNA_11])
episode8 = Episode(players8, result8,
                   {Player.ART_11: TestInput({19: 2}, jokers = 1)},
                   {19: question8_19})

# Aflevering 9 (afvaller: Karin) (leugens in testvragen door editing)
# Vragen:
# 1 - Wie is de Mol:
# 1: Art; 2: Karin; 3: Patrick; 4: Soundos;
# 8 - Heeft de Mol aangegeven contact te willen met de Mol:
# 1: Karin, Patrick; 2: Art, Soundos;
# 20 - Heeft de Mol een gesprek gehad in de kerk:
# 1: Art, Karin; 2: Patrick, Soundos;
# 21 - Waar zat de Mol tijdens de Bomenopdracht:
# 1: Karin, Soundos; 2: Art, Patrick;
# 22 - Heeft de Mol geld gepakt bij de Bomenopdracht:
# 1: Art; 2: Karin, Patrick, Soundos;
# 23 - Heeft de Mol geld aangepakt van Pieter Jan:
# 1: Soundos; 2: Art, Karin, Patrick;
# Antwoorden: Soundos (8, 1) (21, 2) (23, 2), Karin (1, 3) (22, 2), Art (20, 2) (22, 2) (1 joker) (23 vragen test)
players9 = [Player.ART_11, Player.KARIN_11, Player.PATRICK_11, Player.SOUNDOS_11]
question9_1 = Question({1: [Player.ART_11], 2: [Player.KARIN_11], 3: [Player.PATRICK_11], 4: [Player.SOUNDOS_11]})
question9_8 = Question({1: [Player.KARIN_11, Player.PATRICK_11],
                        2: [Player.ART_11, Player.SOUNDOS_11]})
question9_20 = Question({1: [Player.ART_11, Player.KARIN_11],
                         2: [Player.PATRICK_11, Player.SOUNDOS_11]})
question9_21 = Question({1: [Player.KARIN_11, Player.SOUNDOS_11],
                         2: [Player.ART_11, Player.PATRICK_11]})
question9_22 = Question({1: [Player.ART_11],
                         2: [Player.KARIN_11, Player.PATRICK_11, Player.SOUNDOS_11]})
question9_23 = Question({1: [Player.SOUNDOS_11],
                         2: [Player.ART_11, Player.KARIN_11, Player.PATRICK_11]})
result9 = Result(DropType.EXECUTION_DROP, [Player.KARIN_11])
episode9 = Episode(players9, result9,
                   {Player.SOUNDOS_11: TestInput({8: 1, 21: 2, 23: 2}), Player.KARIN_11: TestInput({1: 3, 22: 2}),
                    Player.ART_11: TestInput({20: 2, 22: 2}, jokers = 1)},
                   {1: question9_1, 8: question9_8, 20: question9_20, 21: question9_21, 22: question9_22,
                    23: question9_23}, num_questions = 23)

# Aflevering 10 (afvaller: Soundos)
# Vragen:
# 1 (Vraagnummer onbekend) - Wat had de Mol gepakt bij de vrijstellingsroute:
# 1: Soundos (Niks); 2: Patrick (4 jokers); 3: Art (5 jokers);
# 3 (Vraagnummer onbekend) - Hoe is de Mol doodgegaan tijdens de boobytrap opdracht:
# 1: Patrick (Boobytrap); 2: Art (Landmijn); 3: Soundos (Sniper);
# 4 (Vraagnummer onbekend) - Heeft de Mol een blauw kokertje in de mand gegooid:
# 1: Patrick, Soundos (Ja); 2: Art (Nee);
# 5 (Vraagnummer onbekend) - Van welk woord maakte de Mol een foto:
# 1: Art (Harmonie); 2: Patrick (Nicaraguaanse); 3: Soundos (Vogels);
# 6 (Vraagnummer onbekend) - Welke naam had de Mol op zijn shirt tijdens de ziekenhuisopdracht:
# 1: Art (Jan); 2: Patrick (Miryanna); 3: Soundos (Pepijn);
# 7 (Vraagnummer onbekend) - Hoeveel meter heeft de Mol afgelegd bij de duivelspoort:
# 1: Soundos; 2: Patrick; 3: Art;
# 8 (Vraagnummer onbekend) - Hoe snel was de Mol beneden bij de bergopdracht:
# 1: Art; 2: Patrick; 3: Soundos;
# 21 - Wat was het kamernummer van de Mol bij de eerste overnachting in El Salvador:
# 1: Art; 2: Patrick; 3: Soundos;
# 22 - De Mol was tijdens de Vuurwerkopdracht:
# 1: Art, Soundos; 2: Patrick;
# 27 - Hoe beantwoordde de Mol de vraag tijdens de opdracht 'Levend Stilleven'?
# 1: Patrick, Soundos; 2: Art;
# 31 - De Mol was tijdens de Billboard/Muralesopdracht:
# 1: Art; 2: Patrick, Soundos;
# 40 - Wie is de Mol:
# 1: Art; 2: Patrick; 3: Soundos;
# Antwoorden: Patrick (1, 3) (3, 2) (5, 1) (6, 1) (22, 1) (31, 1) (40, 1), Soundos (4, 1) (27, 1) (40, 2),
# Art (7, 2) (8, 2) (21, 1) (40, 2)
players10 = [Player.ART_11, Player.PATRICK_11, Player.SOUNDOS_11]
question10_1 = Question({1: [Player.SOUNDOS_11], 2: [Player.PATRICK_11], 3: [Player.ART_11]})
question10_3 = Question({1: [Player.PATRICK_11], 2: [Player.ART_11], 3: [Player.SOUNDOS_11]})
question10_4 = Question({1: [Player.PATRICK_11, Player.SOUNDOS_11],
                         2: [Player.ART_11]})
question10_5 = Question({1: [Player.ART_11], 2: [Player.PATRICK_11], 3: [Player.SOUNDOS_11]})
question10_6 = Question({1: [Player.ART_11], 2: [Player.PATRICK_11], 3: [Player.SOUNDOS_11]})
question10_7 = Question({1: [Player.SOUNDOS_11], 2: [Player.PATRICK_11], 3: [Player.ART_11]})
question10_8 = Question({1: [Player.ART_11], 2: [Player.PATRICK_11], 3: [Player.SOUNDOS_11]})
question10_21 = Question({1: [Player.ART_11], 2: [Player.PATRICK_11], 3: [Player.SOUNDOS_11]})
question10_22 = Question({1: [Player.ART_11, Player.SOUNDOS_11],
                          2: [Player.PATRICK_11]})
question10_27 = Question({1: [Player.PATRICK_11, Player.SOUNDOS_11],
                          2: [Player.ART_11]})
question10_31 = Question({1: [Player.ART_11], 2: [Player.PATRICK_11], 3: [Player.SOUNDOS_11]})
question10_40 = Question({1: [Player.ART_11], 2: [Player.PATRICK_11], 3: [Player.SOUNDOS_11]})
result10 = Result(DropType.EXECUTION_DROP, [Player.SOUNDOS_11])
episode10 = Episode(players10, result10,
                   {Player.PATRICK_11: TestInput({1: 3, 3: 2, 5: 1, 6: 1, 22: 1, 31: 1, 40: 1}),
                    Player.SOUNDOS_11: TestInput({4: 1, 27: 1, 40: 2}),
                    Player.ART_11: TestInput({7: 2, 8: 2, 21: 1, 40: 2})},
                   {1: question10_1, 3: question10_3, 4: question10_4, 5: question10_5, 6: question10_6,
                    7: question10_7, 8: question10_8, 21: question10_21, 22: question10_22, 27: question10_27,
                    31: question10_31, 40: question10_40}, num_questions = 40)

season11 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                             8: episode8, 9.5: episode9, 10: episode10})