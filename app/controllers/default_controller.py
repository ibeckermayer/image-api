from app import util
from flask import Flask

app = Flask(__name__)

@app.route("/image/image-process")
def hello():
    return "Hello World!"


def image_process_post(image, processes):  # noqa: E501
    """Takes an image and processes it according to accompanying json.

     # noqa: E501

    :param image: The image.
    :type image: werkzeug.datastructures.FileStorage
    :param processes: JSON string containing array of the processes, in the order they should be preformed.
    :type processes: werkzeug.datastructures.FileStorage

    :rtype: None
    """
    return 'do some magic!'
