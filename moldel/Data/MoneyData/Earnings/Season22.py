from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €2500): Niks verdiend
# Opdracht 2 (Maximaal €1500):
# €75 (Major: Charlotte) (Minor: Remco), €100 (Major: Joshua) (Minor: Marije),
# €125 (Major: Rocky) (Minor: Charlotte), €150 (Major: Splinter)
# Opdracht 3 (Maximaal €2000):
# €900 (Major: Florentijn, Remco) (Minor: Allen)
alive1 = {Player.CHARLOTTE_22, Player.ERIK_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.LAKSHMI_22,
          Player.MARIJE_22, Player.REMCO_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 2500, earned = [])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 1500, earned = [
                            Earning(money = 75, major = {Player.CHARLOTTE_22}, minor = {Player.REMCO_22}),
                            Earning(money = 100, major = {Player.JOSHUA_22}, minor = {Player.MARIJE_22}),
                            Earning(money = 125, major = {Player.ROCKY_22}, minor = {Player.CHARLOTTE_22}),
                            Earning(money = 150, major = {Player.SPLINTER_22})
                        ])
exercise1_3 = Exercise(episode = 1, alive = alive1, maximum = 2000, earned = [
                            Earning(money = 900, major = {Player.FLORENTIJN_22, Player.REMCO_22},
                                minor = {Player.CHARLOTTE_22, Player.ERIK_22, Player.JOSHUA_22, Player.LAKSHMI_22,
                                    Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22}),
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €2000):
# €700 (Major: Renée) (Minor: Erik, Lakschmi, Marije, Splinter)
# Opdracht 2 (Maximaal €2000):
# €400 (Major: Rocky)
# Opdracht 3 (Maximaal €2100):
# Goed bord: €350, Fout bord: -€350
# +/- €350 (Major: Lakshmi, Marije) (Minor: Florentijn, Joshua, Renée) (Rood, Losse Diagonaal, Rechtsbovenin Vierkant),
# +/- €350 (Major: Erik, Splinter) (Minor: Florentijn, Joshua, Renée) (Zwart, Vaste Diagonaal, Rechtsbovenin Bierkant),
# +/- €350 (Major: Erik, Splinter) (Minor: Florentijn, Joshua, Renée) (Groen, Vaste Diagonaal, Linksboven, Rechtsonder Vierkant)
# Groen, Losse Diagonaal, Linksboven Vierkantje = Joshua, Renée,
# Zwart, Vaste Diagonaal, Linksboven, Rechtsonder Vierkant = Charlotte, Rocky
# -€350 (Major: Erik, Splinter) (Minor: Marije) (Groen, Losse Diagonaal, Rechtsboven Vierkantje)
# +/- €350 (Major: Lakshmi, Marije) (Minor: Florentijn, Joshua, Renée, Splinter) (Zwart, Losse Diagonaal, Linksboven Vierkant),
# +/- €350 (Major: Erik, Splinter) (Minor: Florentijn, Joshua, Renée) (Groen, Losse Diagonaal, Linksboven Vierkantje)
# +/- €350 (Major: Lakshmi, Marije) (Minor: Charlotte, Florentijn, Rocky) (Zwart, Vaste Diagonaal, Linksboven, Rechtsonder Vierkant),
# +/- €350 (Major: Erik, Splinter) (Minor: Charlotte, Florentijn, Rocky) (Rood, Vaste Diagonaal, Rechtsboven Vierkantje)
# Resultaat: 5 Goede Borden en 3 Foute Borden, 2 doorgestuurd door Charlotte & Rocky, 5 doorgestuurd door Joshua & Renée
# 2 fouten moeten bij Joshua & Renée zitten omdat zij met het doorgeven van 5 borden minstens 2 fouten moeten hebben
# doorgegeven.
# Fout Ratio: 0/2 bij Charlotte & Rocky (€350 gemiddeld), 2/5 bij Joshua, Renée (€70 gemiddeld)
# €700 verdiend in totaal
# Inschatting:
# €70 (Major: Lakshmi, Marije) (Minor: Florentijn, Joshua, Renée)
# €70 (Major: Erik, Splinter) (Minor: Florentijn, Joshua, Renée)
# €70 (Major: Erik, Splinter) (Minor: Florentijn, Joshua, Renée)
# -€350 (Major: Erik, Splinter) (Minor: Marije)
# €70 (Major: Lakshmi, Marije) (Minor: Florentijn, Joshua, Renée, Splinter)
# €70 (Major: Erik, Splinter) (Minor: Florentijn, Joshua, Renée)
# €350 (Major: Lakshmi, Marije) (Minor: Charlotte, Florentijn, Rocky)
# €350 (Major: Erik, Splinter) (Minor: Charlotte, Florentijn, Rocky)
alive2 = {Player.CHARLOTTE_22, Player.ERIK_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.LAKSHMI_22,
          Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [
                            Earning(money = 700, major = {Player.RENEE_22}, minor = {Player.ERIK_22, Player.LAKSHMI_22,
                                Player.MARIJE_22, Player.SPLINTER_22}),
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [
                            Earning(money = 400, major = {Player.ROCKY_22}),
                        ])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 2100, earned = [
                            Earning(money = 70, major = {Player.LAKSHMI_22, Player.MARIJE_22},
                                minor = {Player.FLORENTIJN_22, Player.JOSHUA_22, Player.RENEE_22}),
                            Earning(money = 210, major = {Player.ERIK_22, Player.SPLINTER_22},
                                minor = {Player.FLORENTIJN_22, Player.JOSHUA_22, Player.RENEE_22}),
                            Earning(money = -350, major = {Player.ERIK_22, Player.SPLINTER_22},
                                minor = {Player.MARIJE_22}),
                            Earning(money = 70, major = {Player.LAKSHMI_22, Player.MARIJE_22},
                                minor = {Player.FLORENTIJN_22, Player.JOSHUA_22, Player.RENEE_22, Player.SPLINTER_22}),
                            Earning(money = 350, major = {Player.LAKSHMI_22, Player.MARIJE_22},
                                minor = {Player.CHARLOTTE_22, Player.FLORENTIJN_22, Player.ROCKY_22}),
                            Earning(money = 350, major = {Player.ERIK_22, Player.SPLINTER_22},
                                minor = {Player.CHARLOTTE_22, Player.FLORENTIJN_22, Player.ROCKY_22}),
                        ])

# Aflevering 3
# Opdracht 1 (Maximaal €2000):
# €500 (Major: Charlotte) (Minor: Renée), €500 (Major: Joshua) (Minor: Marije)
# Opdracht 2 (Maximaal €2000):
# €500 (Major: Rocky) (Minor: Renée), €500 (Major: Rocky) (Minor: Charlotte, Splinter),
# €500 (Major: Rocky) (Minor: Joshua, Florentijn), €500 (Major: Rocky) (Minor: Lakshmi, Marije)
alive3 = {Player.CHARLOTTE_22, Player.FLORENTIJN_22, Player.JOSHUA_22, Player.LAKSHMI_22, Player.MARIJE_22,
          Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [
                            Earning(money = 500, major = {Player.CHARLOTTE_22}, minor = {Player.RENEE_22}),
                            Earning(money = 500, major = {Player.JOSHUA_22}, minor = {Player.MARIJE_22})
                        ])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [
                            Earning(money = 500, major = {Player.ROCKY_22}, minor = {Player.RENEE_22}),
                            Earning(money = 500, major = {Player.ROCKY_22}, minor = {Player.CHARLOTTE_22, Player.SPLINTER_22}),
                            Earning(money = 500, major = {Player.ROCKY_22}, minor = {Player.JOSHUA_22, Player.FLORENTIJN_22}),
                            Earning(money = 500, major = {Player.ROCKY_22}, minor = {Player.LAKSHMI_22, Player.MARIJE_22}),
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €2250):
# Elk goed antwoord: €5, Complete vraag goed: €50
# €10 (Major: Joshua) (Minor: Rocky), €65 (Major: Charlotte) (Minor: Rocky), €65 (Major: Renée) (Minor: Lakshmi),
# €10 (Major: Marije) (Minor: Splinter), €65 (Major: Joshua) (Minor: Lakshmi), €65 (Major: Charlotte) (Minor: Rocky),
# €10 (Major: Renée) (Minor: Splinter), €75 (Major: Marije) (Minor: Rocky), €5 (Major: Joshua) (Minor: Lakshmi),
# €10 (Major: Charlotte) (Minor: Lakshmi), €15 (Major: Joshua) (Minor: Splinter), €10 (Major: Charlotte) (Minor: Splinter),
# €15 (Major: Renée) (Minor: Lakshmi), €65 (Major: Marije) (Minor: Rocky), €65 (Major: Charlotte) (Minor: Lakshmi),
# €10 (Major: Renée) (Minor: Rocky), €65 (Major: Marije) (Minor: Lakshmi), €10 (Major: Joshua) (Minor: Splinter),
# €5 (Major: Marije) (Minor: Rocky), €5 (Major: Renée) (Minor: Splinter), €10 (Major: Marije) (Minor: Lakshmi),
# €10 (Major: Joshua) (Minor: Rocky), €10 (Major: Charlotte) (Minor: Splinter), €10 (Major: Joshua) (Minor: Lakshmi),
# €15 (Major: Marije) (Minor: Lakshmi), €10 (Major: Joshua) (Minor: Rocky), €10 (Major: Charlotte) (Minor: Splinter)
# In totaal verdiend: €1155, te linken daarvan €720.
# Groepeerd:
# €75 (Major: Charlotte) (Minor: Lakshmi), €130 (Major: Charlotte) (Minor: Rocky), €30 (Major: Charlotte) (Minor: Splinter),
# €80 (Major: Joshua) (Minor: Lakshmi), €30 (Major: Joshua) (Minor: Rocky), €25 (Major: Joshua) (Minor: Splinter),
# €90 (Major: Marije) (Minor: Lakshmi), €145 (Major: Marije) (Minor: Rocky), €10 (Major: Marije) (Minor: Splinter),
# €80 (Major: Renée) (Minor: Lakshmi), €10 (Major: Renée) (Minor: Rocky), €15 (Major: Renée) (Minor: Splinter)
# €435 (Major: Charlotte, Joshua, Marije, Renée) (Minor: Lakshmi, Rocky, Splinter)
#
# Opdracht 2 (Maximaal €1400):
# €200 (Major: Marije) (Minor: Joshua), €150 (Major: Marije) (Minor: Joshua),
# €150 (Major: Charlotte) (Minor: Lakshmi, Splinter), €150 (Major: Charlotte, Marije) (Minor: Joshua, Renée),
# €200 (Major: Charlotte) (Minor: Renée), €150 (Major: Marije) (Minor: Renée), €200 (Major: Charlotte, Marije)
# Opdracht 3 (Maximaal €2000):
# €2000 (Major: Joshua, Marije) (Minor: Charlotte, Lakshmi, Renée, Rocky, Splinter)
alive4 = {Player.CHARLOTTE_22, Player.JOSHUA_22, Player.LAKSHMI_22, Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22,
          Player.SPLINTER_22}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 2250, earned = [
                            Earning(money = 75, major = {Player.CHARLOTTE_22}, minor = {Player.LAKSHMI_22}),
                            Earning(money = 130, major = {Player.CHARLOTTE_22}, minor = {Player.ROCKY_22}),
                            Earning(money = 30, major = {Player.CHARLOTTE_22}, minor = {Player.SPLINTER_22}),
                            Earning(money = 80, major = {Player.JOSHUA_22}, minor = {Player.LAKSHMI_22}),
                            Earning(money = 30, major = {Player.JOSHUA_22}, minor = {Player.ROCKY_22}),
                            Earning(money = 25, major = {Player.JOSHUA_22}, minor = {Player.SPLINTER_22}),
                            Earning(money = 90, major = {Player.MARIJE_22}, minor = {Player.LAKSHMI_22}),
                            Earning(money = 145, major = {Player.MARIJE_22}, minor = {Player.ROCKY_22}),
                            Earning(money = 10, major = {Player.MARIJE_22}, minor = {Player.SPLINTER_22}),
                            Earning(money = 80, major = {Player.RENEE_22}, minor = {Player.LAKSHMI_22}),
                            Earning(money = 10, major = {Player.RENEE_22}, minor = {Player.ROCKY_22}),
                            Earning(money = 15, major = {Player.RENEE_22}, minor = {Player.SPLINTER_22}),
                            Earning(money = 435, major = {Player.CHARLOTTE_22, Player.JOSHUA_22, Player.MARIJE_22,
                                Player.RENEE_22}, minor = {Player.LAKSHMI_22, Player.ROCKY_22, Player.SPLINTER_22}),
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = 1400, earned = [
                            Earning(money = 200, major = {Player.MARIJE_22}, minor = {Player.JOSHUA_22}),
                            Earning(money = 150, major = {Player.MARIJE_22}, minor = {Player.JOSHUA_22}),
                            Earning(money = 150, major = {Player.CHARLOTTE_22}, minor = {Player.LAKSHMI_22,
                                Player.SPLINTER_22}),
                            Earning(money = 150, major = {Player.CHARLOTTE_22, Player.MARIJE_22},
                                minor = {Player.JOSHUA_22, Player.RENEE_22}),
                            Earning(money = 200, major = {Player.CHARLOTTE_22}, minor = {Player.RENEE_22}),
                            Earning(money = 150, major = {Player.MARIJE_22}, minor = {Player.RENEE_22}),
                            Earning(money = 200, major = {Player.CHARLOTTE_22, Player.MARIJE_22})
                        ])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 2000, earned = [
                            Earning(money = 2000, major = {Player.JOSHUA_22, Player.MARIJE_22},
                                minor = {Player.CHARLOTTE_22, Player.LAKSHMI_22, Player.RENEE_22, Player.ROCKY_22,
                                    Player.SPLINTER_22})
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €1900): Niks verdiend
# Opdracht 2 (Maximaal €0):
# -€5000 (Major: Charlotte, Marije, Rocky)
# Opdracht 3 (Maximaal €1800):
# €850 (Major: Marije) (Minor: Charlotte, Rocky)
alive5 = {Player.CHARLOTTE_22, Player.JOSHUA_22, Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 1900, earned = [])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = None, earned = [
                            Earning(money = -5000, major = {Player.CHARLOTTE_22, Player.MARIJE_22, Player.ROCKY_22})
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 1800, earned = [
                            Earning(money = 850, major = {Player.MARIJE_22}, minor = {Player.CHARLOTTE_22, Player.ROCKY_22})
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €1750):
# €250 (Major: Renée), -€350 (Major: Marije), €250 (Major: Splinter), -€250 (Major: Renée), €250 (Major: Charlotte),
# €250 (Major: Renée), €250 (Major: Rocky)
# Opdracht 2 (Maximaal €1500): Niks verdiend
# Opdracht 3 (Maximaal €2000):
# €500 (Major: Renée), €250 (Major: Rocky)
alive6 = {Player.CHARLOTTE_22, Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22}
exercise6_1 = Exercise(episode = 6, alive = alive6, maximum = 1750, earned = [
                            Earning(money = 250, major = {Player.RENEE_22}),
                            Earning(money = -350, major = {Player.MARIJE_22}),
                            Earning(money = 250, major = {Player.SPLINTER_22}),
                            Earning(money = 250, major = {Player.CHARLOTTE_22}),
                            Earning(money = 250, major = {Player.ROCKY_22})
                        ])
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 1500, earned = [])
exercise6_3 = Exercise(episode = 6, alive = alive6, maximum = 2000, earned = [
                            Earning(money = 500, major = {Player.RENEE_22}),
                            Earning(money = 250, major = {Player.ROCKY_22})
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €1750): Onduidelijk wie wat verdiend heeft
# Opdracht 2 (Maximaal €1500):
# €150 (Major: Charlotte) (Minor: Marije, Renée, Rocky, Splinter)
# Opdracht 3 (Maximaal €2000):
# €100 (Major: Charlotte) (Minor: Marije, Rocky, Splinter), €100 (Major: Charlotte) (Minor: Marije, Rocky, Splinter),
# €100 (Major: Charlotte) (Minor: Marije, Rocky, Splinter), €100 (Major: Marije) (Minor: Charlotte, Rocky, Splinter),
# €100 (Major: Marije) (Minor: Charlotte, Rocky, Splinter), €100 (Major: Marije, Renée) (Minor: Charlotte, Rocky, Splinter),
# €100 (Major: Splinter) (Minor: Charlotte, Renée, Rocky), €100 (Major: Marije) (Minor: Charlotte, Renée, Rocky),
# €100 (Major: Splinter) (Minor: Charlotte, Renée, Rocky), €100 (Major: Marije) (Minor: Charlotte, Renée, Rocky),
# €100 (Major: Marije) (Minor: Charlotte, Renée, Rocky), €100 (Major: Splinter) (Minor: Charlotte, Marije, Renée),
# €100 (Major: Splinter) (Minor: Charlotte, Marije, Renée)
# 8 liedjes goed gerekend, dus 8/13 ratio
alive7 = {Player.CHARLOTTE_22, Player.MARIJE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 1750, earned = [])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 1500, earned = [
                            Earning(money = 150, major = {Player.CHARLOTTE_22}, minor = {Player.MARIJE_22,
                                Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22}),
                        ])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 2000, earned = [
                            Earning(money = 300 * 8/13, major = {Player.CHARLOTTE_22}, minor = {Player.MARIJE_22,
                                Player.ROCKY_22, Player.SPLINTER_22}),
                            Earning(money = 200 * 8/13, major = {Player.MARIJE_22}, minor = {Player.CHARLOTTE_22,
                                Player.ROCKY_22, Player.SPLINTER_22}),
                            Earning(money = 100 * 8/13, major = {Player.MARIJE_22, Player.RENEE_22},
                                minor = {Player.CHARLOTTE_22, Player.ROCKY_22, Player.SPLINTER_22}),
                            Earning(money = 200 * 8/13, major = {Player.SPLINTER_22},
                                minor = {Player.CHARLOTTE_22, Player.RENEE_22, Player.ROCKY_22}),
                            Earning(money = 300 * 8/13, major = {Player.MARIJE_22},
                                minor = {Player.CHARLOTTE_22, Player.RENEE_22, Player.ROCKY_22}),
                            Earning(money = 200 * 8/13, major = {Player.SPLINTER_22},
                                minor = {Player.CHARLOTTE_22, Player.MARIJE_22, Player.RENEE_22}),
                        ])

