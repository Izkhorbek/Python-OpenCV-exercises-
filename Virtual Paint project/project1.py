import cv2
import numpy as np

framewidth = 640
frameheigth = 480
cap = cv2.VideoCapture(0)
cap.set(2, framewidth)
cap.set(3, frameheigth)
cap.set(10, 150)

myColors = [[125, 65, 48, 179, 239, 255],
            [75, 33, 167, 103, 172, 255],
            [10, 116, 248, 28, 169, 255]]
myColorValues = [[0, 0, 153],
                 [204, 204, 0],
                 [0, 204, 204]]
myPoints = []   ## [x,y, colorid]

def findcolor(img, myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count  = 0
    newpoints = []
    for color in myColors:

        lower = np.array(color[0:3])
        upper = np.array(color[3:6])

        mask = cv2.inRange(imgHSV,lower,upper)
        x, y = findContours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],-1)
        if x!=0 and y!=0:
            newpoints.append([x,y,count])
        count += 1
    return newpoints
def findContours(img):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>100:
            # cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLengthcnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2, y

def drawonCanvas(mypoints,myColorValues):
    for point in  mypoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)


while True:
    success, img = cap.read()
    imgResult = img.copy()
    newpoints = findcolor(img,myColors,myColorValues)
    if len(newpoints)!=0:
        for newp in newpoints:
            myPoints.append(newp)

    if len(myPoints)!=0:
        drawonCanvas(myPoints,myColorValues)

    cv2.imshow("Result",imgResult)

    if cv2.waitKey(1) == ord('s'):
        break
