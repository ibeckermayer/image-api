#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load
from app.controllers import default_controller

SWAGGER_URL = '/image/ui'
SWAGGER_PATH = 'app/swagger/swagger.yaml'

# app = Flask(__name__)

# @app.route("/image/image-process")
# def hello():
#     return "Hello World!"

def main():
    swagger_yml = load(open(SWAGGER_PATH, 'r'), Loader=Loader)
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, SWAGGER_PATH, config={'spec': swagger_yml})
    default_controller.app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    # app.run(ssl_context='adhoc', port=8080)
    default_controller.app.run(port=8080)

if __name__ == '__main__':
    main()
