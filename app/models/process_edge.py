# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util


class ProcessEdge(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessEdge - a model defined in Swagger

        :param name: The name of this ProcessEdge.  # noqa: E501
        :type name: str
        :param array_of_parameter: The array_of_parameter of this ProcessEdge.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'ProcessEdge':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Edge of this ProcessEdge.  # noqa: E501
        :rtype: ProcessEdge
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this ProcessEdge.

        The name of image processing you want to preform. See Enum for array of supported processes.  # noqa: E501

        :return: The name of this ProcessEdge.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this ProcessEdge.

        The name of image processing you want to preform. See Enum for array of supported processes.  # noqa: E501

        :param name: The name of this ProcessEdge.
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
        """Gets the array_of_parameter of this ProcessEdge.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :return: The array_of_parameter of this ProcessEdge.
        :rtype: List[Parameter]
        """
        return self._array_of_parameter

    @array_of_parameter.setter
    def array_of_parameter(self, array_of_parameter: List[Parameter]):
        """Sets the array_of_parameter of this ProcessEdge.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :param array_of_parameter: The array_of_parameter of this ProcessEdge.
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
