import os
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH= os.getcwd()
IMG_PATH= os.path.join(FILE_PATH, '../low_resdog.png')
#IMPORTS

import cv2 as cv
import numpy as np
import math
from matplotlib import pyplot as plt
def clip(img):
    y, x= img.shape[:2]
    for yi in range(y):
        for xi in range(x):
            for i in range(3):
                img[yi,xi,i]= img[yi,xi,i] if 0<=img[yi,xi,i]<=255 else (0 if img[yi,xi,i]<0 else 255)
    return img 
img= cv.imread(IMG_PATH)
def gaussian(sigma, x, y) :

    return (1/math.sqrt(2*math.pi*sigma**2)) *math.e**(-(x**2 + y**2)/(2*sigma**2))

def gaussian_blur(img, sigma, sigmax, sigmay):
    mask= np.array([[gaussian(sigma, x, y) for x in range(sigmax)] for y in range(sigmay)], np.float32)
    return cv.filter2D(src= img, ddepth=-1, kernel=mask)

#Sharpening isn't working, even by applying a sharpening mask :/
def sharpen(src):
    mask= np.array([[-1,-2,-1],[-2,12,-2],[-1,-2,-1]],np.float32)*1/16
    return cv.filter2D(src, -1, mask)
def sobel_x(src):
    scale = 1
    delta = 0
    ddepth = cv.CV_16S

    src = cv.GaussianBlur(src, (3, 3), 0)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    abs_grad_x = cv.convertScaleAbs(grad_x)
    return abs_grad_x

def sobel_y(src):
    scale = 1
    delta = 0
    ddepth = cv.CV_16S

    src = cv.GaussianBlur(src, (3, 3), 0)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
    abs_grad_y = cv.convertScaleAbs(grad_y)
    return abs_grad_y

def canny(src):
    return cv.Canny(src,100,200)

#Nearest neighbor Interpolation
def scale(src, x, y):
    res= np.zeros((y,x,3), dtype=np.uint8)
    original_y, original_x= src.shape[:2]
    for yi in range(y):
        y_percent= yi/(y-1)
        y_index= int(y_percent * (original_y-1))
        for xi in range(x):
            x_percent= xi/(x-1)
            x_index= int(x_percent * (original_x-1))
            res[yi,xi]+= src[y_index, x_index,:]
            #print(f'{res[yi,xi]} == {src[y_index, x_index]}')
    
    return res 
#bl= gaussian_blur(img,15,5,5)
#cv.imshow('Blur', bl)
#cv.imshow('Sharpened', sharpen(bl))
#v.imshow('sobelx',sobel_x(img))
#cv.imshow('sobely', sobel_y(img))
#cv.imshow('canny', canny(img))
cv.imshow('bozu', img)
cv.imshow('Scale', scale(img, 300, 300))
cv.waitKey(0)