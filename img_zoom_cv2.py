#!/usr/bin/python3

import cv2
import numpy as np

img=cv2.imread('dog.jpg',0)
rows,cols = img.shape
pts1 = np.float32([[156,165],[468,152],[128,487],[489,490]])
pts2 = np.float32([[0,0],[700,0],[0,900],[900,900]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))
cv2.imshow('a',dst)
