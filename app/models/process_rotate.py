# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util

class ProcessRotate(Process):
    def __init__(self, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessRotate - a model defined in Swagger

        :param name: The name of this ProcessRotate.  # noqa: E501
        :param array_of_parameter: The array_of_parameter of this ProcessRotate.  # noqa: E501
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
        super(ProcessRotate, self).__init__()

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessRotate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Rotate of this ProcessRotate.  # noqa: E501
        :rtype: ProcessRotate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def array_of_parameter(self) -> List[Parameter]:
        """Gets the array_of_parameter of this ProcessRotate.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :return: The array_of_parameter of this ProcessRotate.
        :rtype: List[Parameter]
        """
        return self._array_of_parameter

    @array_of_parameter.setter
    def array_of_parameter(self, array_of_parameter: List[Parameter]):
        """Sets the array_of_parameter of this ProcessRotate.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :param array_of_parameter: The array_of_parameter of this ProcessRotate.
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
