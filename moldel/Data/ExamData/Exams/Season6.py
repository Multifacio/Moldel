from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Geert)
# Antwoorden: Roderick (Vrijstelling), Liz (Vrijstelling), Toine (Vrijstelling), Milouska (2 jokers), Geert (2 jokers),
# Peggy (3 jokers), Richard (3 jokers), Chris (5 jokers), Frederique (3 jokers), Mary-Lou (3 jokers)
players1 = [Player.CHRIS_6, Player.FREDERIQUE_6, Player.GEERT_6, Player.LIZ_6, Player.MARY_LOU_6, Player.MILOUSKA_6,
            Player.PEGGY_6, Player.RICHARD_6, Player.RODERICK_6, Player.TOINE_6]
result1 = Result(DropType.EXECUTION_DROP, [Player.GEERT_6])
episode1 = Episode(players1, result1,
                   {Player.CHRIS_6: TestInput(jokers = 5), Player.FREDERIQUE_6: TestInput(jokers = 3),
                    Player.GEERT_6: TestInput(jokers = 2), Player.LIZ_6: TestInput(immunity = True),
                    Player.MARY_LOU_6: TestInput(jokers = 3), Player.MILOUSKA_6: TestInput(jokers = 2),
                    Player.PEGGY_6: TestInput(jokers = 3), Player.RICHARD_6: TestInput(jokers = 3),
                    Player.RODERICK_6: TestInput(immunity = True), Player.TOINE_6: TestInput(immunity = True)},
                   dict())

# Aflevering 2 (afvaller: Chris)
# Antwoorden: Roderick (Vrijstelling), Liz (Vrijstelling), Mary-Lou (3 jokers), Toine (3 jokers), Peggy (2 jokers),
# Frederique (2 jokers)
players2 = [Player.CHRIS_6, Player.FREDERIQUE_6, Player.LIZ_6, Player.MARY_LOU_6, Player.MILOUSKA_6, Player.PEGGY_6,
            Player.RICHARD_6, Player.RODERICK_6, Player.TOINE_6]
result2 = Result(DropType.EXECUTION_DROP, [Player.CHRIS_6])
episode2 = Episode(players2, result2,
                   {Player.FREDERIQUE_6: TestInput(jokers = 2), Player.LIZ_6: TestInput(immunity = True),
                    Player.MARY_LOU_6: TestInput(jokers = 3), Player.PEGGY_6: TestInput(jokers = 2),
                    Player.RODERICK_6: TestInput(immunity = True), Player.TOINE_6: TestInput(jokers = 3)},
                   dict())

# Aflevering 3 (afvaller: Richard)
# Antwoorden: Roderick (Vrijstelling), Liz (Vrijstelling), Toine (2 jokers)
players3 = [Player.FREDERIQUE_6, Player.LIZ_6, Player.MARY_LOU_6, Player.MILOUSKA_6, Player.PEGGY_6, Player.RICHARD_6,
            Player.RODERICK_6, Player.TOINE_6]
result3 = Result(DropType.EXECUTION_DROP, [Player.RICHARD_6])
episode3 = Episode(players3, result3,
                   {Player.LIZ_6: TestInput(immunity = True), Player.RODERICK_6: TestInput(immunity = True),
                    Player.TOINE_6: TestInput(jokers = 2)},
                   dict())

# Aflevering 4 (afvaller: Mary-Lou)
# Antwoorden: Toine (3 jokers), Milouska (4 jokers), Roderick (3 jokers), Peggy (2 jokers), Richard (Vrijstelling)
players4 = [Player.FREDERIQUE_6, Player.LIZ_6, Player.MARY_LOU_6, Player.MILOUSKA_6, Player.PEGGY_6, Player.RICHARD_6,
            Player.RODERICK_6, Player.TOINE_6]
result4 = Result(DropType.EXECUTION_DROP, [Player.MARY_LOU_6])
episode4 = Episode(players4, result4,
                   {Player.MILOUSKA_6: TestInput(jokers = 4), Player.PEGGY_6: TestInput(jokers = 2),
                    Player.RICHARD_6: TestInput(immunity = True), Player.RODERICK_6: TestInput(jokers = 3),
                    Player.TOINE_6: TestInput(jokers = 3)},
                   dict())

# Aflevering 5 (afvaller: Liz)
# Antwoorden: Peggy (2 jokers), Frederique (1 joker), Roderick (2 jokers), Richard (2 jokers), Milouska (2 jokers),
# Toine (2 jokers)
players5 = [Player.FREDERIQUE_6, Player.LIZ_6, Player.MILOUSKA_6, Player.PEGGY_6, Player.RICHARD_6, Player.RODERICK_6,
            Player.TOINE_6]
result5 = Result(DropType.EXECUTION_DROP, [Player.LIZ_6])
episode5 = Episode(players5, result5,
                   {Player.FREDERIQUE_6: TestInput(jokers = 1), Player.MILOUSKA_6: TestInput(jokers = 2),
                    Player.PEGGY_6: TestInput(jokers = 2), Player.RICHARD_6: TestInput(jokers = 2),
                    Player.RODERICK_6: TestInput(jokers = 2), Player.TOINE_6: TestInput(jokers = 2)},
                   dict())

# Aflevering 6 (afvaller: Richard)
# Antwoorden: Roderick (1 joker)
players6 = [Player.FREDERIQUE_6, Player.MILOUSKA_6, Player.PEGGY_6, Player.RICHARD_6, Player.RODERICK_6, Player.TOINE_6]
result6 = Result(DropType.EXECUTION_DROP, [Player.RICHARD_6])
episode6 = Episode(players6, result6,
                   {Player.RODERICK_6: TestInput(jokers = 1)},
                   dict())

# Aflevering 7 (afvaller: Toine)
# Antwoorden: Peggy (1 joker)
players7 = [Player.FREDERIQUE_6, Player.MILOUSKA_6, Player.PEGGY_6, Player.RODERICK_6, Player.TOINE_6]
result7 = Result(DropType.EXECUTION_DROP, [Player.TOINE_6])
episode7 = Episode(players7, result7,
                   {Player.PEGGY_6: TestInput(jokers = 1)},
                   dict())

# Aflevering 8 (afvaller: Peggy)
# Antwoorden: Frederique (Vrijstelling)
players8 = [Player.FREDERIQUE_6, Player.MILOUSKA_6, Player.PEGGY_6, Player.RODERICK_6]
result8 = Result(DropType.EXECUTION_DROP, [Player.PEGGY_6])
episode8 = Episode(players8, result8,
                   {Player.FREDERIQUE_6: TestInput(immunity = True)},
                   dict())

# Aflevering 9 (afvaller: Roderick)
players9 = [Player.FREDERIQUE_6, Player.MILOUSKA_6, Player.RODERICK_6]
result9 = Result(DropType.EXECUTION_DROP, [Player.RODERICK_6])
episode9 = Episode(players9, result9, dict(), dict())

season6 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                            8: episode8, 10: episode9})