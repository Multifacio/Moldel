from aenum import Enum, NoAlias

class DropType(Enum):
    """ Whether someone dropped out of the game or not and how they dropped out of the game or stayed in the game. The
    boolean value represents if the list of players can be excluded from being the Mol. True means that they can be
    excluded from being the Mol. False means that they cannot be excluded from being the Mol. """
    _settings_ = NoAlias

    # Use the EXECUTION_DROP when player(s) dropped out of the game, because they had the worst score on the test
    # or have seen a red screen. Also if a player returned after dropping out of the game (e.g. Tim from season 13
    # dropped out during the execution of episode 3 but returned in episode 4) or if the player has seen a red screen
    # during execution but it did not have any consequence (e.g. Daphne from season 14 got a red screen during the
    # first execution, but she did not dropped out). In most cases the list consists of a single player (since generally
    # only 1 player drops off every execution), but sometimes multiple players drop off during
    # the same execution (for example Rick Paul and Jamie during episode 7 of season 19) in which case the list consists
    # of multiple players.
    EXECUTION_DROP = True

    # Use the VOLUNTARY_DROP when player(s) dropped out of the game, because of other reasons. So this player did not
    # have the worst score on the test and did not see a red screen (e.g. Janine from season 16 dropped off in episode 3
    # because an accident happend during an assignment and Jean-Marc from season 18 dropped of voluntarily in episode 2)
    # Do not classify drops as VOLUNTARY_DROP when a player mentioned that he/she intentionally made a lot of errors on
    # the test (such as Nikkie from season 19).
    VOLUNTARY_DROP = True

    # Use the POSSIBLE_DROP when some player(s) have not seen their screen and some player(s) have seen their
    # screen and nobody dropped off (because the player with the red screen is in the group of players that did not see
    # their screens). The list of players in this case are the players that did NOT see their screen and therefore could
    # possibly have dropped off.
    POSSIBLE_DROP = False

    # Use the NO_DROP_NOR_SCREEN when no player has seen their screen and nobody dropped off or in cases when nobody
    # dropped off and you cannot derive any information about who could possibly have dropped off. Do not use this type
    # but use POSSIBLE_DROP if at least 1 player has seen a green screen.
    NO_DROP_NOR_SCREENS = False
