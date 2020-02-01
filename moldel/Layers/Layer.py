class Layer:
    """ A Layer computes the likelihood distribution which indicates how likely someone is the 'Mol'. """

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: set) -> dict:
        """ Compute the likelihood distribution which indicates how likely a player is the 'Mol'.

            Parameters:
                predict_season (int): The season number for which the likelihood distribution is computed
                    (the season started at 19 november 1999 is considered as season number 1).
                latest_episode (int): From the predict_season we only use episode data from episodes with number until
                    the latest_episode number as observation data. This also includes the entire episode data from the
                    episode with the latest_episode number. <br>
                    - Set this value to sys.maxsize if you want to use all episodes from the predict_season as
                    observation data.
                    - Set this value to 0 if you want to use no episodes from the predict_season as observation data.
                    (Which can be used to check the performance of only the pre-layers)
                train_seasons (set): A set of season number (int) which are used for training this layer.

            Returns:
                dict: A dictionary that contains the likelihood for each player that it is the 'Mol'. The key of this
                dictionary is a Player and the value is a float.
        """
        pass