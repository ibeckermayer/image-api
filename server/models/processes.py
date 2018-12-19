# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server.models.process import Process  # noqa: F401,E501
from server import util

from PIL.Image import Image, BICUBIC, FLIP_LEFT_RIGHT, FLIP_TOP_BOTTOM
from PIL import ImageEnhance
from PIL import ImageFilter
from typing import Callable, Tuple, Union
from functools import reduce
from enum import Enum



class Processes(Model):
    def __init__(self, processes: List[Process]=None):  # noqa: E501
        """Processes - a model defined in Swagger

        :param processes: The processes of this Processes.  # noqa: E501
        :type processes: List[Process]
        """
        self.swagger_types = {
            'processes': List[Process]
        }

        self.attribute_map = {
            'processes': 'processes'
        }

        self._processes = processes

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
    def processes(self) -> List[Process]:
        """Gets the processes of this Processes.


        :return: The processes of this Processes.
        :rtype: List[Process]
        """
        return self._processes

    @processes.setter
    def processes(self, processes: List[Process]):
        """Sets the processes of this Processes.


        :param processes: The processes of this Processes.
        :type processes: List[Process]
        """
        if processes is None:
            raise ValueError("Invalid value for `processes`, must not be `None`")  # noqa: E501

        self._processes = processes

    def run(self, image: Image):
        """verifies the Processes and then runs each of them on the image.
        """
        return self._pipeline(image, self._verify_processes_get_operations())

    def _pipeline(self, image: Image, operations: [Callable[[Image], Image]]) -> Image:
        return reduce(lambda last, operation: operation(last), operations, image)

    def _verify_processes_get_operations(self):
        """Verifies the validity of each Process in self._processes

        :return: a list of operations to preform
        """
        operations = []
        for process in self._processes:
            operations.server.nd(process.verify_process_get_operation())
