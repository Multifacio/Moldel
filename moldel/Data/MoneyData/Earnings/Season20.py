from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €0): Niks verdiend
# Opdracht 2 (Maximaal €2500): Niet duidelijk wie wat verdiend heeft
# Opdracht 3 (Maximaal €2100):
# €18 (Major: Buddy) (Minor: Anita, Jaike, Johan, Miljuschka, Nathan),
# €2 (Major: Johan) (Minor: Jaike, Miljuschka, Nathan)
alive1 = {Player.ANITA_20, Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.JOHAN_20, Player.LEONIE_20,
          Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20, Player.TINA_20}
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 2500, earned = [])
exercise1_3 = Exercise(episode = 1, alive = alive1, maximum = 2100, earned = [
                            Earning(money = 18, major = {Player.BUDDY_20}, minor = {Player.ANITA_20, Player.JAIKE_20,
                                Player.JOHAN_20, Player.MILJUSCHKA_20, Player.NATHAN_20}),
                            Earning(money = 2, major = {Player.JOHAN_20}, minor = {Player.JAIKE_20,
                                Player.MILJUSCHKA_20, Player.NATHAN_20})
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €2500):
# €500 (Major: Claes, Rob), €500 (Major: Johan, Tina), €500 (Major: Buddy, Jaike)
# Opdracht 2 (Maximaal €1750):
# -€100 (Major: Tina)
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive2 = {Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.JOHAN_20, Player.LEONIE_20, Player.MILJUSCHKA_20,
          Player.NATHAN_20, Player.ROB_20, Player.TINA_20}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 2500, earned = [
                            Earning(money = 500, major = {Player.CLAES_20, Player.ROB_20}),
                            Earning(money = 500, major = {Player.JOHAN_20, Player.TINA_20}),
                            Earning(money = 500, major = {Player.BUDDY_20, Player.JAIKE_20}),
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 1750, earned = [
                            Earning(money = -100, major = {Player.TINA_20})
                        ])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [])

