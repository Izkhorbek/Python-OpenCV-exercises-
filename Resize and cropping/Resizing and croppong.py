import numpy as np
import matplotlib.pyplot as plt
import cv2
img = cv2.imread('IU2.jpeg')
print(img.shape)

imgResize = cv2.resize(img,(300,200))
imgCropped = img[0:300,300:900]

cv2.imshow("Image",img)
cv2.imshow("Image_Resize",imgResize)
cv2.imshow("Image_Cropped",imgCropped)

cv2.waitKey(0)