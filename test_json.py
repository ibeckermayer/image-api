import io
import json
from app import util
from flask import Flask, request
from werkzeug.datastructures import FileStorage
from PIL import Image
from app.models import Model
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

with open("valid_example.json") as f:
    processes = json.load(f)

pprint(processes)
