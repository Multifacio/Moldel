class Moldel:
    def __init__(self, layers, distribution_transformers):
        self.layers = layers
        self.distribution_transformers = distribution_transformers

    def compute_likelihood(self, predict_season: int, latest_episode: int, train_seasons: list):
        pass