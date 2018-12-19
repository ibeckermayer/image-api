#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load
from server.controllers import default_controller
import os

SWAGGER_URL = '/image/ui'
SWAGGER_PATH = 'server/swagger/swagger.yaml'

try:
    PORT = os.environ["IMAGE_PORT"]
except KeyError:
    raise ValueError("Must have environment variable IMAGE_PORT defined to run this server")

try:
    HOST = os.environ["IMAGE_HOST"]
except KeyError:
    raise ValueError("Must have environment variable IMAGE_PORT defined to run this server")

def main():
    swagger_yml = load(open(SWAGGER_PATH, 'r'), Loader=Loader)
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, SWAGGER_PATH, config={'spec': swagger_yml})
    default_controller.app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    # server.run(ssl_context='adhoc', port=8080)
    default_controller.app.run(host=HOST, port=PORT)

if __name__ == '__main__':
    main()
