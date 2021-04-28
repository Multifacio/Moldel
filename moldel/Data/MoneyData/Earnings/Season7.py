from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Onbeperkt): Gezamelijk verdiend
# Opdracht 2 (Maximaal €2500):
# €2500 (Major: Inge, Renate) (Minor: Eva, Menno, Nadja, Sander)
# Opdracht 3 (Maximaal €2250): Niks verdiend
alive1 = {Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.LIESBETH_7, Player.MENNO_7, Player.NADJA_7,
          Player.PAUL_7, Player.RENATE_7, Player.SANDER_7}
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 2500, earned = [
                            Earning(money = 2500, major = {Player.INGE_7, Player.RENATE_7}, minor = {Player.EVA_7,
                                Player.MENNO_7, Player.NADJA_7, Player.SANDER_7})
                        ])
exercise1_3 = Exercise(episode = 1, alive = alive1, maximum = 2250, earned = [])

# Aflevering 2
# Opdracht 1 (Maximaal €3000): Niks verdiend
# Opdracht 2 (Maximaal €10000): Niks verdiend
alive2 = {Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.LIESBETH_7, Player.MENNO_7, Player.NADJA_7,
          Player.PAUL_7, Player.RENATE_7}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 3000, earned = [])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 10000, earned = [])

# Aflevering 3
# Opdracht 1 (Maximaal €3000):
# €3000 (Major: Menno) (Minor: Alex, Dick, Eva, Paul, Renate)
# Opdracht 2 (Maximaal €3000): Niks verdiend
alive3 = {Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.MENNO_7, Player.NADJA_7, Player.PAUL_7,
          Player.RENATE_7}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 3000, earned = [
                            Earning(money = 3000, major = {Player.MENNO_7}, minor = {Player.ALEX_7, Player.DICK_7,
                                Player.EVA_7, Player.PAUL_7, Player.RENATE_7})
                        ])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 3000, earned = [])

