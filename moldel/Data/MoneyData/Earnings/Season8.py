from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €1500):
# €250 (Major: Coen) (Minor: Regina), €250 (Major: Annette) (Minor: Georgina). €250 (Major: Regina) (Minor: Patrick)
# Opdracht 2 (Maximaal €5000):
# €1000 (Major: Georgina), €1000 (Major: Nicolette) (Minor: Georgina), €1000 (Major: Dunya) (Minor: Georgina, Nicolette)
# Opdracht 3 (Maximaal €0):
# 10 jokers van de 17 zijn ingeleverd (-€1000 dus)
# Annette: 2 jokers, Coen: 1 joker, Dennis: 1 joker, Dunya: 1 joker, Edo: 1 joker, Georgina: 3 jokers, Joris: 2 jokers,
# Nicolette: 1 joker, Patrick: 2 jokers, Regina: 3 jokers
# -€200 (Major: Patrick), -€100 (Major: Dunya), -€300 (Major: Georgina), -€100 (Major: Nicolette),
# -€75 (Minor: Annette), -€75 (Minor: Joris), -€37.50 (Minor: Coen), -€37.50 (Minor: Dennis), -€37.50 (Minor: Edo),
# -€37.50 (Minor: Regina)
alive1 = {Player.ANNETTE_8, Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.GEORGINA_8,
          Player.JORIS_8, Player.NICOLETTE_8, Player.PATRICK_8, Player.REGINA_8}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 1500, earned = [
                            Earning(money = 250, major = {Player.COEN_8}, minor = {Player.REGINA_8}),
                            Earning(money = 250, major = {Player.ANNETTE_8}, minor = {Player.GEORGINA_8}),
                            Earning(money = 250, major = {Player.REGINA_8}, minor = {Player.PATRICK_8})
                        ])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 5000, earned = [
                            Earning(money = 1000, major = {Player.GEORGINA_8}),
                            Earning(money = 1000, major = {Player.NICOLETTE_8}, minor = {Player.GEORGINA_8}),
                            Earning(money = 1000, major = {Player.DUNYA_8}, minor = {Player.GEORGINA_8, Player.NICOLETTE_8})
                        ])
exercise1_3 = Exercise(episode = 1, alive = alive1, maximum = None, earned = [
                            Earning(money = -75, minor = {Player.ANNETTE_8}),
                            Earning(money = -37.50, minor = {Player.COEN_8}),
                            Earning(money = -37.50, minor = {Player.DENNIS_8}),
                            Earning(money = -100, major = {Player.DUNYA_8}),
                            Earning(money = -37.50, minor = {Player.EDO_8}),
                            Earning(money = -300, major = {Player.GEORGINA_8}),
                            Earning(money = -75, minor = {Player.JORIS_8}),
                            Earning(money = -100, major = {Player.NICOLETTE_8}),
                            Earning(money = -200, major = {Player.PATRICK_8}),
                            Earning(money = -37.50, minor = {Player.REGINA_8})
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €?):
# €1050 (Major: Joris), €75 (Major: Coen), €400 (Major: Patrick)
# Opdracht 2 (Maximaal €3000): Niks verdiend
# Opdracht 3 (Maximaal €10000): Niks verdiend
alive2 = {Player.ANNETTE_8, Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.GEORGINA_8,
          Player.JORIS_8, Player.PATRICK_8, Player.REGINA_8}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = None, earned = [
                            Earning(money = 1050, major = {Player.JORIS_8}),
                            Earning(money = 75, major = {Player.COEN_8}),
                            Earning(money = 400, major = {Player.PATRICK_8})
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 3000, earned = [])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 10000, earned = [])

