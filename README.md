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
docker build --build-arg IMAGE_PORT=$IMAGE_PORT --build-arg IMAGE_HOST=$IMAGE_HOST -t image_server ./

# starting up a container
docker run -p $IMAGE_PORT:$IMAGE_PORT image_server
```

## Examples

This API works by taking an image, and a JSON with a list of processes to preform on the image. The processes will be preformed in the order they are given in the JSON.

Inside the `examples` folder you can find a collection of example JSON operation definitions to play with. If you don't want to manually execute the requests yourself, you can use `test.sh` and provide it with the `.json` file you want to run with. The operation will be run against `pics/kek.jpeg`.

For example, if I run `./test.sh blur blurredDog.jpeg` then `blur.json` will be used, and the output saved in `blurredDog.jpeg`.

The app must be running on http://localhost:5000/ for the `test.sh` script to work.

#### Example JSON

This example JSON is the same as the one saved in `examples/json/all.json`, that contains all of the different available processes besides reformat (an example of which can be found in `examples/json/reformat.json`).

```json
{
	"processes": [
		{
			"name": "Rotate",
			"parameters": [
				{
					"parameter": "degrees",
					"value": "30"
				}
			]
		},
		{
			"name": "Scale",
			"parameters": [
				{
					"parameter": "ysize",
					"value": "300"
				}
			]
		},
		{
			"name": "Crop",
			"parameters": [
				{
					"parameter": "top_left_x",
					"value": "30"
				},
				{
					"parameter": "top_left_y",
					"value": "30"
				},
				{
					"parameter": "bottom_right_x",
					"value": "60"
				},
				{
					"parameter": "bottom_right_y",
					"value": "60"
				}
			]
		},
		{
			"name": "Mirror",
			"parameters": [
				{
					"parameter": "flip",
					"value": "horizontal"
				}
			]
		},
		{
			"name": "Color",
			"parameters": [
				{
					"parameter": "factor",
					"value": "1.7"
				}
			]
		},
		{
			"name": "Brightness",
			"parameters": [
				{
					"parameter": "factor",
					"value": "1.7"
				}
			]
		},
		{
			"name": "Contrast",
			"parameters": [
				{
					"parameter": "factor",
					"value": "1.7"
				}
			]
		},
		{
			"name": "Sharpen",
			"parameters": [
				{
					"parameter": "factor",
					"value": "1.7"
				}
			]
		},
		{
			"name": "Blur",
			"parameters": [
				{
					"parameter": "radius",
					"value": "1.7"
				}
			]
		},
		{
			"name": "MaxFilter",
			"parameters": [
				{
					"parameter": "size",
					"value": "3"
				}
			]
		},
		{
			"name": "MinFilter",
			"parameters": [
				{
					"parameter": "size",
					"value": "3"
				}
			]
		},
		{
			"name": "ModeFilter",
			"parameters": [
				{
					"parameter": "size",
					"value": "3"
				}
			]
		},
		{
			"name": "MedianFilter",
			"parameters": [
				{
					"parameter": "size",
					"value": "3"
				}
			]
		},
		{
			"name": "Edge",
			"parameters": null
		}
	]
}
```