# Aflevering 4
# Opdracht 1 (Maximaal €5000):
# €1000 (Major: Alex, Renate), €1000 (Major: Alex) (Minor: Renate), €1000 (Major: Inge, Nadja),
# €2000 (Major: Alex, Renate)
# Opdracht 2 (Maximaal €0):
# Hotel overnachting: -€1000 (Major: Eva) (Minor: Alex, Menno, Nadja)
# 3 jokers: -€2450 (Major: Eva) (Minor: Alex, Inge, Menno, Nadja, Renate)
# 4 Molboekjes + Paul: -€300 (Major: Nadja) (Minor: Inge)
# 1 joker: -€1750 (Major: Alex) (Minor: Eva, Inge, Menno)
# 5 jokers: -€6700 (Major: Nadja) (Minor: Alex, Eva, Inge, Menno, Renate)
alive4 = {Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.MENNO_7, Player.NADJA_7, Player.PAUL_7,
          Player.RENATE_7}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 5000, earned = [
                            Earning(money = 3000, major = {Player.ALEX_7, Player.RENATE_7}),
                            Earning(money = 1000, major = {Player.ALEX_7}, minor = {Player.RENATE_7}),
                            Earning(money = 1000, major = {Player.INGE_7, Player.NADJA_7})
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = None, earned = [
                            Earning(money = -1000, major = {Player.EVA_7}, minor = {Player.ALEX_7, Player.MENNO_7,
                                Player.NADJA_7}),
                            Earning(money = -2450, major = {Player.EVA_7}, minor = {Player.ALEX_7, Player.INGE_7,
                                Player.MENNO_7, Player.NADJA_7, Player.RENATE_7}),
                            Earning(money = -300, major = {Player.NADJA_7}, minor = {Player.INGE_7}),
                            Earning(money = -1750, major = {Player.ALEX_7}, minor = {Player.EVA_7, Player.INGE_7,
                                Player.MENNO_7}),
                            Earning(money = -6700, major = {Player.NADJA_7}, minor = {Player.ALEX_7, Player.EVA_7,
                                Player.INGE_7, Player.MENNO_7, Player.RENATE_7})
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €4500): Niks verdiend
# Opdracht 2 (Maximaal €4000):
# €250 (Major: Inge) (Minor: Alex, Paul), €250 (Major: Dick, Renate), €500 (Major: Inge) (Minor: Alex, Paul),
# €250 (Major: Renate) (Minor: Dick), €750 (Major: Inge) (Minor: Alex, Dick, Paul, Renate)
alive5 = {Player.ALEX_7, Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.PAUL_7, Player.RENATE_7}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 4500, earned = [])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = 4000, earned = [
                            Earning(money = 750, major = {Player.INGE_7}, minor = {Player.ALEX_7, Player.PAUL_7}),
                            Earning(money = 250, major = {Player.DICK_7, Player.RENATE_7}),
                            Earning(money = 250, major = {Player.RENATE_7}, minor = {Player.DICK_7}),
                            Earning(money = 750, major = {Player.INGE_7}, minor = {Player.ALEX_7, Player.DICK_7,
                                Player.PAUL_7, Player.RENATE_7})
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €5000): Niks verdiend
# Opdracht 2 (Maximaal €5000): Onduidelijk wie wat verdiend heeft
# Opdracht 3 (Maximaal €5000):
# €5000 (Major: Eva)
alive6 = {Player.DICK_7, Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.PAUL_7, Player.RENATE_7}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 5000, earned = [])
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 5000, earned = [])
exercise6_3 = Exercise(episode = 6, alive = alive6, maximum = 5000, earned = [
                            Earning(money = 5000, major = {Player.EVA_7})
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €?): Onduidelijk wie wat verdiend heeft
# Opdracht 2 (Maximaal €5000): Niks verdiend
# Opdracht 3 (Maximaal €3000):
# €3000 (Major: Paul)
alive7 = {Player.EVA_7, Player.INGE_7, Player.NADJA_7, Player.PAUL_7, Player.RENATE_7}
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 5000, earned = [])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 3000, earned = [
                            Earning(money = 3000, major = {Player.PAUL_7})
                        ])

# Aflevering 8
# Opdracht 1 (Maximaal €3000): Niks verdiend
# Opdracht 2 (Maximaal €3000):
# €3000 (Major: Renate) (Minor: Eva, Inge, Paul)
# Opdracht 3 (Maximaal €3000):
# €1000 (Minor: Paul, Renate), -€1000 (Minor: Inge, Paul, Renate), €1000 (Minor: Eva, Inge, Paul, Renate)
alive8 = {Player.EVA_7, Player.INGE_7, Player.PAUL_7, Player.RENATE_7}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 3000, earned = [])
exercise8_2 = Exercise(episode = 8, alive = alive8, maximum = 3000, earned = [
                            Earning(money = 3000, major = {Player.RENATE_7}, minor = {Player.EVA_7, Player.INGE_7,
                                Player.PAUL_7})
                        ])
exercise8_3 = Exercise(episode = 8, alive = alive8, maximum = 3000, earned = [
                            Earning(money = 1000, minor = {Player.PAUL_7, Player.RENATE_7}),
                            Earning(money = -1000, minor = {Player.INGE_7, Player.PAUL_7, Player.RENATE_7}),
                            Earning(money = 1000, minor = {Player.EVA_7, Player.INGE_7, Player.PAUL_7, Player.RENATE_7})
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €5000): Niks verdiend
alive9 = {Player.EVA_7, Player.INGE_7, Player.PAUL_7, Player.RENATE_7}
exercise9_1 = Exercise(episode = 9, alive = alive9, maximum = 5000, earned = [])

season7 = Season([exercise1_2, exercise1_3, exercise2_1, exercise2_2, exercise3_1, exercise3_2, exercise4_1,
                  exercise4_2, exercise5_1, exercise5_2, exercise6_1, exercise6_2, exercise6_3, exercise7_2,
                  exercise7_3, exercise8_1, exercise8_2, exercise8_3, exercise9_1])