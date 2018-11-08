from operations import rotate, scale, crop, pipeline
from PIL import Image

im = Image.open("kek.jpg")
rotated = pipeline(im, [rotate(100), scale(1000, 500), crop(100, 100, 400, 400)])
rotated.show()
