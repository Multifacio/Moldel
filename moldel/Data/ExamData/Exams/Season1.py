from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Sandy)
# Antwoorden: -
players1 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1, Player.PETRA_1, Player.ROBIN_1,
            Player.SANDY_1, Player.WARNER_1, Player.WILLY_1, Player.WILMIE_1]
result1 = Result(DropType.EXECUTION_DROP, [Player.SANDY_1])
episode1 = Episode(players1, result1, dict(), dict())

# Aflevering 2 (afvaller: Willy)
# Antwoorden: -
players2 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1, Player.PETRA_1, Player.ROBIN_1,
            Player.WARNER_1, Player.WILLY_1, Player.WILMIE_1]
result2 = Result(DropType.EXECUTION_DROP, [Player.WILLY_1])
episode2 = Episode(players2, result2, dict(), dict())

# Aflevering 3 (afvaller: John)
# Antwoorden: -
players3 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.JOHN_1, Player.PETRA_1, Player.ROBIN_1,
            Player.WARNER_1, Player.WILMIE_1]
result3 = Result(DropType.EXECUTION_DROP, [Player.JOHN_1])
episode3 = Episode(players3, result3, dict(), dict())

# Aflevering 4 (afvaller: Warner)
# Antwoorden: -
players4 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.PETRA_1, Player.ROBIN_1, Player.WARNER_1,
            Player.WILMIE_1]
result4 = Result(DropType.EXECUTION_DROP, [Player.WARNER_1])
episode4 = Episode(players4, result4, dict(), dict())

# Aflevering 5 (afvaller: Foke)
# Antwoorden: -
players5 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.FOKE_1, Player.PETRA_1, Player.ROBIN_1,  Player.WILMIE_1]
result5 = Result(DropType.EXECUTION_DROP, [Player.FOKE_1])
episode5 = Episode(players5, result5, dict(), dict())

# Aflevering 6 (afvaller: Arnoud)
# Antwoorden: -
players6 = [Player.ARNOUD_1, Player.DEBORAH_1, Player.PETRA_1, Player.ROBIN_1,  Player.WILMIE_1]
result6 = Result(DropType.EXECUTION_DROP, [Player.ARNOUD_1])
episode6 = Episode(players6, result6, dict(), dict())

# Aflevering 7 (afvaller: Wilmie)
# Antwoorden: -
players7 = [Player.DEBORAH_1, Player.PETRA_1, Player.ROBIN_1,  Player.WILMIE_1]
result7 = Result(DropType.EXECUTION_DROP, [Player.WILMIE_1])
episode7 = Episode(players7, result7, dict(), dict())

season1 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7})