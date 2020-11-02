from point import Point
from numpy import array
import copy

# класс описывающий плоский многогранник
# для ее задания будет использоваться минимум 3 точки
class FlatPolyhedron:
    def __init__(self, point_a: Point, point_b: Point, point_c: Point, colour=(255, 255, 255)):
        self.color = colour
        self._vertices = [point_a, point_b, point_c]  # хранит все ребра фигуры
        v1 = point_b - point_a  # здесь происходит рассчет функции z(x, y), которая выражена через уравнение плоскости
        v2 = point_c - point_a  # полученное как раз по тем трем точкам, которые мы передали в качестве параметров
        v3 = Point(v1.y * v2.z - v1.z * v2.y, v1.z * v2.x - v1.x * v2.z,\
                       v1.x * v2.y - v1.y * v2.x)
        self.__z_function = lambda x, y: (-v3.x * (x - point_a.x) - v3.y * (y - point_a.y) + v3.z * point_a.z) / v3.z

    def rasterisation(self):
        pass

    def get_bacground_rectagle(self):  # получает прямоугольник, который оисывает эту фигуру
        max_x = max(self._vertices, key=lambda point: point.x).x
        min_x = min(self._vertices, key=lambda point: point.x).x
        max_y = max(self._vertices, key=lambda point: point.y).y
        min_y = min(self._vertices, key=lambda point: point.y).y
        return array([min_x, min_y]), array([max_x - min_x, max_y - min_y])  # left-top point, size

    def z(self, x, y):  # z = f(x, y)
        return self.__z_function(x, y)

    def move(self, delta):  # перемещение фигуры по вектору
        new_figure = copy.deepcopy(self)
        for vertex in new_figure._vertices:
            vertex.x = (vertex + delta).x
            vertex.y = (vertex + delta).y
            vertex.z = (vertex + delta).z
        return new_figure