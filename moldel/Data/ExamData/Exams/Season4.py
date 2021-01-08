from Data.Player import Player
from ..Dataclasses.DropType import DropType
from ..Dataclasses.Episode import Episode
from ..Dataclasses.Question import Question
from ..Dataclasses.Result import Result
from ..Dataclasses.Season import Season
from ..Dataclasses.TestInput import TestInput, DelayedAnswer

# Aflevering 1 (afvaller: Louis)
# Antwoorden: -
players1 = [Player.AAFKE_4, Player.ASTRID_4, Player.CHANDRIKA_4, Player.ELISE_4, Player.FERDI_4, Player.JULIEN_4,
            Player.LOUIS_4, Player.PATRICIA_4, Player.RENE_4, Player.RON_4]
result1 = Result(DropType.EXECUTION_DROP, [Player.LOUIS_4])
episode1 = Episode(players1, result1, dict(), dict())

# Aflevering 2 (afvaller: Julien)
# Antwoorden: -
players2 = [Player.AAFKE_4, Player.ASTRID_4, Player.CHANDRIKA_4, Player.ELISE_4, Player.FERDI_4, Player.JULIEN_4,
            Player.PATRICIA_4, Player.RENE_4, Player.RON_4]
result2 = Result(DropType.EXECUTION_DROP, [Player.JULIEN_4])
episode2 = Episode(players2, result2, dict(), dict())

# Aflevering 3 (afvaller: -)
# Antwoorden: -
players3 = [Player.AAFKE_4, Player.ASTRID_4, Player.CHANDRIKA_4, Player.ELISE_4, Player.FERDI_4, Player.PATRICIA_4,
            Player.RENE_4, Player.RON_4]
result3 = Result(DropType.POSSIBLE_DROP, [Player.ASTRID_4, Player.CHANDRIKA_4, Player.RENE_4, Player.RON_4])
episode3 = Episode(players3, result3, dict(), dict())

# Aflevering 4 (afvaller: Aafke)
# Antwoorden: -
players4 = [Player.AAFKE_4, Player.ASTRID_4, Player.CHANDRIKA_4, Player.ELISE_4, Player.FERDI_4, Player.PATRICIA_4,
            Player.RENE_4, Player.RON_4]
result4 = Result(DropType.EXECUTION_DROP, [Player.AAFKE_4])
episode4 = Episode(players4, result4, dict(), dict())

# Aflevering 6 - First (afvaller: Astrid)
# Antwoorden: -
players6f = [Player.ASTRID_4, Player.CHANDRIKA_4, Player.ELISE_4, Player.FERDI_4, Player.PATRICIA_4, Player.RENE_4,
             Player.RON_4]
result6f = Result(DropType.VOLUNTARY_DROP, [Player.ASTRID_4])
episode6f = Episode(players6f, result6f, dict(), dict())

# Aflevering 6 - Second (afvaller: Patricia)
# Antwoorden: -
players6s = [Player.CHANDRIKA_4, Player.ELISE_4, Player.FERDI_4, Player.PATRICIA_4, Player.RENE_4, Player.RON_4]
result6s = Result(DropType.EXECUTION_DROP, [Player.PATRICIA_4])
episode6s = Episode(players6s, result6s, dict(), dict())

# Aflevering 8 (afvaller: Ferdi)
# Antwoorden: -
players8 = [Player.CHANDRIKA_4, Player.ELISE_4, Player.FERDI_4, Player.RENE_4, Player.RON_4]
result8 = Result(DropType.EXECUTION_DROP, [Player.FERDI_4])
episode8 = Episode(players8, result8, dict(), dict())

# Aflevering 9 (afvaller: René)
# Antwoorden: -
players9 = [Player.CHANDRIKA_4, Player.ELISE_4, Player.RENE_4, Player.RON_4]
result9 = Result(DropType.EXECUTION_DROP, [Player.RENE_4])
episode9 = Episode(players9, result9, dict(), dict())

season4 = Season(players1, {1: episode1, 2: episode2, 3: episode3, 4: episode4, 5.5: episode6f, 6: episode6s,
                            8: episode8, 9: episode9})