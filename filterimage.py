import cv2
import numpy as np

# Load the image
image_path = 'C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg'
img = cv2.imread(image_path)

# Check if the image was loaded properly
if img is None:
    print("Error: Image not loaded properly.")
else:
    # Define a custom filter kernel
    custom_filter = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])

    # Apply the custom filter using convolution
    filtered_img = cv2.filter2D(img, -1, custom_filter)

    # Display the original and filtered images side by side
    cv2.imshow('oriiginnal',img)
    cv2.imshow('filtered',filtered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
