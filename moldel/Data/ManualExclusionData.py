from Data.Player import Player

# Exclusions is a dictionary with as keys the season numbers and as values a list of tuples where the first value
# in the tuple is the player and the second value is the episode from which on it is known that this player
# is not the Mol.
MANUAL_EXCLUSIONS = {9: [(Player.VIVIENNE_9, 9)], 10: [(Player.FRITS_10, 9)], 14: [(Player.FREEK_14, 9)]}