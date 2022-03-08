import os
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH= os.getcwd()
IMG_PATH= os.path.join(FILE_PATH, '../Bozu.png')
BG_PATH= os.path.join(FILE_PATH,  '../frame2.webp')

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
    return cv.copyMakeBorder(img,
        top=thickness,bottom=thickness, left=thickness,right=thickness,
        borderType=cv.BORDER_CONSTANT,value=color)

def superimpose(background, img, x=None, y=None, size=(200,200)):
    img = cv.resize(img,size)
    if x is None:
        x= background.shape[1]//2
    if y is None:
        y= background.shape[0]//2

    width, height = size
    background[y-height//2:y+height//2,
            x-width//2:x+width//2] = img
    return background
#cv.imwrite('Bozu_frame_1.jpg', addframe(img))
#cv.imwrite('Bozu_headshot.jpg', crop(img, 0,0, img.shape[1], 300))
#cv.imwrite('Galaxy_Bozu.jpg', superimpose(background, img, 700, 600))
cv.imwrite('Bozu_frame_2.jpg', superimpose(background, img, size=(300,420)))
cv.waitKey(0) 