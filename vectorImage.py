from PIL import Image
from PIL import ImageDraw
from numpy import array
from zBufferAlgorithm import ZBufferAlgorithm
from point import Point


# векторное изображение
class VectorImage:
    def __init__(self):
        self.__figures = []  # фигуры
        self.__size = array([0, 0])  # размер векторного изображения в текущем масштабе
        self.__delta = array([float('inf'), float('inf')])  # смещение, относительно начала координат

    def add_figure(self, figure):  # добавление фигуры
        left_bottom_point, size = figure.get_bacground_rectagle()
        if list(self.__size) == list(array([0, 0])):
            self.__size = size
            self.__delta = left_bottom_point
        else:
            if self.__delta[0] > left_bottom_point[0]:
                self.__size[0] += self.__delta[0] - left_bottom_point[0]
                self.__delta[0] = left_bottom_point[0]
            if self.__delta[1] > left_bottom_point[1]:
                self.__size[1] += self.__delta[1] - left_bottom_point[1]
                self.__delta[1] = left_bottom_point[1]
            if self.__size[0] < size[0] - left_bottom_point[0]:
                self.__size[0] += size[0] - left_bottom_point[0]
            if self.__size[1] < size[1] - left_bottom_point[1]:
                self.__size[1] += size[1] - left_bottom_point[1]
        self.__figures.append(figure)

    def draw(self, image_name):  # растеризация
        z_buffer = ZBufferAlgorithm(self.__size)
        for figure in self.__figures:
            z_buffer.addFigure(figure.move(Point(-self.__delta[0], -self.__delta[1], 0)))
        z_buffer.save_img(image_name)
        z_buffer.get_depth_map()
