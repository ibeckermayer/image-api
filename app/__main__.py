#!/usr/bin/env python3

from flask import Flask, jsonify

from app import encoder


def main():
    app = Flask(__name__, static_url_path = "")
    app.run(port=8080)


if __name__ == '__main__':
    main()
