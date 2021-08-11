import numpy as np
import matplotlib.pyplot as plt
import cv2
img = cv2.imread('IU.jpg')
# cv2.imshow("output",img)
# cv2.waitKey(0)
# cap = cv2.VideoCapture("construction_fence.m4v")

# while True:
#     succes, img = cap.read()
#     cv2.imshow('Video',img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap = cv2.VideoCapture(0)
# cap.set(3,640,)
# cap.set(4,480)
# cap.set(10,200)
#
# while True:
#     succes, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF==ord('q'):
#         break
# ////////////////////////

kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(img,50,200)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("ImgGray",imgGray)
cv2.imshow("ImgBlur",imgBlur)
cv2.imshow("ImgCanny",imgCanny)
cv2.imshow("ImgDialation",imgDialation)
cv2.imshow("ImgEroded",imgEroded)


cv2.waitKey(0)