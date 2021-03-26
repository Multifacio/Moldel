from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €8000):
# €1000 (Major: Erik, Tim) (Minor: Arjen, Barbara, Hint, Kim, Loretta, Sanne)
# Opdracht 2 (Maximaal €2000):
# Barbara (Major: Manuel) (Minor: Barbara), Kim (Major: Loretta) (Minor: Kim), Erik (Major: Arjen) (Minor: Erik),
# Arjen (Major: Arjen), Hind (Major: Tim) (Minor: Hind), Tim (Major: Tim), Sanne (Major: Arjen, Hind) (Minor: Sanne),
# Frits (Minor: Barbara, Erik, Frits, Kim, Sanne, Tim)
# €250 (Per correct persoon)
alive1 = {Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10,
          Player.LORETTA_10, Player.MANUEL_10, Player.SANNE_10, Player.TIM_10}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 8000, earned = [
                            Earning(money = 1000, major = {Player.ERIK_10, Player.TIM_10}, minor = {Player.ARJEN_10,
                                Player.BARBARA_10, Player.HIND_10, Player.KIM_10, Player.LORETTA_10, Player.SANNE_10}),
                        ])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 2000, earned = [
                            Earning(money = 250, major = {Player.MANUEL_10}, minor = {Player.BARBARA_10}),
                            Earning(money = 250, major = {Player.LORETTA_10}, minor = {Player.KIM_10}),
                            Earning(money = 250, major = {Player.ARJEN_10}, minor = {Player.ERIK_10}),
                            Earning(money = 250, major = {Player.ARJEN_10}),
                            Earning(money = 250, major = {Player.TIM_10}, minor = {Player.HIND_10}),
                            Earning(money = 250, major = {Player.TIM_10}),
                            Earning(money = 250, major = {Player.ARJEN_10, Player.HIND_10}, minor = {Player.SANNE_10}),
                            Earning(money = 250, minor = {Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10,
                                Player.KIM_10, Player.SANNE_10, Player.TIM_10})
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €2500):
# €2500 (Minor: Arjen, Barbara, Erik, Kim, Manuel)
# Opdracht 2 (Maximaal €3000): Niks verdiend
# Opdracht 3 (Maximaal €0): Niks verdiend
alive2 = {Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10,
          Player.MANUEL_10, Player.SANNE_10, Player.TIM_10}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 2500, earned = [
                            Earning(money = 2500, minor = {Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10,
                                Player.KIM_10, Player.MANUEL_10}),
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 3000, earned = [])

# Aflevering 3
# Opdracht 1 (Maximaal €?): Niks verdiend
# Opdracht 2 (Maximaal €3000): Onduidelijk wie wat verdiend heeft
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive3 = {Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10,
          Player.MANUEL_10, Player.SANNE_10}
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 3000, earned = [])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [])

