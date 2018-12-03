from PIL import Image

noAlphaWithP = ['1', 'L', 'P', 'RGB']

supportedModes = {
    'BMP': ['1', 'L', 'P', 'RGB'],
    'EPS': ['L', 'RGB', 'CMYK'],
    'GIF': ['L', 'P'],
    'JPEG': ['L', 'RGB', 'CMYK'],
    'PNG': ['1', 'L', 'P', 'RGB', 'RGBA'],
    'TGA': ['L', 'LA', 'P', 'RGB', 'RGBA'],
    'TIFF': ['1', 'L', 'P', 'RGB', 'RGBA'],
    'PDF': ['1', 'L', 'P', 'RGB', 'RGBA']
}

def switch_modes_if_needed(image: Image, desiredFormat: str) -> Image:
    mode = image.mode
    if not mode in supportedModes[desiredFormat]:
        return image.convert(mode=supportedModes[desiredFormat][-1])
    return image
