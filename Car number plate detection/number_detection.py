import cv2
import numpy as np

img = cv2.imread("russian_car/russian_car.jpg")
russian_car = img.copy()
Plate_num_Cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 500
color = (15, 255, 0)
def find_plate(img):
    imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    numberPlate = Plate_num_Cascade.detectMultiScale(imgGRAY,1.1,4)
    for (x,y,w,h) in numberPlate:
        area = w*h
        if area>minArea:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),10)
            cv2.putText(img,"Number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("Result",imgRoi)
            cv2.imshow("Image",img)
            cv2.waitKey(0)

    cv2.imwrite("scanned/rasm_"+str(1)+".jpg",imgRoi)

find_plate(russian_car)