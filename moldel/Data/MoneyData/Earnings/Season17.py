from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €0): Niks verdiend
# Opdracht 2 (Maximaal €2500):
# €750 (Major: Imanuelle) (Minor: Diederik, Sanne), €500 (Major: Jochem) (Minor: Sigrid, Yvonne),
# €1000 (Major: Sanne) (Minor: Diederik, Imanuelle), €250 (Major: Yvonne) (Minor: Jochem, Sigrid)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive1 = {Player.DIEDERIK_17, Player.IMANUELLE_17, Player.JEROEN_17, Player.JOCHEM_17, Player.ROOS_17, Player.SANNE_17,
          Player.SIGRID_17, Player.THOMAS_17, Player.VINCENT_17, Player.YVONNE_17}
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 2500, earned = [
                            Earning(money = 750, major = {Player.IMANUELLE_17}, minor = {Player.DIEDERIK_17, Player.SANNE_17}),
                            Earning(money = 500, major = {Player.JOCHEM_17}, minor = {Player.SIGRID_17, Player.YVONNE_17}),
                            Earning(money = 1000, major = {Player.SANNE_17}, minor = {Player.DIEDERIK_17, Player.IMANUELLE_17}),
                            Earning(money = 250, major = {Player.YVONNE_17}, minor = {Player.JOCHEM_17, Player.SIGRID_17}),
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €3500):
# €100 (Major: Jochem) (Minor: Yvonne), €50 (Major: Jochem) (Minor: Yvonne), €50 (Major: Jochem) (Minor: Yvonne),
# €250 (Major: Yvonne) (Minor: Jochem)
# Opdracht 2 (Maximaal €?):
# €500 (Major: Sanne), €500 (Major: Imanuelle), €250 (Major: Thomas)
# Opdracht 3 (Maximaal €1000): Niks verdiend
alive2 = {Player.DIEDERIK_17, Player.IMANUELLE_17, Player.JEROEN_17, Player.JOCHEM_17, Player.ROOS_17, Player.SANNE_17,
          Player.SIGRID_17, Player.THOMAS_17, Player.YVONNE_17}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 3500, earned = [
                            Earning(money = 200, major = {Player.JOCHEM_17}, minor = {Player.YVONNE_17}),
                            Earning(money = 250, major = {Player.YVONNE_17}, minor = {Player.JOCHEM_17})
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = None, earned = [
                            Earning(money = 500, major = {Player.SANNE_17}),
                            Earning(money = 500, major = {Player.IMANUELLE_17}),
                            Earning(money = 250, major = {Player.THOMAS_17})
                        ])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 1000, earned = [])

# Aflevering 3
# Opdracht 1 (Maximaal: €3000):
# €20 (Major: Jeroen), 3x (Major: Roos), €500 (Major: Roos, Sanne), €250 (Major: Sigrid), 2x (Major: Sigrid),
# 2x (Major: Sanne), €70 (Major: Imanuelle), -€1000 (Major: Jochem, Thomas), 2x (Major: Jochem), €500 (Major: Thomas),
# 4x (Major: Thomas) (€500 missing, so Roos, Sanne, Thomas only earn €250)
# Opdracht 2 (Maximaal: €4000):
# €500 (Major: Sigrid), €500 (Major: Imanuelle), €500 (Major: Sigrid), €500 (Major: Sigrid), €500 (Major: Sigrid)
# For all earned (Minor: Diederik, Jeroen, Jochem, Roos, Sanne, Thomas)
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive3 = {Player.DIEDERIK_17, Player.IMANUELLE_17, Player.JEROEN_17, Player.JOCHEM_17, Player.ROOS_17, Player.SANNE_17,
          Player.SIGRID_17, Player.THOMAS_17}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 3000, earned = [
                            Earning(money = 20, major = {Player.JEROEN_17}, minor = {Player.DIEDERIK_17, Player.IMANUELLE_17,
                                Player.JOCHEM_17, Player.ROOS_17, Player.SANNE_17, Player.SIGRID_17, Player.THOMAS_17}),
                            Earning(money = 66.92, major = {Player.ROOS_17}, minor = {Player.DIEDERIK_17, Player.IMANUELLE_17,
                                Player.JEROEN_17, Player.JOCHEM_17, Player.SANNE_17, Player.SIGRID_17, Player.THOMAS_17}),
                            Earning(money = 250, major = {Player.ROOS_17, Player.SANNE_17}, minor = {Player.DIEDERIK_17,
                                Player.IMANUELLE_17, Player.JEROEN_17, Player.JOCHEM_17, Player.SIGRID_17, Player.THOMAS_17}),
                            Earning(money = 294.62, major = {Player.SIGRID_17}, minor = {Player.DIEDERIK_17, Player.IMANUELLE_17,
                                Player.JEROEN_17, Player.JOCHEM_17, Player.ROOS_17, Player.SANNE_17, Player.THOMAS_17}),
                            Earning(money = 44.62, major = {Player.SANNE_17}, minor = {Player.DIEDERIK_17, Player.IMANUELLE_17,
                                Player.JEROEN_17, Player.JOCHEM_17, Player.ROOS_17, Player.SIGRID_17, Player.THOMAS_17}),
                            Earning(money = 70, major = {Player.IMANUELLE_17}, minor = {Player.DIEDERIK_17, Player.JEROEN_17,
                                Player.JOCHEM_17, Player.ROOS_17, Player.SANNE_17, Player.SIGRID_17, Player.THOMAS_17}),
                            Earning(money = -1000, major = {Player.JOCHEM_17, Player.THOMAS_17}),
                            Earning(money = 44.62, major = {Player.JOCHEM_17}, minor = {Player.DIEDERIK_17, Player.IMANUELLE_17,
                                Player.JEROEN_17, Player.ROOS_17, Player.SANNE_17, Player.SIGRID_17, Player.THOMAS_17}),
                            Earning(money = 250, major = {Player.THOMAS_17}, minor = {Player.DIEDERIK_17, Player.IMANUELLE_17,
                                Player.JEROEN_17, Player.JOCHEM_17, Player.ROOS_17, Player.SANNE_17, Player.SIGRID_17}),
                            Earning(money = 89.23, major = {Player.SANNE_17}, minor = {Player.DIEDERIK_17, Player.IMANUELLE_17,
                                Player.JEROEN_17, Player.JOCHEM_17, Player.ROOS_17, Player.SIGRID_17, Player.THOMAS_17})
                        ])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 4000, earned = [
                            Earning(money = 2000, major = {Player.SIGRID_17}, minor = {Player.DIEDERIK_17,
                                Player.JEROEN_17, Player.JOCHEM_17, Player.ROOS_17, Player.SANNE_17, Player.THOMAS_17}),
                            Earning(money = 500, major = {Player.IMANUELLE_17}, minor = {Player.DIEDERIK_17,
                                Player.JEROEN_17, Player.JOCHEM_17, Player.ROOS_17, Player.SANNE_17, Player.THOMAS_17}),
                        ])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [])

