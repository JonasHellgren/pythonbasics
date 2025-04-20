import numpy as np

class Sigmoid:
    def __init__(self):
        pass  # No special setup needed for now

    def compute(self, x):
        return 1 / (1 + np.exp(-x))

    def derivative(self, x):
        s = self.compute(x)
        return s * (1 - s)