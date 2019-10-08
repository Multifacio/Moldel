from aenum import Enum, NoAlias

class SuspicionLevel(Enum):
    """ The suspicion levels used for the Social Media Data. The values (float) of these enums correspond to the
    relative probability decrease of being the mol when a player has this suspicion level. """
    _settings_ = NoAlias

    NOT_UNLIKELY = 1.00
    SLIGHTLY_UNLIKELY = 0.65
    UNLIKELY = 0.20
    VERY_UNLIKELY = 0.00