# Aflevering 4
# Opdracht 1 (Maximaal €3000):
# €250 (Major: Jeroen), €250 (Major: Sanne), €250 (Major: Diederik), €250 (Major: Imanuelle),
# -€500 (Major: Thomas) (Verwerkt met anderen)
# Opdracht 2 (Maximaal ?):
# €250 (Major: Jochem), €500 (Major: Sigrid)
# Opdracht 3 (Maximaal €500):
# -€2700 (Major: Diederik) (Minor: Imanuelle, Jochem, Thomas), -€2000 (Major: Sanne) (Minor: Jochem, Thomas),
# -€3500 (Major: Jochem) (Minor: Sigrid, Thomas) (€1400 protected)
alive4 = {Player.DIEDERIK_17, Player.IMANUELLE_17, Player.JEROEN_17, Player.JOCHEM_17, Player.SANNE_17,
          Player.SIGRID_17, Player.THOMAS_17}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 3000, earned = [
                            Earning(money = 125, major = {Player.JEROEN_17}),
                            Earning(money = 125, major = {Player.SANNE_17}),
                            Earning(money = 125, major = {Player.DIEDERIK_17}),
                            Earning(money = 125, major = {Player.IMANUELLE_17})
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = None, earned = [
                            Earning(money = 250, major = {Player.JOCHEM_17}),
                            Earning(money = 500, major = {Player.SIGRID_17})
                        ])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = None, earned = [
                            Earning(money = -2700, major = {Player.DIEDERIK_17}, minor = {Player.IMANUELLE_17,
                                Player.JOCHEM_17, Player.THOMAS_17}),
                            Earning(money = -2000, major = {Player.SANNE_17}, minor = {Player.JOCHEM_17, Player.THOMAS_17}),
                            Earning(money = -3500, major = {Player.JOCHEM_17}, minor = {Player.SIGRID_17, Player.THOMAS_17}),
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €12000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €0): Niks verdiend
# Opdracht 3 (Maximaal €2000):
# €2000 (Major: Diederik) (Minor: Imanuelle, Jeroen, Jochem, Sanne, Thomas)
alive5 = {Player.DIEDERIK_17, Player.IMANUELLE_17, Player.JEROEN_17, Player.JOCHEM_17, Player.SANNE_17, Player.THOMAS_17}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 12000, earned = [])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 2000, earned = [
                            Earning(money = 2000, major = {Player.DIEDERIK_17}, minor = {Player.IMANUELLE_17,
                                Player.JEROEN_17, Player.JOCHEM_17, Player.SANNE_17, Player.THOMAS_17}),
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €?):
# Jochem (3x), Imanuelle (4x), Diederik (1x):
# €150 (Major: Jochem) (Minor: Sanne, Thomas), €200 (Major: Imanuelle) (Minor: Sanne, Thomas),
# €50 (Major: Diederik) (Minor: Sanne, Thomas)
# Opdracht 2 (Maximaal €2000):
# €2000 (Major: Diederik, Sanne) (Minor: Imanuelle, Jochem, Thomas)
# Opdracht 3 (Maximaal €?):
# €10 (Major: Imanuelle), €100 (Major: Thomas), €500 (Major: Imanuelle), €20 (Major: Imanuelle)
alive6 = {Player.DIEDERIK_17, Player.IMANUELLE_17, Player.JOCHEM_17, Player.SANNE_17, Player.THOMAS_17}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = None, earned = [
                            Earning(money = 150, major = {Player.JOCHEM_17}, minor = {Player.SANNE_17, Player.THOMAS_17}),
                            Earning(money = 200, major = {Player.IMANUELLE_17}, minor = {Player.SANNE_17, Player.THOMAS_17}),
                            Earning(money = 50, major = {Player.DIEDERIK_17}, minor = {Player.SANNE_17, Player.THOMAS_17})
                        ])
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 2000, earned = [
                            Earning(money = 2000, major = {Player.DIEDERIK_17, Player.SANNE_17},
                                    minor = {Player.IMANUELLE_17, Player.JOCHEM_17, Player.THOMAS_17}),
                        ])
