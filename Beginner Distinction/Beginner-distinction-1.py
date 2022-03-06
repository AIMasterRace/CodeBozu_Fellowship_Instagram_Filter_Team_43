#!/usr/bin/env python
# coding: utf-8

# Libaries

# In[1]:


import cv2 as cv
import numpy as np


# Function

# In[2]:


def crop(image,rows):
    image = img
    height, width = img.shape[:2]
    crop = img[rows:height, width]
    cv.imshow('Bozu_headshot',crop) 
    cv.imwrite('Bozu_headshot.jpg',crop)
    return;
def addframe (image,color):
    image = img
    rows,colums = img.shape[:2]
    bordersize = 20
    border = cv.copyMakeBorder(img,top=bordersize,bottom=bordersize,left=bordersize,right=bordersize,borderType=cv.BORDER_CONSTANT,value=color)
    cv.imshow('Bozu_frame',border)
    cv,imwrite('Bozu_frame.jpg',border)
    return;
def superimpose(background, image):
    Galaxy_Bozu = cv.resize(image,(300,300))
    rows_1,colums_1 = background.shape[:2]
    rows_2,colums_2 = image.shape[:2]
    x_offset, y_offset = [(rows_1-rows_2)/2,(colums_1-colums_2)/2]
    x_end, y_end = [(rows_1+rows_2)/2,(colums_1+colums_2)/2]
    background [y_offset:y_end,x_offset:x_end] = Galaxy_Bozu
    cv.imshow('Galaxy_Bozu',Galaxy_Bozu )
    cv.imwrite('Bozu_headshot.jpg',Galaxy_Bozu)
    return;


# Main

# In[ ]:


img = cv.imread('/Users/sara/Desktop/Bozu.png')

b,g,r = cv.split(img)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
    

cv.destroyAllWindows()
cv.waitKey(0)


# 
# 

# 