# Aflevering 4
# Opdracht 1 (Maximaal €?): Niks verdiend
# Opdracht 2 (Maximaal €4000):
# Arjen (3 zakken), Erik (3 zakken), Hint (4 zakken), Barbara & Frits & Kim & Sanne (18 zakken)
# €1200 verdiend
# Opdracht 3 (Maximaal €3200):
# €50 (Major: Sanne), €50 (Major: Arjen) (Minor: Sanne), €100 (Major: Barbara) (Minor: Arjen, Sanne),
# €200 (Major: Erik) (Minor: Arjen, Barbara, Sanne), €400 (Major: Kim) (Minor: Arjen, Barbara, Erik, Sanne),
# €800 (Major: Hind) (Minor: Arjen, Barbara, Erik, Kim, Sanne)
alive4 = {Player.ARJEN_10, Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10,
          Player.SANNE_10}
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = 4000, earned = [
                            Earning(money = 1200 * 18 / 28, major = {Player.BARBARA_10, Player.FRITS_10, Player.KIM_10,
                                Player.SANNE_10}, minor = {Player.ARJEN_10, Player.ERIK_10, Player.HIND_10}),
                            Earning(money = 1200 * 3 / 28, major = {Player.ARJEN_10}, minor = {Player.BARBARA_10,
                                Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10}),
                            Earning(money = 1200 * 3 / 28, major = {Player.ERIK_10}, minor = {Player.ARJEN_10,
                                Player.BARBARA_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10}),
                            Earning(money = 1200 * 4 / 28, major = {Player.HIND_10}, minor = {Player.ARJEN_10,
                                Player.BARBARA_10, Player.ERIK_10, Player.FRITS_10, Player.KIM_10, Player.SANNE_10})
                        ])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 3200, earned = [
                            Earning(money = 50, major = {Player.SANNE_10}),
                            Earning(money = 50, major = {Player.ARJEN_10}, minor = {Player.SANNE_10}),
                            Earning(money = 100, major = {Player.BARBARA_10}, minor = {Player.ARJEN_10, Player.SANNE_10}),
                            Earning(money = 200, major = {Player.ERIK_10}, minor = {Player.ARJEN_10, Player.BARBARA_10,
                                Player.SANNE_10}),
                            Earning(money = 400, major = {Player.KIM_10}, minor = {Player.ARJEN_10, Player.BARBARA_10,
                                Player.ERIK_10, Player.SANNE_10}),
                            Earning(money = 800, major = {Player.HIND_10}, minor = {Player.ARJEN_10, Player.BARBARA_10,
                                Player.ERIK_10, Player.KIM_10, Player.SANNE_10})
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €5000):
# €500 (Major: Erik, Sanne) (Minor: Allen), €500 (Major: Erik, Sanne) (Minor: Allen),
# €500 (Major: Erik, Hind) (Minor: Allen)
# Opdracht 2 (Maximaal €1500):
# €1500 (Major: Sanne) (Minor: Arjen, Frits, Hind)
# Opdracht 3 (Maximaal €?):
# €100 (Major: Arjen) (Minor: Erik, Frits, Hind), €100 (Major: Erik) (Minor: Arjen, Kim, Sanne),
# €100 (Major: Arjen) (Minor: Erik, Frits, Hind), €100 (Major: Erik) (Minor: Arjen, Kim, Sanne),
# €100 (Major: Arjen) (Minor: Erik, Frits, Hind), €100 (Major: Arjen) (Minor: Erik, Frits, Hind),
# €100 (Major: Frits) (Minor: Arjen, Kim, Sanne), €100 (Major: Arjen. Kim) (Minor: Erik, Frits, Hind),
# €100 (Major: Erik) (Minor: Arjen, Hind, Kim, Sanne), €100 (Major: Arjen) (Minor: Erik, Frits, Hind),
# €100 (Major: Erik) (Minor: Arjen, Kim, Sanne), €500 (Minor: Allen)
alive5 = {Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10, Player.HIND_10, Player.KIM_10, Player.SANNE_10}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 5000, earned = [
                            Earning(money = 1000, major = {Player.ERIK_10, Player.SANNE_10}, minor = {Player.ARJEN_10,
                                Player.FRITS_10, Player.HIND_10, Player.KIM_10}),
                            Earning(money = 500, major = {Player.ERIK_10, Player.HIND_10}, minor = {Player.ARJEN_10,
                                Player.FRITS_10, Player.KIM_10, Player.SANNE_10}),
                        ])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = 1500, earned = [
                            Earning(money = 1500, major = {Player.SANNE_10}, minor = {Player.ARJEN_10, Player.FRITS_10,
                                Player.HIND_10})
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = None, earned = [
                            Earning(money = 500, major = {Player.ARJEN_10}, minor = {Player.ERIK_10, Player.FRITS_10,
                                Player.HIND_10}),
                            Earning(money = 300, major = {Player.ERIK_10}, minor = {Player.ARJEN_10, Player.KIM_10,
                                Player.SANNE_10}),
                            Earning(money = 100, major = {Player.FRITS_10}, minor = {Player.ARJEN_10, Player.KIM_10,
                                Player.SANNE_10}),
                            Earning(money = 100, major = {Player.ARJEN_10, Player.KIM_10}, minor = {Player.ERIK_10,
                                Player.FRITS_10, Player.HIND_10}),
                            Earning(money = 100, major = {Player.ERIK_10}, minor = {Player.ARJEN_10, Player.HIND_10,
                                Player.KIM_10, Player.SANNE_10}),
                            Earning(money = 500, minor = {Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10,
                                Player.HIND_10, Player.KIM_10, Player.SANNE_10}),
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €2500): Niks verdiend
# Opdracht 2 (Maximaal €0): Niks verdiend
# Opdracht 3 (Maximaal €?):
# Container €250 (Minor: Arjen, Kim), Container €500 (Minor: Arjen, Kim), Container €250 (Minor: Erik, Sanne),
# Container (Minor: Arjen, Kim), Container €500 (Minor: Arjen, Kim), Container €500 (Minor: Erik, Sanne),
# Container €500 (Minor: Erik, Sanne)
# 6 Containers gepakt (2 van €250 en 4 van €500). Sowieso €500 (Minor: Arjen, Kim), €500 (Minor: Erik, Sanne)
# Conclusie:
# €500 (Major: Frits) (Minor: Arjen, Erik, Kim, Sanne), €500 (Major: Frits) (Minor: Arjen, Erik, Kim, Sanne)
# €500 (Major: Frits) (Minor: Arjen, Kim), €500 (Major: Frits) (Minor: Erik, Sanne),
# €250 (Major: Frits) (Minor: Arjen, Erik, Kim, Sanne), €250 (Major: Frits) (Minor: Arjen, Erik, Kim, Sanne)
# Opdracht 4 (Maximaal €0):
# -€1000 (Major: Frits), -€1000 (Major: Sanne), -€1000 (Major: Kim), -€1000 (Major: Erik)
alive6 = {Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10, Player.KIM_10, Player.SANNE_10}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 2500, earned = [])
exercise6_3 = Exercise(episode = 6, alive = alive6, maximum = None, earned = [
                            Earning(money = 1500, major = {Player.FRITS_10}, minor = {Player.ARJEN_10, Player.ERIK_10,
                                Player.KIM_10, Player.SANNE_10}),
                            Earning(money = 500, major = {Player.FRITS_10}, minor = {Player.ARJEN_10, Player.KIM_10}),
                            Earning(money = 500, major = {Player.FRITS_10}, minor = {Player.ERIK_10, Player.SANNE_10})
                        ])
