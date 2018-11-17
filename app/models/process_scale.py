# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util


class ProcessScale(Model):
    def __init__(self, name: str=None, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessScale - a model defined in Swagger

        :param name: The name of this ProcessScale.  # noqa: E501
        :type name: str
        :param array_of_parameter: The array_of_parameter of this ProcessScale.  # noqa: E501
        :type array_of_parameter: List[Parameter]
        """
        self.swagger_types = {
            'name': str,
            'array_of_parameter': List[Parameter]
        }

        self.attribute_map = {
            'name': 'name',
            'array_of_parameter': 'array_of_Parameter'
        }

        self._name = name
        self._array_of_parameter = array_of_parameter

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessScale':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Scale of this ProcessScale.  # noqa: E501
        :rtype: ProcessScale
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ProcessScale.

        The name of image processing you want to preform. See Enum for array of supported processes.  # noqa: E501

        :return: The name of this ProcessScale.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ProcessScale.

        The name of image processing you want to preform. See Enum for array of supported processes.  # noqa: E501

        :param name: The name of this ProcessScale.
        :type name: str
        """
        allowed_values = ["Rotate", "Scale", "Crop", "Mirror", "Color", "Brightness", "Contrast", "Sharpen", "Blur", "maxFilter", "minFilter", "modeFilter", "medianFilter", "Edge", "Reformat"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def array_of_parameter(self) -> List[Parameter]:
        """Gets the array_of_parameter of this ProcessScale.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :return: The array_of_parameter of this ProcessScale.
        :rtype: List[Parameter]
        """
        return self._array_of_parameter

    @array_of_parameter.setter
    def array_of_parameter(self, array_of_parameter: List[Parameter]):
        """Sets the array_of_parameter of this ProcessScale.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :param array_of_parameter: The array_of_parameter of this ProcessScale.
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
