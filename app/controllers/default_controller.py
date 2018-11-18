import io
import json
from app import util
from flask import Flask, request
from werkzeug.datastructures import FileStorage
from PIL import Image
from app.models import Parameter
from app.models import Process
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
from app.models import ProcessReformat
from app.models import ProcessRotate
from app.models import ProcessScale
from app.models import ProcessSharpen
from app.models import Processes

#from app.models.process import Process

app = Flask(__name__)

@app.route("/image/image-process", methods=['POST'])
def image_process():
    # check for valid request body
    if 'Image' not in request.files:
        return "No Image specified", 400
    if 'Processes' not in request.files:
        return "No Processes specified", 400

    print("has fields")

    # check for valid image
    image = loadImage(request.files['Image'])
    if image is None:
        return "Invalid image format for Image", 400

    # check for valid json
    processes_dict = json_to_dict(request.files['Processes'])
    if processes_dict is None:
        return "Invalid JSON format for Processes", 400

    # convert to Processes object
    try:            
        if not "array_of_Process" in processes_dict:
            return 'Invalid JSON: JSON must have property "array_of_Process"'

        processes = [dict_to_process(x) for x in processes_dict["array_of_Process"]]
        print(processes)
    except Exception as e:
        return str(e), 400

    try:
        # TODO:
        # Go through each Process, check that it has a name, if not throw error.

        # If it has a name, check that it has an array_of_parameter if necessary. If not, throw error.

        # If it has a list_of_parameter, make sure that each parameter in that list is properly formed (no missing fields). If not, throw error.

        # If it has necessary list of parameter and each parameter is properly formed, check that it has the correct parameters based on the
        # name of the process. If not, throw error.

        # If it has necessary list of parameter and each parameter is properly formed and the parameters are correct based on the name of the
        # process, check that the value of the parameter is correct based on the name ("parameter" property) of the parameters.

        # If all of those pass, call the appropriate operation function in a list. If you get all the way through
        # and don't get any errors, return that list. Now that you have that list, throw it through the process
        # function with the image, and return that image.
        return processes.run(image)
        processes = None
    except Exception as e:
        return str(e), 400

    return process(processes, image)

def process(processes, image: Image):
    return "WIP", 200

def dict_to_process(obj) -> Process:
    if not "name" in obj:
        raise ValueError("Process is missing the required field 'name'")

    klass = lookupType(obj["name"])
    return klass(obj["array_of_Parameter"])

def json_to_dict(processes: FileStorage):
    try:
        return json.load(processes)
    except:
        return None

def loadImage(imageUpload: FileStorage):
    try:
        in_memory_file = io.BytesIO()
        imageUpload.save(in_memory_file)
        image = Image.open(in_memory_file)
    except:
        image = None
    return image

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

def lookupType(processName):
    if not processName in typeTable:
        raise ValueError(processName + " is not a valid process name")
    return typeTable[processName]