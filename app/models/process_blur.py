# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util
from app.operations import *

class ProcessBlur(Process):
    def __init__(self, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessBlur - a model defined in Swagger

        :param name: The name of this ProcessBlur.  # noqa: E501
        :param array_of_parameter: The array_of_parameter of this ProcessBlur.  # noqa: E501
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
        super(ProcessBlur, self).__init__(requires_params=True,
                                                minimum_params=1,
                                                maximum_params=1,
                                                valid_params=[["radius"]],
                                                param_type=float,
                                                operation=blur)

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessBlur':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Blur of this ProcessBlur.  # noqa: E501
        :rtype: ProcessBlur
        """
        return util.deserialize_model(dikt, cls)

    def _make_operation(self):
        """fill out the operation with it's parameters"""
        return self._operation(float(self._array_of_parameter[0]["value"]))
