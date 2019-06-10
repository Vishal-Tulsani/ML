#!/usr/bin/python3

import cv2
from time import sleep

img=cv2.imread('cat.jpg',0)
rows,cols= img.shape
for i in range(10):
    M=cv2.getRotationMatrix2D((cols/2,rows/2),25,1)
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow('d',dst)
    
    
