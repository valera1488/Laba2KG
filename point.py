from math import sqrt

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def coordinates(self):
        return (self.x, self.y, self.z)

    @staticmethod
    def len(point_a, point_b):
        return sqrt((point_a.x - point_b.x)**2 + (point_a.y - point_b.y)**2 + (point_a.z - point_b.z)**2)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)