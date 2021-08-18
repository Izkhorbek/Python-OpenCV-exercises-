import cv2
import numpy as np

img = cv2.imread("document.jpg")
imgContours = img.copy()
width, height = 600, 900

def preProcessing(img):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
    kernel = np.ones((3,3))
    imgCanny = cv2.Canny(imgBlur,200,200)

    imgDial = cv2.dilate(imgCanny,kernel,iterations=2)
    imgThrash =  cv2.erode(imgDial,kernel,iterations=1)
    # cv2.imshow("imgBlur",imgBlur)
    # cv2.imshow("imgCanny",imgCanny)
    # cv2.imshow("imgThras",imgThrash)
    return imgThrash

def getContours(img):
    contours, _  = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    list_area = []
    approx = np.array([])
    # max_cnt = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        list_area.append(area)
        max_area = np.max(list_area)
        if area >= max_area:
            # cv2.drawContours(imgContours,cnt,-1,(255,0,0),3)
            peri  = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            # x,y,w,h = cv2.boundingRect(approx)
            cv2.drawContours(imgContours,approx,-1,(255,0,0),20)
    return approx

def getWarp(img, approx):
    cnt1 = np.float32([approx[1],approx[0],approx[2],approx[3]])
    cnt2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

    matrix = cv2.getPerspectiveTransform(cnt1,cnt2)
    imgOutput = cv2.warpPerspective(img,matrix,(width,height))

    return imgOutput

imgThras = preProcessing(img)
approx = getContours(imgThras)
imgOutput = getWarp(img,approx)

cv2.imshow("Image",img)
cv2.imshow("ImgContours",imgContours)
cv2.imshow("ImgOutput",imgOutput)
cv2.waitKey(0)