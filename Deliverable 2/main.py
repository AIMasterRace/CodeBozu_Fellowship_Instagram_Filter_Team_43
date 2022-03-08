import os
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH= os.getcwd()
IMG_PATH= os.path.join(FILE_PATH, '../Bozu.png')

import cv2 as cv
import numpy as np
img= cv.imread(IMG_PATH)
blank_channel= np.zeros(img.shape[:2], dtype='uint8')

def horizontal_flip(img):
    temp= np.copy(img)
    y, x= img.shape[:2]
    for yi in range(y):
        for xi in range(x):
            temp[yi,-xi-1] = img[yi,xi]
    return temp  

def vertical_flip(img):
    temp= np.copy(img)
    y, x= img.shape[:2]
    for yi in range(y):
        for xi in range(x):
            temp[-yi-1,xi] = img[yi,xi]
    return temp  

def clip(img):
    y, x= img.shape[:2]
    for yi in range(y):
        for xi in range(x):
            for i in range(3):
                img[yi,xi,i]= img[yi,xi,i] if 0<=img[yi,xi,i]<=255 else (0 if img[yi,xi,i]<0 else 255)
    return img 

def contrast(img, alpha):
    return clip(img*alpha)

def add_brightness(img, beta):
    return clip(img+beta)

def apply_threshold(img, threshold):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    y, x= gray.shape
    for yi in range(y):
        for xi in range(x):
            img[yi,xi]= 255 if gray[yi,xi]>threshold else 0
    return img
#cv.imshow("Bozu", img)
#cv.imshow("Horizontal Flip", horizontal_flip(img))
#cv.imshow("Vertical Flip", vertical_flip(img))
#cv.imshow("Contrast", contrast(img, 2))
#cv.imshow("Bright", add_brightness(img, 90))
#cv.imwrite("Bozu_in_the_dark.jpg", apply_threshold(img, 254.5))
#cv.imwrite('Silhouette_Bozu.jpg', apply_threshold(img, 50))
cv.waitKey(0)