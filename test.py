from operations import rotate, scale, pipeline
from PIL import Image

im = Image.open("kek.jpg")
rotated = pipeline(im, [rotate(100), scale((1000, 500))])
rotated.show()
