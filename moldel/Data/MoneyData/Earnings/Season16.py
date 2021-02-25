from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €1000): Gezamelijk verdiend
# Opdracht 2 (Maximaal €2000): Niks verdiend
alive1 = {Player.AIREN_16, Player.ANNEMIEKE_16, Player.CECILE_16, Player.ELLIE_16, Player.KLAAS_16, Player.MARJOLEIN_16,
          Player.REMY_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 1000, earned = [])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 2000, earned = [])

# Aflevering 2
# Opdracht 1 (Maximaal €2000): Niks verdiend
# Opdracht 2 (Maximaal €2000): 1e goed, 2e goed, 3e fout, 4e fout, 5e fout, 6e fout, 7e fout, 8e goed, 9e goed (All)
# €100 (Major: Airen, Cecile, Tim) (Minor: Marjolein), €100 (Major: Airen, Cecile, Tim) (Minor: Marjolein),
# €100 (Major: Klaas, Rop, Taeke) (Minor: Marjolein), €100 (Minor: Rest)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive2 = {Player.AIREN_16, Player.ANNEMIEKE_16, Player.CECILE_16, Player.ELLIE_16, Player.KLAAS_16, Player.MARJOLEIN_16,
          Player.REMY_16, Player.ROP_16, Player.TAEKE_16, Player.TIM_16}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [
                            Earning(money = 200, major = {Player.AIREN_16, Player.CECILE_16, Player.TIM_16},
                                    minor = {Player.MARJOLEIN_16}),
                            Earning(money = 100, major = {Player.KLAAS_16, Player.ROP_16, Player.TAEKE_16},
                                    minor = {Player.MARJOLEIN_16}),
                            Earning(money = 100, minor = {Player.AIREN_16, Player.ANNEMIEKE_16, Player.CECILE_16,
                                    Player.ELLIE_16, Player.KLAAS_16, Player.MARJOLEIN_16, Player.REMY_16, Player.ROP_16,
                                    Player.TAEKE_16, Player.TIM_16}),
                        ])

# Aflevering 3
# Opdracht 1 (Maximaal €1750):
# €500 (Major: Annemieke) (Minor: Taeke), €250 (Major: Klaas, Tim)
# Opdracht 2 (Maximaal €3000):
# €200 (Major: Klaas), €1000 (Major: Taeke), €400 (Major: Ellie, Remy), €100 (Major: Cecille)
# Opdracht 3 (Maximaal €0):
# -€2345 (Major: Annemieke, Cecile, Ellie, Klaas, Marjolein, Rop, Taeke, Tim)