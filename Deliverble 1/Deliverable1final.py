#!/usr/bin/env python
# coding: utf-8

# In[4]:


import cv2 as cv
import numpy as np


# In[5]:


def reddify(r,blank):
    red = cv.merge([blank,blank,r])
    cv.imshow ('Red_Bozu', red)
    cv.imwrite('Red_Bozu.jpg', red)
    return;
def greenify(g,blank):
    green = cv.merge([blank,g,blank])
    cv.imshow ('Green_Bozu',green)
    cv.imwrite('Green_Bozu.jpg', green)
    return;
def blueify(b,blank):
    blue = cv.merge([b,blank,blank])
    cv.imshow ('Blue_Bozu', blue)
    cv.imwrite('Blue_Bozu.jpg', blue)
    return;
def grayscale(b,g,r):
    b_grayscale = 0.1140 * b
    g_grayscale = 0.5870 * g
    r_grayscale = 0.2989 * r
    gray = cv.merge([b_grayscale,g_grayscale,r_grayscale])
    cv.imshow ('Gray_Bozu', gray)
    cv.imwrite('Gray_Bozu.jpg', gray)
    return; 
def negative(img):
    negative = abs(255-img)
    cv.imshow('Bozu_negative', negative)
    cv.imwrite('Bozu_negative.jpg', negative)
    return;


# In[6]:


img = cv.imread('/Users/sara/Desktop/Bozu.png')
cv.imshow('Bozu',img)

b,g,r = cv.split(img)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
    
reddify(r,blank)
greenify(g,blank)
blueify(b,blank)
grayscale(b,g,r)
negative(img)

cv.waitKey(0)


# In[ ]:





# In[ ]:




