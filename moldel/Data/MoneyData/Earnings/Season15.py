from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €2000): Niks verdiend
# Opdracht 2 (Maximaal €2000): Niks verdiend
alive1 = {Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15, Player.EVELIEN_15, Player.MARGRIET_15, Player.MARLIJN_15,
          Player.MARTINE_15, Player.PIETER_15, Player.RIK_15, Player.VIKTOR_15}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 2000, earned = [])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 2000, earned = [])

# Aflevering 2
# Opdracht 1 (Maximaal €2000):
# -€100 (Major: Chris), -€100 (Major: Marlijn), -€100 (Major: Viktor), -€100 (Major: Margriet), -€100 (Major: Marlijn),
# -€100 (Major: Evelien), -€100 (Major: Carolina), -€100 (Major: Chris), €900 (Minor: Allen)
# Opdracht 2 (Maximaal €1500):
# €500 (Major: Ajouad, Evelien) (Minor: Carolina), €500 (Major: Margriet, Rik) (Minor: Marlijn),
# €500 (Major: Chris, Viktor) (Minor: Martine)
# Opdracht 3 (Maximaal €1500): Gezamelijk verdiend
# Daarnaast: -€200 ingeleverd door Margriet
alive2 = {Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15, Player.EVELIEN_15, Player.MARGRIET_15, Player.MARLIJN_15,
          Player.MARTINE_15, Player.RIK_15, Player.VIKTOR_15}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [
                            Earning(money = 900, minor = {Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15,
                                Player.EVELIEN_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15,
                                Player.RIK_15, Player.VIKTOR_15}),
                            Earning(money = -200, major = {Player.CHRIS_15}),
                            Earning(money = -200, major = {Player.MARLIJN_15}),
                            Earning(money = -100, major = {Player.VIKTOR_15}),
                            Earning(money = -100, major = {Player.MARGRIET_15}),
                            Earning(money = -100, major = {Player.EVELIEN_15}),
                            Earning(money = -100, major = {Player.CAROLINA_15}),
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 1500, earned = [
                            Earning(money = 500, major = {Player.AJOUAD_15, Player.EVELIEN_15}, minor = {Player.CAROLINA_15}),
                            Earning(money = 500, major = {Player.MARGRIET_15, Player.RIK_15}, minor = {Player.MARLIJN_15}),
                            Earning(money = 500, major = {Player.CHRIS_15, Player.VIKTOR_15}, minor = {Player.MARTINE_15}),
                        ])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 1500, earned = [])
exercise2_4 = Exercise(episode = 2, alive = alive2, maximum = None, earned = [
                            Earning(money = -200, major = {Player.MARGRIET_15}),
                        ])

# Aflevering 3
# Opdracht 1 (Maximaal €3000):
# €100 (Major: Viktor)
# Opdracht 2 (Maximaal €?): Niks verdiend
alive3 = {Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15,
          Player.RIK_15, Player.VIKTOR_15}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 3000, earned = [
                            Earning(money = 100, major = {Player.VIKTOR_15})
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €1750):
# €250 (Major: Marlijn, Viktor), €250 (Major: Ajouad, Chris, Martine), €250 (Major: Chris, Margriet, Martine, Rik)
# Opdracht 2 (Maximaal €?):
# €500 (Major: Marlijn), €250 (Major: Chris)
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive4 = {Player.AJOUAD_15, Player.CAROLINA_15, Player.CHRIS_15, Player.MARGRIET_15, Player.MARLIJN_15, Player.MARTINE_15,
          Player.RIK_15, Player.VIKTOR_15}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 1750, earned = [
                            Earning(money = 250, major = {Player.MARLIJN_15, Player.VIKTOR_15}),
                            Earning(money = 250, major = {Player.AJOUAD_15, Player.CHRIS_15, Player.MARTINE_15}),
                            Earning(money = 250, major = {Player.CHRIS_15, Player.MARGRIET_15, Player.MARTINE_15,
                                Player.RIK_15})
                        ])
exercise4_2 = Exercise(episode = 4, alive = alive4, maximum = None, earned = [
                            Earning(money = 500, major = {Player.MARLIJN_15}),
                            Earning(money = 250, major = {Player.CHRIS_15})
                        ])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 2000, earned = [])

# Aflevering 5
# Opdracht 1 (Maximaal €?): Niks verdiend
# Opdracht 2 (Maximaal €?): Niks verdiend