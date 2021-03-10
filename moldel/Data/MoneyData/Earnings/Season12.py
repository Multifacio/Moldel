from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €2500): Niks verdiend
# Opdracht 2 (Maximaal €?):
# Liesbeth (0 kokers), Marion (0 kokers), Marit (3 kokers), Tim (1 koker), William (1 koker)
# Minor: Anne-Marie, Dio, Frits, Hadewych, Maarten
# -€500 verdiend
# Opdracht 3 (Maximaal €3000): Niks verdiend
alive1 = {Player.ANNE_MARIE_12, Player.DIO_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12,
          Player.MAARTEN_12, Player.MARIT_12, Player.MARION_12, Player.TIM_12, Player.WILLIAM_12}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 2500, earned = [])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = None, earned = [
                            Earning(money = -300, major = {Player.MARIT_12}, minor = {Player.ANNE_MARIE_12,
                                Player.DIO_12, Player.FRITS_12, Player.HADEWYCH_12, Player.MAARTEN_12}),
                            Earning(money = -100, major = {Player.TIM_12}, minor = {Player.ANNE_MARIE_12,
                                Player.DIO_12, Player.FRITS_12, Player.HADEWYCH_12, Player.MAARTEN_12}),
                            Earning(money = -100, major = {Player.WILLIAM_12}, minor = {Player.ANNE_MARIE_12,
                                Player.DIO_12, Player.FRITS_12, Player.HADEWYCH_12, Player.MAARTEN_12}),
                        ])
exercise1_3 = Exercise(episode = 1, alive = alive1, maximum = 3000, earned = [])

# Aflevering 2
# Opdracht 1 (Maximaal €2000): Niks verdiend
# Opdracht 2 (Maximaal €2500): Niks verdiend
# Opdracht 3 (Maximaal €3000): Gezamelijk verdiend
alive2 = {Player.ANNE_MARIE_12, Player.DIO_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12,
          Player.MAARTEN_12, Player.MARIT_12, Player.TIM_12, Player.WILLIAM_12}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 2500, earned = [])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 3000, earned = [])

