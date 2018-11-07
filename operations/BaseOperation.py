from PIL import Image
from abc import ABCMeta, abstractmethod

class BaseOperation(object):
    @abstractmethod
    def process(self, image: Image) -> Image:
        pass
