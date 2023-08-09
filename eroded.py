import cv2
import numpy as np

def erode_image(image_path, kernel_size):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Define an erosion kernel (square with all ones)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    
    # Perform image erosion
    eroded_image = cv2.erode(image, kernel, iterations=4)
    
    # Display the original and eroded images
    cv2.imshow("Original Image", image)
    cv2.imshow("Eroded Image", eroded_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

erode_image("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/input.jpg", kernel_size=3)
