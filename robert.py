import cv2
import numpy as np


def robert_edge_detection(image_path, threshold):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Robert operator matrices
    Gx = np.array([[1, 0], [0, -1]])
    Gy = np.array([[0, 1], [-1, 0]])

    # Convolve the image with Gx and Gy
    gradient_x = cv2.filter2D(image, cv2.CV_64F, Gx)
    gradient_y = cv2.filter2D(image, cv2.CV_64F, Gy)

    # Calculate gradient magnitude
    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

    # Apply thresholding
    edges = np.where(gradient_magnitude > threshold, 255, 0)

    # Display the result
    cv2.imshow("Original Image", image)
    cv2.imshow("Edges", edges.astype(np.uint8))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Call the function with your image path and threshold
robert_edge_detection("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg", threshold=50)
