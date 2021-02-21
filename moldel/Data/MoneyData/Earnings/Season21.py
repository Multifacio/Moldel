from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €2000):
# €1000 (Major: Ellie, Horace) (Minor: Jeroen, Nikkie, Patrick, Ron, Tina)
# Opdracht 2 (Maximaal €2000): Onduidelijk wie wat verdiend heeft
# Opdracht 3 (Maximaal €2500):
# Horace (Major: €250) (Pas bekend aflevering 3)
alive1 = {Player.ELLIE_21, Player.HORACE_21, Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21, Player.PATRICK_21,
          Player.PEGGY_21, Player.RON_21, Player.TINA_21, Player.TYGO_21}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 2000, earned = [
                            Earning(money = 1000, major = {Player.ELLIE_21, Player.HORACE_21},
                                    minor = {Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.RON_21,
                                             Player.TINA_21})
                        ])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 2000, earned = [])
exercise1_3 = Exercise(episode = 1, alive = alive1, maximum = 2500, earned = [
                            Earning(money = 250, major = {Player.HORACE_21}, minor = set())
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €2222.50):
# €80 (Major: Ellie, Horace, Patrick, Ron) (Minor: Jeroen, Nadja, Nikkie, Peggy, Tygo),
# €17.50 (Major: Jeroen, Nadja, Nikkie, Peggy, Tygo) (Minor: Ellie, Horace, Patrick, Ron), €2.50 (Minor: Iedereen)
# Opdracht 2 (Maximaal €2000):
# €260 (Major: Jeroen, Horace, Nadja, Nikkie) (Minor: Ellie, Patrick, Peggy, Ron, Tygo)
# Opdracht 3 (Maximaal €1500):
# €1500 (Major: Patrick)
alive2 = {Player.ELLIE_21, Player.HORACE_21, Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21, Player.PATRICK_21,
          Player.PEGGY_21, Player.RON_21, Player.TYGO_21}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 2222.50, earned = [
                            Earning(money = 80, major = {Player.ELLIE_21, Player.HORACE_21, Player.PATRICK_21,
                                Player.RON_21}, minor = {Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21,
                                Player.PEGGY_21, Player.TYGO_21}),
                            Earning(money = 17.50, major = {Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21,
                                Player.PEGGY_21, Player.TYGO_21}, minor = {Player.ELLIE_21, Player.HORACE_21,
                                Player.PATRICK_21, Player.RON_21}),
                            Earning(money = 2.50, major = set(), minor = {Player.ELLIE_21, Player.HORACE_21,
                                Player.JEROEN_21, Player.NADJA_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21,
                                Player.RON_21, Player.TYGO_21})
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [
                            Earning(money = 260, major = {Player.JEROEN_21, Player.HORACE_21, Player.NADJA_21,
                                Player.NIKKIE_21}, minor = {Player.ELLIE_21, Player.PATRICK_21, Player.PEGGY_21,
                                Player.RON_21, Player.TYGO_21})
                        ])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 1500, earned = [
                            Earning(money = 1500, major = {Player.PATRICK_21}, minor = set())
                        ])

