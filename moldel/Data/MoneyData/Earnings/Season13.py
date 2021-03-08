from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €4000):
# €300 (Major: Janine), €200 (Major: Joep), €200 (Major: Carolien), €100 (Major: Kees)
# Opdracht 2 (Maximaal €10000): Niks verdiend
alive1 = {Player.CAROLIEN_13, Player.DANIEL_13, Player.EWOUT_13, Player.JANINE_13, Player.JOEP_13, Player.KEES_13,
          Player.PAULIEN_13, Player.TANIA_13, Player.TIM_13, Player.ZARAYDA_13}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 4000, earned = [
                            Earning(money = 300, major = {Player.JANINE_13}),
                            Earning(money = 200, major = {Player.JOEP_13}),
                            Earning(money = 200, major = {Player.CAROLIEN_13}),
                            Earning(money = 100, major = {Player.KEES_13})
                        ])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 10000, earned = [])

# Aflevering 2
# Opdracht 1 (Maximaal €3000):
# €1000 (Major: Carolien) (Minor: Kees, Tim)
# Opdracht 2 (Maximaal €2000):
# €500 (Major: Carolien, Joep, Paulien)
# Opdracht 3 (Maximaal €?):
# €750 (Major: Daniel) (Minor: Allen), 1x (Major: Janine, Tim) (Minor: Allen), 1x (Major: Kees) (Minor: Allen),
# 1x (Major: Joep) (Minor: Allen), 1x (Major: Carolien, Tim) (Minor: Allen) (€1750 in totaal verdiend)
alive2 = {Player.CAROLIEN_13, Player.DANIEL_13, Player.JANINE_13, Player.JOEP_13, Player.KEES_13, Player.PAULIEN_13,
          Player.TANIA_13, Player.TIM_13, Player.ZARAYDA_13}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 3000, earned = [
                            Earning(money = 1000, major = {Player.CAROLIEN_13}, minor = {Player.KEES_13, Player.TIM_13})
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [
                            Earning(money = 500, major = {Player.CAROLIEN_13, Player.JOEP_13, Player.PAULIEN_13})
                        ])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = None, earned = [
                            Earning(money = 750, major = {Player.DANIEL_13}, minor = {Player.CAROLIEN_13,
                                Player.JANINE_13, Player.JOEP_13, Player.KEES_13, Player.PAULIEN_13, Player.TANIA_13,
                                Player.TIM_13, Player.ZARAYDA_13}),
                            Earning(money = 250, major = {Player.JANINE_13, Player.TIM_13}, minor = {Player.CAROLIEN_13,
                                Player.DANIEL_13, Player.JOEP_13, Player.KEES_13, Player.PAULIEN_13, Player.TANIA_13,
                                Player.ZARAYDA_13}),
                            Earning(money = 250, major = {Player.KEES_13}, minor = {Player.CAROLIEN_13, Player.DANIEL_13,
                                Player.JANINE_13, Player.JOEP_13, Player.PAULIEN_13, Player.TANIA_13, Player.TIM_13,
                                Player.ZARAYDA_13}),
                            Earning(money = 250, major = {Player.JOEP_13}, minor = {Player.CAROLIEN_13, Player.DANIEL_13,
                                Player.JANINE_13, Player.KEES_13, Player.PAULIEN_13, Player.TANIA_13, Player.TIM_13,
                                Player.ZARAYDA_13}),
                            Earning(money = 250, major = {Player.CAROLIEN_13, Player.TIM_13}, minor = {Player.DANIEL_13,
                                Player.JANINE_13, Player.JOEP_13, Player.KEES_13, Player.PAULIEN_13, Player.TANIA_13,
                                Player.ZARAYDA_13}),
                        ])

