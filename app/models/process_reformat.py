# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util
from app.operations import *

class ProcessReformat(Process):
    def __init__(self, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessReformat - a model defined in Swagger

        :param name: The name of this ProcessReformat.  # noqa: E501
        :param array_of_parameter: The array_of_parameter of this ProcessReformat.  # noqa: E501
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
        super(ProcessReformat, self).__init__()
        super(ProcessReformat, self).__init__(requires_params=True,
                                                minimum_params=1,
                                                maximum_params=1,
                                                valid_params=[["format"]],
                                                param_type=str,
                                                operation=mirror)


    @classmethod
    def from_dict(cls, dikt) -> 'ProcessReformat':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Reformat of this ProcessReformat.  # noqa: E501
        :rtype: ProcessReformat
        """
        return util.deserialize_model(dikt, cls)

    def _make_operation(self):
        """fill out the operation with it's parameters"""
        return self._operation(str(self._array_of_parameter[0]["value"]))
