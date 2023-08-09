import cv2
import numpy as np

# Load the image
image_path = 'C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Load as grayscale

# Check if the image was loaded properly
if img is None:
    print("Error: Image not loaded properly.")
else:
    # Apply Sobel edge detection along the X-axis
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Sobel along X-axis

    # Convert the gradient values to absolute values
    sobel_x_abs = cv2.convertScaleAbs(sobel_x)

    # Display the original image and the Sobel result side by side
    combined_img = cv2.hconcat([img, sobel_x_abs])
    cv2.imshow('Original', img)
    cv2.imshow('sobel_x',sobel_x_abs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