# Aflevering 3
# Opdracht 1 (Maximaal €?):
# €1500 (Major: Tim) (Minor: Allen), —€500 (Major: Tania) (Minor: Allen)
# Opdracht 2 (Maximaal €4000):
# €500 (Major: Daniel) (Minor: Zarayda), €500 (Major: Tim) (Minor: Tania), €500 (Major: Paulien) (Minor: Tim)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive3 = {Player.CAROLIEN_13, Player.DANIEL_13, Player.JANINE_13, Player.KEES_13, Player.PAULIEN_13, Player.TANIA_13,
          Player.TIM_13, Player.ZARAYDA_13}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = None, earned = [
                            Earning(money = 1500, major = {Player.TIM_13}, minor = {Player.CAROLIEN_13, Player.DANIEL_13,
                                Player.JANINE_13, Player.KEES_13, Player.PAULIEN_13, Player.TANIA_13, Player.ZARAYDA_13}),
                            Earning(money = -500, major = {Player.TANIA_13}, minor = {Player.CAROLIEN_13, Player.DANIEL_13,
                                Player.JANINE_13, Player.KEES_13, Player.PAULIEN_13, Player.TIM_13, Player.ZARAYDA_13})
                        ])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 4000, earned = [
                            Earning(money = 500, major = {Player.DANIEL_13}, minor = {Player.ZARAYDA_13}),
                            Earning(money = 500, major = {Player.TIM_13}, minor = {Player.TANIA_13}),
                            Earning(money = 500, major = {Player.PAULIEN_13}, minor = {Player.TIM_13}),
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €?): Niks verdiend
# Opdracht 2 (Maximaal €?):
# €100 (Major: Daniel) (Minor: Tania) (Kunstnijverheidstentoonstelling),
# €50 (Major: Daniel) (Minor: Zarayda) (Schorriemorrie)
# €50 (Major: Daniel) (Minor: Paulien) (Idyllisch)
# €25 (Major: Daniel) (Minor: Paulien) (Jottum)
# €50 (Major: Carolien) (Minor: Tania) (Belhamel)
# €50 (Major: Carolien) (Minor: Zarayda) (Schobbejak)
# €50 (Major: Carolien) (Minor: Zarayda) (Kakefonie)
# €25 (Major: Carolien) (Minor: Paulien) (Mieters)
# €25 (Major: Carolien) (Minor: Kees) (Phantoom)
# €25 (Major: Carolien) (Minor: Kees) (Woord)
# €100 (Major: Tim) (Minor: Tania) (Chronischevermoeidheidssyndroom)
# €50 (Major: Tim) (Minor: Tania) (Copulaire)
# €25 (Major: Tim) (Minor: Paulien) (Schaars)
# €50 (Major: Tim) (Minor: Paulien) (Xenofobie)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive4 = {Player.CAROLIEN_13, Player.DANIEL_13, Player.KEES_13, Player.PAULIEN_13, Player.TANIA_13, Player.TIM_13,
          Player.ZARAYDA_13}
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = None, earned = [
                            Earning(money = 100, major = {Player.DANIEL_13}, minor = {Player.TANIA_13}),
                            Earning(money = 50, major = {Player.DANIEL_13}, minor = {Player.ZARAYDA_13}),
                            Earning(money = 75, major = {Player.DANIEL_13}, minor = {Player.PAULIEN_13}),
                            Earning(money = 50, major = {Player.CAROLIEN_13}, minor = {Player.TANIA_13}),
                            Earning(money = 100, major = {Player.CAROLIEN_13}, minor = {Player.ZARAYDA_13}),
                            Earning(money = 25, major = {Player.CAROLIEN_13}, minor = {Player.PAULIEN_13}),
                            Earning(money = 50, major = {Player.CAROLIEN_13}, minor = {Player.KEES_13}),
                            Earning(money = 150, major = {Player.TIM_13}, minor = {Player.TANIA_13}),
                            Earning(money = 75, major = {Player.TIM_13}, minor = {Player.PAULIEN_13})
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €3000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €1500): Niks verdiend
# Opdracht 3 (Maximaal €2500): Gezamelijk verdiend
alive5 = {Player.CAROLIEN_13, Player.DANIEL_13, Player.KEES_13, Player.PAULIEN_13, Player.TANIA_13, Player.TIM_13,
          Player.ZARAYDA_13}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 3000, earned = [])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 2500, earned = [])

# Aflevering 6
# Opdracht 1 (Maximaal €0): Niks verdiend
# Opdracht 2 (Maximaal €0): Niks verdiend
# Opdracht 3 (Maximaal €?): Gezamelijk verdiend

# Aflevering 7
# Opdracht 1 (Maximaal €6000):
# €500 (Major: Kees, Paulien) (Minor: Allen)
# Opdracht 2 (Maximaal €0): Niks verdiend
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive7 = {Player.CAROLIEN_13, Player.DANIEL_13, Player.KEES_13, Player.PAULIEN_13, Player.ZARAYDA_13}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 6000, earned = [
                            Earning(money = 500, major = {Player.KEES_13, Player.PAULIEN_13}, minor = {
                                Player.CAROLIEN_13, Player.DANIEL_13, Player.ZARAYDA_13}),
                        ])

# Aflevering 8
# Opdracht 1 (Maximaal €6000):
# €200 (Major: Paulien) (Minor: Carolien, Kees), €200 (Major: Zarayda) (Minor: Carolien, Kees),
# €200 (Major: Paulien) (Minor: Carolien, Kees), €200 (Major: Paulien) (Minor: Carolien, Kees),
# €200 (Major: Zarayda) (Minor: Carolien, Kees), €200 (Major: Paulien) (Minor: Carolien, Kees),
# €200 (Major: Paulien) (Minor: Carolien, Kees), €200 (Major: Paulien) (Minor: Carolien, Kees)
# Opdracht 2 (Maximaal €1500): Niks verdiend
# Opdracht 3 (Maximaal €2000): Gezamelijk verdiend
alive8 = {Player.CAROLIEN_13, Player.KEES_13, Player.PAULIEN_13, Player.ZARAYDA_13}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 6000, earned = [
                            Earning(money = 1200, major = {Player.PAULIEN_13}, minor = {Player.CAROLIEN_13, Player.KEES_13}),
                            Earning(money = 400, major = {Player.ZARAYDA_13}, minor = {Player.CAROLIEN_13, Player.KEES_13}),
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €?):
# €200 (Major: Paulien), €300 (Major: Paulien), €700 (Major: Carolien)
# Opdracht 2 (Maximaal €?):
# €250 (Major: Kees), €250 (Major: Kees), €250 (Major: Kees), €250 (Major: Paulien), €250 (Major: Paulien),
# €250 (Major: Paulien), €250 (Major: Carolien), €250 (Major: Carolien), €250 (Major: Carolien)
alive9 = {Player.CAROLIEN_13, Player.KEES_13, Player.PAULIEN_13}
exercise9_1 = Exercise(episode = 9, alive = alive9, maximum = None, earned = [
                            Earning(money = 500, major = {Player.PAULIEN_13}),
                            Earning(money = 700, major = {Player.CAROLIEN_13})
                        ])
exercise9_2 = Exercise(episode = 9, alive = alive9, maximum = None, earned = [
                            Earning(money = 750, major = {Player.CAROLIEN_13}),
                            Earning(money = 750, major = {Player.KEES_13}),
                            Earning(money = 750, major = {Player.PAULIEN_13})
                        ])

season13 = Season([exercise1_1, exercise1_2, exercise2_1, exercise2_2, exercise2_3, exercise3_1, exercise3_2,
                   exercise4_2, exercise5_1, exercise5_3, exercise7_1, exercise8_1, exercise9_1, exercise9_2])