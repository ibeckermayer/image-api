from operations.BaseOperation import BaseOperation
from PIL import Image

class RotateOperation(BaseOperation):
    def __init__(self, degrees):
        self.degrees = degrees
        super().__init__()

    def process(self, image: Image) -> Image:
        return image.rotate(self.degrees)