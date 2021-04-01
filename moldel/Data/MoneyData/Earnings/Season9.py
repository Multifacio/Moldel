from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €5000): (Telt niet mee omdat de Mol nog niet gekozen was)
# €500 (Major: Dennis), -€500 (Major: Vivienne), €? (Major: Rick), €? (Major: Anniek), -€500 (Major: Sebastiaan),
# -€500 (Major: Vera), -€500 (Major: Jon), €? (Major: Paula), €? (Major: Hans), -€500 (Major: Froukje)
# 8x -€500 en 2x +€500
# Opdracht 2 (Maximaal €3000):
# €3000 (Major: Sebastiaan) (Minor: Allen)
# Opdracht 3 (Maximaal €0):
# -€1000 (Major: Dennis, Jon), -€1000 (Major: Paula, Rick)
alive1 = {Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.HANS_9, Player.JON_9, Player.PAULA_9,
          Player.RICK_9, Player.SEBASTIAAN_9, Player.VERA_9, Player.VIVIENNE_9}
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 3000, earned = [
                            Earning(money = 3000, major = {Player.SEBASTIAAN_9}, minor = {Player.ANNIEK_9,
                                Player.DENNIS_9, Player.FROUKJE_9, Player.HANS_9, Player.JON_9, Player.PAULA_9,
                                Player.RICK_9, Player.VERA_9, Player.VIVIENNE_9})
                        ])
exercise1_3 = Exercise(episode = 1, alive = alive1, maximum = None, earned = [
                            Earning(money = -1000, major = {Player.DENNIS_9, Player.JON_9}),
                            Earning(money = -1000, major = {Player.PAULA_9, Player.RICK_9})
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €10000):
# €2300 (Major: Anniek, Hans)
# Opdracht 2 (Maximaal €?): Te complex om te analyseren
# Opdracht 3 (Maximaal €2000):
# €500 (Major: Rick) (Minor: Anniek, Dennis) (Huisnummers), €500 (Major: Dennis) (Tattoo's)
alive2 = {Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.HANS_9, Player.JON_9, Player.PAULA_9,
          Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 10000, earned = [
                            Earning(money = 2300, major = {Player.ANNIEK_9, Player.HANS_9})
                        ])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [
                            Earning(money = 500, major = {Player.RICK_9}, minor = {Player.ANNIEK_9, Player.DENNIS_9}),
                            Earning(money = 500, major = {Player.DENNIS_9})
                        ])

# Aflevering 3
# Opdracht 1 (Maximaal €?): Niks verdiend
# Opdracht 2 (Maximaal €2500): Niks verdiend
# Opdracht 3 (Maximaal €6000):
# Team 1 (2x) (Rijder: Vivienne, Bijrijder: Hans, Coach: Rick)
# Team 2 (0.5x) (Rijder: Anniek, Bijrijder: Jon, Coach: Paula)
# Team 3 (1x) (Rijder: Froukje, Bijrijder: Sebastiaan, Coach: Dennis)
# €200 (Major: Froukje) (Minor: Dennis, Sebastiaan), €400 (Major: Vivienne) (Minor: Hans, Rick),
# €100 (Major: Anniek) (Minor: Jon, Paula), €2000 (Major: Vivienne) (Minor: Dennis, Hans, Jon, Rick),
# €200 (Major: Froukje) (Minor: Dennis, Sebastiaan), €100 (Major: Anniek) (Minor: Jon, Paula),
# €100 (Major: Anniek) (Minor: Jon, Paula), €100 (Major: Anniek) (Minor: Jon, Paula)
alive3 = {Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.HANS_9, Player.JON_9, Player.PAULA_9,
          Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9}
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 2500, earned = [])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 6000, earned = [
                            Earning(money = 400, major = {Player.FROUKJE_9}, minor = {Player.DENNIS_9, Player.SEBASTIAAN_9}),
                            Earning(money = 400, major = {Player.VIVIENNE_9}, minor = {Player.HANS_9, Player.RICK_9}),
                            Earning(money = 2000, major = {Player.VIVIENNE_9}, minor = {Player.DENNIS_9, Player.HANS_9,
                                Player.JON_9, Player.RICK_9}),
                            Earning(money = 400, major = {Player.ANNIEK_9}, minor = {Player.JON_9, Player.PAULA_9})
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €?):
# In totaal verdiend: €7000
# €4250 (Major: Sebastiaan, Vivienne), €2750 (Minor: Dennis, Froukje, Rick)
# Opdracht 2 (Maximaal €0):
# -€1500 (Major: Dennis, Froukje, Jon, Sebastiaan, Vivienne)
# Opdracht 3 (Maximaal €8000):
# -€500 (Major: Paula), -€1000 (Major: Sebastiaan), -€1000 (Major: Dennis), €200 (Major: Rick), €100 (Major: Jon),
# -€450 (Major: Vivienne)
# Opdracht 4 (Maximaal €2000):
# €250 (Major: Froukje), €250 (Major: Rick), €250 (Major: Sebastiaan)
alive4 = {Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9, Player.PAULA_9, Player.RICK_9,
          Player.SEBASTIAAN_9, Player.VIVIENNE_9}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = None, earned = [
                            Earning(money = 4250, major = {Player.SEBASTIAAN_9, Player.VIVIENNE_9}),
                            Earning(money = 2750, minor = {Player.DENNIS_9, Player.FROUKJE_9, Player.RICK_9})
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = None, earned = [
                            Earning(money = -1500, major = {Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9,
                                Player.SEBASTIAAN_9, Player.VIVIENNE_9})
                        ])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 8000, earned = [
                            Earning(money = -500, major = {Player.PAULA_9}),
                            Earning(money = -1000, major = {Player.SEBASTIAAN_9}),
                            Earning(money = -1000, major = {Player.DENNIS_9}),
                            Earning(money = 200, major = {Player.RICK_9}),
                            Earning(money = 100, major = {Player.JON_9}),
                            Earning(money = -450, major = {Player.VIVIENNE_9})
                        ])
