import numpy as np

class MLE_Gradient:
    MAX_LEARNING_RATE = 2e-2
    MIN_CHANGE = 1e-3
    NUM_STEPS = 2000

    def gradient_ascend(self, data_points):
        coefs = self.get_start_coefs(data_points)
        for _ in range(self.NUM_STEPS):
            gradient = self.get_gradient(data_points, coefs)
            learning_rate = self.get_learning_rate(gradient)
            coefs += learning_rate * gradient
        return coefs

    def get_start_coefs(self, data_points):
        max_value = 0
        for dp in data_points:
            for value in dp[0]:
                max_value = max(max_value, value)
        start_value = 1 / (max_value * len(data_points[0][0]))
        return np.array([start_value] * len(data_points[0][0]))

    def get_learning_rate(self, gradient):
        max_value = max(abs(gradient))
        learning_rate = self.MIN_CHANGE / max_value
        return min(learning_rate, self.MAX_LEARNING_RATE)

    def get_gradient(self, data_points, coefs):
        gradient = []
        for i, coef in enumerate(coefs):
            gradient_value = 0
            for dp in data_points:
                sub_score = 0
                for value, coef in zip(dp[0], coefs):
                    sub_score += coef * value
                if dp[1]:
                    gradient_value += dp[0][i] / sub_score
                else:
                    gradient_value -= dp[0][i] / (1 - sub_score)
            gradient.append(gradient_value)
        return np.array(gradient)