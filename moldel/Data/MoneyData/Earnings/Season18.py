from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €10000):
# -€500 (Major: Emilio, Stine), €2000 (Major: Ruben) (Minor: Olcay), -€1000 (Major: Olcay, Ruben),
# -€1000 (Major: Emilio, Stine), -€1000 (Major: Loes, Ron), -€1000 (Major: Jan, Jean-Marc),
# -€500 (Minor: Bella, Emilio, Jan, Jean-Marc, Loes, Olcay, Ron, Ruben, Simone, Stine)
alive1 = {Player.BELLA_18, Player.EMILIO_18, Player.JAN_18, Player.JEAN_MARC_18, Player.LOES_18, Player.OLCAY_18,
          Player.RON_18, Player.RUBEN_18, Player.SIMONE_18, Player.STINE_18}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 10000, earned = [
                            Earning(money = -1500, major = {Player.EMILIO_18, Player.STINE_18}),
                            Earning(money = 2000, major = {Player.RUBEN_18}, minor = {Player.OLCAY_18}),
                            Earning(money = -1000, major = {Player.OLCAY_18, Player.RUBEN_18}),
                            Earning(money = -1000, major = {Player.LOES_18, Player.RON_18}),
                            Earning(money = -1000, major = {Player.JAN_18, Player.JEAN_MARC_18}),
                            Earning(money = -500, minor = {Player.BELLA_18, Player.EMILIO_18, Player.JAN_18,
                                Player.JEAN_MARC_18, Player.LOES_18, Player.OLCAY_18, Player.RON_18, Player.RUBEN_18,
                                Player.SIMONE_18, Player.STINE_18}),
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €1000):
# €20 (Major: Olcay), €60 (Major: Jan) (Minor: Olcay), €120 (Major: Emilio) (Minor: Jan, Olcay),
# €200 (Major: Jean-Marc) (Minor: Emilio, Jan, Olcay), €600 (Major: Ruben) (Minor: Emilio, Jan, Jean-Marc, Olcay),
# €1000 (Major: Ruben) (Minor: Emilio, Jan, Jean-Marc, Olcay) (All multiplied by 0.86)
# Opdracht 2 (Maximaal €2000): Niks verdiend
# Opdracht 3 (Maximaal €3000): Gezamelijk verdiend
alive2 = {Player.BELLA_18, Player.EMILIO_18, Player.JAN_18, Player.JEAN_MARC_18, Player.LOES_18, Player.OLCAY_18,
          Player.RUBEN_18, Player.SIMONE_18, Player.STINE_18}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 1000, earned = [
                            Earning(money = 20 * 0.86, major = {Player.OLCAY_18}),
                            Earning(money = 60 * 0.86, major = {Player.JAN_18}, minor = {Player.OLCAY_18}),
                            Earning(money = 120 * 0.86, major = {Player.EMILIO_18}, minor = {Player.JAN_18,
                                Player.OLCAY_18}),
                            Earning(money = 200 * 0.86, major = {Player.JEAN_MARC_18}, minor = {Player.EMILIO_18,
                                Player.JAN_18, Player.OLCAY_18}),
                            Earning(money = 600 * 0.86, major = {Player.RUBEN_18}, minor = {Player.EMILIO_18,
                                Player.JAN_18, Player.JEAN_MARC_18, Player.OLCAY_18}),
                            Earning(money = 1000 * 0.86, major = {Player.RUBEN_18}, minor = {Player.EMILIO_18,
                                Player.JAN_18, Player.JEAN_MARC_18, Player.OLCAY_18}),
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 3000, earned = [])

