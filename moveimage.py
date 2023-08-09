import cv2
import numpy as np

def move_image(image_path, x_offset, y_offset):
    image = cv2.imread(image_path)
    
    # Get image dimensions
    height, width = image.shape[:2]
    
    # Create a larger canvas
    canvas_height = height + abs(y_offset)
    canvas_width = width + abs(x_offset)
    canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)
    
    # Calculate the position to paste the image
    x_pos = max(0, x_offset)
    y_pos = max(0, y_offset)
    
    # Paste the image onto the canvas
    canvas[y_pos:y_pos+height, x_pos:x_pos+width] = image
    
    # Display the canvas with the moved image
    cv2.imshow("Moved Image", canvas)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

move_image("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/input.jpg", x_offset=50, y_offset=100)  # Adjust offsets as needed
