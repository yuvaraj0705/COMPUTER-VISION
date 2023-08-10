import cv2
img = cv2.imread('C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/modi.jpg')
gray_img = cv2.cvtColor(img,cv2.IMREAD_GRAYSCALE)
haarcascade =cv2.CascadeClassifier("C:\\Users\\ASUS\\OneDrive\\Documents\\COMPUTER VISION\\images\\haarcascade_smile.xml")
faces_rec = haarcascade.detectMultiScale(gray_img,1.1,10)
for (x,y,w,h) in faces_rec:
    cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0), 2)
    cv2.imshow('Detected faces',img)

    cv2.waitKey(0)