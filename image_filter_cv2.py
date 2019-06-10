#!/usr/bin/python3

import cv2
import numpy as np

img=cv2.imread('t2.jpg')

fil1=cv2.bitwise_not(img)
#cv2.imshow('filter1',fil1)
fil2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#cv2.imshow('filter2',fil2)
fil3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('filter3',fil3)
src=np.array(img)
a=src+[10]
cv2.imshow('w',a)