# Aflevering 3
# Opdracht 1 (Maximaal €2000):
# €150 (Minor: Ron), €100 (Minor: Jeroen), €150 (Minor: Ellie), €150 (Minor: Patrick), €150 (Minor: Peggy),
# €150 (Minor: Horace), €250 (Minor: Tygo), €200 (Minor: Nikkie)
# Opdracht 2 (Maximaal €2000):
# €600 (Major: Patrick, Peggy) (Minor: Ron, Tygo), €400 (Major: Jeroen, Nikkie) (Minor: Ellie, Horace)
# Opdracht 3 (Maximaal €1600):
# €200 (Major: Patrick) (Minor: Jeroen, Nikkie, Ron, Tygo), €200 (Major: Nikkie) (Minor: Jeroen, Ron, Tygo),
# €200 (Major: Peggy) (Minor: Jeroen, Nikkie, Ron, Tygo), €200 (Major: Horace) (Minor: Ellie, Patrick, Peggy),
# €200 (Major: Patrick) (Minor: Jeroen, Nikkie, Ron, Tygo), €200 (Major: Jeroen) (Minor: Ellie, Horace, Patrick, Peggy)
alive3 = {Player.ELLIE_21, Player.HORACE_21, Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21,
          Player.RON_21, Player.TYGO_21}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [
                            Earning(money = 150, major = set(), minor = {Player.RON_21}),
                            Earning(money = 100, major = set(), minor = {Player.JEROEN_21}),
                            Earning(money = 150, major = set(), minor = {Player.ELLIE_21}),
                            Earning(money = 150, major = set(), minor = {Player.PATRICK_21}),
                            Earning(money = 150, major = set(), minor = {Player.PEGGY_21}),
                            Earning(money = 150, major = set(), minor = {Player.HORACE_21}),
                            Earning(money = 250, major = set(), minor = {Player.TYGO_21}),
                            Earning(money = 200, major = set(), minor = {Player.NIKKIE_21}),
                        ])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [
                            Earning(money = 600, major = {Player.PATRICK_21, Player.PEGGY_21}, minor = {Player.RON_21,
                                Player.TYGO_21}),
                            Earning(money = 400, major = {Player.JEROEN_21, Player.NIKKIE_21}, minor = {Player.ELLIE_21,
                                Player.HORACE_21})
                        ])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 1600, earned = [
                            Earning(money = 200, major = {Player.PATRICK_21}, minor = {Player.JEROEN_21, Player.NIKKIE_21,
                                Player.RON_21, Player.TYGO_21}),
                            Earning(money = 200, major = {Player.NIKKIE_21}, minor = {Player.JEROEN_21, Player.RON_21,
                                Player.TYGO_21}),
                            Earning(money = 200, major = {Player.PEGGY_21}, minor = {Player.JEROEN_21, Player.NIKKIE_21,
                                Player.RON_21, Player.TYGO_21}),
                            Earning(money = 200, major = {Player.HORACE_21}, minor = {Player.ELLIE_21, Player.PATRICK_21,
                                Player.PEGGY_21}),
                            Earning(money = 200, major = {Player.PATRICK_21}, minor = {Player.JEROEN_21, Player.NIKKIE_21,
                                Player.RON_21, Player.TYGO_21}),
                            Earning(money = 200, major = {Player.JEROEN_21}, minor = {Player.ELLIE_21, Player.HORACE_21,
                                Player.PATRICK_21, Player.PEGGY_21}),
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €2000):
# €1000 (Major: Ellie, Patrick, Ron) (Minor: Nikkie, Tygo)
# Opdracht 2 (Maximaal €2250): Niks verdiend
# Opdracht 3 (Maximaal €1350):
# €50 (Major: Jeroen, Patrick), €50 (Major: Ellie, Peggy, Tygo), €100 (Major: Jeroen, Patrick),
# €50 (Major: Jeroen, Patrick), €100 (Major: Nikkie, Ron), €250 (Major: Ellie, Peggy, Tygo), €100 (Major: Jeroen, Patrick),
# €150 (Major: Ellie, Peggy, Tygo)
alive4 = {Player.ELLIE_21, Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21, Player.RON_21,
          Player.TYGO_21}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 2000, earned = [
                            Earning(money = 1000, major = {Player.ELLIE_21, Player.PATRICK_21, Player.RON_21},
                                    minor = {Player.NIKKIE_21, Player.TYGO_21}),
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = 2250, earned = [])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 1350, earned = [
                            Earning(money = 50, major = {Player.JEROEN_21, Player.PATRICK_21}, minor = set()),
                            Earning(money = 50, major = {Player.ELLIE_21, Player.PEGGY_21, Player.TYGO_21}, minor = set()),
                            Earning(money = 100, major = {Player.JEROEN_21, Player.PATRICK_21}, minor = set()),
                            Earning(money = 50, major = {Player.JEROEN_21, Player.PATRICK_21}, minor = set()),
                            Earning(money = 100, major = {Player.NIKKIE_21, Player.RON_21}, minor = set()),
                            Earning(money = 250, major = {Player.ELLIE_21, Player.PEGGY_21, Player.TYGO_21}, minor = set()),
                            Earning(money = 100, major = {Player.JEROEN_21, Player.PATRICK_21}, minor = set()),
                            Earning(money = 150, major = {Player.ELLIE_21, Player.PEGGY_21, Player.TYGO_21}, minor = set()),
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €1750): Niks verdiend
# Opdracht 2 (Maximaal €1500): Niks verdiend
# Opdracht 3 (Maximaal €0): Niks te verdienen
alive5 = {Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21, Player.RON_21, Player.TYGO_21}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 1750, earned = [])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = 1500, earned = [])

# Aflevering 6
# Opdracht 1 (Maximaal €4500):
# €500 (Major: Patrick), €1000 (Major: Patrick), €500 (Major: Peggy), €1000 (Major: Patrick),
# €100 (Major: Ron), €100 (Major: Ron), €100 (Major: Patrick), €100 (Major: Patrick)
alive6 = {Player.JEROEN_21, Player.NIKKIE_21, Player.PATRICK_21, Player.PEGGY_21, Player.RON_21, Player.TYGO_21}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 4500, earned = [
                            Earning(money = 500, major = {Player.PATRICK_21}, minor = set()),
                            Earning(money = 1000, major = {Player.PATRICK_21}, minor = set()),
                            Earning(money = 500, major = {Player.PEGGY_21}, minor = set()),
                            Earning(money = 1000, major = {Player.PATRICK_21}, minor = set()),
                            Earning(money = 100, major = {Player.RON_21}, minor = set()),
                            Earning(money = 100, major = {Player.RON_21}, minor = set()),
                            Earning(money = 100, major = {Player.PATRICK_21}, minor = set()),
                            Earning(money = 100, major = {Player.PATRICK_21}, minor = set()),
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €0): Niks verdiend
# Opdracht 2 (Maximaal €3400): Gezamelijk verdiend
# Opdracht 3 (Maximaal €1500):
# €250 (Major: Jeroen, Minor: Tygo), €250 (Major: Jeroen, Minor: Nikkie, Tygo), €250 (Major: Nikkie, Minor: Tygo)
alive7 = {Player.JEROEN_21, Player.NIKKIE_21, Player.TYGO_21}
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 3400, earned = [])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [
                            Earning(money = 250, major = {Player.JEROEN_21}, minor = {Player.TYGO_21}),
                            Earning(money = 250, major = {Player.JEROEN_21}, minor = {Player.NIKKIE_21, Player.TYGO_21}),
                            Earning(money = 250, major = {Player.NIKKIE_21}, minor = {Player.TYGO_21}),
                        ])

season21 = Season([exercise1_1, exercise1_2, exercise1_3, exercise2_1, exercise2_2, exercise2_3, exercise3_1,
                   exercise3_2, exercise3_3, exercise4_1, exercise4_2, exercise4_3, exercise5_1, exercise5_2,
                   exercise6_1, exercise7_2, exercise7_3])