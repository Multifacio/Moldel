from aenum import Enum, NoAlias

class Job(Enum):
    """ The most common jobs for the players. Each job has a corresponding list of words which belongs to that job."""
    _settings_ = NoAlias

    CABARETIER = ["speelde", "theater", "speelt", "schrijver", "schreef", "spelen", "theaterstuk", "cabaretier", "voorstelling", "stand", "comedytrain"]
    DJ = ["radio", "top", "3fm", "horen", "tmf", "radioprogramma", "dj", "music"]
    INSTRUMENTALIST = ["speelde", "top", "theater", "album", "single", "speelt", "muziek", "nummer", "spelen", "tmf", "cd", "band", "theaterstuk", "singles", "hitnotering", "discografie", "music"]
    JOURNALIST = ["radio", "televisie", "bnn", "rtl", "avro", "omroep", "schrijver", "vara", "kro", "ncrv", "schreef", "verslaggever", "nieuws", "veronica", "vpro", "nos", "at5", "tros", "npo", "journalistiek", "journalist", "rtv"]
    RADIO_PRESENTATOR = ["radio", "presentator", "presenteerde", "bnn", "rtl", "avro", "top", "omroep", "presenteert", "3fm", "presentatrice", "vara", "kro", "presentatornederlands", "ncrv", "verslaggever", "horen", "presenteren", "nieuws", "veronica", "radioprogramma", "vpro", "nos", "tros", "npo", "music"]
    RADIO_PRODUCER = ["radio", "bnn", "rtl", "avro", "top", "omroep", "producent", "3fm", "schrijver", "vara", "kro", "ncrv", "schreef", "veronica", "radioprogramma", "vpro", "nos", "tros", "npo", "music"]
    SCHRIJVER = ["schrijver", "isbn", "boek", "schreef", "columns", "boeken"]
    SONGWRITER = ["top", "album", "single", "muziek", "nummer", "tmf", "cd", "band", "singles", "hitnotering", "discografie", "music"]
    STEM_ACTEUR = ["rol", "film", "radio", "televisie", "imdb", "serie", "televisieprogramma", "hoofdrol", "televisieserie", "3fm", "stem", "films", "horen", "hoofdrollen", "rollen", "filmografie", "movie", "gastrol", "voice", "nickelodeon", "vertolkte", "zapp", "gastrollen"]
    TONEEL_ACTEUR = ["rol", "speelde", "musical", "acteur", "actrice", "theater", "hoofdrol", "speelt", "toneel", "spelen", "hoofdrollen", "rollen", "acteurnederlands", "theaterstuk", "gastrol", "voorstelling", "vertolkte", "gastrollen", "musicals"]
    TONEEL_PRODUCER = ["theater", "producent", "schrijver", "toneel", "schreef", "theaterstuk", "voorstelling"]
    TV_ACTEUR = ["rol", "film", "speelde", "televisie", "bnn", "acteur", "rtl", "imdb", "serie", "avro", "televisieprogramma", "actrice", "hoofdrol", "speelt", "televisieserie", "vara", "kro", "films", "aflevering", "ncrv", "spelen", "uitgezonden", "sbs", "hoofdrollen", "rollen", "afl", "filmografie", "acteurnederlands", "movie", "televizier", "gastrol", "nickelodeon", "tros", "npo", "vertolkte", "zapp", "gastrollen", "nps"]
    TV_PRESENTATOR = ["presentator", "presenteerde", "televisie", "bnn", "rtl", "avro", "televisieprogramma", "omroep", "presenteert", "presentatrice", "vara", "kro", "presentatornederlands", "ncrv", "verslaggever", "tmf", "uitgezonden", "presenteren", "sbs", "nieuws", "veronica", "vpro", "nos", "televizier", "nickelodeon", "at5", "tros", "npo", "rtv", "zapp", "nps"]
    TV_PRODUCER = ["film", "televisie", "bnn", "rtl", "imdb", "serie", "avro", "televisieprogramma", "omroep", "televisieserie", "producent", "schrijver", "vara", "kro", "films", "ncrv", "schreef", "tmf", "uitgezonden", "sbs", "veronica", "filmografie", "movie", "vpro", "nos", "televizier", "at5", "tros", "npo", "rtv", "zapp", "nps"]
    ZANGER = ["musical", "top", "theater", "album", "single", "zanger", "muziek", "nummer", "zangeres", "horen", "tmf", "cd", "band", "theaterstuk", "voice", "singles", "hitnotering", "discografie", "music", "musicals"]