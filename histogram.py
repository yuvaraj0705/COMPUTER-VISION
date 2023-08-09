import cv2
from matplotlib import pyplot as plt
img = cv2.imread("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg",cv2.IMREAD_GRAYSCALE)
histogram = cv2.calcHist([img],[0],None,[256],[0,256] )
plt.plot(histogram)
plt.title('Histogram')
plt.xlabel('Pixel value')
plt.ylabel('frequency')
plt.show()
