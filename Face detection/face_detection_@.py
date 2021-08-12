import cv2

img = cv2.imread("D:\Python\PyCharm\Face detection\people.jpg")
imgGrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
Imgcascade = cv2.CascadeClassifier("D:\Python\PyCharm\Face detection\haarcascade_frontalface_default.xml")

faces = Imgcascade.detectMultiScale(imgGrey,1.2,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("result",img)
cv2.waitKey(0)
