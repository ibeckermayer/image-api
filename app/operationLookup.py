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

def lookup_operation_by_name(operation_name: str):
    if not operation_name in typeTable:
        raise ValueError(operation_name + " is not a valid process name")
    return typeTable[operation_name]
