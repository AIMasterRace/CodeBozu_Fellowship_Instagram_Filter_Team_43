import os
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH= os.getcwd()
IMG_PATH= os.path.join(FILE_PATH, '../Bozu.png')
VID_PATH= os.path.join(FILE_PATH, '../sakura.gif')
OUTPUT_NAME= 'output.avi'
VIDEO_WIDTH= 500
VIDEO_HEIGHT= 281

#IMPORTS
def superimpose(background, img, x=None, y=None, size=(200,200), transparent=True):
    img = cv.resize(img,size)
    if x is None:
        x= background.shape[1]//2
    if y is None:
        y= background.shape[0]//2
    width, height = size
    for yi in range(0, height):
        for xi in range(0,width):
            bg_y, bg_x= y+yi-height//2, x+xi-width//2
            background[bg_y, bg_x]= img[yi,xi,:3] if img[yi,xi,3] != 0 and transparent else background[bg_y,bg_x] 
    return background

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img= cv.imread(IMG_PATH, cv.IMREAD_UNCHANGED)
cap = cv.VideoCapture(VID_PATH)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter(OUTPUT_NAME, fourcc, 20.0, (VIDEO_WIDTH,  VIDEO_HEIGHT))

def make_vid(vid, img):
    ret, frame = cap.read()
    while ret:
        new_frame = superimpose(frame,img, 155,160,size=(75,75))
        out.write(new_frame)
        ret, frame= cap.read()
    cap.release()
    out.release()
    cv.destroyAllWindows()

make_vid(cap, img)