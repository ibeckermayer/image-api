# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app import util

from PIL import Image

class Process(Model):
    def __init__(self):
        self.name = self.__class__.__name__[7:]
        self._requires_params = None  # boolean denoting whether this process needs params
        self._minimum_params = None  # minimum number of parameters taken by this process
        self._maximum_params = None  # maximum number of parameters taken by this process
        self._valid_params = None  # list of valid parameter names
        self._param_type = None    # type that string param must get converted into
        self._operation = None     # Operation (TODO: define operation class and subclasses) that process preforms

        self.swagger_types = {
            'name': str,
            'array_of_parameter': List[Parameter]
        }

        self.attribute_map = {
            'name': 'name',
            'array_of_parameter': 'array_of_Parameter'
        }

    @property
    def operation(self):
        """verifies the process is properly formed, then fills out the operation with it's parameters"""
        self._verify_parameters()
        return self._operation

    def _verify_parameters(self):
        if self._requires_params:
            self._has_array_of_param_check()
            self._len_array_of_param_check()
            self._param_name_check()
            self._param_val_check()
        raise NotImplementedError()  # virtual method

    def _has_array_of_param_check(self):
        """optionally called by _verify() if Process requires array_of_Parameter"""
        if self._array_of_parameter == None:
            raise ValueError("Process [" + self.name + "] must have property array_of_Parameter")

    def _len_array_of_param_check(self, minimum: int, maximum: int):
        if not(len(self._array_of_parameter) >= minimum and len(self._array_of_parameter) <= maximum):
            raise ValueError("Process [" + self.name + "] must have property array_of_Parameter between length {0} and {1}".format(minimum, maximum))

    def _param_name_check(self, valid_names: List[str]):
        for param_name in [param.parameter for param in self._array_of_parameter]:
            if param_name not in valid_names



    @property
    def array_of_parameter(self) -> List[Parameter]:
        """Gets the array_of_parameter of this ProcessBlur.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :return: The array_of_parameter of this ProcessBlur.
        :rtype: List[Parameter]
        """
        return self._array_of_parameter

    @array_of_parameter.setter
    def array_of_parameter(self, array_of_parameter: List[Parameter]):
        """Sets the array_of_parameter of this ProcessBlur.

        Parameter array to further specify the process, if necessary.  # noqa: E501

        :param array_of_parameter: The array_of_parameter of this ProcessBlur.
        :type array_of_parameter: List[Parameter]
        """

        self._array_of_parameter = array_of_parameter
