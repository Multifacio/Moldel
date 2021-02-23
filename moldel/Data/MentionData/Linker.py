from Data.Player import Player

# The path where the mentions are stored.
WIKI_FILES_PATH = "moldel/Data/Wikipedia/WikiFiles/"

# The LINKER maps players to corresponding texts recognized in speeches
LINKER = {Player.CHARLOTTE_22: {"charlotte", "sjalotten", "charlot", "sjalot"},
          Player.ERIK_22: {"eric", "erik"},
          Player.FLORENTIJN_22: {"florentijn", "floor", "tijn", "florestein", "florentijnen", "valentijn"},
          Player.JOSHUA_22: {"joshua", "george", "josh"},
          Player.LAKSHMI_22: {"lakshmi", "laxmi", "lax", "laksmien"},
          Player.MARIJE_22: {"marije", "marijn", "marij", "mareille"},
          Player.ROCKY_22: {"rocky", "hockey"},
          Player.REMCO_22: {"remco", "remko"},
          Player.RENEE_22: {"rené", "renée", "renee"},
          Player.SPLINTER_22: {"splinter", "sprinter", "splitter", "splint"}}