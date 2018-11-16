# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util


class ProcessBlur(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, list_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessBlur - a model defined in Swagger

        :param type: The type of this ProcessBlur.  # noqa: E501
        :type type: str
        :param list_of_parameter: The list_of_parameter of this ProcessBlur.  # noqa: E501
        :type list_of_parameter: List[Parameter]
        """
        self.swagger_types = {
            'type': str,
            'list_of_parameter': List[Parameter]
        }

        self.attribute_map = {
            'type': 'type',
            'list_of_parameter': 'list_of_Parameter'
        }

        self._type = type
        self._list_of_parameter = list_of_parameter

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessBlur':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Blur of this ProcessBlur.  # noqa: E501
        :rtype: ProcessBlur
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this ProcessBlur.

        The type of image processing you want to preform. See enum for list of supported processes.  # noqa: E501

        :return: The type of this ProcessBlur.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this ProcessBlur.

        The type of image processing you want to preform. See enum for list of supported processes.  # noqa: E501

        :param type: The type of this ProcessBlur.
        :type type: str
        """
        allowed_values = ["rotate", "scale", "crop", "mirror", "color", "brightness", "contrast", "sharpen", "blur", "maxFilter", "minFilter", "modeFilter", "medianFilter", "edge", "reformat"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def list_of_parameter(self) -> List[Parameter]:
        """Gets the list_of_parameter of this ProcessBlur.

        Parameter list to further specify the process, if necessary.  # noqa: E501

        :return: The list_of_parameter of this ProcessBlur.
        :rtype: List[Parameter]
        """
        return self._list_of_parameter

    @list_of_parameter.setter
    def list_of_parameter(self, list_of_parameter: List[Parameter]):
        """Sets the list_of_parameter of this ProcessBlur.

        Parameter list to further specify the process, if necessary.  # noqa: E501

        :param list_of_parameter: The list_of_parameter of this ProcessBlur.
        :type list_of_parameter: List[Parameter]
        """

        self._list_of_parameter = list_of_parameter
