import cv2
import numpy as np
img = cv2.imread('C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg')
if  img is None:
    print('error')
else:
    prewitt1_x = np.array([ [-1,0,1],[-1,0,1],[-1,0,1] ])
    prewitt1_y = np.array([ [-1,-1,-1],[0,0,0],[1,1,1]])

    prewitt_x= cv2.filter2D(img, cv2.CV_64F, prewitt1_x)
    
    prewitt_y= cv2.filter2D(img, cv2.CV_64F, prewitt1_y)
    prewitt_x= cv2.convertScaleAbs(prewitt_x)
    prewitt_y=cv2.convertScaleAbs(prewitt_x)
    cv2.imshow('original',img)
    cv2.imshow('prewitt_x',prewitt_x)
    cv2.imshow('prewitt_y',prewitt_y)
    cv2.waitKey(0)
    cv2.destroyAllWindows()