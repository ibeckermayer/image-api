# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app.models.process import Process  # noqa: F401,E501
from app import util

class ProcessRotate(Process):
    def __init__(self, array_of_parameter: List[Parameter]=None):  # noqa: E501
        """ProcessRotate - a model defined in Swagger

        :param name: The name of this ProcessRotate.  # noqa: E501
        :param array_of_parameter: The array_of_parameter of this ProcessRotate.  # noqa: E501
        :type array_of_parameter: List[Parameter]
        """
        # self._requires_params = True
        # self._minimum_params = 1
        # self._maximum_params = 1


        self._array_of_parameter = array_of_parameter
        super(ProcessRotate, self).__init__(requires_params=True,
                                            minimum_params=1,
                                            maximum_params=1,
                                            valid_params=[("degrees")],
                                            param_type=float)

    @classmethod
    def from_dict(cls, dikt) -> 'ProcessRotate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Process --&gt; Rotate of this ProcessRotate.  # noqa: E501
        :rtype: ProcessRotate
        """
        return util.deserialize_model(dikt, cls)

    # def verify(self):
    #     self._has_array_of_param_check()
    #     self._len_array_of_param_check(1, 1)

