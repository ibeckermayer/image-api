# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util
from app.operations import *

class ProcessEdge(Process):
    def __init__(self, parameters: List[Parameter]=None):  # noqa: E501
        """ProcessEdge - a model defined in Swagger

        :param name: The name of this ProcessEdge.  # noqa: E501
        :param parameters: The parameters of this ProcessEdge.  # noqa: E501
        :type parameters: List[Parameter]
        """

        self._parameters = parameters
        super(ProcessEdge, self).__init__(valid_params=None,
                                          param_type=None,
                                          operation=edge)


    @classmethod
    def from_dict(cls, dikt) -> 'ProcessEdge':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Edge of this ProcessEdge.  # noqa: E501
        :rtype: ProcessEdge
        """
        return util.deserialize_model(dikt, cls)

    def _make_operation(self):
        """fill out the operation with it's parameters"""
        return self._operation()
