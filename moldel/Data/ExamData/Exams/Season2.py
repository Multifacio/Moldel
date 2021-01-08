from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Gerda)
# Antwoorden: -
players1 = [Player.BJORN_2, Player.COR_2, Player.DAN_2, Player.DOORTJE_2, Player.GERDA_2, Player.NAZIFE_2,
            Player.NICO_2, Player.SIGRID_2, Player.WARD_2, Player.YVONNE_2]
result1 = Result(DropType.EXECUTION_DROP, [Player.GERDA_2])
episode1 = Episode(players1, result1, dict(), dict())

# Aflevering 2 (afvaller: Ward)
# Antwoorden: -
players2 = [Player.BJORN_2, Player.COR_2, Player.DAN_2, Player.DOORTJE_2, Player.NAZIFE_2, Player.NICO_2,
            Player.SIGRID_2, Player.WARD_2, Player.YVONNE_2]
result2 = Result(DropType.EXECUTION_DROP, [Player.WARD_2])
episode2 = Episode(players2, result2, dict(), dict())

# Aflevering 3 (afvallers: Björn, Dan)
# Antwoorden: -
players3 = [Player.BJORN_2, Player.COR_2, Player.DAN_2, Player.DOORTJE_2, Player.NAZIFE_2, Player.NICO_2,
            Player.SIGRID_2, Player.YVONNE_2]
result3 = Result(DropType.EXECUTION_DROP, [Player.BJORN_2, Player.DAN_2])
episode3 = Episode(players3, result3, dict(), dict())

# Aflevering 4 (afvaller: Nazife)
# Antwoorden: -
players4 = [Player.COR_2, Player.DAN_2, Player.DOORTJE_2, Player.NAZIFE_2, Player.NICO_2, Player.SIGRID_2,
            Player.YVONNE_2]
result4 = Result(DropType.EXECUTION_DROP, [Player.NAZIFE_2])
episode4 = Episode(players4, result4, dict(), dict())

# Aflevering 5 (afvaller: Cor)
# Antwoorden: -
players5 = [Player.COR_2, Player.DAN_2, Player.DOORTJE_2, Player.NICO_2, Player.SIGRID_2, Player.YVONNE_2]
result5 = Result(DropType.EXECUTION_DROP, [Player.COR_2])
episode5 = Episode(players5, result5, dict(), dict())

# Aflevering 6 (afvaller: Dan)
# Antwoorden: -
players6 = [Player.DAN_2, Player.DOORTJE_2, Player.NICO_2, Player.SIGRID_2, Player.YVONNE_2]
result6 = Result(DropType.EXECUTION_DROP, [Player.DAN_2])
episode6 = Episode(players6, result6, dict(), dict())

# Aflevering 7 (afvaller: Doortje)
# Antwoorden: -
players7 = [Player.DOORTJE_2, Player.NICO_2, Player.SIGRID_2, Player.YVONNE_2]
result7 = Result(DropType.EXECUTION_DROP, [Player.DOORTJE_2])
episode7 = Episode(players7, result7, dict(), dict())

season2 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7})