exercise6_4 = Exercise(episode = 6, alive = alive6, maximum = None, earned = [
                            Earning(money = -1000, major = {Player.ERIK_10}),
                            Earning(money = -1000, major = {Player.FRITS_10}),
                            Earning(money = -1000, major = {Player.KIM_10}),
                            Earning(money = -1000, major = {Player.SANNE_10})
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €2000): Niks verdiend
# Opdracht 2 (Maximaal €2500): Niks verdiend
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive7 = {Player.ARJEN_10, Player.ERIK_10, Player.FRITS_10, Player.KIM_10, Player.SANNE_10}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 2000, earned = [])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 2500, earned = [])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 2000, earned = [])

# Aflevering 8
# Opdracht 1 (Maximaal €2500): Gezamelijk verdiend
# Opdracht 2 (Maximaal €3000):
# -€1000 (Major: Sanne)
# Opdracht 3 (Maximaal €2000):
# €250 (Major: Frits) (Minor: Erik), €250 (Major: Sanne) (Minor: Erik), €250 (Major: Sanne) (Minor: Kim),
# €250 (Major: Erik) (Minor: Sanne)
alive8 = {Player.ERIK_10, Player.FRITS_10, Player.KIM_10, Player.SANNE_10}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 2500, earned = [])
exercise8_2 = Exercise(episode = 8, alive = alive8, maximum = 3000, earned = [
                            Earning(money = -1000, major = {Player.SANNE_10})
                        ])
exercise8_3 = Exercise(episode = 8, alive = alive8, maximum = 2000, earned = [
                            Earning(money = 250, major = {Player.FRITS_10}, minor = {Player.ERIK_10}),
                            Earning(money = 250, major = {Player.SANNE_10}, minor = {Player.ERIK_10}),
                            Earning(money = 250, major = {Player.SANNE_10}, minor = {Player.KIM_10}),
                            Earning(money = 250, major = {Player.ERIK_10}, minor = {Player.SANNE_10})
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €2000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €?):
# €3050 in totaal verdiend
# €500 (Ingeschat) (Major: Sanne) (Minor: Allen), €250 (Major: Frits) (Minor: Allen),
# €500 (Ingeschat) (Major: Frits) (Minor: Allen), €1000 (Major: Frits) (Minor: Allen), €250 (Major: Kim) (Minor: Allen)
# €550 (Major: Frits)
alive9 = {Player.FRITS_10, Player.KIM_10, Player.SANNE_10}
exercise9_1 = Exercise(episode = 9, alive = alive9, maximum = 2000, earned = [])
exercise9_2 = Exercise(episode = 9, alive = alive9, maximum = None, earned = [
                            Earning(money = 500, major = {Player.SANNE_10}, minor = {Player.FRITS_10, Player.KIM_10}),
                            Earning(money = 1750, major = {Player.FRITS_10}, minor = {Player.KIM_10, Player.SANNE_10}),
                            Earning(money = 250, major = {Player.KIM_10}, minor = {Player.FRITS_10, Player.SANNE_10}),
                            Earning(money = 550, major = {Player.FRITS_10})
                        ])

season10 = Season([exercise1_1, exercise1_2, exercise2_1, exercise2_2, exercise3_2, exercise3_3, exercise4_2,
                   exercise4_3, exercise5_1, exercise5_2, exercise5_3, exercise6_1, exercise6_3, exercise6_4,
                   exercise7_1, exercise7_2, exercise7_3, exercise8_1, exercise8_2, exercise8_3, exercise9_1,
                   exercise9_2])