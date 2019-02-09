from math import pow
from math import sqrt


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


def distance(p1, p2):
    """Calculates the distance between the two dots"""
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return sqrt(pow(dx, 2) + pow(dy, 2))


print(distance(Point(0, 0), Point(1, 1)))
