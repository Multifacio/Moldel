from aenum import Enum, NoAlias

class Job(Enum):
    """ The most common jobs for the players. Each job has a corresponding set of words which belongs to that job."""
    _settings_ = NoAlias

    CABARETIER = {"cabaret", "comedy", "speel", "spel", "theater", "voorstelling"}
    DJ = {"3fm", "dj", "jockey", "music", "programma", "radio", "tmf", "top"}
    INSTRUMENTALIST = {"album", "artiest", "cd", "concert", "discografie", "harp", "hitnotering", "lied", "music", "muziek", "nummer", "orkest", "single", "song", "speel", "spel", "theater", "tmf", "top"}
    JOURNALIST = {"at5", "avro", "bnn", "journaal", "journalist", "krant", "kro", "ncrv", "nieuws", "omroep", "radio", "televisie", "rtl", "vara", "verslag"}
    RADIO_PRESENTATOR = {"3fm", "avro", "bnn", "journaal", "kro", "music", "ncrv", "nieuws", "omroep", "presentatie", "presentator", "presentatrice", "presenteer", "presenteren", "programma", "radio", "top", "vara", "veronica", "zender"}
    RADIO_PRODUCER = {"3fm", "avro", "bnn", "kro", "ncrv", "omroep", "produce", "programma", "radio", "schreef", "schrijf", "tekstschrijver", "vara", "veronica", "zender"}
    SCHRIJVER = {"blad", "boek", "column", "isbn", "krant", "schreef", "schrijf", "schrijver", "strip", "uitgever"}
    SONGWRITER = {"album", "artiest", "cd", "discografie", "hitnotering", "lied", "music", "muziek", "nummer", "schreef", "schrijf", "single", "song", "songwriter", "tmf", "top"}
    # SPORTER = {"kampioen", "olympisch", "speel", "spel", "sport", "voetbal", "wk", "zwem"}
    STEM_ACTEUR = {"animatie", "bijrol", "fabeltjeskrant", "film", "gastrol", "hoofdrol", "imdb", "movie", "nickelodeon", "personage", "programma", "radio", "reclame", "rol", "rollen", "serie", "stem", "stemacteur", "stemactrice", "televisie", "vertolk", "voice"}
    TONEEL_ACTEUR = {"acteer", "acteur", "actrice", "bijrol", "fabeltjeskrant", "gastrol", "hoofdrol", "musical", "personage", "rol", "rollen", "speel", "spel", "theater", "toneel", "vertolk", "voorstelling"}
    TONEEL_PRODUCER = {"fabeltjeskrant", "produce", "regisseur", "schreef", "schrijf", "theater", "toneel", "tekstschrijver", "voorstelling"}
    TV_ACTEUR = {"acteer", "acteur", "actrice", "avro", "baantjer", "bijrol", "bnn", "film", "gastrol", "hoofdrol", "imdb", "kro", "movie", "ncrv", "nickelodeon", "personage", "programma", "reclame", "rol", "rollen", "rtl", "sbs", "sbs6", "serie", "soap", "speel", "spel", "televisie", "televizier", "tv", "uitgezonden", "vara", "vertolk", "zoop", "zwartboek"}
    TV_PRESENTATOR = {"at5", "avro", "bnn", "journaal", "kro", "ncrv", "nickelodeon", "nieuws", "omroep", "presentatie", "presentator", "presentatrice", "presenteer", "presenteren", "programma", "rtl", "sbs", "sbs6", "televisie", "televizier", "tmf", "tv", "uitgezonden", "vara", "veronica", "zender"}
    TV_PRODUCER = {"animatie", "at5", "avro", "baantjer", "bnn", "documentaire", "fabeltjeskrant", "film", "imdb", "kro", "movie", "ncrv", "nickelodeon", "omroep", "produce", "programma", "regisseur", "rtl", "sbs", "sbs6", "schreef", "schrijf", "serie", "soap", "tekstschrijver", "televisie", "televizier", "tmf", "tv", "uitgezonden", "vara", "veronica", "zender", "zoop"}
    ZANGER = {"album", "artiest", "cd", "concert", "discografie", "hitnotering", "lied", "music", "muziek", "nummer", "orkest", "single", "song", "theater", "tmf", "top", "voice", "zang", "zing", "zong"}
