# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util
from app.operations import *

class ProcessMinFilter(Process):
    def __init__(self, parameters: List[Parameter]=None):  # noqa: E501
        """ProcessMinFilter - a model defined in Swagger

        :param name: The name of this ProcessMinFilter.  # noqa: E501
        :param parameters: The parameters of this ProcessMinFilter.  # noqa: E501
        :type parameters: List[Parameter]
        """

        self._parameters = parameters
        super(ProcessMinFilter, self).__init__(valid_params=[["size"]],
                                               param_type=int,
                                               operation=minFilter)


    @classmethod
    def from_dict(cls, dikt) -> 'ProcessMinFilter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; minfilter of this ProcessMinFilter.  # noqa: E501
        :rtype: ProcessMinFilter
        """
        return util.deserialize_model(dikt, cls)

    def _make_operation(self):
        """fill out the operation with it's parameters"""
        return self._operation(int(self._parameters[0]["value"]))
