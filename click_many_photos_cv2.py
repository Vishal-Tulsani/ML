#!/usr/bin/python3

import cv2
camera = cv2.VideoCapture(0)
for i in range(100):
    return_value, image = camera.read()
    cv2.imwrite('opencv'+str(i)+'.png', image)
del(camera)
