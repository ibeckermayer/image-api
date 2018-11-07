from operations.BaseOperation import BaseOperation
from PIL import Image

class ScaleOperation(BaseOperation):
    def __init__(self, xy):
        self.xy = xy
        super().__init__()

    def process(self, image: Image) -> Image:
        return image.resize(self.xy, Image.BICUBIC)