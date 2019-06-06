#!/usr/bin/python3
import cv2
# checking version
print(cv2.__version__)

# starting camera
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('live',frame)
    cv2.imshow('live',gray_frame)
    if cv2.waitKey(10) & 0xff ==ord('q'):
        break


cv2.destroyAllWindows()
cap.release()
