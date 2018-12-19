# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from server.models.base_model_ import Model
from server.models.parameter import Parameter  # noqa: F401,E501
from server.models.process import Process  # noqa: F401,E501
from server import util
from server.operations import *

class ProcessMedianFilter(Process):
    def __init__(self, parameters: List[Parameter]=None):  # noqa: E501
        """ProcessMedianFilter - a model defined in Swagger

        :param name: The name of this ProcessMedianFilter.  # noqa: E501
        :param parameters: The parameters of this ProcessMedianFilter.  # noqa: E501
        :type parameters: List[Parameter]
        """

        self._parameters = parameters

        super(ProcessMedianFilter, self).__init__(valid_params=[["size"]],
                                                  param_type=int,
                                                  operation=medianFilter)

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessMedianFilter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; medianFilter of this ProcessMedianFilter.  # noqa: E501
        :rtype: ProcessMedianFilter
        """
        return util.deserialize_model(dikt, cls)

    def _make_operation(self):
        """fill out the operation with it's parameters"""
        return self._operation(int(self._parameters[0]["value"]))
