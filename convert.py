import os
import io
import cv2
import pytesseract as pt
from pathlib import Path



directory_in_str = './images/'


def ocr(file):
    img = file
    # preprocess the image
    img = cv2.imread(img)
    img = cv2.resize(img, None, fx=2, fy=2,interpolation=cv2.INTER_CUBIC)
    retval, threshold = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    # perform ocr extractions
    txt = pt.image_to_string(threshold)
    return txt


pathlist = Path(directory_in_str).glob('**/*.jpg')
text = []

with open("test.txt", "a") as myfile:
    for i,path in pathlist:
        # because path is object not string

        path_in_str = str(path)
        print("{0} IMAGE PATH: ".format(i), path_in_str)
        extract = ocr(path_in_str)
        print(extract)
        myfile.write(extract)
