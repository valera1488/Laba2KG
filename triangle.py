from figure import FlatPolyhedron
from point import  Point

# треугольник
class Triangle(FlatPolyhedron):
    def __init__(self, point_a: Point, point_b: Point, point_c: Point, color: tuple, ):
        FlatPolyhedron.__init__(self, point_a, point_b, point_c, colour=color)
        self.point_a = point_a
        self.point_b = point_b
        self.point_c = point_c

    def rasterisation(self):
        left_bottom, size = self.get_bacground_rectagle()
        pixels_array = []
        x_a = self.point_a.x
        y_a = self.point_a.y
        x_b = self.point_b.x
        y_b = self.point_b.y
        x_c = self.point_c.x
        y_c = self.point_c.y
        x_0, y_0 = left_bottom
        for i in range(size[1]):
            for j in range(size[0]):
                if ((x_a - (x_0 + j))*(y_b - y_a) - (x_b - x_a)*(y_a - (y_0 + i)))\
                        * ((x_b - (x_0 + j))*(y_c - y_b) - (x_c - x_b) * (y_b - (y_0+i))) > 0 and \
                    ((x_a - (x_0 + j)) * (y_b - y_a) - (x_b - x_a) * (y_a - (y_0 + i))) \
                        * ((x_c - (x_0 + j)) * (y_a - y_c) - (x_a - x_c) * (y_c - (y_0 + i))) > 0 and \
                    ((x_b - (x_0 + j)) * (y_c - y_b) - (x_c - x_b) * (y_b - (y_0 + i))) \
                        * ((x_c - (x_0 + j)) * (y_a - y_c) - (x_a - x_c) * (y_c - (y_0 + i))) > 0:
                    pixels_array.append((x_0 + j, y_0 + i))
        pixels_array.extend(self._bresenhams_line_algorithm(x_a, y_a, x_b, y_b))
        pixels_array.extend(self._bresenhams_line_algorithm(x_b, y_b, x_c, y_c))
        pixels_array.extend(self._bresenhams_line_algorithm(x_c, y_c, x_a, y_a))
        return pixels_array

    def _bresenhams_line_algorithm(self, x1, y1, x2, y2):
        points_array = []
        dx = x2 - x1
        dy = y2 - y1
        sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
        sign_y = 1 if dy > 0 else -1 if dy < 0 else 0
        if dx < 0: dx = -dx
        if dy < 0: dy = -dy
        if dx > dy:
            pdx, pdy = sign_x, 0
            es, el = dy, dx
        else:
            pdx, pdy = 0, sign_y
            es, el = dx, dy
        x, y = x1, y1
        error, t = el / 2, 0
        points_array.append((x, y))
        while t < el:
            error -= es
            if error < 0:
                error += el
                x += sign_x
                y += sign_y
            else:
                x += pdx
                y += pdy
            t += 1
            points_array.append((x, y))
        return points_array