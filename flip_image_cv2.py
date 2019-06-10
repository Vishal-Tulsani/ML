#!/usr/bin/python3

import cv2
from time import sleep
img=cv2.imread('dog.jpg')
f_img=cv2.flip(img,0)
cv2.imshow('ORIGINAL',img)
cv2.waitKey(1000)
cv2.destroyWindow('ORIGINAL')
cv2.imshow('FLIPED ONE',f_img)
cv2.waitKey(1000)
cv2.destroyWindow('FLIPED ONE')
f2_img=cv2.flip(f_img,0)
cv2.imshow('ORIGINAL ONE',f2_img)
