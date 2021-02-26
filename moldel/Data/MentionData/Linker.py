from Data.Player import Player

# The path where the mentions are stored.
WIKI_FILES_PATH = "moldel/Data/Wikipedia/WikiFiles/"

# Season 20 too hard for speech recognition.

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
          Player.SPLINTER_22: {"splinter", "sprinter", "splitter", "splint"},
          Player.ELLIE_21: {"ellie", "elly"},
          Player.JEROEN_21: {"jeroen"},
          Player.HORACE_21: {"horace", "horatio", "horoscoop", "horus", "horse", "horst"},
          Player.NADJA_21: {"nadja", "nadia"},
          Player.NIKKIE_21: {"nicky", "nikki", "niki", "nikkie"},
          Player.PATRICK_21: {"patrick"},
          Player.PEGGY_21: {"peggy"},
          Player.RON_21: {"ron", "roon", "rhoon"},
          Player.TINA_21: {"tina"},
          Player.TYGO_21: {"tygo", "ticho", "tigo", "tycho"},
          }