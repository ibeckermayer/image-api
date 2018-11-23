# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util
from app.operations import *


class ProcessMirror(Process):
    def __init__(self, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessMirror - a model defined in Swagger

        :param name: The name of this ProcessMirror.  # noqa: E501
        :param array_of_parameter: The array_of_parameter of this ProcessMirror.  # noqa: E501
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
        super(ProcessMirror, self).__init__(requires_params=False,
                                            minimum_params=None,
                                            maximum_params=None,
                                            valid_params=None,
                                            param_type=None,
                                            operation=mirror)

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessMirror':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Mirror of this ProcessMirror.  # noqa: E501
        :rtype: ProcessMirror
        """
        return util.deserialize_model(dikt, cls)

    def _make_operation(self):
        return self._operation()
