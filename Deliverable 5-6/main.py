import os
FILE_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH= os.getcwd()
IMG_PATH= os.path.join(FILE_PATH, '../hippo.jpg')

#IMPORTS
def apply_threshold(img, threshold):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    y, x= gray.shape
    for yi in range(y):
        for xi in range(x):
            img[yi,xi]= 255 if gray[yi,xi]>threshold else 0
    return img

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img= cv.imread(IMG_PATH)
blank_channel= np.zeros(img.shape[:2], dtype='uint8')

#Deliverable 5
def vintage(img):
    y, x = img.shape[:2] 
 
    # generating vignette mask using Gaussian kernels 
    kernel_x = cv.getGaussianKernel(x,200) 
    kernel_y = cv.getGaussianKernel(y,200) 
    kernel = kernel_y * kernel_x.T 
    mask = 255 * kernel / np.linalg.norm(kernel) 
    output = np.copy(img) 
 
    # applying the mask to each channel in the input image 
    for i in range(3): 
        output[:,:,i] = output[:,:,i] * mask 
    
    return output
def sepia(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    normalized_gray = np.array(gray, np.float32)/255
    #solid color
    sepia = np.ones(img.shape)
    sepia[:,:,0] *= 153 #B
    sepia[:,:,1] *= 204 #G
    sepia[:,:,2] *= 255 #R
    #hadamard
    sepia[:,:,0] *= normalized_gray #B
    sepia[:,:,1] *= normalized_gray #G
    sepia[:,:,2] *= normalized_gray #R
    return np.array(sepia, np.uint8)

def sharpen(img):
    f=  np.array([[-1, -1, -1], [-1, 9.5, -1], [-1, -1, -1]])
    return cv.filter2D(img, -1, f)


#Deliverable 6
def cartoonize_grayscale(img):
    gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray= cv.medianBlur(gray, 51)
    return apply_threshold(img, 60)

def cartoonize_color(img):
    Z= np.float32(img.reshape((-1,6)))
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 20, 1.5)
    K = 6
    ret,label,center=cv.kmeans(Z,K,None,criteria,20,cv.KMEANS_RANDOM_CENTERS)
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))
    return res2
#cv.imshow('Vintage', vintage(img))
#cv.imshow('Sepia', sepia(img))
#cv.imshow("Sharpened", sharpen(sepia(img)))
#cv.imshow("Cartoon Gray", cartoonize_grayscale(img))
cv.imshow("Cartoon Color", cartoonize_color(img))
cv.waitKey(0)