# Aflevering 3
# Opdracht 1 (Maximaal €2500):
# €250 (Major: Loes) (Minor: Emilio), €200 (Major: Simone), €450 (Major: Jan, Stine) (Minor: Emilio, Loes, Simone)
# Opdracht 2 (Maximaal €2500):
# -€500 (Major: Bella) (Minor: Emilio, Ruben), €250 (Major: Loes) (Minor: Emilio, Ruben),
# €500 (Major: Emilio, Ruben) (Minor: Bella, Loes), -€500 (Major: Emilio, Ruben) (Minor: Bella, Loes),
# -€500 (Major: Olcay, Stine) (Minor: Jan, Simone), -€500 (Major: Simone) (Minor: Olcay, Stine)
# Opdracht 3 (Maximaal €4000):
# €100 (Major: Jan) (Minor: Olcay), €100 (Major: Loes) (Minor: Ruben), €100 (Major: Bella) (Minor: Emilio),
# €100 (Major: Bella) (Minor: Emilio), €100 (Major: Loes) (Minor: Ruben), €100 (Major: Simone) (Minor: Stine),
# €100 (Major: Jan) (Minor: Olcay), €100 (Major: Bella) (Minor: Emilio), €100 (Major: Simone) (Minor: Stine),
# €100 (Major: Loes) (Minor: Ruben), €800 (Major: Bella, Jan, Loes, Simone) (Minor: Emilio, Olcay, Ruben, Stine)
alive3 = {Player.BELLA_18, Player.EMILIO_18, Player.JAN_18, Player.LOES_18, Player.OLCAY_18, Player.RUBEN_18,
          Player.SIMONE_18, Player.STINE_18}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 2500, earned = [
                            Earning(money = 250, major = {Player.LOES_18}, minor = {Player.EMILIO_18}),
                            Earning(money = 200, major = {Player.SIMONE_18}),
                            Earning(money = 450, major = {Player.JAN_18, Player.STINE_18}, minor = {Player.EMILIO_18,
                                Player.LOES_18, Player.SIMONE_18})
                        ])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 2500, earned = [
                            Earning(money = -500, major = {Player.BELLA_18}, minor = {Player.EMILIO_18, Player.RUBEN_18}),
                            Earning(money = 250, major = {Player.LOES_18}, minor = {Player.EMILIO_18, Player.RUBEN_18}),
                            Earning(money = -500, major = {Player.OLCAY_18, Player.STINE_18}, minor = {Player.JAN_18,
                                Player.SIMONE_18}),
                            Earning(money = -500, major = {Player.SIMONE_18}, minor = {Player.OLCAY_18,
                                Player.STINE_18}),
                        ])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 4000, earned = [
                            Earning(money = 200, major = {Player.JAN_18}, minor = {Player.OLCAY_18}),
                            Earning(money = 300, major = {Player.LOES_18}, minor = {Player.RUBEN_18}),
                            Earning(money = 300, major = {Player.BELLA_18}, minor = {Player.EMILIO_18}),
                            Earning(money = 200, major = {Player.SIMONE_18}, minor = {Player.STINE_18}),
                            Earning(money = 800, major = {Player.BELLA_18, Player.JAN_18, Player.LOES_18, Player.SIMONE_18},
                                    minor = {Player.EMILIO_18, Player.OLCAY_18, Player.RUBEN_18, Player.STINE_18}),
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €1500): Niks verdiend
# Opdracht 2 (Maximaal €0): Niks verdiend
# Opdracht 3 (Maximaal €5000):
# €5000 (Minor: Emilio, Jan, Loes, Olcay, Simone)
alive4 = {Player.EMILIO_18, Player.JAN_18, Player.LOES_18, Player.OLCAY_18, Player.RUBEN_18, Player.SIMONE_18,
          Player.STINE_18}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 1500, earned = [])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 5000, earned = [
                            Earning(money = 5000, minor = {Player.EMILIO_18, Player.JAN_18, Player.LOES_18,
                                                           Player.OLCAY_18, Player.SIMONE_18}),
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €4000):
# €250 (Major: Jan, Ruben), €100 (Major: Simone, Stine), €200 (Major: Loes, Simone, Stine), €50 (Major: Simone),
# €20 (Major: Ruben), €20 (Major: Loes), €20 (Major: Simone), €20 (Major: Stine), €50 (Major: Jan), €100 (Major: Loes),
# €500 (Major: Loes), €310 (Minor: Jan, Loes, Olcay, Ruben, Simone, Stine)
# Opdracht 2 (Maximaal €2000):
# €1000 (Major: Loes) (Minor: Ruben)
# Opdracht 3 (Maximaal €1000): Niks verdiend
alive5 = {Player.JAN_18, Player.LOES_18, Player.OLCAY_18, Player.RUBEN_18, Player.SIMONE_18, Player.STINE_18}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 4000, earned = [
                            Earning(money = 250, major = {Player.JAN_18, Player.RUBEN_18}),
                            Earning(money = 100, major = {Player.SIMONE_18, Player.STINE_18}),
                            Earning(money = 200, major = {Player.LOES_18, Player.SIMONE_18, Player.STINE_18}),
                            Earning(money = 70, major = {Player.SIMONE_18}),
                            Earning(money = 20, major = {Player.RUBEN_18}),
                            Earning(money = 620, major = {Player.LOES_18}),
                            Earning(money = 20, major = {Player.STINE_18}),
                            Earning(money = 50, major = {Player.JAN_18}),
                            Earning(money = 310, minor = {Player.JAN_18, Player.LOES_18, Player.OLCAY_18,
                                    Player.RUBEN_18, Player.SIMONE_18, Player.STINE_18})
                        ])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = 2000, earned = [
                            Earning(money = 1000, major = {Player.LOES_18}, minor = {Player.RUBEN_18})
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 1000, earned = [])

