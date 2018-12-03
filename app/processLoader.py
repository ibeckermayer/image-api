from app.models import ProcessBlur
from app.models import ProcessBrightness
from app.models import ProcessColor
from app.models import ProcessContrast
from app.models import ProcessCrop
from app.models import ProcessEdge
from app.models import ProcessMaxFilter
from app.models import ProcessMedianFilter
from app.models import ProcessMinFilter
from app.models import ProcessMirror
from app.models import ProcessModeFilter
from app.models import ProcessRotate
from app.models import ProcessScale
from app.models import ProcessSharpen
from app.models import Process

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
