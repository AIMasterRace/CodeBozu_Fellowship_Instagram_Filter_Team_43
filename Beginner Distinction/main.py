import os
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH= os.getcwd()
IMG_PATH= os.path.join(FILE_PATH, '../Bozu.png')
BG_PATH= os.path.join(FILE_PATH,  '../Bakery.jpg')

import cv2 as cv
import numpy as np
img= cv.imread(IMG_PATH)
background= cv.imread(BG_PATH)
blank_channel= np.zeros(img.shape[:2], dtype='uint8')

def crop(img,x1,y1,x2,y2):
    height, width = img.shape[:2]
    crop = img[y1:y2, x1:x2]
    return crop

def addframe (img, color= (255,255,255), thickness= 20):
    return cv.copyMakeBorder(img,top=thickness,bottom=thickness,left=thickness,right=thickness,borderType=cv.BORDER_CONSTANT,value=color)

def superimpose(background, img, x=None, y=None):
    img = cv.resize(img,(300,300))
    if x is None:
        x= background.shape[1]//2
    if y is None:
        y= background.shape[0]//2

    width, height = img.shape[:2]
    background[y-height//2:y+height//2,
            x-width//2:x+width//2] = img
    return background
cv.imshow('frame', addframe(img))
cv.imshow('crop', crop(img, 0,0, img.shape[1], 300))
cv.imwrite('Galaxy.png', superimpose(background, img))
cv.waitKey(0) 