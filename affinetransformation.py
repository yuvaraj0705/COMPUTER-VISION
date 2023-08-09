import cv2
import numpy as np

def apply_affine_transform(image_path):
    image = cv2.imread(image_path)
    
    # Define the points for the original and transformed images
    original_points = np.float32([[50, 50], [200, 50], [50, 200]])
    transformed_points = np.float32([[10, 100], [200, 50], [100, 250]])
    
    # Calculate the affine transformation matrix
    matrix = cv2.getAffineTransform(original_points, transformed_points)
    
    # Apply the affine transformation
    transformed_image = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
    
    # Display the original and transformed images
    cv2.imshow("Original Image", image)
    cv2.imshow("Transformed Image", transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

apply_affine_transform("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/input.jpg")  # Replace with your image path
