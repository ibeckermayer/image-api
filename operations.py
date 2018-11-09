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
    return lambda image: image.rotate(degrees)

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
    return lambda image: image.crop((left, top, right, bottom))

def mirror(method: Flip) -> Callable[[Image], Image]:
    return lambda image: image.transpose(method.value)

def color(factor: float) -> Callable[[Image], Image]:
    return _enhance(ImageEnhance.Color, factor)

def brightness(factor: float) -> Callable[[Image], Image]:
    return _enhance(ImageEnhance.Brightness, factor)

def contrast(factor: float) -> Callable[[Image], Image]:
    return _enhance(ImageEnhance.Contrast, factor)

def sharpen(factor: float) -> Callable[[Image], Image]:
    return _enhance(ImageEnhance.Sharpness, factor)

def blur(radius: int = 2) -> Callable[[Image], Image]:
    return lambda image: image.filter(ImageFilter.GaussianBlur(radius))

def maxFilter(size: int = 3) -> Callable[[Image], Image]:
    return lambda image: image.filter(ImageFilter.MaxFilter(size))

def minFilter(size: int = 3) -> Callable[[Image], Image]:
    return lambda image: image.filter(ImageFilter.MinFilter(size))

def modeFilter(size: int = 3) -> Callable[[Image], Image]:
    return lambda image: image.filter(ImageFilter.ModeFilter(size))

def medianFilter(size: int = 3) -> Callable[[Image], Image]:
    return lambda image: image.filter(ImageFilter.MedianFilter(size))

def edge() -> Callable[[Image], Image]:
    return lambda image: image.filter(ImageFilter.EDGE_ENHANCE)

def _enhance(enhancer, factor):
    return lambda image: enhancer(image).enhance(factor)

def pipeline(image: Image, operations: [Callable[[Image], Image]]) -> Image:
    return reduce(lambda last, operation: operation(last), operations, image)