# Aflevering 3
# Opdracht 1 (Maximaal €0): Niks verdiend
# Opdracht 2 (Maximaal €4000):
# €2250 in totaal verdiend
# Regina -> Coen -> Edo (Correct 3) -> Dennis (Correct 4) -> (Patrick -> Dunya) -> Joris (Correct 5) ->
# Georgina (Correct 9)
# €750 (Major: Coen, Edo, Regina), €250 (Major: Edo) (Minor: Coen, Dennis, Regina),
# €250 (Major: Dennis) (Minor: Coen, Dunya, Edo, Joris, Patrick, Regina), €1000 (Minor: Allen)
# Opdracht 3 (Maximaal €4000):
# Uitkijkers: Edo, Joris
# Verkenners:
# Dennis -> 1/4 * 500 (Veilig gesteld), Dunya -> 2 * 500 (Veilig gesteld), Georgina -> 3 * 500 (Veilig gesteld),
# Georgina -> 1 * 500 (Veilig gesteld), Georgina -> 1/2 * 500 (Veilig gesteld)
# Ophalers:
# Regina -> 2 * 500, Coen/Patrick -> 1/4 * 500, Coen/Patrick -> 3 * 500, Patrick -> 1 * 500
# €500 (Major: Patrick) (Minor: Dennis, Edo, Georgina, Joris)
alive3 = {Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.GEORGINA_8, Player.JORIS_8,
          Player.PATRICK_8, Player.REGINA_8}
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 4000, earned = [
                            Earning(money = 750, major = {Player.COEN_8, Player.EDO_8, Player.REGINA_8}),
                            Earning(money = 250, major = {Player.EDO_8}, minor = {Player.COEN_8, Player.DENNIS_8,
                                Player.REGINA_8}),
                            Earning(money = 250, major = {Player.DENNIS_8}, minor = {Player.COEN_8, Player.DUNYA_8,
                                Player.EDO_8, Player.JORIS_8, Player.PATRICK_8, Player.REGINA_8}),
                            Earning(money = 1000, minor = {Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8,
                                Player.GEORGINA_8, Player.JORIS_8, Player.PATRICK_8, Player.REGINA_8})
                        ])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 4000, earned = [
                            Earning(money = 500, major = {Player.PATRICK_8}, minor = {Player.DENNIS_8, Player.EDO_8,
                                Player.GEORGINA_8, Player.JORIS_8})
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €2500): Niks verdiend
# Opdracht 2 (Maximaal €?):
# €500 (Major: Patrick) (Minor: Dennis), €500 (Major: Dunya) (Minor: Joris, Regina), €500 (Major: Regina),
# €500 (Major: Regina) (Minor: Patrick), €100 (Major: Patrick)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive4 = {Player.COEN_8, Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.JORIS_8, Player.PATRICK_8,
          Player.REGINA_8}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 2500, earned = [])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = None, earned = [
                            Earning(money = 500, major = {Player.PATRICK_8}, minor = {Player.DENNIS_8}),
                            Earning(money = 500, major = {Player.DUNYA_8}, minor = {Player.JORIS_8, Player.REGINA_8}),
                            Earning(money = 500, major = {Player.REGINA_8}),
                            Earning(money = 500, major = {Player.REGINA_8}, minor = {Player.PATRICK_8}),
                            Earning(money = 100, major = {Player.PATRICK_8}),
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €?): Niks verdiend
# Opdracht 2 (Maximaal €0):
# -€1000 (Major: Regina)
# Opdracht 3 (Maximaal €2500):
# €2500 (Major: Dennis) (Minor: Edo, Joris)
alive5 = {Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.JORIS_8, Player.PATRICK_8, Player.REGINA_8}
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = None, earned = [
                            Earning(money = -1000, major = {Player.REGINA_8})
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 2500, earned = [
                            Earning(money = 2500, major = {Player.DENNIS_8}, minor = {Player.EDO_8, Player.JORIS_8})
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €4000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €2500): Gezamelijk verdiend
# Opdracht 3 (Maximaal €6000):
# -€250 (Major: Dunya) (Minor: Edo), -€250 (Major: Joris) (Minor: Edo), -€250 (Major: Regina) (Minor: Edo),
# -€250 (Major: Dennis) (Minor: Edo), -€250 (Major: Edo), -€250 (Major: Patrick) (Minor: Edo),
# -€250 (Major: Patrick) (Minor: Dennis), -€250 (Major: Dennis), -€250 (Major: Joris) (Minor: Dennis),
# -€250 (Major: Dunya) (Minor: Dennis), -€250 (Major: Regina) (Minor: Dennis), -€250 (Major: Edo) (Minor: Dennis)
alive6 = {Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.JORIS_8, Player.PATRICK_8, Player.REGINA_8}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 4000, earned = [])
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 2500, earned = [])
exercise6_3 = Exercise(episode = 6, alive = alive6, maximum = 6000, earned = [
                            Earning(money = -250, major = {Player.DUNYA_8}, minor = {Player.EDO_8}),
                            Earning(money = -250, major = {Player.JORIS_8}, minor = {Player.EDO_8}),
                            Earning(money = -250, major = {Player.REGINA_8}, minor = {Player.EDO_8}),
                            Earning(money = -250, major = {Player.DENNIS_8}, minor = {Player.EDO_8}),
                            Earning(money = -250, major = {Player.EDO_8}),
                            Earning(money = -250, major = {Player.PATRICK_8}, minor = {Player.EDO_8}),
                            Earning(money = -250, major = {Player.PATRICK_8}, minor = {Player.DENNIS_8}),
                            Earning(money = -250, major = {Player.DENNIS_8}),
                            Earning(money = -250, major = {Player.JORIS_8}, minor = {Player.DENNIS_8}),
                            Earning(money = -250, major = {Player.DUNYA_8}, minor = {Player.DENNIS_8}),
                            Earning(money = -250, major = {Player.REGINA_8}, minor = {Player.DENNIS_8}),
                            Earning(money = -250, major = {Player.EDO_8}, minor = {Player.DENNIS_8})
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €2500):
# -€250 per fout, €2500 in totaal te verdienen
# 0 fouten (Major: Edo) (Minor: Patrick, Regina), 1 fout (Major: Patrick) (Minor: Edo, Regina),
# 1 fout (Major: Regina) (Minor: Edo, Patrick)
# Opdracht 2 (Maximaal €1500): Niks verdiend
# Opdracht 3 (Maximaal €3000):
# €500 (Major: Dennis, Edo) (Minor: Regina), €750 (Major: Dunya) (Minor: Dennis, Patrick, Regina)
alive7 = {Player.DENNIS_8, Player.DUNYA_8, Player.EDO_8, Player.PATRICK_8, Player.REGINA_8}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 2500, earned = [
                            Earning(money = 2500/3, major = {Player.EDO_8}, minor = {Player.PATRICK_8, Player.REGINA_8}),
                            Earning(money = 2500/3 - 250, major = {Player.PATRICK_8}, minor = {Player.EDO_8, Player.REGINA_8}),
                            Earning(money = 2500/3 - 250, major = {Player.REGINA_8}, minor = {Player.EDO_8, Player.PATRICK_8})
                        ])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 3000, earned = [
                            Earning(money = 500, major = {Player.DENNIS_8, Player.EDO_8}, minor = {Player.REGINA_8}),
                            Earning(money = 750, major = {Player.DUNYA_8}, minor = {Player.DENNIS_8, Player.PATRICK_8,
                                Player.REGINA_8}),
                        ])

