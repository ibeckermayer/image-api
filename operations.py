from PIL.Image import Image, BICUBIC
from typing import Callable, Tuple, Union
from functools import reduce

def rotate(degrees: Union[int, float]) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.rotate(degrees)
    return closure

def scale(xy: Tuple[int, int]) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.resize(xy, BICUBIC)
    return closure

def pipeline(image: Image, operations: [Callable[[Image], Image]]) -> Image:
    return reduce(lambda last, operation: operation(last), operations, image)
