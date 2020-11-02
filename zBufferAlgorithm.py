from numpy import array
from PIL import Image
from PIL import ImageDraw
import copy

# z-буффер и кадр изображения
class ZBufferAlgorithm:
    def __init__(self, size):
        self._size = size
        self._buffer = array([[float('-inf') for j in range(size[0] + 1)] for i in range(size[1] + 1)])  # Z-буффер
        self._image = array([[(255, 255, 255) for j in range(size[0] + 1)] for i in range(size[1] + 1)])  # кадр

    def addFigure(self, figure):  # добавляет фигуру к изображению
        pixels = figure.rasterisation()
        for pixel in pixels:
            x, y = pixel
            if self._buffer[y][x] < figure.z(x, y):
                self._buffer[y][x] = figure.z(x, y)
                self._image[y][x] = figure.color

    def save_img(self, name):  # сохраняет кадр
        img = Image.new('RGB', tuple(self._size), color="white")
        draw = ImageDraw.Draw(img)
        for i in range(len(self._image)):
            for j in range(len(self._image[i])):
                draw.point((j, i), tuple(self._image[i][j]))
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.save(name, "PNG")

    def get_depth_map(self):
        depth_map = copy.deepcopy(self._buffer).tolist()
        for i in range(len(depth_map)):
            for j in range(len(depth_map[i])):
                if depth_map[i][j] == float('-inf'):
                    depth_map[i][j] = float('inf')
        minimum = min([min(line) for line in depth_map])
        for i in range(len(depth_map)):
            for j in range(len(depth_map[i])):
                depth_map[i][j] -= minimum
        maximum = max(max(filter(lambda x: x != float('inf'), line)) for line in depth_map)
        for i in range(len(depth_map)):
            for j in range(len(depth_map[i])):
                depth_map[i][j] *= (255 / maximum)
                if depth_map[i][j] == float('inf'):
                    depth_map[i][j] = 255
        for i in range(len(depth_map)):
            for j in range(len(depth_map[i])):
                depth_map[i][j] = (int(depth_map[i][j]), int(depth_map[i][j]), int(depth_map[i][j]))
        img = Image.new('RGB', tuple(self._size), color="white")
        draw = ImageDraw.Draw(img)
        for i in range(len(depth_map)):
            for j in range(len(depth_map[i])):
                draw.point((j, i), depth_map[i][j])
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img.save('depth_map.png', "PNG")
