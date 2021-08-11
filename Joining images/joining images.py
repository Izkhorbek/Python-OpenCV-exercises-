import cv2
import numpy as np
def Imagestack(scale, imgArray):
    rows,cols = imgArray.shape
    rowsAvailable = isinstance(imgArray,list)
    width = imgArray[0][0].shape[1]


img = cv2.imread('IU2.jpeg')
img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

imgHor = np.hstack((img,img))
imgVert = np.vstack((img,img))

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgVert)

cv2.waitKey(0)