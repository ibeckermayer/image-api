# Image Server

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

## Examples

Inside the `examples` folder you can find a collection of example JSON operation definitions to play with. If you don't want to manually execute the requests yourself, you can use `test.sh` and provide it with the `.json` file you want to run with. The operation will be run against `pics/kek.jpeg`.

For example, if I run `./test.sh blur blurredDog.jpeg` then `blur.json` will be used, and the output saved in `blurredDog.jpeg`.

The app must be running on http://localhost:5000/ for the `test.sh` script to work.
