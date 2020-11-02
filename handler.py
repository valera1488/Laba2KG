from rectangle import Rectangle
from triangle import Triangle
from point import Point

# обработчик
class ImgHandler:
    def __init__(self, vector_img):
        self._vector_img = vector_img

    def get_info(self, file_name):
        with open(file_name) as file:  # читаем файл со входными данными
            text = file.read().split('\n')
            for string in text:
                figure_type, point_a, point_b, point_c, color = string.split('; ')
                for symbol in tuple(chr(code) for code in range(65, 123)) + (',', '(', ')'):
                    point_a = point_a.replace(symbol, '')
                    point_b = point_b.replace(symbol, '')
                    point_c = point_c.replace(symbol, '')
                    color = color.replace(symbol, '')
                point_a = tuple(int(number) for number in point_a.split())
                point_b = tuple(int(number) for number in point_b.split())
                point_c = tuple(int(number) for number in point_c.split())
                color = tuple(int(number) for number in color.split())
                if figure_type == 'Triangle':  # создаем на их основе фигуры
                    figure = Triangle(Point(point_a[0], point_a[1], point_a[2]), Point(point_b[0], point_b[1], point_b[2]),\
                             Point(point_c[0], point_c[1], point_c[2]), color)
                    self._vector_img.add_figure(figure)
                if figure_type == 'Rectangle':
                    figure = Rectangle(Point(point_a[0], point_a[1], point_a[2]), Point(point_b[0], point_b[1], point_b[2]),\
                             Point(point_c[0], point_c[1], point_c[2]), color)
                    self._vector_img.add_figure(figure)  # передаем в вектор

    def run(self, file_name):  # растеризация
        self._vector_img.draw(file_name)
