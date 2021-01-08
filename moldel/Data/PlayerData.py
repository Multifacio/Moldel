from Data.Player import Player
from typing import NamedTuple, Union, Set

PlayerData = NamedTuple("PlayerData", [("name", str), ("season", int), ("is_mol", Union[bool, None]), ("age", int)])

# This variable contains the first name of every player, the season in which every player participated and which player
# is the Mol. If the is_mol value of a player is set to None then it is unknown whether that player is the Mol. Moreover
# the age of every player when the first episode was broadcast of the season in which that player participated. Or if
# the players birthdate is unknown, the age revealed during the season.
__ALL_PLAYER_DATA = {
    Player.ARNOUD_1: PlayerData("Arnoud", 1, False, 52), Player.DEBORAH_1: PlayerData("Deborah", 1, True, 34),
    Player.FOKE_1: PlayerData("Foke", 1, False, 56), Player.JOHN_1: PlayerData("John", 1, False, 37),
    Player.PETRA_1: PlayerData("Petra", 1, False, 22), Player.ROBIN_1: PlayerData("Robin", 1, False, 29),
    Player.SANDY_1: PlayerData("Sandy", 1, False, 27), Player.WARNER_1: PlayerData("Warner", 1, False, 30),
    Player.WILLY_1: PlayerData("Willy", 1, False, 44), Player.WILMIE_1: PlayerData("Wilmie", 1, False, 43),

    Player.BJORN_2: PlayerData("Björn", 2, False, 26), Player.COR_2: PlayerData("Cor", 2, False, 61),
    Player.DAN_2: PlayerData("Dan", 2, False, 32), Player.DOORTJE_2: PlayerData("Doortje", 2, False, 22),
    Player.GERDA_2: PlayerData("Gerda", 2, False, 48), Player.NAZIFE_2: PlayerData("Nazife", 2, False, 30),
    Player.NICO_2: PlayerData("Nico", 2, True, 35), Player.SIGRID_2: PlayerData("Sigrid", 2, False, 27),
    Player.WARD_2: PlayerData("Ward", 2, False, 26), Player.YVONNE_2: PlayerData("Yvonne", 2, False, 32),

    Player.DICK_3: PlayerData("Dick", 3, False, 50), Player.ELLEN_3: PlayerData("Ellen", 3, False, 37),
    Player.ERIK_3: PlayerData("Erik", 3, False, 47), Player.GEORGE_3: PlayerData("George", 3, True, 30),
    Player.HARRY_3: PlayerData("Harry", 3, False, 39), Player.JANTIEN_3: PlayerData("Jantien", 3, False, 35),
    Player.JOHN_3: PlayerData("John", 3, False, 27), Player.KAREN_3: PlayerData("Karen", 3, False, 33),
    Player.KERSTIN_3: PlayerData("Kerstin", 3, False, 36), Player.PAMELA_3: PlayerData("Paméla", 3, False, 26),
    Player.PRINCE_3: PlayerData("Prince", 3, False, 26),

    Player.AAFKE_4: PlayerData("Aafke", 4, False, 40), Player.ASTRID_4: PlayerData("Astrid", 4, False, 44),
    Player.CHANDRIKA_4: PlayerData("Chandrika", 4, False, 26), Player.ELISE_4: PlayerData("Elise", 4, True, 26),
    Player.FERDI_4: PlayerData("Ferdi", 4, False, 27), Player.JULIEN_4: PlayerData("Julien", 4, False, 30),
    Player.LOUIS_4: PlayerData("Louis", 4, False, 38), Player.PATRICIA_4: PlayerData("Patricia", 4, False, 39),
    Player.RENE_4: PlayerData("René", 4, False, 37), Player.RON_4: PlayerData("Ron", 4, False, 33),

    Player.GIJS_5: PlayerData("Gijs", 5, False, 38), Player.ISABELLE_5: PlayerData("Isabelle", 5, False, 32),
    Player.JIM_5: PlayerData("Jim", 5, False, 32), Player.LOTTIE_5: PlayerData("Lottie", 5, False, 27),
    Player.MARC_MARIE_5: PlayerData("Marc-Marie", 5, False, 40), Player.ROELAND_5: PlayerData("Roeland", 5, False, 32),
    Player.SANDER_5: PlayerData("Sander", 5, False, 29), Player.VICTORIA_5: PlayerData("Victoria", 5, False, 24),
    Player.YVON_5: PlayerData("Yvon", 5, True, 31), Player.YVONNE_5: PlayerData("Yvonne", 5, False, 45),

    Player.CHRIS_6: PlayerData("Chris", 6, False, 44), Player.FREDERIQUE_6: PlayerData("Frederique", 6, False, 38),
    Player.GEERT_6: PlayerData("Geert", 6, False, 22), Player.LIZ_6: PlayerData("Liz", 6, False, 50),
    Player.MARY_LOU_6: PlayerData("Mary-Lou", 6, False, 42), Player.MILOUSKA_6: PlayerData("Milouska", 6, True, 32),
    Player.PEGGY_6: PlayerData("Peggy", 6, False, 29), Player.RICHARD_6: PlayerData("Richard", 6, False, 33),
    Player.RODERICK_6: PlayerData("Roderick", 6, False, 41), Player.TOINE_6: PlayerData("Toine", 6, False, 38),

    Player.ALEX_7: PlayerData("Alex", 7, False, 30), Player.DICK_7: PlayerData("Dick", 7, False, 50),
    Player.EVA_7: PlayerData("Eva", 7, False, 29), Player.INGE_7: PlayerData("Inge", 7, True, 49),
    Player.LIESBETH_7: PlayerData("Liesbeth", 7, False, 31), Player.MENNO_7: PlayerData("Menno", 7, False, 39),
    Player.NADJA_7: PlayerData("Nadja", 7, False, 34), Player.PAUL_7: PlayerData("Paul", 7, False, 27),
    Player.RENATE_7: PlayerData("Renate", 7, False, 27), Player.SANDER_7: PlayerData("Sander", 7, False, 30),

    Player.ANNETTE_8: PlayerData("Annette", 8, False, 51), Player.COEN_8: PlayerData("Coen", 8, False, 27),
    Player.DENNIS_8: PlayerData("Dennis", 8, True, 30), Player.DUNYA_8: PlayerData("Dunya", 8, False, 26),
    Player.EDO_8: PlayerData("Edo", 8, False, 37), Player.GEORGINA_8: PlayerData("Georgina", 8, False, 28),
    Player.JORIS_8: PlayerData("Joris", 8, False, 41), Player.NICOLETTE_8: PlayerData("Nicolette", 8, False, 23),
    Player.PATRICK_8: PlayerData("Patrick", 8, False, 29), Player.REGINA_8: PlayerData("Regina", 8, False, 31),

    Player.ANNIEK_9: PlayerData("Anniek", 9, False, 31), Player.DENNIS_9: PlayerData("Dennis", 9, False, 23),
    Player.FROUKJE_9: PlayerData("Froukje", 9, False, 32), Player.HANS_9: PlayerData("Hans", 9, False, 48),
    Player.JON_9: PlayerData("Jon", 9, True, 48), Player.PAULA_9: PlayerData("Paula", 9, False, 41),
    Player.RICK_9: PlayerData("Rick", 9, False, 49), Player.SEBASTIAAN_9: PlayerData("Sebastiaan", 9, False, 37),
    Player.VERA_9: PlayerData("Vera", 9, False, 45), Player.VIVIENNE_9: PlayerData("Vivienne", 9, False, 25),

    Player.ARJEN_10: PlayerData("Arjen", 10, False, 30), Player.BARBARA_10: PlayerData("Barbara", 10, False, 35),
    Player.ERIK_10: PlayerData("Erik", 10, False, 46), Player.FRITS_10: PlayerData("Frits", 10, False, 46),
    Player.HIND_10: PlayerData("Hind", 10, False, 25), Player.KIM_10: PlayerData("Kim", 10, True, 30),
    Player.LORETTA_10: PlayerData("Loretta", 10, False, 53), Player.MANUEL_10: PlayerData("Manuel", 10, False, 33),
    Player.SANNE_10: PlayerData("Sanne", 10, False, 25), Player.TIM_10: PlayerData("Tim", 10, False, 29),

    Player.ANNA_11: PlayerData("Anna", 11, False, 27), Player.ART_11: PlayerData("Art", 11, False, 36),
    Player.HANNA_11: PlayerData("Hanna", 11, False, 26), Player.HORACE_11: PlayerData("Horace", 11, False, 39),
    Player.JAN_11: PlayerData("Jan", 11, False, 29), Player.KARIN_11: PlayerData("Karin", 11, False, 47),
    Player.MIRYANNA_11: PlayerData("Miryanna", 11, False, 43), Player.PATRICK_11: PlayerData("Patrick", 11, True, 43),
    Player.PEPIJN_11: PlayerData("Pepijn", 11, False, 34), Player.SOUNDOS_11: PlayerData("Soundos", 11, False, 29),

    Player.ANNE_MARIE_12: PlayerData("Anne-Marie", 12, True, 35), Player.DIO_12: PlayerData("Dio", 12, False, 23),
    Player.FRITS_12: PlayerData("Frits", 12, False, 43), Player.HADEWYCH_12: PlayerData("Hadewych", 12, False, 35),
    Player.LIESBETH_12: PlayerData("Liesbeth", 12, False, 38), Player.MAARTEN_12: PlayerData("Maarten", 12, False, 30),
    Player.MARIT_12: PlayerData("Marit", 12, False, 40), Player.MARION_12: PlayerData("Marion", 12, False, 38),
    Player.TIM_12: PlayerData("Tim", 12, False, 32), Player.WILLIAM_12: PlayerData("William", 12, False, 28),

    Player.CAROLIEN_13: PlayerData("Carolien", 13, False, 29), Player.DANIEL_13: PlayerData("Daniel", 13, False, 43),
    Player.EWOUT_13: PlayerData("Ewout", 13, False, 27), Player.JANINE_13: PlayerData("Janine", 13, False, 36),
    Player.JOEP_13: PlayerData("Joep", 13, False, 52), Player.KEES_13: PlayerData("Kees", 13, True, 30),
    Player.PAULIEN_13: PlayerData("Paulien", 13, False, 36), Player.TANIA_13: PlayerData("Tania", 13, False, 36),
    Player.TIM_13: PlayerData("Tim", 13, False, 31), Player.ZARAYDA_13: PlayerData("Zarayda", 13, False, 30),

    Player.AAF_14: PlayerData("Aaf", 14, False, 38), Player.DAPHNE_14: PlayerData("Daphne", 14, False, 40),
    Player.FREEK_14: PlayerData("Freek", 14, False, 27), Player.JAN_WILLEM_14: PlayerData("Jan-Willem", 14, False, 36),
    Player.JENNIFER_14: PlayerData("Jennifer", 14, False, 33), Player.MAURICE_14: PlayerData("Maurice", 14, False, 27),
    Player.OWEN_14: PlayerData("Owen", 14, False, 46), Player.SOFIE_14: PlayerData("Sofie", 14, False, 33),
    Player.SUSAN_14: PlayerData("Susan", 14, True, 48), Player.TYGO_14: PlayerData("Tygo", 14, False, 39),

    Player.AJOUAD_15: PlayerData("Ajouad", 15, False, 27), Player.CAROLINA_15: PlayerData("Carolina", 15, False, 34),
    Player.CHRIS_15: PlayerData("Chris", 15, False, 43), Player.EVELIEN_15: PlayerData("Evelien", 15, False, 33),
    Player.MARGRIET_15: PlayerData("Margriet", 15, True, 44), Player.MARLIJN_15: PlayerData("Marlijn", 15, False, 31),
    Player.MARTINE_15: PlayerData("Martine", 15, False, 44), Player.PIETER_15: PlayerData("Pieter", 15, False, 30),
    Player.RIK_15: PlayerData("Rik", 15, False, 43), Player.VIKTOR_15: PlayerData("Viktor", 15, False, 43),

    Player.AIREN_16: PlayerData("Airen", 16, False, 30), Player.ANNEMIEKE_16: PlayerData("Annemieke", 16, False, 36),
    Player.CECILE_16: PlayerData("Cecile", 16, False, 45), Player.ELLIE_16: PlayerData("Ellie", 16, False, 49),
    Player.KLAAS_16: PlayerData("Klaas", 16, True, 43), Player.MARJOLEIN_16: PlayerData("Marjolein", 16, False, 53),
    Player.REMY_16: PlayerData("Remy", 16, False, 26), Player.ROP_16: PlayerData("Rop", 16, False, 41),
    Player.TAEKE_16: PlayerData("Taeke", 16, False, 35), Player.TIM_16: PlayerData("Tim", 16, False, 27),

    Player.DIEDERIK_17: PlayerData("Diederik", 17, False, 32), Player.IMANUELLE_17: PlayerData("Imanuelle", 17, False, 31),
    Player.JEROEN_17: PlayerData("Jeroen", 17, False, 42), Player.JOCHEM_17: PlayerData("Jochem", 17, False, 53),
    Player.ROOS_17: PlayerData("Roos", 17, False, 41), Player.SANNE_17: PlayerData("Sanne", 17, False, 45),
    Player.SIGRID_17: PlayerData("Sigrid", 17, False, 23), Player.THOMAS_17: PlayerData("Thomas", 17, True, 32),
    Player.VINCENT_17: PlayerData("Vincent", 17, False, 32), Player.YVONNE_17: PlayerData("Yvonne", 17, False, 30),

    Player.BELLA_18: PlayerData("Bella", 18, False, 27), Player.EMILIO_18: PlayerData("Emilio", 18, False, 36),
    Player.JAN_18: PlayerData("Jan", 18, True, 32), Player.JEAN_MARC_18: PlayerData("Jean-Marc", 18, False, 50),
    Player.LOES_18: PlayerData("Loes", 18, False, 36), Player.OLCAY_18: PlayerData("Olcay", 18, False, 37),
    Player.RON_18: PlayerData("Ron", 18, False, 54), Player.RUBEN_18: PlayerData("Ruben", 18, False, 35),
    Player.SIMONE_18: PlayerData("Simone", 18, False, 46), Player.STINE_18: PlayerData("Stine", 18, False, 45),

    Player.EVELIEN_19: PlayerData("Evelien", 19, False, 44), Player.EVI_19: PlayerData("Evi", 19, False, 40),
    Player.JAMIE_19: PlayerData("Jamie", 19, False, 28), Player.MEREL_19: PlayerData("Merel", 19, True, 39),
    Player.NIELS_19: PlayerData("Niels", 19, False, 29), Player.NIKKIE_19: PlayerData("Nikkie", 19, False, 24),
    Player.RICK_PAUL_19: PlayerData("Rick-Paul", 19, False, 37), Player.ROBERT_19: PlayerData("Robert", 19, False, 57),
    Player.SARAH_19: PlayerData("Sarah", 19, False, 32), Player.SINAN_19: PlayerData("Sinan", 19, False, 41),

    Player.ANITA_20: PlayerData("Anita", 20, False, 58), Player.BUDDY_20: PlayerData("Buddy", 20, False, 25),
    Player.CLAES_20: PlayerData("Claes", 20, False, 42), Player.JAIKE_20: PlayerData("Jaike", 20, False, 42),
    Player.JOHAN_20: PlayerData("Johan", 20, False, 37), Player.LEONIE_20: PlayerData("Leonie", 20, False, 39),
    Player.MILJUSCHKA_20: PlayerData("Miljuschka", 20, False, 34), Player.NATHAN_20: PlayerData("Nathan", 20, False, 36),
    Player.ROB_20: PlayerData("Rob", 20, True, 33), Player.TINA_20: PlayerData("Tina", 20, False, 44),

    Player.ELLIE_21: PlayerData("Ellie", 21, False, 54), Player.HORACE_21: PlayerData("Horace", 21, False, 48),
    Player.JEROEN_21: PlayerData("Jeroen", 21, True, 46), Player.NADJA_21: PlayerData("Nadja", 21, False, 48),
    Player.NIKKIE_21: PlayerData("Nikkie", 21, False, 26), Player.PATRICK_21: PlayerData("Patrick", 21, False, 42),
    Player.PEGGY_21: PlayerData("Peggy", 21, False, 43), Player.RON_21: PlayerData("Ron", 21, False, 56),
    Player.TINA_21: PlayerData("Tina", 21, False, 45), Player.TYGO_21: PlayerData("Tygo", 21, False, 46),

    Player.CHARLOTTE_22: PlayerData("Charlotte", 22, None, 32), Player.ERIK_22: PlayerData("Erik", 22, None, 63),
    Player.FLORENTIJN_22: PlayerData("Florentijn", 22, None, 43), Player.JOSHUA_22: PlayerData("Joshua", 22, None, 32),
    Player.LAKSHMI_22: PlayerData("Lakshmi", 22, None, 27), Player.MARIJE_22: PlayerData("Marije", 22, None, 33),
    Player.RENEE_22: PlayerData("Renée", 22, None, 59), Player.REMCO_22: PlayerData("Remco", 22, None, 47),
    Player.ROCKY_22: PlayerData("Rocky", 22, None, 36), Player.SPLINTER_22: PlayerData("Splinter", 22, None, 24)
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

def get_age(player: Player) -> int:
    """ Get the age of a given player when the first episode of his/her season was broadcast. """
    return __ALL_PLAYER_DATA[player].age

def get_players_in_season(season: int) -> Set[Player]:
    """ Get all players that participated in a certain season. """
    return {player for player in Player if __ALL_PLAYER_DATA[player].season == season}

def get_mol_in_season(season: int) -> Player:
    """ Get the mol in a certain season. """
    for player in get_players_in_season(season):
        if get_is_mol(player):
            return player
    return None