import cv2

face_cascade = cv2.CascadeClassifier("C:\\Users\\Zeynep\\Desktop\\face_haarcascade.xml")
eye_cascade = cv2.CascadeClassifier("C:\\Users\\Zeynep\\Desktop\\eye_detection.xml")

img = cv2.imread("C:\\Users\\Zeynep\\Downloads\\4.1 face.png.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray)

for (x,y,w,h) in faces :
    cv2.rectangle(img,(x,y),(x+w,y+h),(150,250,0),2)

gray2 = gray[y:y+h,x:x+w]
img2 = img[y:y+h,x:x+w]

eyes = eye_cascade.detectMultiScale(gray2)

for (ex,ey,ew,eh) in eyes:
	cv2.rectangle(img2,(ex,ey),(ex+ew,ey+eh),(220,0,150),2)
         
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
