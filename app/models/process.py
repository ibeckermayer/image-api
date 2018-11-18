# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app import util

from PIL import Image

class Process(Model):
    def __init__(self):
        self.name = self.__class__.__name__

        self.swagger_types = {
            'name': str,
            'array_of_parameter': List[Parameter]
        }

        self.attribute_map = {
            'name': 'name',
            'array_of_parameter': 'array_of_Parameter'
        }

        self.validate()

    def validate(self):
        requirements = self.getRequirements()
        for name, predicate in requirements.items():
            if not predicate(Parameter.lookup(self._array_of_parameter, name)):
                raise ValueError(self.name + " invalid property [" + name + "]")

    def getRequirements(self):
        pass #abstract

    def apply(self, image: Image) -> Image:
        pass #abstract
            
    @property
    def array_of_parameter(self) -> List[Parameter]:
        """Gets the array_of_parameter of this ProcessBlur.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :return: The array_of_parameter of this ProcessBlur.
        :rtype: List[Parameter]
        """
        return self._array_of_parameter

    @array_of_parameter.setter
    def array_of_parameter(self, array_of_parameter: List[Parameter]):
        """Sets the array_of_parameter of this ProcessBlur.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :param array_of_parameter: The array_of_parameter of this ProcessBlur.
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
