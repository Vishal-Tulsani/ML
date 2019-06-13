#!/usr/bin/python3

import cv2
# loading  face trained  data
facehaar=cv2.CascadeClassifier('face.xml')
smilehaar=cv2.CascadeClassifier('smile.xml')
#  starting  camera
cap=cv2.VideoCapture(0)

while cap.isOpened(): 
        status,frame=cap.read()
#  face detector  apply on live camera
        face_only=facehaar.detectMultiScale(frame,1.15,3)
	
        for  x,y,w,h in  face_only:       # face is detected here
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)   # rectangle for face area
                face_image = frame[(y/2):y+h, x:x+w]  # face is seprated from the full image
                smile=smilehaar.detectMultiScale(face_image)  # smile is detected here from seprated face or part
                for x,y,w,h in smile:
                        cv2.rectangle(face_image,(x,y),(x+w,y+h),(250,250,0),2)  # rectangl for the smile area
        cv2.imshow('face_and _smile_detect',frame)
        if cv2.waitKey(10) & 0xff == ord('q'):
                break


cv2.destroyAllWindows()
cap.release()
