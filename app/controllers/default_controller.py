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

    # check for valid file formats
    processes = deserialize(request.files['Processes'])
    if processes is None:
        return "Invalid JSON format for Processes", 400
    image = loadImage(request.files['Image'])
    if image is None:
        return "Invalid image format for Image", 400

    return process(processes, image)

def process(processes, image: Image):
    return "WIP", 200

def deserialize(processes: FileStorage):
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
