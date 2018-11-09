from operations import rotate, scale, crop, mirror, pipeline, Flip
from PIL import Image

im = Image.open("kek.jpg")

rotated = pipeline(im, [
    rotate(100), 
    scale(1000, 500), 
    crop(100, 0, 400, 500), 
    mirror(Flip.Horizontal), 
    mirror(Flip.Vertical),
    scale(None, 700)
])

rotated.show()
