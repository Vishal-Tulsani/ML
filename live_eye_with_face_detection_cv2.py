#!/usr/bin/python3

import cv2
# loading  face trained  data
facehaar=cv2.CascadeClassifier('face.xml')
eyehaar=cv2.CascadeClassifier('eye.xml')
#  starting  camera
cap=cv2.VideoCapture(0)

while cap.isOpened(): 
        status,frame=cap.read()
#  face detector  apply in  virat_img--scalling  range 
        face_only=facehaar.detectMultiScale(frame,1.15,5)
	#print(face_only)
        for  x,y,w,h in  face_only:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                face_image = frame[y:y+h, x:x+w]
                eye=eyehaar.detectMultiScale(face_image)
                for x,y,w,h in eye:
                        cv2.rectangle(face_image,(x,y),(x+w,y+h),(250,250,0),2)
        cv2.imshow('face_and _eye_detect',frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
                break


cv2.destroyAllWindows()
cap.release()
