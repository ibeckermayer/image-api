from app import util
from flask import Flask, request
from werkzeug.datastructures import FileStorage
from PIL import Image
import io
import json
#from app.models.process import Process

app = Flask(__name__)

@app.route("/image/image-process", methods=['POST'])
def image_process():
    if 'Image' not in request.files:
        return "No Image specified", 400

    if 'Processes' not in request.files:
        return "No Processes specified", 400

    processes = deserialize(request.files['Processes'])
    image = loadImage(request.files['Image'])

    parseJSON(processes)

    return process(processes, image)

def process(processes, image: Image):
    return "WIP", 200

def deserialize(processes: FileStorage):
    json = processes.stream.read(-1).decode('utf-8')
    return json


def loadImage(imageUpload: FileStorage):
    in_memory_file = io.BytesIO()
    imageUpload.save(in_memory_file)
    image = Image.open(in_memory_file)
    # image.show()
    return image

def parseJSON(json_string: str):
    processes = json.loads(json_string)
    # print(processes)
