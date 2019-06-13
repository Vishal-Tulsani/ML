#!/usr/bin/python3

import cv2
# loading  face trained  data
haar=cv2.CascadeClassifier('fist.xml')
#  starting  camera
cap=cv2.VideoCapture(0)

while cap.isOpened(): 
        status,frame=cap.read()
#  face detector  apply in  virat_img--scalling  range 
        fist_only=haar.detectMultiScale(frame,1.19,3)
	#print(face_only)
        for  x,y,w,h in  fist_only:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.imshow('fistdetect',frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
                break


cv2.destroyAllWindows()
cap.release()
