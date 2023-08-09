import cv2
img = cv2.imread('C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg')
if img is None:
    print("error")
else:
    blur_img = cv2.blur(img, (5,5),0)
    cv2.imshow('original', img)
    cv2.imshow('blur_img', blur_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()