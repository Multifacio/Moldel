# The Last Episodes dictionary stores the last episode (final episode) for each season. This should be filled in for
# all seasons that are used as train data.
LAST_EPISODES = {5: 8, 6: 9, 7: 9, 8: 9, 9: 9, 10: 9, 11: 10, 12: 9, 13: 9, 14: 9, 15: 9, 16: 9, 17: 9, 18: 9, 19: 9,
                 20: 9, 21: 7}

def get_last_episode(season: int) -> int:
    return LAST_EPISODES[season]