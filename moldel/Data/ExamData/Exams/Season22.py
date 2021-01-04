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

season22 = Season(players1, {1: episode1})