exercise4_4 = Exercise(episode = 4, alive = alive4, maximum = 2000, earned = [
                            Earning(money = 250, major = {Player.FROUKJE_9}),
                            Earning(money = 250, major = {Player.RICK_9}),
                            Earning(money = 250, major = {Player.SEBASTIAAN_9})
                        ])

# Aflevering 5
# Opdracht 1 (Maximaal €?):
# €2500 (Major: Dennis) (Minor: Jon, Vivienne)
# Opdracht 2 (Maximaal €1750):
# Sebastiaan (Banaan) (Goed), Froukje (Munt) (Goed), Anniek (Appel) (Goed), Rick (Limoen) (Goed),
# Dennis (Sinaasappel) (Goed), Anniek (Watermeloen) (Goed), (Aardbeien) (Fout)
# €250 (Per correcte combinatie) (Minor: Allen)
# Opdracht 3 (Maximaal €?):
# In totaal verdiend: €1350
# 5 vragen goed beantwoord, €100 meegenomen onderweg
# Team met geld: Anniek, Jon, Sebastiaan
# Goede Vragen:
# (Major: Dennis) (Team van Vivienne), (Major: Anniek) (Team van Vivienne), (Major: Jon), (Major: Jon),
# (Major: Jon) (Team van Vivienne), (Major: Sebastiaan) (Team van Jon)
# Conclusie:
# €500 (Major: Jon), €250 (Major: Sebastiaan), €500 (Minor: Allen), €100 (Minor: Allen behalve Froukje)
alive5 = {Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9, Player.RICK_9, Player.SEBASTIAAN_9,
          Player.VIVIENNE_9}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = None, earned = [
                            Earning(money = 2500, major = {Player.DENNIS_9}, minor = {Player.JON_9, Player.VIVIENNE_9})
                        ])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = 1750, earned = [
                            Earning(money = 250, major = {Player.SEBASTIAAN_9}, minor = {Player.ANNIEK_9,
                                Player.DENNIS_9, Player.FROUKJE_9, Player.JON_9, Player.RICK_9, Player.VIVIENNE_9}),
                            Earning(money = 250, major = {Player.FROUKJE_9}, minor = {Player.ANNIEK_9,
                                Player.DENNIS_9, Player.JON_9, Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9}),
                            Earning(money = 500, major = {Player.ANNIEK_9}, minor = {Player.DENNIS_9, Player.FROUKJE_9,
                                Player.JON_9, Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9}),
                            Earning(money = 250, major = {Player.RICK_9}, minor = {Player.ANNIEK_9, Player.DENNIS_9,
                                Player.FROUKJE_9, Player.JON_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9}),
                            Earning(money = 250, major = {Player.DENNIS_9}, minor = {Player.ANNIEK_9, Player.FROUKJE_9,
                                Player.JON_9, Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9})
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = None, earned = [
                            Earning(money = 500, major = {Player.JON_9}),
                            Earning(money = 250, major = {Player.SEBASTIAAN_9}),
                            Earning(money = 500, minor = {Player.ANNIEK_9, Player.DENNIS_9, Player.FROUKJE_9,
                                Player.JON_9, Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9}),
                            Earning(money = 100, minor = {Player.ANNIEK_9, Player.DENNIS_9, Player.JON_9, Player.RICK_9,
                                Player.SEBASTIAAN_9, Player.VIVIENNE_9}),
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €0): Niks verdiend
# Opdracht 2 (Maximaal €1500):
# €250 (Major: Vivienne) (Minor: Sebastiaan), €250 (Major: Rick) (Minor: Dennis), €250 (Major: Anniek) (Minor: Jon, Rick),
# €250 (Major: Sebastiaan), €250 (Major: Dennis, Rick), €250 (Major: Jon) (Minor: Anniek, Rick)
# Opdracht 3 (Maximaal €?): Niks verdiend
alive6 = {Player.ANNIEK_9, Player.DENNIS_9, Player.JON_9, Player.RICK_9, Player.SEBASTIAAN_9, Player.VIVIENNE_9}
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 1500, earned = [
                            Earning(money = 250, major = {Player.VIVIENNE_9}, minor = {Player.SEBASTIAAN_9}),
                            Earning(money = 250, major = {Player.RICK_9}, minor = {Player.DENNIS_9}),
                            Earning(money = 250, major = {Player.ANNIEK_9}, minor = {Player.JON_9, Player.RICK_9}),
                            Earning(money = 250, major = {Player.SEBASTIAAN_9}),
                            Earning(money = 250, major = {Player.DENNIS_9, Player.RICK_9}),
                            Earning(money = 250, major = {Player.JON_9}, minor = {Player.ANNIEK_9, Player.RICK_9})
                        ])

