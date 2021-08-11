import numpy as np
import cv2
import wget
wget.download("https://github.com/Izkhorbek/Python-OpenCV-exercises-/blob/main/Contours_and_shape_detection/basic_shapes.png")
path = 'basic_shapes.png'
img = cv2.imread(path)
img = cv2.resize(img,(img.shape[1]//2, img.shape[0]//2 ))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgContour = img.copy()
def getContours(img):
    contours, hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) # this gives us corner points.
            print(approx)

            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if objCor==3: objType = "Tri"
            elif objCor==4:
                aspRatio = w/float(h)
                if aspRatio>0.5 and aspRatio<1.05: objType="Square"
                else: objType="Rectangle"
            elif objCor==5:
                objType="Fivetangle"
            elif objCor>5:
                objType="Circle"
            else: objType='None'

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objType,(x+(w//2)-10, y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)



getContours(imgCanny)

cv2.imshow('Shapes_Image',imgContour)
cv2.waitKey(0)