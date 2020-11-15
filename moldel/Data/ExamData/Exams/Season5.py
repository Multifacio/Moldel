from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: -)
# Antwoorden: -
players1 = [Player.GIJS_5, Player.ISABELLE_5, Player.JIM_5, Player.LOTTIE_5, Player.MARC_MARIE_5, Player.ROELAND_5,
            Player.SANDER_5, Player.VICTORIA_5, Player.YVON_5, Player.YVONNE_5]
result1 = Result(DropType.NO_DROP_NOR_SCREENS, [Player.GIJS_5, Player.ISABELLE_5, Player.JIM_5, Player.LOTTIE_5,
                                                Player.MARC_MARIE_5, Player.ROELAND_5, Player.SANDER_5,
                                                Player.VICTORIA_5, Player.YVON_5, Player.YVONNE_5])
episode1 = Episode(players1, result1, dict(), dict())

# Aflevering 2 (afvaller: Gijs)
# Antwoorden: -
players2 = [Player.GIJS_5, Player.ISABELLE_5, Player.JIM_5, Player.LOTTIE_5, Player.MARC_MARIE_5, Player.ROELAND_5,
            Player.SANDER_5, Player.VICTORIA_5, Player.YVON_5, Player.YVONNE_5]
result2 = Result(DropType.EXECUTION_DROP, [Player.GIJS_5])
episode2 = Episode(players2, result2, dict(), dict())

# Aflevering 3 (afvaller: Roeland)
# Antwoorden: -
players3 = [Player.GIJS_5, Player.ISABELLE_5, Player.JIM_5, Player.LOTTIE_5, Player.MARC_MARIE_5, Player.ROELAND_5,
            Player.SANDER_5, Player.VICTORIA_5, Player.YVON_5, Player.YVONNE_5]
result3 = Result(DropType.VOLUNTARY_DROP, [Player.ROELAND_5])
episode3 = Episode(players3, result3, dict(), dict())

# Aflevering 4 (afvaller: Yvonne)
# Antwoorden: Victoria (-1 joker), Isabelle (3 jokers) (kreeg 'aantal' goede antwoorden als hulpmol)
players4 = [Player.GIJS_5, Player.ISABELLE_5, Player.JIM_5, Player.LOTTIE_5, Player.MARC_MARIE_5, Player.SANDER_5,
            Player.VICTORIA_5, Player.YVON_5, Player.YVONNE_5]
result4 = Result(DropType.EXECUTION_DROP, [Player.YVONNE_5])
episode4 = Episode(players4, result4,
                   {Player.GIJS_5: TestInput(jokers = 1), Player.ISABELLE_5: TestInput(jokers = 4),
                    Player.JIM_5: TestInput(jokers = 1), Player.LOTTIE_5: TestInput(jokers = 1),
                    Player.MARC_MARIE_5: TestInput(jokers = 1), Player.SANDER_5: TestInput(jokers = 1),
                    Player.YVON_5: TestInput(jokers = 1), Player.YVONNE_5: TestInput(jokers = 1)},
                   dict())

# Aflevering 5 (afvaller: Victoria)
# Antwoorden: Lottie (Vrijstelling), Jim (3 jokers)
players5 = [Player.GIJS_5, Player.ISABELLE_5, Player.JIM_5, Player.LOTTIE_5, Player.MARC_MARIE_5, Player.SANDER_5,
            Player.VICTORIA_5, Player.YVON_5]
result5 = Result(DropType.EXECUTION_DROP, [Player.VICTORIA_5])
episode5 = Episode(players5, result5,
                   {Player.JIM_5: TestInput(jokers = 3), Player.LOTTIE_5: TestInput(immunity = True)},
                   dict())

# Aflevering 6 (afvallers: Gijs, Jim)
# Antwoorden: -
players6 = [Player.GIJS_5, Player.ISABELLE_5, Player.JIM_5, Player.LOTTIE_5, Player.MARC_MARIE_5, Player.SANDER_5,
            Player.YVON_5]
result6 = Result(DropType.EXECUTION_DROP, [Player.GIJS_5, Player.JIM_5])
episode6 = Episode(players6, result6, dict(), dict())

# Aflevering 7 (afvaller: Sander)
# Antwoorden: -
players7 = [Player.ISABELLE_5, Player.LOTTIE_5, Player.MARC_MARIE_5, Player.SANDER_5, Player.YVON_5]
result7 = Result(DropType.EXECUTION_DROP, [Player.SANDER_5])
episode7 = Episode(players7, result7, dict(), dict())

# Aflevering 8 (afvaller: Isabelle)
# Antwoorden: Yvon (Vrijstelling)
players8 = [Player.ISABELLE_5, Player.LOTTIE_5, Player.MARC_MARIE_5, Player.YVON_5]
result8 = Result(DropType.EXECUTION_DROP, [Player.ISABELLE_5])
episode8 = Episode(players8, result8,
                   {Player.YVON_5: TestInput(immunity = True)},
                   dict())

# Aflevering 9 (afvaller: Lottie)
players9 = [Player.LOTTIE_5, Player.MARC_MARIE_5, Player.YVON_5]
result9 = Result(DropType.EXECUTION_DROP, [Player.LOTTIE_5])
episode9 = Episode(players9, result9, dict(), dict())

season5 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                            8: episode8, 9: episode9})