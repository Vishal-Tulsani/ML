#!/usr/bin/python3
import cv2

# describing version
print(cv2.__version__)


# search for camera handling function
x=[i for i in dir(cv2) if 'video' in i]
print(x)



# starting video capture
cap=cv2.VideoCapture()  # data live,stored,streamed
print(dir(cap))  # exploring camera ops


# checking camera start point
print(cap.isOpened)
~

