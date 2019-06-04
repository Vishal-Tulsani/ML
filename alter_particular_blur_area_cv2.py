import cv2
import numpy as np

img = cv2.imread("cat.jpg")
blurred_img = cv2.blur(img,(10,10))

mask = np.zeros((500, 500,3), dtype=np.uint8)
mask = cv2.circle(mask, (310,200), 150,(255, 255, 255), -1)

out = np.where(mask==np.array([255, 255, 255]), blurred_img, img)

cv2.imshow("./out.png", out)

#print(blurred_img)

