from app import util
from flask import Flask, request
from werkzeug.datastructures import FileStorage
from PIL import Image
import io
#from app.models.process import Process

app = Flask(__name__)

@app.route("/image/image-process", methods=['POST'])
def hello():
    if 'Image' not in request.files:
        return "No Image specified", 400

    if 'Processes' not in request.files:
        return "No Processes specified", 400
    
    processes = deserialize(request.files['Processes'])
    image = loadImage(request.files['Image'])

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
    image.show()
    return image