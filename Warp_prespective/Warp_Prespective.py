import cv2
import numpy as np

img = cv2.imread('D:/Python/PyCharm/cards2.jpg')
width, height = 200,300

plt1 = np.float32([[366,136],[496,162],[276,291],[415,330]])
plt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(plt1,plt2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)

cv2.waitKey(0)