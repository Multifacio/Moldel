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
# €225 (Major: Carolien) (In totaal)
# €225 (Major: Tim) (In totaal)