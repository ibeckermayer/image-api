# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util


class ProcessCrop(Process):
    def __init__(self, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessCrop - a model defined in Swagger

        :param name: The name of this ProcessCrop.  # noqa: E501
        :param array_of_parameter: The array_of_parameter of this ProcessCrop.  # noqa: E501
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
        super(ProcessCrop, self).__init__()

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessCrop':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Crop of this ProcessCrop.  # noqa: E501
        :rtype: ProcessCrop
        """
        return util.deserialize_model(dikt, cls)
