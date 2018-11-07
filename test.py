from operations import rotate, scale
from PIL import Image
from functools import reduce

def pipeline(image, operations):
    return reduce((lambda last, operation: operation(last)), operations, image)

im = Image.open("kek.png")
rotated = pipeline(im, [rotate(100), scale((1000, 500))])

rotated.show()