# Aflevering 8
# Opdracht 1 (Maximaal €2400):
# €100 (Major: Dennis) (Minor: Edo), €100 (Major: Edo) (Minor: Regina), €100 (Major: Dennis) (Minor: Regina),
# €100 (Major: Edo) (Minor: Dennis), €100 (Major: Edo) (Minor: Dennis)
# Opdracht 2 (Maximaal €3000): Niks verdiend
# Opdracht 3 (Maximaal €3000):
# €3000 (Major: Edo)
alive8 = {Player.DENNIS_8, Player.EDO_8, Player.PATRICK_8, Player.REGINA_8}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 2400, earned = [
                            Earning(money = 100, major = {Player.DENNIS_8}, minor = {Player.EDO_8}),
                            Earning(money = 100, major = {Player.EDO_8}, minor = {Player.REGINA_8}),
                            Earning(money = 100, major = {Player.DENNIS_8}, minor = {Player.REGINA_8}),
                            Earning(money = 200, major = {Player.EDO_8}, minor = {Player.DENNIS_8})
                        ])
exercise8_2 = Exercise(episode = 8, alive = alive8, maximum = 3000, earned = [])
exercise8_3 = Exercise(episode = 8, alive = alive8, maximum = 3000, earned = [
                            Earning(money = 3000, major = {Player.EDO_8})
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €5000):
# €1500 (Major: Edo) (Minor: Dennis, Regina)
# Opdracht 2 (Maximaal €0): Niks verdiend
alive9 = {Player.DENNIS_8, Player.EDO_8, Player.REGINA_8}
exercise9_1 = Exercise(episode = 9, alive = alive9, maximum = 5000, earned = [
                            Earning(money = 1500, major = {Player.EDO_8}, minor = {Player.DENNIS_8, Player.REGINA_8})
                        ])

season8 = Season([exercise1_1, exercise1_2, exercise1_3, exercise2_1, exercise2_2, exercise2_3, exercise3_2,
                  exercise3_3, exercise4_1, exercise4_2, exercise5_2, exercise5_3, exercise6_1, exercise6_2,
                  exercise6_3, exercise7_1, exercise7_2, exercise7_3, exercise8_1, exercise8_2, exercise8_3,
                  exercise9_1])