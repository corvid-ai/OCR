# import dependencies
import pytesseract as pt
from PIL import Image
import argparse
import cv2
import os
import io

'''
Author:Kapps
USAGE
first things first: install pytesseract-ocr.exe and add to file path 
on windows cmd :
python ocr.py --file filepath
eg: python ocr.py --file C:/Users/username/imgdirectory/test_img.png
'''


'''--ocr functions takes in one parameter,the file path
	--we split the file path into the file name and extenstion
	--we use the filename to save the ocr text later 
	--we use the file extension to check the formats of our file 
	before manipulations
	--if the file is an image,preprocess and perform ocr extraction
	--else if pdf do like wise 
	---------------------------------------------------------------
	packages pytesseract for ocr conversions uses the pytesseract 
	library as a backend ..make sure you install requirements and pytesseract-ocr.exe
	file befor you run the script

'''
ap = argparse.ArgumentParser()
ap.add_argument('-f','--file',required=True,help ='path to file to be ocr-ed')
args =vars(ap.parse_args())
# replace file with args['file'] if using argparse on the command line 

def ocr(file):

	

    alert = 'input_file_not_accepted'
    # split the path/filename into name and extension
    name_of_file,extension =os.path.splitext(file)
    # convert the extension name to lower case 
    extension = extension.lower()
    # a conditional for image inputs
    if extension == '.png' or 'jpg' or 'jpeg':
        img = file
        # preprocess the image
        img = cv2.imread(img)
        img = cv2.resize(img, None, fx=2, fy=2,interpolation=cv2.INTER_CUBIC)
        retval, threshold = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        # perform ocr extractions
        txt = pt.image_to_string(threshold)
        # print output
        print(txt)

        # Todo-save output to csv 
        # todo: work on pdf version
    elif extension == '.pdf':
        pdf = file
        # convert pdf to jpeg
        pdf = pdf.convert('jpeg')
        # preprocessing
        img = cv2.imread(pdf)
        img = cv2.resize(img, None, fx=2, fy=2,interpolation=cv2.INTER_CUBIC)
        retval, threshold = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        # perform ocr extraction
        txt = pt.image_to_string(threshold)
        print(txt)
        # todo:save output to csv file
    else:
    	print(alert)


file = args['file']
ocr(file)
