#!/usr/bin/python3

import cv2
img = cv2.imread('dog.jpg')
blur = cv2.blur(img,(100,100))
cv2.imshow('blue_window',blur)
