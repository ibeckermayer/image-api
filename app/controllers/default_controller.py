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
from app.operationLookup import lookup_operation_by_name
from app.operations import pipeline
import PIL
from app.models import Process

#from app.models.process import Process

app = Flask(__name__)

@app.route("/image/image-process", methods=['POST'])
def image_process():
    # check for valid request body
    if 'Image' not in request.files:
        return "No Image specified", 400
    if 'Processes' not in request.files:
        return "No Processes specified", 400

    # check for valid image
    image = Image.open(request.files['Image'])
    if type(image) == PIL.PngImagePlugin.PngImageFile:
        image_format = "png"
    elif type(image) == PIL.JpegImagePlugin.JpegImageFile:
        image_format = "jpg"
    else:
        return "Invalid image format for Image", 400

    # check for valid json
    try:
        processes_dict = json.load(request.files['Processes'])
    except:
        return "Invalid JSON format for Processes", 400

    # convert to Processes object
    try:
        if not "array_of_Process" in processes_dict:
            return 'Invalid JSON: JSON must have property "array_of_Process"', 400
        processes = [dict_to_process(x).operation() for x in processes_dict["array_of_Process"]]
    except Exception as e:
        return str(e), 400

    try:
        processedImage = pipeline(image, processes)
        return serve_pil_image(processedImage, image_format), 200
    except Exception as e:
        return str(e), 400

def serve_pil_image(pil_img: Image, image_format: str):
    """Convert PIL image into image that can be returned by flask endpoint"""
    img_io = BytesIO()
    if image_format == "png":
        pil_img.save(img_io, 'PNG', quality=70)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')
    elif image_format == "jpg":
        pil_img.save(img_io, 'JPEG', quality=70)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')

def dict_to_process(dikt: dict) -> Process:
    if not "name" in dikt:
        raise ValueError("Process is missing the required field 'name'")

    operation_class = lookup_operation_by_name(dikt["name"])
    return operation_class(dikt.get("array_of_Parameter"))

def loadImage(imageUpload: FileStorage) -> Image:
    try:
        in_memory_file = io.BytesIO()
        imageUpload.save(in_memory_file)
        image = Image.open(in_memory_file)
    except:
        image = None
    return image
