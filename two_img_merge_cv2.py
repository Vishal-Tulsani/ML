#!/usr/bin/python3

import cv2
import numpy as np


img1=cv2.imread('cat.jpg')
img2=cv2.imread('dog.jpg')
vis = np.concatenate((img1, img2), axis=1)
cv2.imshow('win_1',vis)
