import os
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH= os.getcwd()
IMG_PATH= os.path.join(FILE_PATH, '../Bozu.png')

import cv2 as cv
import numpy as np
img= cv.imread(IMG_PATH)
blank_channel= np.zeros(img.shape[:2], dtype='uint8')

def blueify(img):
    return cv.merge([img[:,:,0], blank_channel, blank_channel])

def greenify(img):
    return cv.merge([blank_channel, img[:,:,1], blank_channel]) 

def reddify(img):
    return cv.merge([blank_channel, blank_channel, img[:,:,2]])

def grayify(img):
    return cv.merge([
        img[:,:,0]*0.1140,   #Blue
        img[:,:,1]*0.5870,   #Green
        img[:,:,2]*0.2989,]) #Red

def invert(img):
    return 255-img

def test():
    cv.imshow('Blue Bozu', blueify(img))
    cv.imshow('Green Bozu', greenify(img))
    cv.imshow('Red Bozu', reddify(img))
    cv.imshow('Gray Bozu', grayify(img))
    cv.imshow('Negative Bozu', invert(img))
    cv.waitKey(0)

if __name__=='__main__':
    test()

