# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util
from app.operations import *

class ProcessScale(Process):
    def __init__(self, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessScale - a model defined in Swagger

        :param name: The name of this ProcessScale.  # noqa: E501
        :param array_of_parameter: The array_of_parameter of this ProcessScale.  # noqa: E501
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
        super(ProcessScale, self).__init__()
        super(ProcessScale, self).__init__(requires_params=True,
                                            minimum_params=1,
                                            maximum_params=2,
                                            valid_params=[("xsize", "ysize")],
                                            param_type=int,
                                            operation=scale)


    @classmethod
    def from_dict(cls, dikt) -> 'ProcessScale':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Scale of this ProcessScale.  # noqa: E501
        :rtype: ProcessScale
        """
        return util.deserialize_model(dikt, cls)

    def _make_operation(self):
        """fill out the operation with it's parameters"""
        for param in self._array_of_parameter:
            xsize = None
            ysize = None
            if param["parameter"] == "xsize":
                xsize = param["value"]
            elif param["parameter"] == "ysize":
                ysize = param["value"]
        if xsize and ysize:
            return self._operation(int(xsize), int(ysize))
        elif xsize:
            return self._operation(xsize=int(xsize))
        else:
            return self._operation(ysize=int(ysize))