exercise6_3 = Exercise(episode = 6, alive = alive6, maximum = None, earned = [
                            Earning(money = 530, major = {Player.IMANUELLE_17}),
                            Earning(money = 100, major = {Player.THOMAS_17})
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €2500):
# Imanuelle (2x), Jochem (4x), Sanne (1x), Diederik (0x), Thomas (1x)
# €200 (Major: Imanuelle) (Minor: All), €400 (Major: Jochem) (Minor: All), €100 (Major: Sanne) (Minor: All),
# €100 (Major: Thomas) (Minor: All)
# Opdracht 2 (Maximaal €1500):
# €1500 (Major: Sanne) (Minor: Diederik, Imanuelle, Jochem, Thomas)
# Opdracht 3 (Maximaal €2500):
# €100 (Major: Diederik), €300 (Major: Jochem), €300 (Major: Imanuelle), €400 (Major: Sanne)
alive7 = {Player.DIEDERIK_17, Player.IMANUELLE_17, Player.JOCHEM_17, Player.SANNE_17, Player.THOMAS_17}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 2500, earned = [
                            Earning(money = 200, major = {Player.IMANUELLE_17}, minor = {Player.DIEDERIK_17,
                                Player.JOCHEM_17, Player.SANNE_17, Player.THOMAS_17}),
                            Earning(money = 400, major = {Player.JOCHEM_17}, minor = {Player.DIEDERIK_17,
                                Player.IMANUELLE_17, Player.SANNE_17, Player.THOMAS_17}),
                            Earning(money = 100, major = {Player.SANNE_17}, minor = {Player.DIEDERIK_17,
                                Player.IMANUELLE_17, Player.JOCHEM_17, Player.THOMAS_17}),
                            Earning(money = 100, major = {Player.THOMAS_17}, minor = {Player.DIEDERIK_17,
                                Player.IMANUELLE_17, Player.JOCHEM_17, Player.SANNE_17})
                        ])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [
                            Earning(money = 1500, major = {Player.SANNE_17}, minor = {Player.DIEDERIK_17,
                                Player.IMANUELLE_17, Player.JOCHEM_17, Player.THOMAS_17}),
                        ])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 2500, earned = [
                            Earning(money = 100, major = {Player.DIEDERIK_17}),
                            Earning(money = 300, major = {Player.JOCHEM_17}),
                            Earning(money = 300, major = {Player.IMANUELLE_17}),
                            Earning(money = 400, major = {Player.SANNE_17})
                        ])

# Aflevering 8
# Opdracht 1 (Maximaal €1000): Niks verdiend
# Opdracht 2 (Maximaal €?):
# €100 (Major: Thomas) (Minor: Diederik, Jochem), €100 (Major: Sanne) (Minor: Diederik, Jochem),
# €100 (Major: Thomas) (Minor: Diederik, Jochem), €100 (Major: Sanne) (Minor: Diederik, Jochem),
# €100 (Major: Thomas) (Minor: Diederik, Jochem), €100 (Major: Sanne) (Minor: Diederik, Jochem),
# €100 (Major: Sanne) (Minor: Diederik, Jochem), €100 (Major: Sanne) (Minor: Diederik, Jochem),
# €100 (Major: Sanne) (Minor: Diederik, Jochem),
# €100 (Major: Diederik) (Minor: Sanne, Thomas), €100 (Major: Diederik) (Minor: Sanne, Thomas),
# €100 (Major: Diederik) (Minor: Sanne, Thomas), €100 (Major: Diederik) (Minor: Sanne, Thomas),
# €100 (Major: Jochem) (Minor: Sanne, Thomas), €100 (Major: Diederik) (Minor: Sanne, Thomas),
# €100 (Major: Jochem) (Minor: Sanne, Thomas), €100 (Major: Diederik) (Minor: Sanne, Thomas)