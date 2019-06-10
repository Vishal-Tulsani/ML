#!/usr/bin/python3
import cv2
import numpy as np

im = cv2.imread('dog.jpg')
img = cv2.imread('dog.jpg',0)

# Convert grayscale image to 3-channel image,so that they can be stacked together    
imgc = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
both = np.concatenate((im,imgc), axis=1)   #1 : horz, 0 : Vert. 

cv2.imshow('imgc',both)
cv2.waitKey(0)
cv2.destroyAllWindows()
