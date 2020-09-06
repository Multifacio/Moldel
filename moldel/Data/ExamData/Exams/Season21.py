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
                   {Player.JEROEN_21: TestInput({3: 1}), Player.RON_21: TestInput(jokers = 1),
                    Player.NIKKIE_21: TestInput({7: 2}), Player.TYGO_21: TestInput({20: 1}),
                    Player.TINA_21: TestInput({18: 3}), Player.PEGGY_21: TestInput({13: 1}),
                    Player.ELLIE_21: TestInput({20: 6})},
                   {3: question1_3, 7: question1_7, 13: question1_13, 18: question1_18, 20: question1_20})

season21 = Season(players1, {1: episode1})