# Aflevering 8
# Opdracht 1 (Maximaal €1500): Niks verdiend
# Opdracht 2 (Maximaal €1500):
# €225 (Major: Splinter) (Minor: Charlotte, Renée, Rocky), €225 (Major: Charlotte) (Minor: Renée, Rocky, Splinter),
# €225 (Major: Charlotte) (Minor: Renée, Rocky, Splinter), €225 (Minor: Charlotte, Renée, Rocky, Splinter)
# Goed: Dames in het rood, meisjes met rode haren, hoofddeksels, bloemen in het haar
# Opdracht 3 (Maximaal €8000):
# -€2000 (Major: Charlotte) (Minor: Splinter)
alive8 = {Player.CHARLOTTE_22, Player.RENEE_22, Player.ROCKY_22, Player.SPLINTER_22}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 1500, earned = [])
exercise8_2 = Exercise(episode = 8, alive = alive8, maximum = 1500, earned = [
                            Earning(money = 225, major = {Player.SPLINTER_22}, minor = {Player.CHARLOTTE_22,
                                Player.RENEE_22, Player.ROCKY_22}),
                            Earning(money = 450, major = {Player.CHARLOTTE_22}, minor = {Player.RENEE_22,
                                Player.ROCKY_22, Player.SPLINTER_22}),
                            Earning(money = 225, minor = {Player.CHARLOTTE_22, Player.RENEE_22, Player.ROCKY_22,
                                Player.SPLINTER_22}),
                        ])