# Aflevering 3
# Opdracht 1 (Maximaal €2250): Niks verdiend
# Opdracht 2 (Maximaal €2000):
# €150 (Major: Buddy, Johan, Rob) (Minor: Claes, Miljuschka),
# €450 (Major: Jaike, Leonie, Nathan) (Minor: Claes, Miljuschka)
# Opdracht 3 (Maximaal €2700):
# €1500 (Major: Johan) (Minor: Buddy, Claes, Jaike, Leonie, Miljuschka, Nathan, Rob)
alive3 = {Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.JOHAN_20, Player.LEONIE_20, Player.MILJUSCHKA_20,
          Player.NATHAN_20, Player.ROB_20}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 2250, earned = [])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [
                            Earning(money = 150, major = {Player.BUDDY_20, Player.JOHAN_20, Player.ROB_20},
                                    minor = {Player.CLAES_20, Player.MILJUSCHKA_20}),
                            Earning(money = 450, major = {Player.JAIKE_20, Player.LEONIE_20, Player.NATHAN_20},
                                    minor = {Player.CLAES_20, Player.MILJUSCHKA_20})
                        ])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 2700, earned = [
                            Earning(money = 1500, major = {Player.JOHAN_20},
                                    minor = {Player.BUDDY_20, Player.CLAES_20, Player.JAIKE_20, Player.LEONIE_20,
                                             Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20})
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €2850):
# €5 (Minor: Iedereen), €600 (Major: Buddy), €350 (Major: Claes), €200 (Major: Johan), €250 (Major: Leonie),
# €450 (Major: Miljuschka), €250 (Major: Nathan), €225 (Major: Rob)
# Opdracht 2: Niet duidelijk wie wat verdiend heeft
# Opdracht 3 (Maximaal €3500):
# €500 (Major: Claes), €500 (Major: Leonie)
alive4 = {Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20,
          Player.ROB_20}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 2850, earned = [
                            Earning(money = 600, major = {Player.BUDDY_20}),
                            Earning(money = 350, major = {Player.CLAES_20}),
                            Earning(money = 200, major = {Player.JOHAN_20}),
                            Earning(money = 250, major = {Player.LEONIE_20}),
                            Earning(money = 450, major = {Player.MILJUSCHKA_20}),
                            Earning(money = 250, major = {Player.NATHAN_20}),
                            Earning(money = 225, major = {Player.ROB_20}),
                            Earning(money = 5, minor = {Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20,
                                Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20})
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = 2560, earned = [])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 3500, earned = [
                            Earning(money = 500, major = {Player.CLAES_20}),
                            Earning(money = 500, major = {Player.LEONIE_20})
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €1500):
# €250 (Minor: Buddy, Claes, Leonie, Miljuschka, Rob)
# Opdracht 2 (Maximaal €1500):
# €600 (Major: Buddy) (Minor: Claes, Leonie, Rob)
# Opdracht 3 (Maximaal €1750):
# €250 (Major: Nathan)
alive5 = {Player.BUDDY_20, Player.CLAES_20, Player.JOHAN_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20,
          Player.ROB_20}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 1500, earned = [
                            Earning(money = 250, minor = {Player.BUDDY_20, Player.CLAES_20, Player.LEONIE_20,
                                    Player.MILJUSCHKA_20, Player.ROB_20})
                        ])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = 1500, earned = [
                            Earning(money = 600, major = {Player.BUDDY_20}, minor = {Player.CLAES_20, Player.LEONIE_20,
                                    Player.ROB_20})
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 1750, earned = [
                            Earning(money = 250, major = {Player.NATHAN_20})
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €1500): Niks verdiend
# Opdracht 2 (Maximaal €2500): Niet duidelijk wie wat verdiend heeft
# Opdracht 3 (Maximaal €1500):
# -€200 (Major: Nathan, Minor: Buddy, Claes, Leonie, Miljuschka, Rob)
alive6 = {Player.BUDDY_20, Player.CLAES_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 1500, earned = [])
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 2500, earned = [])
exercise6_3 = Exercise(episode = 6, alive = alive6, maximum = 1500, earned = [
                            Earning(money = -200, major = {Player.NATHAN_20}, minor = {Player.BUDDY_20, Player.CLAES_20,
                                    Player.LEONIE_20, Player.MILJUSCHKA_20, Player.ROB_20})
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €1500): Niks verdiend
# Opdracht 2 (Maximaal €1600): Niet duidelijk wie wat verdiend heeft
# Opdracht 3 (Maximaal €1500): Niet duidelijk wie wat verdiend heeft
alive7 = {Player.BUDDY_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 1600, earned = [])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [])

# Aflevering 8
# Opdracht 1 (Maximaal €1650):
# €250 (Major: Nathan) (Minor: Miljuschka, Rob)
# Opdracht 2 (Maximaal €0): Niks verdiend
# Opdracht 3 (Maximaal €2000):
# €80 (Major: Buddy)
alive8 = {Player.BUDDY_20, Player.LEONIE_20, Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 1650, earned = [
                            Earning(money = 250, major = {Player.NATHAN_20}, minor = {Player.MILJUSCHKA_20, Player.ROB_20})
                        ])
exercise8_3 = Exercise(episode = 8, alive = alive8, maximum = 2000, earned = [
                            Earning(money = 80, major = {Player.BUDDY_20})
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €1750): Niks verdiend
# Opdracht 2 (Maximaal €?): Niet duidelijk wie wat verdiend heeft
# Opdracht 3 (Maximaal €4500): Niet duidelijk wie wat verdiend heeft
alive9 = {Player.BUDDY_20, Player.MILJUSCHKA_20, Player.NATHAN_20, Player.ROB_20}
exercise9_1 = Exercise(episode = 9, alive = alive6, maximum = 1750, earned = [])
exercise9_3 = Exercise(episode = 9, alive = alive6, maximum = 4500, earned = [])

season20 = Season([exercise1_2, exercise1_3, exercise2_1, exercise2_2, exercise2_3, exercise3_2, exercise3_3,
                   exercise4_1, exercise4_2, exercise4_3, exercise5_1, exercise5_2, exercise5_3, exercise6_1,
                   exercise6_2, exercise6_3, exercise7_1, exercise7_2, exercise7_3, exercise8_1, exercise8_3,
                   exercise9_1, exercise9_3])