# Aflevering 7
# Opdracht 1 (Maximaal €1200):
# €100 (Major: Jon) (Nederland), €100 (Major: Dennis) (Italië), €100 (Major: Rick) (Oostenrijk),
# €100 (Major: Vivienne) (Frankrijk), -€200 (Minor: Allen) (Belgie, Duitsland), €100 (Minor: Allen) (Griekenland)
# Opdracht 2 (Maximaal €2000): Gezamelijk verdiend
# Opdracht 3 (Maximaal €2500):
# €850 (Major: Vivienne) (Minor: Jon, Rick), €850 (Major: Jon, Vivienne) (Minor: Rick)
alive7 = {Player.ANNIEK_9, Player.DENNIS_9, Player.JON_9, Player.RICK_9, Player.VIVIENNE_9}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 1200, earned = [
                            Earning(money = 100, major = {Player.JON_9}),
                            Earning(money = 100, major = {Player.DENNIS_9}),
                            Earning(money = 100, major = {Player.RICK_9}),
                            Earning(money = 100, major = {Player.VIVIENNE_9}),
                            Earning(money = -100, minor = {Player.ANNIEK_9, Player.DENNIS_9, Player.JON_9,
                                                           Player.RICK_9, Player.VIVIENNE_9}),
                        ])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 2000, earned = [])
exercise7_3 = Exercise(episode = 7, alive = alive7, maximum = 2500, earned = [
                            Earning(money = 850, major = {Player.VIVIENNE_9}, minor = {Player.JON_9, Player.RICK_9}),
                            Earning(money = 850, major = {Player.JON_9, Player.VIVIENNE_9}, minor = {Player.RICK_9}),
                        ])

# Aflevering 8
# Opdracht 1 (Maximaal €1600):
# €100 (Major: Jon) (Minor: Dennis), €300 (Major: Vivienne) (Minor: Anniek, Dennis, Jon)
# Opdracht 2 (Maximaal €1000): Niks verdiend
# Opdracht 3 (Maximaal €0): Niks verdiend
alive8 = {Player.ANNIEK_9, Player.DENNIS_9, Player.JON_9, Player.VIVIENNE_9}
exercise8_1 = Exercise(episode = 8, alive = alive8, maximum = 1600, earned = [
                            Earning(money = 100, major = {Player.JON_9}, minor = {Player.DENNIS_9}),
                            Earning(money = 300, major = {Player.VIVIENNE_9}, minor = {Player.ANNIEK_9, Player.DENNIS_9,
                                Player.JON_9}),
                        ])
exercise8_2 = Exercise(episode = 8, alive = alive8, maximum = 1000, earned = [])

# Aflevering 9
# Opdracht 1 (Maximaal €?):
# €100 (Major: Vivienne) (Minor: Jon), -€100 (Major: Vivienne) (Minor: Jon)
# Opdracht 2 (Maximaal €850):
# €850 (Major: Vivienne) (Minor: Anniek, Jon)
# Opdracht 3 (Maximaal €?): Onduidelijk wie wat verdiend heeft
alive9 = {Player.ANNIEK_9, Player.JON_9, Player.VIVIENNE_9}
exercise9_2 = Exercise(episode = 9, alive = alive9, maximum = 850, earned = [
                            Earning(money = 850, major = {Player.VIVIENNE_9}, minor = {Player.ANNIEK_9, Player.JON_9})
                        ])

season9 = Season([exercise1_2, exercise1_3, exercise2_1, exercise2_3, exercise3_2, exercise3_3, exercise4_1,
                  exercise4_2, exercise4_3, exercise4_4, exercise5_1, exercise5_2, exercise5_3, exercise6_2,
                  exercise7_1, exercise7_2, exercise7_3, exercise8_1, exercise8_2, exercise9_2])