# Aflevering 3
# Opdracht 1 (Maximaal €?):
# 1e ronde:
# Frits: Sporters met M (€50 per stuk), Liesbeth: Europose Steden met M (€50 per stuk),
# William: Acteurs met C (€100 per stuk)
# €300 (Major: Anne-Marie, Maarten, Tim) (Minor: Frits, Liesbeth, Hadewych, Marit)
#
# 2e ronde:
# Tim: Popgroepen met een B (€50 per stuk), Anne-Marie: Dieren met een B (€50 per stuk),
# Maarten: Schrijvers met een Q (€200 per stuk)
# €200 (Major: Frits, Liesbeth, William) (Minor: Hadewych, Maarten, Marit)
# €300 (Major: Frits, Liesbeth, William) (Minor: Anne-Marie, Hadewych, Marit, Tim)
#
# Opdracht 2 (Maximaal €?):
# €1000 (Major: William), €1000 (Major: Tim), €1000 (Major: Marit)
# Opdracht 3 (Maximaal €2000):
# €2000 (Major: Maarten) (Minor: Anne-Marie, Frits, Hadewych, Liesbeth, Marit, Tim, William)
alive3 = {Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MAARTEN_12,
          Player.MARIT_12, Player.TIM_12, Player.WILLIAM_12}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = None, earned = [
                            Earning(money = 300, major = {Player.ANNE_MARIE_12, Player.MAARTEN_12, Player.TIM_12},
                                    minor = {Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12}),
                            Earning(money = 200, major = {Player.FRITS_12, Player.LIESBETH_12, Player.WILLIAM_12},
                                    minor = {Player.HADEWYCH_12, Player.MAARTEN_12, Player.MARIT_12}),
                            Earning(money = 300, major = {Player.FRITS_12, Player.LIESBETH_12, Player.WILLIAM_12},
                                    minor = {Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.MARIT_12, Player.TIM_12}),
                        ])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = None, earned = [
                            Earning(money = 1000, major = {Player.WILLIAM_12}),
                            Earning(money = 1000, major = {Player.TIM_12}),
                            Earning(money = 1000, major = {Player.MARIT_12})
                        ])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [
                            Earning(money = 2000, major = {Player.MAARTEN_12}, minor = {Player.ANNE_MARIE_12,
                                Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12, Player.TIM_12,
                                Player.WILLIAM_12})
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €2500):
# €2500 (Major: William) (Minor: Anne-Marie, Frits, Hadewych, Liesbeth, Marit, Tim)
# Opdracht 2 (Maximaal €2000): Niks verdiend
# Opdracht 3 (Maximaal €3000):
# -€10800 (Minor: Anne-Marie, Frits, Hadewych, Liesbeth, Tim)
alive4 = {Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12, Player.TIM_12,
          Player.WILLIAM_12}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 2500, earned = [
                            Earning(money = 2500, major = {Player.WILLIAM_12}, minor = {Player.ANNE_MARIE_12,
                                Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12, Player.TIM_12})
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = 2000, earned = [])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 3000, earned = [
                            Earning(money = -10800, minor = {Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12,
                                Player.LIESBETH_12, Player.TIM_12})
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €3200):
# Hadewych: €0 -> Tim: €50 -> William: €100 -> Frits: €50 -> Liesbeth: €100 -> Marit: €50 -> Anne-Marie: €100
# €50 / 4 (Major: Tim), €50 / 4 (Major: William), €50 / 2 (Major: Liesbeth), €50 (Major: Anne-Marie)
# Opdracht 2 (Maximaal €4500):
# €1500 (Major: Frits)
# Opdracht 3 (Maximaal €2000):
# €2000 (Major: Tim) (Minor: Anne-Marie, Frits, Hadewych, Liesbeth, Marit, William)
alive5 = {Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12, Player.TIM_12,
          Player.WILLIAM_12}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 3200, earned = [
                            Earning(money = 50 / 4, major = {Player.TIM_12}),
                            Earning(money = 50 / 4, major = {Player.WILLIAM_12}),
                            Earning(money = 50 / 2, major = {Player.LIESBETH_12}),
                            Earning(money = 50, major = {Player.ANNE_MARIE_12})
                        ])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = 4500, earned = [
                            Earning(money = 1500, major = {Player.FRITS_12})
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 2000, earned = [
                            Earning(money = 2000, major = {Player.TIM_12}, minor = {Player.ANNE_MARIE_12,
                                Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.MARIT_12,
                                Player.WILLIAM_12})
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €2500):
# €2500 (Major: Anne-Marie) (Minor: Frits, Liesbeth)
# Opdracht 2 (Maximaal €2500): Niks verdiend
# Opdracht 3 (Maximaal €2000):
# €1000 (Major: William) (Minor: Anne-Marie, Frits, Tim), €1000 (Major: Tim) (Minor: Anne-Marie, Hadewych, William)
alive6 = {Player.ANNE_MARIE_12, Player.FRITS_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.TIM_12,
          Player.WILLIAM_12}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 2500, earned = [
                            Earning(money = 2500, major = {Player.ANNE_MARIE_12}, minor = {Player.FRITS_12,
                                Player.LIESBETH_12})
                        ])
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 2500, earned = [])
exercise6_3 = Exercise(episode = 6, alive = alive6, maximum = 2000, earned = [
                            Earning(money = 1000, major = {Player.WILLIAM_12}, minor = {Player.ANNE_MARIE_12,
                                Player.FRITS_12, Player.TIM_12}),
                            Earning(money = 1000, major = {Player.TIM_12}, minor = {Player.ANNE_MARIE_12,
                                Player.HADEWYCH_12, Player.WILLIAM_12})
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €2000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €2500):
# €500 (Major: Hadewych), -€500 (Major: Liesbeth), €500 (Major: William), -€500 (Major: Anne-Marie), -€500 (Major: Tim)
# Opdracht 3 (Maximaal €2000): Niks verdiend
# Daarnaast:
# -€500 (Major: Hadewych)
alive7 = {Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.TIM_12, Player.WILLIAM_12}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 2000, earned = [])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 2500, earned = [
                            Earning(money = 500, major = {Player.HADEWYCH_12}),
                            Earning(money = -500, major = {Player.LIESBETH_12}),
                            Earning(money = 500, major = {Player.WILLIAM_12}),
                            Earning(money = -500, major = {Player.ANNE_MARIE_12}),
                            Earning(money = -500, major = {Player.TIM_12})
                        ])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 2000, earned = [])
exercise7_4 = Exercise(episode = 7, alive = alive7, maximum = None, earned = [
                            Earning(money = -500, major = {Player.HADEWYCH_12}),
                        ])

# Aflevering 8
# Opdracht 1 (Maximaal €2000):
# €500 (Major: Hadewych)
# Opdracht 2 (Maximaal €3500):
# €1000 (Major: Tim), €500 (Major: Hadewych) (Minor: Tim)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive8 = {Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12, Player.TIM_12}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 2000, earned = [
                            Earning(money = 500, major = {Player.HADEWYCH_12}),
                        ])
exercise8_2 = Exercise(episode = 8, alive = alive8, maximum = 3500, earned = [
                            Earning(money = 1000, major = {Player.TIM_12}),
                            Earning(money = 500, major = {Player.HADEWYCH_12}, minor = {Player.TIM_12}),
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €2500):
# €2500 (Major: Anne-Marie) (Minor: Hadewych, Liesbeth)
alive9 = {Player.ANNE_MARIE_12, Player.HADEWYCH_12, Player.LIESBETH_12}
exercise9_1 = Exercise(episode = 9, alive = alive9, maximum = 2500, earned = [
                            Earning(money = 2500, major = {Player.ANNE_MARIE_12}, minor = {Player.HADEWYCH_12,
                                Player.LIESBETH_12}),
                        ])

season12 = Season([exercise1_1, exercise1_2, exercise1_3, exercise2_1, exercise2_2, exercise2_3, exercise3_1,
                   exercise3_2, exercise3_3, exercise4_1, exercise4_2, exercise4_3, exercise5_1, exercise5_2,
                   exercise5_3, exercise6_1, exercise6_2, exercise6_3, exercise7_1, exercise7_2, exercise7_3,
                   exercise7_4, exercise8_1, exercise8_2, exercise9_1])