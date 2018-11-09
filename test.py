from operations import rotate, scale, crop, mirror, pipeline, color, brightness, contrast, sharpen, blur, maxFilter, minFilter, maxFilter, modeFilter, Flip
from PIL import Image

im = Image.open("kek.jpg")

rotated = pipeline(im, [
    rotate(100), 
    scale(1000, 500), 
    crop((100, 0), (400, 500)), 
    mirror(Flip.Horizontal), 
    mirror(Flip.Vertical),
    scale(None, 700),
    color(0.1),
    brightness(0.5),
    contrast(5),
    sharpen(10),
    maxFilter(15),
    blur(2)
])

rotated.show()
