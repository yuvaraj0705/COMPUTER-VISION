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

    # Apply Gaussian blur to the grayscale image
    blurred = cv2.GaussianBlur(gray_img, (5, 5), 0)

    # Calculate the high-pass filtered image by subtracting the blurred image from the original
    high_pass = gray_img - blurred

    # Define the scaling factor (boost factor)
    boost_factor = 2.0

    # Calculate the sharpened image by adding the scaled high-pass filtered image to the original
    sharpened = gray_img + boost_factor * high_pass

    # Clip pixel values to the valid range [0, 255]
    sharpened = np.clip(sharpened, 0, 255)

    # Convert the sharpened image to uint8 format
    sharpened = np.uint8(sharpened)

    # Display the original and sharpened images side by side
    cv2.imshow('Original', img)
    cv2.imshow('sharpened', sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
