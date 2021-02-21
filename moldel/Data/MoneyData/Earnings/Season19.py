from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €2500): Niks verdiend
# Opdracht 2 (Maximaal €1000): Gezamelijk verdiend
# Opdracht 3 (Maximaal €1800):
# €300 (Major: Nikkie, Minor: Rick-Paul, Niels)
alive1 = {Player.EVELIEN_19, Player.EVI_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19,
          Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 2500, earned = [])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 1000, earned = [])
exercise1_3 = Exercise(episode = 1, alive = alive1, maximum = 1800, earned = [
                            Earning(money = 300, major = {Player.NIKKIE_19}, minor = {Player.RICK_PAUL_19, Player.NIELS_19})
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €1200):
# €300 (Major: Nikkie, Rick-Paul) (Minor: Evelien, Evi, Jamie, Merel, Niels, Robert, Sarah, Sinan)
# Opdracht 2 (Maximaal €3500):
# €250 (Major: Merel), €50 (Major: Rick-Paul), €125 (Major: Robert), €225 (Major: Evi)
# Opdracht 3 (Maximaal €2500):
# €250 (Major: Niels), €250 (Major: Sarah), €250 (Major: Jamie), -€250 (Major: Evelien), -€250 (Major: Evi),
# -€250 (Major: Nikkie), -€250 (Major: Rick-Paul),
alive2 = {Player.EVELIEN_19, Player.EVI_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19,
          Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 1200, earned = [
                            Earning(money = 300, major = {Player.NIKKIE_19, Player.RICK_PAUL_19},
                                    minor = {Player.EVELIEN_19, Player.EVI_19, Player.JAMIE_19, Player.MEREL_19,
                                             Player.NIELS_19, Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19})
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 3500, earned = [
                            Earning(money = 250, major = {Player.MEREL_19}),
                            Earning(money = 50, major = {Player.RICK_PAUL_19}),
                            Earning(money = 125, major = {Player.ROBERT_19}),
                            Earning(money = 225, major = {Player.EVI_19})
                        ])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 2500, earned = [
                            Earning(money = 250, major = {Player.NIELS_19}),
                            Earning(money = 250, major = {Player.SARAH_19}),
                            Earning(money = 250, major = {Player.JAMIE_19}),
                            Earning(money = -250, major = {Player.EVELIEN_19}),
                            Earning(money = -250, major = {Player.EVI_19}),
                            Earning(money = -250, major = {Player.NIKKIE_19}),
                            Earning(money = -250, major = {Player.RICK_PAUL_19}),
                        ])

# Aflevering 3
# Opdracht 1 (Maximaal €1500): Niks verdiend
# Opdracht 2 (Maximaal €0): Niks verdiend
# Opdracht 3 (Maximaal €2500): Gezamelijk verdiend
alive3 = {Player.EVELIEN_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.NIKKIE_19, Player.RICK_PAUL_19,
          Player.ROBERT_19, Player.SARAH_19, Player.SINAN_19}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 1500, earned = [])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 2500, earned = [])

# Aflevering 4
# Opdracht 1 (Maximaal €2250):
# €100 (Major: Evelien, Niels) (Minor: Jamie, Sinan), €150 (Major: Robert, Sarah) (Minor: Jamie, Sinan),
# €250 (Major: Merel, Rick-Paul) (Minor: Jamie, Sinan)
# Opdracht 2 (Maximaal €1500): Niks verdiend
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive4 = {Player.EVELIEN_19, Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.ROBERT_19,
          Player.SARAH_19, Player.SINAN_19}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 2250, earned = [
                            Earning(money = 100, major = {Player.EVELIEN_19, Player.NIELS_19}, minor = {Player.JAMIE_19,
                                    Player.SINAN_19}),
                            Earning(money = 150, major = {Player.ROBERT_19, Player.SARAH_19}, minor = {Player.JAMIE_19,
                                    Player.SINAN_19}),
                            Earning(money = 250, major = {Player.MEREL_19, Player.RICK_PAUL_19}, minor =
                                {Player.JAMIE_19, Player.SINAN_19}),
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = 1500, earned = [])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 2000, earned = [])

