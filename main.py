import os
import numpy
from PIL import Image
import time

while True :
    temp = os.system('adb shell screencap /sdcard/screen.png')
    temp = os.system('adb pull /sdcard/screen.png')

    image = Image.open('screen.png')
    image = numpy.array(image, dtype=numpy.uint8)

    pixels = [list(i[:3]) for i in image[1700]]

    area = []
    ignore = True
    black= True

    for i, pixel in enumerate(pixels) :
        r, g, b = [int(i) for i in pixel]
        
        if ignore and (r + g + b) != 0 :
            continue

        ignore = False

        if black and (r + g + b) != 0 :
            black = not black
            area.append(i)
            continue

        if not black and (r + g + b) == 0 :
            black = not black
            area.append(i)
            continue

    start, targetS, targetE = area

    whitespace = targetS - start
    targetWidth = targetE - targetS 
    longPressTime = whitespace + targetWidth/2

    os.system(f'adb shell input swipe 540 540 540 540 {int(longPressTime)}')
    
    time.sleep(2.5)