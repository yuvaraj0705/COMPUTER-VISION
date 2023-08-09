import cv2
import numpy as np

def apply_perspective_transformation(image_path):
    image = cv2.imread(image_path)
    
    # Define the points for the original and transformed images
    original_points = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    transformed_points = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    
    # Calculate the perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(original_points, transformed_points)
    
    # Apply the perspective transformation
    transformed_image = cv2.warpPerspective(image, matrix, (300, 300))
    
    # Display the original and transformed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Transformed Image", transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

apply_perspective_transformation("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/input.jpg")  # Replace with your image path
