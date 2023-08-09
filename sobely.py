import cv2
import numpy as np

# Load the image
image_path = 'C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load as grayscale

# Check if the image was loaded properly
if img is None:
    print("Error: Image not loaded properly.")
else:
    # Apply Sobel edge detection along the Y-axis
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Sobel along Y-axis

    # Convert the gradient values to absolute values
    sobel_y_abs = cv2.convertScaleAbs(sobel_y)

    # Display the original image and the Sobel result side by side
    cv2.imshow('Original', img)
    cv2.imshow('sobel Y', sobel_y_abs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
