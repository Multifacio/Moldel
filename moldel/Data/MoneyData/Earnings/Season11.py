from Data.MoneyData.Dataclasses.Season import Season
from Data.MoneyData.Dataclasses.Exercise import Exercise
from Data.MoneyData.Dataclasses.Earning import Earning
from Data.Player import Player

# Aflevering 1
# Opdracht 1 (Maximaal €5000): Niks verdiend
# €10 (Major: Miryanna), €20 (Major: Jan) (Minor: Miryanna), €30 (Major: Hanna) (Minor: Jan, Miryanna),
# €40 (Major: Horace) (Minor: Jan, Miryanna, Hanna)
# Opdracht 2 (Maximaal €2500): Niks verdiend
# Opdracht 3 (Maximaal €10000):
# €3000 (Major: Karin), €3000 (Major: Miryanna)
alive1 = {Player.ANNA_11, Player.ART_11, Player.HANNA_11, Player.HORACE_11, Player.JAN_11, Player.KARIN_11,
          Player.MIRYANNA_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11}
exercise1_1 = Exercise(episode = 1, alive = alive1, maximum = 5000, earned = [
                            Earning(money = 10, major = {Player.MIRYANNA_11}),
                            Earning(money = 20, major = {Player.JAN_11}, minor = {Player.MIRYANNA_11}),
                            Earning(money = 30, major = {Player.HANNA_11}, minor = {Player.JAN_11, Player.MIRYANNA_11}),
                            Earning(money = 40, major = {Player.HORACE_11}, minor = {Player.HANNA_11, Player.JAN_11,
                                Player.MIRYANNA_11})
                        ])
exercise1_2 = Exercise(episode = 1, alive = alive1, maximum = 2500, earned = [])
exercise1_3 = Exercise(episode = 1, alive = alive1, maximum = 10000, earned = [
                            Earning(money = 3000, major = {Player.KARIN_11}),
                            Earning(money = 3000, major = {Player.MIRYANNA_11})
                        ])

# Aflevering 2
# Opdracht 1 (Maximaal €2500):
# €250 (Minor: Karin), €250 (Minor: Miryanna), €250 (Minor: Pepijn), €250 (Minor: Anna), €250 (Minor: Jan),
# €250 (Minor: Soundos)
# Opdracht 2 (Maximaal €2500):
# €1500 (Major: Jan) (Minor: Karin, Patrick, Miryanna, Hanna, Soundos, Horace, Anna, Art)
# Opdracht 3 (Maximaal €2000): Niks verdiend
alive2 = {Player.ANNA_11, Player.ART_11, Player.HANNA_11, Player.HORACE_11, Player.JAN_11, Player.KARIN_11,
          Player.MIRYANNA_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11}
exercise2_1 = Exercise(episode = 2, alive = alive2, maximum = 2500, earned = [
                            Earning(money = 250, minor = {Player.KARIN_11}),
                            Earning(money = 250, minor = {Player.MIRYANNA_11}),
                            Earning(money = 250, minor = {Player.PEPIJN_11}),
                            Earning(money = 250, minor = {Player.ANNA_11}),
                            Earning(money = 250, minor = {Player.JAN_11}),
                            Earning(money = 250, minor = {Player.SOUNDOS_11}),
                        ])
exercise2_2 = Exercise(episode = 2, alive = alive2, maximum = 2500, earned = [
                            Earning(money = 1500, major = {Player.JAN_11}, minor = {Player.ANNA_11, Player.ART_11,
                                Player.HANNA_11, Player.HORACE_11, Player.KARIN_11, Player.MIRYANNA_11,
                                Player.PATRICK_11, Player.SOUNDOS_11})
                        ])
exercise2_3 = Exercise(episode = 2, alive = alive2, maximum = 2000, earned = [])

# Aflevering 3
# Opdracht 1 (Maximaal €2000):
# €1000 (Major: Miryanna) (Minor: Jan, Karin, Pepijn)
# Opdracht 2 (Maximaal €2500): Gezamelijk verdiend
# Opdracht 3 (Maximaal €1000):
# -€500 (Major: Patrick) (Minor: Horace), -€500 (Major: Art) (Minor: Horace), -€500 (Major: Pepijn) (Minor: Horace),
# -€500 (Major: Jan) (Minor: Horace)
alive3 = {Player.ANNA_11, Player.ART_11, Player.HORACE_11, Player.JAN_11, Player.KARIN_11, Player.MIRYANNA_11,
          Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11}
