import io
from io import BytesIO
import json
from functools import reduce
from app import util
from flask import Flask, request, send_file
from werkzeug.datastructures import FileStorage
from PIL import Image
from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
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
    image = Image.open(request.files['Image'])
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
    except Exception as e:
        return str(e), 400

    operations = []
    try:
        for process in processes:
            print(process.name)
            if process.name == "MaxFilter":  # TODO: this is tbdeleted
                operations.append(process.operation())
                # return pipeline([proc.get_operation() for proc in processes], image)
        return pipeline(image, operations), 200
    except Exception as e:
        return str(e), 400

    # for process in processes:
    #     if process.name == "Mirror":  # TODO: this is tbdeleted
    #         operations.append(process.operation())




def pipeline(image: Image, operations):

    processed_image = reduce(lambda last, operation: operation(last), operations, image)
    return serve_pil_image(processed_image)

def serve_pil_image(pil_img):
    """Convert PIL image into image that can be returned by flask endpoint
    TODO: need to determine which image format to return based on the input image type"""
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

# def pipeline(processes, image: Image):
#     return "WIP", 200

def dict_to_process(dikt) -> Process:
    if not "name" in dikt:
        raise ValueError("Process is missing the required field 'name'")

    klass = lookupType(dikt["name"])
    return klass(dikt.get("array_of_Parameter"))

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
 "MaxFilter": ProcessMaxFilter,
 "MinFilter": ProcessMinFilter,
 "ModeFilter": ProcessModeFilter,
 "MedianFilter": ProcessMedianFilter,
 "Edge": ProcessEdge,
 "Reformat": ProcessReformat
}

def lookupType(processName):
    if not processName in typeTable:
        raise ValueError(processName + " is not a valid process name")
    return typeTable[processName]
