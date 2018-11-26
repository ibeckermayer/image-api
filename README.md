# Image Server

## Overview
Flask Server

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m app
```

and open your browser to here:

```
http://localhost:5000/image/ui/
```

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t swagger_server .

# starting up a container
docker run -p 5000:50000 swagger_server
```
