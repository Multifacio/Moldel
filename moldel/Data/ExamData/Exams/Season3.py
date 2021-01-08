from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Erik)
# Antwoorden: -
players1 = [Player.DICK_3, Player.ELLEN_3, Player.ERIK_3, Player.GEORGE_3, Player.HARRY_3, Player.JANTIEN_3,
            Player.JOHN_3, Player.KAREN_3, Player.KERSTIN_3, Player.PAMELA_3, Player.PRINCE_3]
result1 = Result(DropType.EXECUTION_DROP, [Player.ERIK_3])
episode1 = Episode(players1, result1, dict(), dict())

# Aflevering 2 (afvaller: Paméla)
# Antwoorden: -
players2 = [Player.DICK_3, Player.ELLEN_3, Player.GEORGE_3, Player.HARRY_3, Player.JANTIEN_3, Player.JOHN_3,
            Player.KAREN_3, Player.KERSTIN_3, Player.PAMELA_3, Player.PRINCE_3]
result2 = Result(DropType.EXECUTION_DROP, [Player.PAMELA_3])
episode2 = Episode(players2, result2, dict(), dict())

# Aflevering 3 (afvaller: Dick)
# Antwoorden: -
players3 = [Player.DICK_3, Player.ELLEN_3, Player.GEORGE_3, Player.HARRY_3, Player.JANTIEN_3, Player.JOHN_3,
            Player.KAREN_3, Player.KERSTIN_3, Player.PRINCE_3]
result3 = Result(DropType.EXECUTION_DROP, [Player.DICK_3])
episode3 = Episode(players3, result3, dict(), dict())

# Aflevering 4 (afvaller: -)
# Antwoorden: -
players4 = [Player.ELLEN_3, Player.GEORGE_3, Player.HARRY_3, Player.JANTIEN_3, Player.JOHN_3, Player.KAREN_3,
            Player.KERSTIN_3, Player.PRINCE_3]
result4 = Result(DropType.NO_DROP_NOR_SCREENS, [Player.ELLEN_3, Player.GEORGE_3, Player.HARRY_3, Player.JANTIEN_3,
                                                Player.JOHN_3, Player.KAREN_3, Player.KERSTIN_3, Player.PRINCE_3])
episode4 = Episode(players4, result4, dict(), dict())

# Aflevering 5 (afvaller: Kerstin)
# Antwoorden: -
players5 = [Player.ELLEN_3, Player.GEORGE_3, Player.HARRY_3, Player.JANTIEN_3, Player.JOHN_3, Player.KAREN_3,
            Player.KERSTIN_3, Player.PRINCE_3]
result5 = Result(DropType.EXECUTION_DROP, [Player.KERSTIN_3])
episode5 = Episode(players5, result5, dict(), dict())

# Aflevering 6 (afvaller: Karen)
# Antwoorden: -
players6 = [Player.ELLEN_3, Player.GEORGE_3, Player.HARRY_3, Player.JANTIEN_3, Player.JOHN_3, Player.KAREN_3,
            Player.PRINCE_3]
result6 = Result(DropType.EXECUTION_DROP, [Player.KAREN_3])
episode6 = Episode(players6, result6, dict(), dict())

# Aflevering 7 (afvaller: Prince)
# Antwoorden: -
players7 = [Player.ELLEN_3, Player.GEORGE_3, Player.HARRY_3, Player.JANTIEN_3, Player.JOHN_3, Player.PRINCE_3]
result7 = Result(DropType.EXECUTION_DROP, [Player.PRINCE_3])
episode7 = Episode(players7, result7, dict(), dict())

# Aflevering 8 (afvaller: Harry)
# Antwoorden: -
players8 = [Player.ELLEN_3, Player.GEORGE_3, Player.HARRY_3, Player.JANTIEN_3, Player.JOHN_3]
result8 = Result(DropType.EXECUTION_DROP, [Player.HARRY_3])
episode8 = Episode(players8, result8, dict(), dict())

# Aflevering 9 (afvaller: Ellen)
# Antwoorden: -
players9 = [Player.ELLEN_3, Player.GEORGE_3, Player.JANTIEN_3, Player.JOHN_3]
result9 = Result(DropType.EXECUTION_DROP, [Player.ELLEN_3])
episode9 = Episode(players9, result9, dict(), dict())

season3 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5: episode5, 6: episode6, 7: episode7,
                            8: episode8, 9: episode9})