exercise8_3 = Exercise(episode = 8, alive = alive8, maximum = 8000, earned = [
                            Earning(money = -2000, major = {Player.CHARLOTTE_22}, minor = {Player.SPLINTER_22})
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €1750):
# €150 (Major: Rocky), -€100 (Major: Charlotte), -€100 (Major: Renée), -€100 (Major: Rocky), €300 (Major: Charlotte),
# €200 (Major: Rocky), €200 (Major: Renée), €300 (Major: Charlotte) (Minor: Renée, Rocky), €100 (Major: Charlotte),
# €100 (Minor: Allen)
# Opdracht 2 (Maximaal €?): Onduidelijk wie wat verdiend heeft
alive9 = {Player.CHARLOTTE_22, Player.RENEE_22, Player.ROCKY_22}
exercise9_1 = Exercise(episode = 9, alive = alive9, maximum = 1750, earned = [
                            Earning(money = 300, major = {Player.CHARLOTTE_22}),
                            Earning(money = 100, major = {Player.RENEE_22}),
                            Earning(money = 250, major = {Player.ROCKY_22}),
                            Earning(money = 300, major = {Player.CHARLOTTE_22}, minor = {Player.RENEE_22,
                                Player.ROCKY_22}),
                            Earning(money = 100, minor = {Player.CHARLOTTE_22, Player.RENEE_22, Player.ROCKY_22}),
                        ])

season22 = Season([exercise1_1, exercise1_2, exercise1_3, exercise2_1, exercise2_2, exercise2_3, exercise3_1,
                   exercise3_2, exercise4_1, exercise4_2, exercise4_3, exercise5_1, exercise5_2, exercise5_3,
                   exercise6_1, exercise6_2, exercise6_3, exercise7_1, exercise7_2, exercise7_3, exercise8_1,
                   exercise8_2, exercise8_3, exercise9_1])