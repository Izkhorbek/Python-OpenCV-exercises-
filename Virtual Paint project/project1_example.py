import cv2
import numpy as np

cap = cv2.VideoCapture(0)

myColors = [[125, 65, 48, 179, 239, 255]]
            # [75, 33, 167, 103, 172, 255],
            # [10, 116, 248, 28, 169, 255]]


def findcolor(img, myColor):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newpoints = []
    for color in myColor:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper,)
        x,y = findcontours(mask)
        cv2.circle(imgResult,(x,y),10,myColor[count],2)

        if x!=0 and y!=0:
            newpoints.append([x,y,count])

        count+=1
    return newpoints

def findcontours(img):
    contours, _ = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(peri,0.2*peri,True)
            x,y,w,h =  cv2.boundingRect(approx)

    return x+w//2,y


def drawonCanvas():
    pass






while True:

    success, img = cap.read()
    imgResult = img.copy()
    newpoints = findcolor(img, myColors)

    if cv2.waitKey(0)==ord('s'):
        break
