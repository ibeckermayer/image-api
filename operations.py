from PIL.Image import Image, BICUBIC, FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM
from PIL import ImageEnhance
from PIL import ImageFilter
from typing import Callable, Tuple, Union
from functools import reduce
from enum import Enum

class Flip(Enum):
    Horizontal = FLIP_LEFT_RIGHT
    Vertical = FLIP_TOP_BOTTOM

def rotate(degrees: Union[int, float]) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.rotate(degrees)
    return closure

def scale(xsize: int = None, ysize: int = None) -> Callable[[Image], Image]:
    if not xsize and not ysize:
        raise ValueError("You must specify either an x dimension, a y dimension, or both")

    def closure(image: Image) -> Image:
        width, height = image.size
        absX = xsize or width * (ysize / height)
        absY = ysize or height * (xsize / width)
        return image.resize((int(round(absX)), int(round(absY))), BICUBIC)
    return closure

def crop(topleft: Tuple[int, int], bottomright: Tuple[int, int]) -> Callable[[Image], Image]:
    top, left = topleft
    bottom, right = bottomright
    def closure(image: Image) -> Image:
        return image.crop((left, top, right, bottom))
    return closure

def mirror(method: Flip) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.transpose(method.value)
    return closure

def color(factor: float) -> Callable[[Image], Image]:
    return _enhance(ImageEnhance.Color, factor)

def brightness(factor: float) -> Callable[[Image], Image]:
    return _enhance(ImageEnhance.Brightness, factor)

def contrast(factor: float) -> Callable[[Image], Image]:
    return _enhance(ImageEnhance.Contrast, factor)
    
def sharpen(factor: float) -> Callable[[Image], Image]:
    return _enhance(ImageEnhance.Sharpness, factor)

def blur(radius: int = 2) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.filter(ImageFilter.GaussianBlur(radius))
    return closure

def _enhance(enhancer, factor):
    def closure(image: Image) -> Image:
        return enhancer(image).enhance(factor)
    return closure

def pipeline(image: Image, operations: [Callable[[Image], Image]]) -> Image:
    return reduce(lambda last, operation: operation(last), operations, image)
