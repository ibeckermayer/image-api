# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict, Tuple  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app import util

from PIL import Image

class Process(Model):
    def __init__(self, requires_params: bool=None, minimum_params: int=None,
                 maximum_params: int=None, valid_params: List[Tuple[str]]=None,
                 param_type: type=None, operation=None):
        self.name = self.__class__.__name__[7:]
        self._requires_params = requires_params  # boolean denoting whether this process needs params
        self._minimum_params = minimum_params  # minimum number of parameters taken by this process
        self._maximum_params = maximum_params  # maximum number of parameters taken by this process
        self._valid_params = valid_params  # list of tuples. Each process must have at least one parameter from each tuple to be considered valid
        self._param_type = param_type    # type that string param must get converted into
        self._operation = operation     # Operation (TODO: define operation class and subclasses) that process preforms

        self.swagger_types = {
            'name': str,
            'array_of_parameter': List[Parameter]
        }

        self.attribute_map = {
            'name': 'name',
            'array_of_parameter': 'array_of_Parameter'
        }

    # @property TODO: make this a property
    def operation(self):
        """verifies the process is properly formed, then fills out the operation with it's parameters"""
        self._verify_parameters()
        # return self._operation
        return None

    def _verify_parameters(self):
        if self._requires_params:
            print("reqs")
            self._has_array_of_param_check()
            self._len_array_of_param_check()
            self._param_name_check()
            # self._param_val_check()

    def _has_array_of_param_check(self):
        """optionally called by _verify() if Process requires array_of_Parameter"""
        if self._array_of_parameter == None:
            raise ValueError("Process [" + self.name + "] must have property array_of_Parameter")
        else:
            print("array_of_param passed")

    def _len_array_of_param_check(self):
        if not(len(self._array_of_parameter) >= self._minimum_params and
               len(self._array_of_parameter) <= self._maximum_params):
            raise ValueError("Process [" + self.name + "] must have property array_of_Parameter between length {0} and {1}".format(minimum, maximum))
        else:
            print("len_array_of_param passed")

    def _param_name_check(self):
        """checks that the process has a parameter that matches at least one parameter in each tuple"""
        param_names = []
        for param in self._array_of_parameter:
            param_name = param.get("parameter")
            if param_name == None:
                raise ValueError("Process [" + self.name + "] has invalidly formatted Parameter. Each Parameter must have property \"parameter\" denoting it's name")
            param_names.append(param.get("parameter"))

        tups_passed = 0
        for tup in self._valid_params:
            for name in param_names:
                if name in tup:
                    tups_passed+=1
                    break
        if tups_passed != len(self._valid_params):
            raise ValueError("Process [" + self.name + "] must have at least one param in each tuple of {}".format(self._valid_params))

    # def _param_name_check(self, valid_names: List[str]):
    #     for param_name in [param.parameter for param in self._array_of_parameter]:
    #         if param_name not in valid_names



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
