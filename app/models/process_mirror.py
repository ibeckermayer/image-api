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
    def __init__(self, parameters: List[Parameter]=None):  # noqa: E501
        """ProcessMirror - a model defined in Swagger

        :param name: The name of this ProcessMirror.  # noqa: E501
        :param parameters: The parameters of this ProcessMirror.  # noqa: E501
        :type parameters: List[Parameter]
        """

        self._parameters = parameters
        super(ProcessMirror, self).__init__(valid_params=[["flip"]],
                                            param_type=str,
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
        if self._parameters[0]["value"] == "horizontal":
            return self._operation(Flip.Horizontal)
        elif self._parameters[0]["value"] == "vertical":
            return self._operation(Flip.Vertical)
        else:
            raise ValueError("In process Mirror, flip parameter must have value 'horizontal' or 'vertical'.")