exercise3_1 = Exercise(episode = 3, alive = alive3, maximum = 2000, earned = [
                            Earning(money = 1000, major = {Player.MIRYANNA_11}, minor = {Player.JAN_11, Player.KARIN_11,
                                Player.PEPIJN_11}),
                        ])
exercise3_2 = Exercise(episode = 3, alive = alive3, maximum = 2500, earned = [])
exercise3_3 = Exercise(episode = 3, alive = alive3, maximum = 1000, earned = [
                            Earning(money = -500, major = {Player.PATRICK_11}, minor = {Player.HORACE_11}),
                            Earning(money = -500, major = {Player.ART_11}, minor = {Player.HORACE_11}),
                            Earning(money = -500, major = {Player.PEPIJN_11}, minor = {Player.HORACE_11}),
                            Earning(money = -500, major = {Player.JAN_11}, minor = {Player.HORACE_11})
                        ])

# Aflevering 4
# Opdracht 1 (Maximaal €3000): Onduidelijk wie wat verdiend heeft
# Opdracht 2 (Maximaal €0): Niks verdiend
# Opdracht 3 (Maximaal €2500): Niks verdiend
alive4 = {Player.ANNA_11, Player.ART_11, Player.JAN_11, Player.KARIN_11, Player.MIRYANNA_11, Player.PATRICK_11,
          Player.PEPIJN_11, Player.SOUNDOS_11}
exercise4_1 = Exercise(episode = 4, alive = alive4, maximum = 3000, earned = [])
exercise4_3 = Exercise(episode = 4, alive = alive4, maximum = 2500, earned = [])

# Aflevering 5
# Opdracht 1 (Maximaal €2500):
# Groep 1: Art, Jan, Patrick; Groep 2: Anna, Karin, Pepijn, Soundos (Geen paard gereden);
# €250 (Major: Anna) (Minor: Art, Jan, Karin, Patrick), €250 (Major: Anna) (Minor: Art, Jan, Patrick),
# €250 (Major: Anna) (Minor: Art, Jan, Patrick)
# Opdracht 2 (Maximaal €1500):
# €250 (Major: Anna) (Minor: Jan, Karin), €250 (Major: Anna) (Minor: Pepijn, Soundos)
# Opdracht 3 (Maximaal €3000):
# Chauffeurs: Anna, Art, Jan, Pepijn
# €250 (Major: Patrick) (Minor: Anna, Art, Jan, Pepijn), €250 (Major: Pepijn) (Minor: Anna, Art, Jan, Patrick),
# €250 (Major: Anna) (Minor: Art, Jan, Patrick, Pepijn), €250 (Major: Pepijn) (Minor: Anna, Art, Jan, Soundos),
# €250 (Major: Jan) (Minor: Anna, Art, Pepijn), €250 (Major: Patrick) (Minor: Anna, Art, Jan, Pepijn),
# €1500 (Major: Patrick) (Minor: Anna, Art, Jan, Pepijn, Soundos)
alive5 = {Player.ANNA_11, Player.ART_11, Player.JAN_11, Player.KARIN_11, Player.PATRICK_11, Player.PEPIJN_11,
          Player.SOUNDOS_11}
exercise5_1 = Exercise(episode = 5, alive = alive5, maximum = 2500, earned = [
                            Earning(money = 250, major = {Player.ANNA_11}, minor = {Player.ART_11, Player.JAN_11,
                                Player.KARIN_11, Player.PATRICK_11}),
                            Earning(money = 500, major = {Player.ANNA_11}, minor = {Player.ART_11, Player.JAN_11,
                                Player.PATRICK_11})
                        ])
exercise5_2 = Exercise(episode = 5, alive = alive5, maximum = 1500, earned = [
                            Earning(money = 250, major = {Player.ANNA_11}, minor = {Player.JAN_11, Player.KARIN_11}),
                            Earning(money = 250, major = {Player.ANNA_11}, minor = {Player.PEPIJN_11, Player.SOUNDOS_11})
                        ])
