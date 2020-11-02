from vectorImage import  VectorImage
from handler import ImgHandler


if __name__ == '__main__':
    img = VectorImage()
    handler = ImgHandler(img)
    handler.get_info('input.txt')
    handler.run('test.png')