import numpy
from PIL import Image

image = Image.open('screen.png')
image = numpy.array(image, dtype=numpy.uint8)

pixels = [list(i[:3]) for i in image[1700]]

area = []
ignore = True

for i, pixel in enumerate(pixels) :
    r, g, b = [int(i) for i in pixel]
    
    if ignore and (r + g + b) != 0 :
        continue

    ignore = False
    print(r, g, b)
    break