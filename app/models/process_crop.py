# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util
from app.operations import *

class ProcessCrop(Process):
    def __init__(self, parameters: List[Parameter]=None):  # noqa: E501
        """ProcessCrop - a model defined in Swagger

        :param name: The name of this ProcessCrop.  # noqa: E501
        :param parameters: The parameters of this ProcessCrop.  # noqa: E501
        :type parameters: List[Parameter]
        """

        self._parameters = parameters
        super(ProcessCrop, self).__init__(valid_params=[["top_left_x"],
                                                        ["top_left_y"],
                                                        ["bottom_right_x"],
                                                        ["bottom_right_y"]],
                                          param_type=int,
                                          operation=crop)

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessCrop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Crop of this ProcessCrop.  # noqa: E501
        :rtype: ProcessCrop
        """
        return util.deserialize_model(dikt, cls)

    def _make_operation(self):
        """fill out the operation with it's parameters"""
        for param in self._parameters:
            if param["parameter"] == "top_left_x":
                top_left_x = int(param["value"])
            elif param["parameter"] == "top_left_y":
                top_left_y = int(param["value"])
            elif param["parameter"] == "bottom_right_x":
                bottom_right_x = int(param["value"])
            elif param["parameter"] == "bottom_right_y":
                bottom_right_y = int(param["value"])
        return self._operation((top_left_x, top_left_y), (bottom_right_x, bottom_right_y))

