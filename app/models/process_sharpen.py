# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util
from app.operations import *

class ProcessSharpen(Process):
    def __init__(self, parameters: List[Parameter]=None):  # noqa: E501
        """ProcessSharpen - a model defined in Swagger

        :param name: The name of this ProcessSharpen.  # noqa: E501
        :param parameters: The parameters of this ProcessSharpen.  # noqa: E501
        :type parameters: List[Parameter]
        """

        self._parameters = parameters
        super(ProcessSharpen, self).__init__(valid_params=[["factor"]],
                                             param_type=float,
                                             operation=sharpen)

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessSharpen':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Sharpen of this ProcessSharpen.  # noqa: E501
        :rtype: ProcessSharpen
        """
        return util.deserialize_model(dikt, cls)

    def _make_operation(self):
        """fill out the operation with it's parameters"""
        return self._operation(float(self._parameters[0]["value"]))
