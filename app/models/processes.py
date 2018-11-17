# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.process import Process  # noqa: F401,E501
from app import util

from PIL.Image import Image, BICUBIC, FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM
from PIL import ImageEnhance
from PIL import ImageFilter
from typing import Callable, Tuple, Union
from functools import reduce
from enum import Enum



class Processes(Model):
    def __init__(self, array_of_process: List[Process]=None):  # noqa: E501
        """Processes - a model defined in Swagger

        :param array_of_process: The array_of_process of this Processes.  # noqa: E501
        :type array_of_process: List[Process]
        """
        self.swagger_types = {
            'array_of_process': List[Process]
        }

        self.attribute_map = {
            'array_of_process': 'array_of_Process'
        }

        self._array_of_process = array_of_process

    @classmethod
    def from_dict(cls, dikt) -> 'Processes':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Processes of this Processes.  # noqa: E501
        :rtype: Processes
        """
        return util.deserialize_model(dikt, cls)

    @property
    def array_of_process(self) -> List[Process]:
        """Gets the array_of_process of this Processes.


        :return: The array_of_process of this Processes.
        :rtype: List[Process]
        """
        return self._array_of_process

    @array_of_process.setter
    def array_of_process(self, array_of_process: List[Process]):
        """Sets the array_of_process of this Processes.


        :param array_of_process: The array_of_process of this Processes.
        :type array_of_process: List[Process]
        """
        if array_of_process is None:
            raise ValueError("Invalid value for `array_of_process`, must not be `None`")  # noqa: E501

        self._array_of_process = array_of_process

    def run(self, image: Image):
        """verifies the Processes and then runs each of them on the image.
        """
        return self._pipeline(image, self._verify_processes_get_operations())

    def _pipeline(self, image: Image, operations: [Callable[[Image], Image]]) -> Image:
        return reduce(lambda last, operation: operation(last), operations, image)

    def _verify_processes_get_operations(self):
        """Verifies the validity of each Process in self._array_of_process

        :return: a list of operations to preform
        """
        operations = []
        for process in self._array_of_process:
            operations.append(process.verify_process_get_operation())
