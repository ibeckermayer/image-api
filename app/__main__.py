#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from yaml import Loader, load

SWAGGER_URL = '/image/ui'
SWAGGER_PATH = 'app/swagger/swagger.yaml'

def main():
    app = Flask(__name__)
    swagger_yml = load(open(SWAGGER_PATH, 'r'), Loader=Loader)
    swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, SWAGGER_PATH, config={'spec': swagger_yml})
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
    # app.run(ssl_context='adhoc', port=8080)
    app.run(port=5000)

if __name__ == '__main__':
    main()
