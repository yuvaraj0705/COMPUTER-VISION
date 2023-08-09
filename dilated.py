import cv2
import numpy as np

def dilate_image(image_path, kernel_size):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Define a dilation kernel (square with all ones)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    
    # Perform image dilation
    dilated_image = cv2.dilate(image, kernel, iterations=4)
    
    # Display the original and dilated images
    cv2.imshow("Original Image", image)
    cv2.imshow("Dilated Image", dilated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

dilate_image("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/input.jpg", kernel_size=3)
