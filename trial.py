#!/usr/bin/python3

import cv2
import numpy as np
# loading  face trained  data
facehaar=cv2.CascadeClassifier('face.xml')
#  starting  camera
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read()
#  face detector  apply in  virat_img--scalling  range 
    face_only=facehaar.detectMultiScale(frame,1.15,5)
    #print(face_only)
    if np.nonzero(face_only):
        
        break
                
    
cv2.destroyAllWindows()
cap.release()
