from point import Point
from triangle import Triangle

# класс прямоугольного параллелепипеда
class Rectangle(Triangle):
    def __init__(self, point_a: Point, point_b: Point, point_c: Point, colour):
        Triangle.__init__(self, point_a, point_b, point_c, colour)
        x = point_a.x - point_b.x + point_c.x
        y = point_a.y - point_b.y + point_c.y
        z = point_a.z - point_b.z + point_c.z
        self.point_d = Point(x, y, z)
        self._vertices.append(self.point_d)

    def rasterisation(self):  # растр строится как объединение растра задающего его трекгольника
        point_array = []  # и второго треугольника, который объединяясь с первым формирует параллелепипед
        point_array.extend(Triangle.rasterisation(self))
        point_array.extend(Triangle(self.point_a, self.point_d, self.point_c, self.color).rasterisation())
        return point_array
