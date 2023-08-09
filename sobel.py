import cv2
import numpy as np

# Load the image
img = cv2.imread("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise
img_blur = cv2.GaussianBlur(img, (3, 3), 0)

# Calculate the gradients using Sobel
gradient_x = cv2.Sobel(img_blur, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(img_blur, cv2.CV_64F, 0, 1, ksize=3)

# Calculate the magnitude of gradients
gradient_magnitude = np.sqrt(gradient_x**2 + gradient_y**2)

# Normalize the magnitude to the range [0, 255]
gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Display the original image, gradient_x, gradient_y, and gradient magnitude
cv2.imshow('Original Image', img)
cv2.imshow('Gradient X', gradient_x)
cv2.imshow('Gradient Y', gradient_y)
cv2.imshow('Gradient Magnitude', gradient_magnitude_normalized)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