# Aflevering 6
# Opdracht 1 (Maximaal €1500):
# €100 (Major: Jan) (Minor: Ruben), €100 (Major: Ruben), €100 (Major: Olcay) (Minor: Jan, Ruben),
# €100 (Major: Olcay) (Minor: Jan, Ruben), €100 (Major: Jan) (Minor: Ruben)
# Opdracht 2 (Maximaal €1500):
# €750 (Major: Jan, Ruben, Simone) (Minor: Olcay, Stine), €250 (Major: Ruben), €250 (Major: Simone)
# Opdracht 3 (Maximaal €1500): Niks verdiend
alive6 = {Player.JAN_18, Player.OLCAY_18, Player.RUBEN_18, Player.SIMONE_18, Player.STINE_18}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 1500, earned = [
                            Earning(money = 200, major = {Player.JAN_18}, minor = {Player.RUBEN_18}),
                            Earning(money = 100, major = {Player.RUBEN_18}),
                            Earning(money = 200, major = {Player.OLCAY_18}, minor = {Player.JAN_18, Player.RUBEN_18}),
                        ])
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 1500, earned = [
                            Earning(money = 750, major = {Player.JAN_18, Player.RUBEN_18, Player.SIMONE_18},
                                    minor = {Player.OLCAY_18, Player.STINE_18}),
                            Earning(money = 250, major = {Player.RUBEN_18}),
                            Earning(money = 250, major = {Player.SIMONE_18}),
                        ])
exercise6_3 = Exercise(episode = 6, alive = alive6, maximum = 1500, earned = [])

# Aflevering 7
# Opdracht 1 (Maximaal €1630):
# €250 (Major: Jan) (Minor: Ruben, Olcay, Simone, Stine), €250 (Major: Simone) (Minor: Jan, Ruben)
# €250 (Major: Simone) (Minor: Jan, Ruben)
# Opdracht 2 (Maximaal €1250): Gezamelijk verdiend
# Opdracht 3 (Maximaal €1500): Onduidelijk wie wat verdiend heeft
alive7 = {Player.JAN_18, Player.OLCAY_18, Player.RUBEN_18, Player.SIMONE_18, Player.STINE_18}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 1630, earned = [
                            Earning(money = 250, major = {Player.JAN_18}, minor = {Player.RUBEN_18, Player.OLCAY_18,
                                Player.SIMONE_18, Player.STINE_18}),
                            Earning(money = 500, major = {Player.SIMONE_18}, minor = {Player.JAN_18, Player.RUBEN_18}),
                        ])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 1250, earned = [])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [])

# Aflevering 8
# Opdracht 1 (Maximaal €1000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €2200):
# €50 (Major: Jan) (Minor: Olcay), €50 (Major: Olcay) (Minor: Jan), €50 (Major: Jan) (Minor: Olcay),
# €50 (Major: Jan) (Minor: Olcay), €50 (Major: Ruben) (Minor: Simone), €50 (Major: Olcay) (Minor: Jan),
# €100 (Major: Jan) (Minor: Olcay), €100 (Major: Ruben) (Minor: Simone), €200 (Minor: Jan, Olcay, Ruben, Simone)
# Opdracht 3 (Maximaal €4000):
# Simone (Minor: €225) (1 koker), Jan (2 kokers) (Minor: €450), Olcay (1 koker) (Minor: €225), -€50 (Major: Olcay)
alive8 = {Player.JAN_18, Player.OLCAY_18, Player.RUBEN_18, Player.SIMONE_18}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 1000, earned = [])
exercise8_2 = Exercise(episode = 8, alive = alive8, maximum = 2200, earned = [
                            Earning(money = 250, major = {Player.JAN_18}, minor = {Player.OLCAY_18}),
                            Earning(money = 100, major = {Player.OLCAY_18}, minor = {Player.JAN_18}),
                            Earning(money = 150, major = {Player.RUBEN_18}, minor = {Player.SIMONE_18}),
                            Earning(money = 200, minor = {Player.JAN_18, Player.OLCAY_18, Player.RUBEN_18,
                                Player.SIMONE_18})
                        ])
exercise8_3 = Exercise(episode = 8, alive = alive8, maximum = 4000, earned = [
                            Earning(money = 225, minor = {Player.SIMONE_18}),
                            Earning(money = 450, minor = {Player.JAN_18}),
                            Earning(money = 225, minor = {Player.OLCAY_18}),
                            Earning(money = -50, major = {Player.OLCAY_18}),
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €1000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €1500): Niks verdiend
# Opdracht 3 (Maximaal €2500): Onduidelijk wie wat verdiend heeft
alive9 = {Player.JAN_18, Player.OLCAY_18, Player.RUBEN_18}
exercise9_1 = Exercise(episode = 9, alive = alive9, maximum = 1000, earned = [])
exercise9_2 = Exercise(episode = 9, alive = alive9, maximum = 1500, earned = [])
exercise9_3 = Exercise(episode = 9, alive = alive9, maximum = 2500, earned = [])

season18 = Season([exercise1_1, exercise2_1, exercise2_2, exercise2_3, exercise3_1, exercise3_2, exercise3_3,
                   exercise4_1, exercise4_3, exercise5_1, exercise5_2, exercise5_3, exercise6_1, exercise6_2,
                   exercise6_3, exercise7_1, exercise7_2, exercise7_3, exercise8_1, exercise8_2, exercise8_3,
                   exercise9_1, exercise9_2, exercise9_3])