# Aflevering 5
# Opdracht 1 (Maximaal €1800):
# €1800 (Major: Jamie, Niels, Sinan) (Minor: Merel, Rick-Paul, Robert, Sarah)
# Opdracht 2 (Maximaal: Unlimited):
# €100 (Major: Merel, Sarah) (Minor: Jamie, Niels, Rick-Paul, Robert, Sinan),
# €100 (Major: Merel, Sarah) (Minor: Jamie, Niels, Rick-Paul, Robert, Sinan),
# €50 (Major: Merel, Sarah, Robert) (Minor: Jamie, Niels, Rick-Paul, Sinan),
# €50 (Major: Merel, Sarah, Robert) (Minor: Jamie, Niels, Rick-Paul, Sinan)
# €50 (Major: Merel, Sarah, Robert) (Minor: Jamie, Niels, Rick-Paul, Sinan)
# €200 (Major: Merel, Sarah, Robert) (Minor: Jamie, Niels, Rick-Paul, Sinan)
# €100 (Major: Merel, Sarah, Robert) (Minor: Jamie, Niels, Rick-Paul, Sinan)
# €100 (Major: Merel, Sarah, Robert) (Minor: Jamie, Niels, Rick-Paul, Sinan)
# €600 (Major: Merel, Sarah, Robert) (Minor: Jamie, Niels, Rick-Paul, Sinan)
# Opdracht 3 (Maximaal €1500):
# €750 (Major: Sarah) (Minor: Merel)
alive5 = {Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19,
          Player.SINAN_19}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 1800, earned = [
                            Earning(money = 1800, major = {Player.JAMIE_19, Player.NIELS_19, Player.SINAN_19},
                                    minor = {Player.MEREL_19, Player.RICK_PAUL_19, Player.ROBERT_19, Player.SARAH_19})
                        ])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = None, earned = [
                            Earning(money = 200, major = {Player.MEREL_19, Player.SARAH_19}, minor = {Player.JAMIE_19,
                                        Player.NIELS_19, Player.RICK_PAUL_19, Player.ROBERT_19, Player.SINAN_19}),
                            Earning(money = 1150, major = {Player.MEREL_19, Player.ROBERT_19, Player.SARAH_19},
                                    minor = {Player.JAMIE_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.SINAN_19})
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 1500, earned = [
                            Earning(money = 750, major = {Player.SARAH_19}, minor = {Player.MEREL_19})
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €2500):
# -€150 (Major: Jamie, Niels), €250 (Major: Sinan) (Minor: Sarah), -€250 (Major: Merel, Rick-Paul),
# -€100 (Major: Jamie & Niels)
# Opdracht 2 (Maximaal €1900):
# €100 (Major: Jamie), €50 (Major: Sinan), €250 (Major: Merel), €50 (Major: Sinan), €100 (Major: Rick-Paul),
# -€50 (Major: Niels), -€100 (Major: Sarah), -€250 (Major: Rick-Paul), —€100 (Major: Niels), -€50 (Major: Sarah),
# -€50 (Major: Merel), -€50 (Major: Jamie)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive6 = {Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.SARAH_19, Player.SINAN_19}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 2500, earned = [
                            Earning(money = 250, major = {Player.SINAN_19}, minor = {Player.SARAH_19}),
                            Earning(money = -250, major = {Player.JAMIE_19, Player.NIELS_19}),
                            Earning(money = -250, major = {Player.MEREL_19, Player.RICK_PAUL_19})
                        ])
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 1900, earned = [
                            Earning(money = 50, major = {Player.JAMIE_19}),
                            Earning(money = 100, major = {Player.SINAN_19}),
                            Earning(money = 200, major = {Player.MEREL_19}),
                            Earning(money = -150, major = {Player.RICK_PAUL_19}),
                            Earning(money = -150, major = {Player.NIELS_19}),
                            Earning(money = -150, major = {Player.SARAH_19}),
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €1500): Gezamelijk verdiend
# Opdracht 2 (Maximaal €1500):
# -€1000 (Major: Sinan),-€1000 (Major: Sarah)
# Opdracht 3 (Maximaal €1500):
# €500 (Major: Sinan), €500 (Major: Niels)
alive7 = {Player.JAMIE_19, Player.MEREL_19, Player.NIELS_19, Player.RICK_PAUL_19, Player.SARAH_19, Player.SINAN_19}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [
                            Earning(money = -1000, major = {Player.SINAN_19}),
                            Earning(money = -1000, major = {Player.SARAH_19}),
                        ])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [
                            Earning(money = 500, major = {Player.SINAN_19}),
                            Earning(money = 500, major = {Player.NIELS_19}),
                        ])

# Aflevering 8
# Opdracht 1 (Maximaal €1550): Niks verdiend
# Opdracht 2 (Maximaal €2000):
# €250 (Major: Merel) (Minor: Niels, Sinan), €250 (Major: Sarah) (Minor: Niels, Sinan),
# €250 (Major: Niels) (Minor: Merel, Sarah, Sinan), €250 (Major: Sarah) (Minor: Merel, Niels, Sinan),
# €250 (Major: Merel) (Minor: Niels, Sarah, Sinan)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive8 = {Player.MEREL_19, Player.NIELS_19, Player.SARAH_19, Player.SINAN_19}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 1550, earned = [])
exercise8_2 = Exercise(episode = 8, alive = alive8, maximum = 2000, earned = [
                            Earning(money = 250, major = {Player.MEREL_19}, minor = {Player.NIELS_19, Player.SINAN_19}),
                            Earning(money = 250, major = {Player.SARAH_19}, minor = {Player.NIELS_19, Player.SINAN_19}),
                            Earning(money = 250, major = {Player.NIELS_19}, minor = {Player.MEREL_19, Player.SARAH_19,
                                Player.SINAN_19}),
                            Earning(money = 250, major = {Player.SARAH_19}, minor = {Player.MEREL_19, Player.NIELS_19,
                                Player.SINAN_19}),
                            Earning(money = 250, major = {Player.MEREL_19}, minor = {Player.NIELS_19, Player.SARAH_19,
                                Player.SINAN_19}),
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €1500):
# €250 (Major: Niels) (Minor: Merel, Sarah)
# Opdracht 2 (Maximaal €1500):
# €300 (Major: Niels) (Minor: Sarah), €300 (Major: Merel, Niels)
alive9 = {Player.MEREL_19, Player.NIELS_19, Player.SARAH_19}
exercise9_1 = Exercise(episode = 9, alive = alive9, maximum = 1500, earned = [
                            Earning(money = 250, major = {Player.NIELS_19}, minor = {Player.MEREL_19, Player.SARAH_19}),
                        ])
exercise9_2 = Exercise(episode = 9, alive = alive9, maximum = 1500, earned = [
                            Earning(money = 300, major = {Player.NIELS_19}, minor = {Player.SARAH_19}),
                            Earning(money = 300, major = {Player.MEREL_19, Player.NIELS_19}),
                        ])

season19 = Season([exercise1_1, exercise1_2, exercise1_3, exercise2_1, exercise2_2, exercise2_3, exercise3_1,
                   exercise3_3, exercise4_1, exercise4_2, exercise4_3, exercise5_1, exercise5_2, exercise5_3,
                   exercise6_1, exercise6_2, exercise7_1, exercise7_2, exercise7_3, exercise8_1, exercise8_2,
                   exercise9_1, exercise9_2])