exercise5_3 = Exercise(episode = 5, alive = alive5, maximum = 3000, earned = [
                            Earning(money = 500, major = {Player.PATRICK_11}, minor = {Player.ANNA_11, Player.ART_11,
                                Player.JAN_11, Player.PEPIJN_11}),
                            Earning(money = 250, major = {Player.PEPIJN_11}, minor = {Player.ANNA_11, Player.ART_11,
                                Player.JAN_11, Player.PATRICK_11}),
                            Earning(money = 250, major = {Player.ANNA_11}, minor = {Player.ART_11, Player.JAN_11,
                                Player.PATRICK_11, Player.PEPIJN_11}),
                            Earning(money = 250, major = {Player.PEPIJN_11}, minor = {Player.ANNA_11, Player.ART_11,
                                Player.JAN_11, Player.SOUNDOS_11}),
                            Earning(money = 250, major = {Player.JAN_11}, minor = {Player.ANNA_11, Player.ART_11,
                                Player.PEPIJN_11}),
                            Earning(money = 1500, major = {Player.PATRICK_11}, minor = {Player.ANNA_11, Player.ART_11,
                                Player.JAN_11, Player.PEPIJN_11, Player.SOUNDOS_11}),
                        ])

# Aflevering 6
# Opdracht 1 (Maximaal €?): Niks verdiend
# Opdracht 2 (Maximaal €2500): Gezamelijk verdiend
# Opdracht 3 (Maximaal €0): Niks verdiend
alive6 = {Player.ANNA_11, Player.ART_11, Player.KARIN_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11}
exercise6_2 = Exercise(episode = 6, alive = alive6, maximum = 2500, earned = [])

# Aflevering 7
# Opdracht 1 (Maximaal €1700):
# Zichtbaar: Soundos (1 koker), Pepijn (1 koker), Art (1 koker), Soundos (1 koker), Anna (1 koker)
# €100 per koker, 4 extra kokers gevonden zonder
# Inschatting: Pepijn (2 kokers), Anna (2 kokers), Art (1 koker), Patrick (2 kokers), Soundos (2 kokers)
# Opdracht 2 (Maximaal €2400):
# Kistdragers: Anna, Art, Patrick, Pepijn
# Geld op tijd in kist: Anna, Art, Karin, Patrick, Pepijn
# €200 (Major: Anna) (Minor: Art, Patrick, Pepijn), €200 (Major: Art) (Minor: Anna, Patrick, Pepijn),
# €200 (Major: Karin) (Minor: Anna, Art, Patrick, Pepijn), €200 (Major: Patrick) (Minor: Anna, Art, Pepijn),
# €200 (Major: Pepijn) (Minor: Anna, Art, Patrick)
# Opdracht 3 (Maximaal €0): Niks verdiend
alive7 = {Player.ANNA_11, Player.ART_11, Player.KARIN_11, Player.PATRICK_11, Player.PEPIJN_11, Player.SOUNDOS_11}
exercise7_1 = Exercise(episode = 7, alive = alive7, maximum = 1700, earned = [
                            Earning(money = 200, major = {Player.PEPIJN_11}),
                            Earning(money = 200, major = {Player.ANNA_11}),
                            Earning(money = 100, major = {Player.ART_11}),
                            Earning(money = 200, major = {Player.PATRICK_11}),
                            Earning(money = 200, major = {Player.SOUNDOS_11})
                        ])
exercise7_2 = Exercise(episode = 7, alive = alive7, maximum = 2400, earned = [
                            Earning(money = 200, major = {Player.ANNA_11}, minor = {Player.ART_11, Player.PATRICK_11,
                                Player.PEPIJN_11}),
                            Earning(money = 200, major = {Player.ART_11}, minor = {Player.ANNA_11, Player.PATRICK_11,
                                Player.PEPIJN_11}),
                            Earning(money = 200, major = {Player.KARIN_11}, minor = {Player.ANNA_11, Player.ART_11,
                                Player.PATRICK_11, Player.PEPIJN_11}),
                            Earning(money = 200, major = {Player.PATRICK_11}, minor = {Player.ANNA_11, Player.ART_11,
                                Player.PEPIJN_11}),
                            Earning(money = 200, major = {Player.PEPIJN_11}, minor = {Player.ANNA_11, Player.ART_11,
                                Player.PATRICK_11}),
                       ])

