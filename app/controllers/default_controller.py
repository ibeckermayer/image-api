from app import util
from flask import Flask, request

app = Flask(__name__)

@app.route("/image/image-process", methods=['POST'])
def hello():
    if 'Image' not in request.files:
        return "No Image specified", 400

    if 'Processes' not in request.files:
        return "No Processes specified", 400
    
    return "WIP", 200
