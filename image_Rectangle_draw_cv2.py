#!/usr/bin/python3
import cv2
# checking version
print(cv2.__version__)

# starting camera
cap=cv2.VideoCapture(0) # here camera no. first

while cap.isOpened():  # return true or false by checking camera status
    status,frame=cap.read() # starting taking frames or pictures
     # draw a line
    cv2.line(frame,(0,0),(200,250),(0,255,0),-1)
    cv2.rectangle(frame,(150,200),(300,300),(100,100,100),2)
    cv2.imshow('live',frame)
    if cv2.waitKey(10) & 0xff ==ord('q'):
        break


cv2.destroyAllWindows()
cap.release()
