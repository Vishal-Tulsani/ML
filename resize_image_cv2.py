#!/usr/bin/python3

import cv2
img=cv2.imread('cat.jpg')
print(img.shape)
resize_img = cv2.resize(img,(32,32))
print(resize_img.shape)
cv2.imshow('original_img',img)
cv2.imshow('resize_img',resize_img)
