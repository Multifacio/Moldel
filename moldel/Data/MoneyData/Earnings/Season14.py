from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €2000):
# €400 (Major: Jennifer, Susan) (Minor: Aaf, Daphne, Freek, Jan-Willem, Maurice, Owen, Sophie, Tygo)
# Opdracht 2 (Maximaal €2000): Niks verdiend
alive1 = {Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.MAURICE_14,
          Player.OWEN_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 2000, earned = [
                            Earning(money = 400, major = {Player.JENNIFER_14, Player.SUSAN_14}, minor = {Player.AAF_14,
                                Player.DAPHNE_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.MAURICE_14,
                                Player.OWEN_14, Player.SOFIE_14, Player.TYGO_14}),
                        ])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 2000, earned = [])

# Aflevering 2
# Opdracht 1 (Maximaal €2000): Niks verdiend
# Opdracht 2 (Maximaal €?):
# €500 (Major: Jennifer) (Minor: Sophie), €500 (Major: Freek) (Minor: Owen, Susan, Tygo), €500 (Major: Owen, Tygo),
# €500 (Major: Freek) (Minor: Owen)
# Opdracht 3 (Maximaal €?): Niks verdiend
alive2 = {Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.OWEN_14,
          Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = None, earned = [
                            Earning(money = 500, major = {Player.JENNIFER_14}, minor = {Player.SOFIE_14}),
                            Earning(money = 500, major = {Player.FREEK_14}, minor = {Player.OWEN_14, Player.SUSAN_14,
                                Player.TYGO_14}),
                            Earning(money = 500, major = {Player.OWEN_14, Player.TYGO_14}),
                            Earning(money = 500, major = {Player.FREEK_14}, minor = {Player.OWEN_14}),
                        ])

# Aflevering 3
# Opdracht 1 (Maximaal €2000): Niks verdiend
# Opdracht 2 (Maximaal €3400):
# €1000 (Major: Daphne, Freek, Jan-Willem, Jennifer, Sofie, Susan, Tygo) (Minor: Aaf)
alive3 = {Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.SOFIE_14,
          Player.SUSAN_14, Player.TYGO_14}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 3400, earned = [])

# Aflevering 4
# Opdracht 1 (Maximaal €1750):
# €350 (Major: Aaf) (Minor: Daphne, Freek, Jan-Willem, Jennifer, Sofie, Susan, Tygo)
# Opdracht 2 (Maximaal €1500): Niks verdiend
# Opdracht 3 (Maximaal €?):
# Tygo <- Sophie, Freek <- Aaf, Jan-Willem <- Susan, Daphne <- Jennifer
# Freek (3 kokers waarvan 1 positieve), Jan-Willem (1 koker), Daphne (4 kokers), Tygo (1 koker)
# (Inschatting in totaal 6 positieve kokers, 3 negatieve kokers)
# €250 (In de positieve kokers) -€100 (In de negatieve kokers)
alive4 = {Player.AAF_14, Player.DAPHNE_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.SOFIE_14,
          Player.SUSAN_14, Player.TYGO_14}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 1750, earned = [
                            Earning(money = 350, major = {Player.AAF_14}, minor = {Player.DAPHNE_14, Player.FREEK_14,
                                Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.SOFIE_14, Player.SUSAN_14,
                                Player.TYGO_14}),
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = 1500, earned = [])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = None, earned = [
                            Earning(money = 250, major = {Player.FREEK_14}, minor = {Player.AAF_14}),
                            Earning(money = 950 * 2/8, minor = {Player.FREEK_14, Player.AAF_14}),
                            Earning(money = 950 * 1/8, minor = {Player.JAN_WILLEM_14, Player.SUSAN_14}),
                            Earning(money = 950 * 4/8, minor = {Player.DAPHNE_14, Player.JENNIFER_14}),
                            Earning(money = 950 * 1/8, minor = {Player.SOFIE_14, Player.TYGO_14}),
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €2500): Niks verdiend
# Opdracht 2 (Maximaal €2500):
# €2500 (Major: Aaf) (Minor: Jan-Willem, Tygo)
# Opdracht 3 (Maximaal €2500): Niks verdiend
alive5 = {Player.AAF_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.JENNIFER_14, Player.SOFIE_14, Player.SUSAN_14,
          Player.TYGO_14}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 2500, earned = [])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = 2500, earned = [
                            Earning(money = 2500, major = {Player.AAF_14}, minor = {Player.JAN_WILLEM_14, Player.TYGO_14}),
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 2500, earned = [])

# Aflevering 6
# Opdracht 1 (Maximaal €2500):
# €1250 (Major: Freek, Sophie) (Minor: Tygo)
# Opdracht 2 (Maximaal €2500):
# €2500 (Major: Tygo) (Minor: Aaf, Freek, Jan-Willem, Sofie, Susan)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive6 = {Player.AAF_14, Player.FREEK_14, Player.JAN_WILLEM_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 2500, earned = [
                            Earning(money = 1250, major = {Player.FREEK_14, Player.SOFIE_14}, minor = {Player.TYGO_14}),
                        ])
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 2500, earned = [
                            Earning(money = 2500, major = {Player.TYGO_14}, minor = {Player.AAF_14, Player.FREEK_14,
                                Player.JAN_WILLEM_14, Player.SOFIE_14, Player.SUSAN_14}),
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €2000):
# €2000 (Major: Jan-Willem) (Minor: Freek, Susan)
# Opdracht 2 (Maximaal €2000): Niks verdiend
# Opdracht 3 (Maximaal €3000):
# €250 (Major: Jan-Willem)
alive7 = {Player.FREEK_14, Player.JAN_WILLEM_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 2000, earned = [
                            Earning(money = 2000, major = {Player.JAN_WILLEM_14}, minor = {Player.FREEK_14,
                                Player.SUSAN_14}),
                        ])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 2000, earned = [])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 3000, earned = [
                            Earning(money = 250, major = {Player.JAN_WILLEM_14})
                        ])

# Aflevering 8
# Opdracht 1 (Maximaal €3000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €0): Niks verdiend
# Opdracht 3 (Maximaal €2500): Niks verdiend
alive8 = {Player.FREEK_14, Player.JAN_WILLEM_14, Player.SOFIE_14, Player.SUSAN_14, Player.TYGO_14}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 3000, earned = [])
exercise8_3 = Exercise(episode = 8, alive = alive8, maximum = 2500, earned = [])

# Aflevering 9
# Opdracht 1 (Maximaal €0): Niks verdiend (Omdat dit geld al eerder verdiend was)
# Opdracht 2 (Maximaal €?): Onduidelijk wie wat verdiend heeft

season14 = Season([exercise1_1, exercise1_2, exercise2_1, exercise2_2, exercise3_1, exercise3_2, exercise4_1,
                   exercise4_2, exercise4_3, exercise5_1, exercise5_2, exercise5_3, exercise6_1, exercise6_2,
                   exercise7_1, exercise7_2, exercise7_3, exercise8_1, exercise8_3])