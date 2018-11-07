from PIL.Image import Image
from PIL.Image import BICUBIC
from typing import Callable, Tuple, Union

def rotate(degrees: Union[int, float]) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.rotate(degrees)
    return closure

def scale(xy: Tuple[int, int]) -> Callable[[Image], Image]:
    def closure(image: Image) -> Image:
        return image.resize(xy, BICUBIC)
    return closure