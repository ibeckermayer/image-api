# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from app.models.base_model_ import Model
from app.models.parameter import Parameter  # noqa: F401,E501
from app import util

from PIL import Image

from app.models.process_rotate import ProcessRotate
from app.models.process_scale import ProcessScale
from app.models.process_crop import ProcessCrop
from app.models.process_mirror import ProcessMirror
from app.models.process_color import ProcessColor
from app.models.process_brightness import ProcessBrightness
from app.models.process_contrast import ProcessContrast
from app.models.process_sharpen import ProcessSharpen
from app.models.process_blur import ProcessBlur
from app.models.process_max_filter import ProcessMaxFilter
from app.models.process_min_filter import ProcessMinFilter
from app.models.process_mode_filter import ProcessModeFilter
from app.models.process_median_filter import ProcessMedianFilter
from app.models.process_edge import ProcessEdge
from app.models.process_reformat import ProcessReformat

typeTable = {
 "Rotate": ProcessRotate, 
 "Scale": ProcessScale, 
 "Crop": ProcessCrop, 
 "Mirror": ProcessMirror, 
 "Color": ProcessColor, 
 "Brightness": ProcessBrightness, 
 "Contrast": ProcessContrast, 
 "Sharpen": ProcessSharpen, 
 "Blur": ProcessBlur, 
 "maxFilter": ProcessMaxFilter, 
 "minFilter": ProcessMinFilter, 
 "modeFilter": ProcessModeFilter, 
 "medianFilter": ProcessMedianFilter, 
 "Edge": ProcessEdge, 
 "Reformat": ProcessReformat   
}

class Process(Model):
    @staticmethod
    def lookupType(operationName):
        if not operationName in typeTable:
            raise ValueError(operationName + " is not a valid type")
        return typeTable[operationName]

    def apply(self, image: Image) -> Image:
        pass
