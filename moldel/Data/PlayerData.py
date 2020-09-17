from Data.Player import Player
from typing import NamedTuple, Union, Set

PlayerData = NamedTuple("PlayerData", [("name", str), ("season", int), ("is_mol", Union[bool, None])])

# This variable contains the first name of every player, the season in which every player participated and which player
# is the Mol. If the is_mol value of a player is set to None then it is unknown whether that player is the Mol.
__ALL_PLAYER_DATA = {
    Player.ALEX_7: PlayerData("Alex", 7, False), Player.DICK_7: PlayerData("Dick", 7, False),
    Player.EVA_7: PlayerData("Eva", 7, False), Player.INGE_7: PlayerData("Inge", 7, True),
    Player.LIESBETH_7: PlayerData("Liesbeth", 7, False), Player.MENNO_7: PlayerData("Menno", 7, False),
    Player.NADJA_7: PlayerData("Nadja", 7, False), Player.PAUL_7: PlayerData("Paul", 7, False),
    Player.RENATE_7: PlayerData("Renate", 7, False), Player.SANDER_7: PlayerData("Sander", 7, False),

    Player.ANNETTE_8: PlayerData("Annette", 8, False), Player.COEN_8: PlayerData("Coen", 8, False),
    Player.DENNIS_8: PlayerData("Dennis", 8, True), Player.DUNYA_8: PlayerData("Dunya", 8, False),
    Player.EDO_8: PlayerData("Edo", 8, False), Player.GEORGINA_8: PlayerData("Georgina", 8, False),
    Player.JORIS_8: PlayerData("Joris", 8, False), Player.NICOLETTE_8: PlayerData("Nicolette", 8, False),
    Player.PATRICK_8: PlayerData("Patrick", 8, False), Player.REGINA_8: PlayerData("Regina", 8, False),

    Player.ANNIEK_9: PlayerData("Anniek", 9, False), Player.DENNIS_9: PlayerData("Dennis", 9, False),
    Player.FROUKJE_9: PlayerData("Froukje", 9, False), Player.HANS_9: PlayerData("Hans", 9, False),
    Player.JON_9: PlayerData("Jon", 9, True), Player.PAULA_9: PlayerData("Paula", 9, False),
    Player.RICK_9: PlayerData("Rick", 9, False), Player.SEBASTIAAN_9: PlayerData("Sebastiaan", 9, False),
    Player.VERA_9: PlayerData("Vera", 9, False), Player.VIVIENNE_9: PlayerData("Vivienne", 9, False),

    Player.ARJEN_10: PlayerData("Arjen", 10, False), Player.BARBARA_10: PlayerData("Barbara", 10, False),
    Player.ERIK_10: PlayerData("Erik", 10, False), Player.FRITS_10: PlayerData("Frits", 10, False),
    Player.HIND_10: PlayerData("Hind", 10, False), Player.KIM_10: PlayerData("Kim", 10, True),
    Player.LORETTA_10: PlayerData("Loretta", 10, False), Player.MANUEL_10: PlayerData("Manuel", 10, False),
    Player.SANNE_10: PlayerData("Sanne", 10, False), Player.TIM_10: PlayerData("Tim", 10, False),

    Player.ANNA_11: PlayerData("Anna", 11, False), Player.ART_11: PlayerData("Art", 11, False),
    Player.HANNA_11: PlayerData("Hanna", 11, False), Player.HORACE_11: PlayerData("Horace", 11, False),
    Player.JAN_11: PlayerData("Jan", 11, False), Player.KARIN_11: PlayerData("Karin", 11, False),
    Player.MIRYANNA_11: PlayerData("Miryanna", 11, False), Player.PATRICK_11: PlayerData("Patrick", 11, True),
    Player.PEPIJN_11: PlayerData("Pepijn", 11, False), Player.SOUNDOS_11: PlayerData("Soundos", 11, False),

    Player.ANNE_MARIE_12: PlayerData("Anne-Marie", 12, True), Player.DIO_12: PlayerData("Dio", 12, False),
    Player.FRITS_12: PlayerData("Frits", 12, False), Player.HADEWYCH_12: PlayerData("Hadewych", 12, False),
    Player.LIESBETH_12: PlayerData("Liesbeth", 12, False), Player.MAARTEN_12: PlayerData("Maarten", 12, False),
    Player.MARIT_12: PlayerData("Marit", 12, False), Player.MARION_12: PlayerData("Marion", 12, False),
    Player.TIM_12: PlayerData("Tim", 12, False), Player.WILLIAM_12: PlayerData("William", 12, False),

    Player.CAROLIEN_13: PlayerData("Carolien", 13, False), Player.DANIEL_13: PlayerData("Daniel", 13, False),
    Player.EWOUT_13: PlayerData("Ewout", 13, False), Player.JANINE_13: PlayerData("Janine", 13, False),
    Player.JOEP_13: PlayerData("Joep", 13, False), Player.KEES_13: PlayerData("Kees", 13, True),
    Player.PAULIEN_13: PlayerData("Paulien", 13, False), Player.TANIA_13: PlayerData("Tania", 13, False),
    Player.TIM_13: PlayerData("Tim", 13, False), Player.ZARAYDA_13: PlayerData("Zarayda", 13, False),

    Player.AAF_14: PlayerData("Aaf", 14, False), Player.DAPHNE_14: PlayerData("Daphne", 14, False),
    Player.FREEK_14: PlayerData("Freek", 14, False), Player.JAN_WILLEM_14: PlayerData("Jan-Willem", 14, False),
    Player.JENNIFER_14: PlayerData("Jennifer", 14, False), Player.MAURICE_14: PlayerData("Maurice", 14, False),
    Player.OWEN_14: PlayerData("Owen", 14, False), Player.SOFIE_14: PlayerData("Sofie", 14, False),
    Player.SUSAN_14: PlayerData("Susan", 14, True), Player.TYGO_14: PlayerData("Tygo", 14, False),

    Player.AJOUAD_15: PlayerData("Ajouad", 15, False), Player.CAROLINA_15: PlayerData("Carolina", 15, False),
    Player.CHRIS_15: PlayerData("Chris", 15, False), Player.EVELIEN_15: PlayerData("Evelien", 15, False),
    Player.MARGRIET_15: PlayerData("Margriet", 15, True), Player.MARLIJN_15: PlayerData("Marlijn", 15, False),
    Player.MARTINE_15: PlayerData("Martine", 15, False), Player.PIETER_15: PlayerData("Pieter", 15, False),
    Player.RIK_15: PlayerData("Rik", 15, False), Player.VIKTOR_15: PlayerData("Viktor", 15, False),

    Player.AIREN_16: PlayerData("Airen", 16, False), Player.ANNEMIEKE_16: PlayerData("Annemieke", 16, False),
    Player.CECILE_16: PlayerData("Cecile", 16, False), Player.ELLIE_16: PlayerData("Ellie", 16, False),
    Player.KLAAS_16: PlayerData("Klaas", 16, True), Player.MARJOLEIN_16: PlayerData("Marjolein", 16, False),
    Player.REMY_16: PlayerData("Remy", 16, False), Player.ROP_16: PlayerData("Rop", 16, False),
    Player.TAEKE_16: PlayerData("Taeke", 16, False), Player.TIM_16: PlayerData("Tim", 16, False),

    Player.DIEDERIK_17: PlayerData("Diederik", 17, False), Player.IMANUELLE_17: PlayerData("Imanuelle", 17, False),
    Player.JEROEN_17: PlayerData("Jeroen", 17, False), Player.JOCHEM_17: PlayerData("Jochem", 17, False),
    Player.ROOS_17: PlayerData("Roos", 17, False), Player.SANNE_17: PlayerData("Sanne", 17, False),
    Player.SIGRID_17: PlayerData("Sigrid", 17, False), Player.THOMAS_17: PlayerData("Thomas", 17, True),
    Player.VINCENT_17: PlayerData("Vincent", 17, False), Player.YVONNE_17: PlayerData("Yvonne", 17, False),

    Player.BELLA_18: PlayerData("Bella", 18, False), Player.EMILIO_18: PlayerData("Emilio", 18, False),
    Player.JAN_18: PlayerData("Jan", 18, True), Player.JEAN_MARC_18: PlayerData("Jean-Marc", 18, False),
    Player.LOES_18: PlayerData("Loes", 18, False), Player.OLCAY_18: PlayerData("Olcay", 18, False),
    Player.RON_18: PlayerData("Ron", 18, False), Player.RUBEN_18: PlayerData("Ruben", 18, False),
    Player.SIMONE_18: PlayerData("Simone", 18, False), Player.STINE_18: PlayerData("Stine", 18, False),

    Player.EVELIEN_19: PlayerData("Evelien", 19, False), Player.EVI_19: PlayerData("Evi", 19, False),
    Player.JAMIE_19: PlayerData("Jamie", 19, False), Player.MEREL_19: PlayerData("Merel", 19, True),
    Player.NIELS_19: PlayerData("Niels", 19, False), Player.NIKKIE_19: PlayerData("Nikkie", 19, False),
    Player.RICK_PAUL_19: PlayerData("Rick-Paul", 19, False), Player.ROBERT_19: PlayerData("Robert", 19, False),
    Player.SARAH_19: PlayerData("Sarah", 19, False), Player.SINAN_19: PlayerData("Sinan", 19, False),

    Player.ANITA_20: PlayerData("Anita", 20, False), Player.BUDDY_20: PlayerData("Buddy", 20, False),
    Player.CLAES_20: PlayerData("Claes", 20, False), Player.JAIKE_20: PlayerData("Jaike", 20, False),
    Player.JOHAN_20: PlayerData("Johan", 20, False), Player.LEONIE_20: PlayerData("Leonie", 20, False),
    Player.MILJUSCHKA_20: PlayerData("Miljuschka", 20, False), Player.NATHAN_20: PlayerData("Nathan", 20, False),
    Player.ROB_20: PlayerData("Rob", 20, True), Player.TINA_20: PlayerData("Tina", 20, False),

    Player.ELLIE_21: PlayerData("Ellie", 21, None), Player.HORACE_21: PlayerData("Horace", 21, None),
    Player.JEROEN_21: PlayerData("Jeroen", 21, None), Player.NADJA_21: PlayerData("Nadja", 21, None),
    Player.NIKKIE_21: PlayerData("Nikkie", 21, None), Player.PATRICK_21: PlayerData("Patrick", 21, None),
    Player.PEGGY_21: PlayerData("Peggy", 21, None), Player.RON_21: PlayerData("Ron", 21, None),
    Player.TINA_21: PlayerData("Tina", 21, None), Player.TYGO_21: PlayerData("Tygo", 21, None)
}

def get_name(player: Player) -> str:
    """ Get the first name of a given player. """
    return __ALL_PLAYER_DATA[player].name

def get_season(player: Player) -> int:
    """ Get the season in which a player participated. """
    return __ALL_PLAYER_DATA[player].season

def get_is_mol(player: Player) -> bool:
    """ Determine if a given player is the mol. """
    return __ALL_PLAYER_DATA[player].is_mol

def get_players_in_season(season: int) -> Set[Player]:
    """ Get all players that participated in a certain season. """
    return {player for player in Player if __ALL_PLAYER_DATA[player].season == season}

def get_mol_in_season(season: int) -> Player:
    """ Get the mol in a certain season. """
    for player in get_players_in_season(season):
        if get_is_mol(player):
            return player
    return None