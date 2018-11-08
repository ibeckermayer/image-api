from PIL.Image import Image, BICUBIC
from typing import Callable, Tuple, Union
from functools import reduce

def rotate(degrees: Union[int, float]) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.rotate(degrees)
    return closure

def scale(xsize: int, ysize: int) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.resize((xsize, ysize), BICUBIC)
    return closure

def crop(top: int, left: int, bottom: int, right: int) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.crop((left, top, right, bottom))
    return closure
        
def pipeline(image: Image, operations: [Callable[[Image], Image]]) -> Image:
    return reduce(lambda last, operation: operation(last), operations, image)
