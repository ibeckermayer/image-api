from app.operations import rotate, scale, crop, mirror, pipeline, color, brightness, contrast, sharpen, blur, maxFilter, minFilter, maxFilter, modeFilter, edge, Flip
from PIL import Image

class Shit(object):
    def __init__(self):
        print("I got inited!")
    pass

def giveMeShit():
    print("I got shitted")
    return Shit

print(giveMeShit())
print(giveMeShit()())

im = Image.open("kek.jpg")

rotated = pipeline(im, [
    # rotate(100), 
    # scale(1000, 500), 
    # crop((100, 0), (400, 500)), 
    # mirror(Flip.Horizontal), 
    # mirror(Flip.Vertical),
    # scale(None, 700),
    # color(0.1),
    # brightness(0.5),
    # contrast(5),
    # edge()
    maxFilter(3)
])

rotated.show()
