import math


class Stats:
    def __init__(self, values):
        if not isinstance(values, tuple):
            raise TypeError("values måste vara en tuple")

        if len(values) == 0:
            raise ValueError("values får inte vara tom")

        for v in values:
            if not isinstance(v, (int, float)):
                raise TypeError("alla värden måste vara tal")

        self.values = values

    def minimum(self):
        return min(self.values)

    def maximum(self):
        return max(self.values)

    def average(self):
        return sum(self.values) / len(self.values)

    def std(self):
        mean = self.average()
        variance = sum((x - mean) ** 2 for x in self.values) / len(self.values)
        return math.sqrt(variance)

    def summary(self):
        return {
            "min": self.minimum(),
            "avg": self.average(),
            "max": self.maximum(),
            "std": self.std(),
        }
