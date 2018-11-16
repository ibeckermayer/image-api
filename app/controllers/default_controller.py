from app import util
from flask import Flask, request

app = Flask(__name__)

@app.route("/image/image-process", methods=['POST'])
def hello():
    if 'file' not in request.files:
        return "No file"
    else:
        return "found file"