# Aflevering 8
# Opdracht 1 (Maximaal €?): Niks verdiend
# Opdracht 2 (Maximaal €1500):
# €200 (Major: Anna), €100 (Major: Anna), €50 (Major: Art), €? (Major: Anna), €50 (Major: Art), €100 (Major: Anna),
# €50 (Major: Soundos), €50 (Major: Patrick), €? (Major: Karin)
# Inschatting: €400 (Major: Anna), €200 (Major: Soundos), €100 (Major: Art), €100 (Major: Karin), €50 (Major: Patrick)
# Opdracht 3 (Maximaal €1800):
# €200 (Major: Soundos) (Minor: Art), €200 (Major: Anna) (Minor: Karin, Patrick)
alive8 = {Player.ANNA_11, Player.ART_11, Player.KARIN_11, Player.PATRICK_11, Player.SOUNDOS_11}
exercise8_2 = Exercise(episode = 8, alive = alive8, maximum = 1500, earned = [
                            Earning(money = 400, major = {Player.ANNA_11}),
                            Earning(money = 200, major = {Player.SOUNDOS_11}),
                            Earning(money = 100, major = {Player.ART_11}),
                            Earning(money = 100, major = {Player.KARIN_11}),
                            Earning(money = 50, major = {Player.PATRICK_11})
                        ])
exercise8_3 = Exercise(episode = 8, alive = alive8, maximum = 1800, earned = [
                            Earning(money = 200, major = {Player.SOUNDOS_11}, minor = {Player.ART_11}),
                            Earning(money = 200, major = {Player.ANNA_11}, minor = {Player.KARIN_11, Player.PATRICK_11})
                        ])

# Aflevering 9
# Opdracht 1 (Maximaal €?):
# €700 (Soundos, Karin) (England, Costa Rica, Duitsland, Ierland, Oostenrijk, Frankrijk, El Salvador)
# Ierland (Major: Karin) (Minor: Soundos), Frankrijk (Major: Karin) (Minor: Soundos),
# El Salvador (Major: Karin) (Minor: Soundos), Oostenrijk (Major: Karin) (Minor: Soundos),
# Duitsland (Major: Karin) (Minor: Soundos), Costa Rica (Major: Karin) (Minor: Soundos),
# England (Major: Karin) (Minor: Soundos)
# Opdracht 2 (Maximaal €2500): Niks verdiend
# Opdracht 3 (Maximaal €2000):
# €200 (Major: Soundos) (Minor: Karin, Patrick), €200 (Major: Art) (Minor: Karin, Patrick),
# €200 (Major: Karin) (Minor: Art, Soundos), €200 (Major: Soundos) (Minor: Karin, Patrick),
# €200 (Major: Art) (Minor: Karin, Patrick), €200 (Major: Patrick) (Minor: Art, Soundos)
# €200 (Major: Soundos) (Minor: Karin, Patrick),
alive9 = {Player.ART_11, Player.KARIN_11, Player.PATRICK_11, Player.SOUNDOS_11}
exercise9_1 = Exercise(episode = 9, alive = alive9, maximum = None, earned = [
                            Earning(money = 700, major = {Player.KARIN_11}, minor = {Player.SOUNDOS_11})
                        ])
exercise9_2 = Exercise(episode = 9, alive = alive9, maximum = 2500, earned = [])
exercise9_3 = Exercise(episode = 9, alive = alive9, maximum = 2000, earned = [
                            Earning(money = 600, major = {Player.SOUNDOS_11}, minor = {Player.KARIN_11, Player.PATRICK_11}),
                            Earning(money = 400, major = {Player.ART_11}, minor = {Player.KARIN_11, Player.PATRICK_11}),
                            Earning(money = 200, major = {Player.KARIN_11}, minor = {Player.ART_11, Player.SOUNDOS_11}),
                            Earning(money = 200, major = {Player.PATRICK_11}, minor = {Player.ART_11, Player.SOUNDOS_11})
                        ])

# Aflevering 10
# Opdracht 1 (Maximaal €?):
# €600 (Major: Patrick) (Minor: Karin, Soundos), €1200 (Major: Art) (Minor: Karin, Soundos)
alive10 = {Player.ART_11, Player.KARIN_11, Player.PATRICK_11, Player.SOUNDOS_11}
exercise10_1 = Exercise(episode = 10, alive = alive10, maximum = None, earned = [
                            Earning(money = 600, major = {Player.PATRICK_11}, minor = {Player.KARIN_11, Player.SOUNDOS_11}),
                            Earning(money = 1200, major = {Player.ART_11}, minor = {Player.KARIN_11, Player.SOUNDOS_11})
                        ])

season11 = Season([exercise1_1, exercise1_2, exercise1_3, exercise2_1, exercise2_2, exercise2_3, exercise3_1,
                   exercise3_2, exercise3_3, exercise4_1, exercise4_3, exercise5_1, exercise5_2, exercise5_3,
                   exercise6_2, exercise7_1, exercise7_2, exercise8_2, exercise8_3, exercise9_1, exercise9_2,
                   exercise9_3, exercise10_1])