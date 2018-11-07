from operations.RotateOperation import RotateOperation
from operations.ScaleOperation import ScaleOperation
from PIL import Image
from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


def pipeline(image, operations):
    return reduce((lambda last, operation: operation.process(last)), operations, image)

im = Image.open("kek.png")
rotate = RotateOperation(100)
scale = ScaleOperation((1000, 1000))
rotated = pipeline(im, [rotate, scale])

rotated.show()
