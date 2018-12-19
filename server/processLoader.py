from server.models import ProcessBlur
from server.models import ProcessBrightness
from server.models import ProcessColor
from server.models import ProcessContrast
from server.models import ProcessCrop
from server.models import ProcessEdge
from server.models import ProcessMaxFilter
from server.models import ProcessMedianFilter
from server.models import ProcessMinFilter
from server.models import ProcessMirror
from server.models import ProcessModeFilter
from server.models import ProcessRotate
from server.models import ProcessScale
from server.models import ProcessSharpen
from server.models import Process

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
 "MaxFilter": ProcessMaxFilter,
 "MinFilter": ProcessMinFilter,
 "ModeFilter": ProcessModeFilter,
 "MedianFilter": ProcessMedianFilter,
 "Edge": ProcessEdge
}

def load_process_from_dict(dikt: dict) -> Process:
    if not "name" in dikt:
        raise ValueError("Process is missing the required field 'name'")

    process_class = lookup_process_by_name(dikt["name"])
    return process_class(dikt.get("parameters"))

def lookup_process_by_name(process_name: str):
    if not process_name in typeTable:
        raise ValueError(process_name + " is not a valid process name")
    return typeTable[process_name]
