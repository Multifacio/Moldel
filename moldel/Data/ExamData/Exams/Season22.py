from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput

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
# Antwoorden: Splinter (1, 2), Rocky (16, 3), Charlotte (12, 1), Joshua (10, 2), Renee (8, 2), Marije (6, 3)
players2 = [Player.CHARLOTTE_22, Player.ERIK_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.LAKSHMI_22,
            Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22]
question2_1 = Question({1: [Player.ERIK_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.SPLINTER_22],
                        2: [Player.CHARLOTTE_22, Player.LAKSHMI_22, Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22]})
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
result2 = Result(DropType.EXECUTION_DROP, [Player.ERIK_22])
episode2 = Episode(players2, result2,
                   {Player.SPLINTER_22: TestInput({1: 2}), Player.ROCKY_22: TestInput({16: 3}),
                    Player.CHARLOTTE_22: TestInput({12: 1}), Player.JOSHUA_22: TestInput({10: 2}),
                    Player.RENEE_22: TestInput({8: 2}), Player.MARIJE_22: TestInput({6: 3})},
                   {1: question2_1, 6: question2_6, 8: question2_8, 10: question2_10, 12: question2_12, 16: question2_16})

season22 = Season(players1, {1: episode1, 2: episode2})