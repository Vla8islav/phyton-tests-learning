from math import pow
from math import sqrt


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def distance(self, p2):
        """Calculates the distance between the two points"""
        dx = self.x - p2.x
        dy = self.y - p2.y
        return sqrt(pow(dx, 2) + pow(dy, 2))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
