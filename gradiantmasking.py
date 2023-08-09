import cv2
import numpy as np

# Load the image
image_path = 'C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg'
img = cv2.imread(image_path)

# Check if the image was loaded properly
if img is None:
    print("Error: Image not loaded properly.")
else:
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Calculate gradients using Sobel operators
    gradient_x = cv2.Sobel(gray_img, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(gray_img, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate gradient magnitude
    gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

    # Define a sharpening factor (adjust this value to control the level of sharpening)
    sharpening_factor = 0.5

    # Combine the original image with the scaled gradient magnitude for sharpening
    sharpened = gray_img + sharpening_factor * gradient_magnitude

    # Clip pixel values to the valid range [0, 255]
    sharpened = np.clip(sharpened, 0, 255)

    # Convert the sharpened image to uint8 format
    sharpened = np.uint8(sharpened)

    # Display the original and sharpened images side by side
    cv2.imshow('Original', img)
    cv2.imshow('sharpened', sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
