import cv2

# Load the image
image_path = 'C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg'
img = cv2.imread(image_path)

# Check if the image was loaded properly
if img is None:
    print("Error: Image not loaded properly.")
else:
    # Define the rotation angle in degrees
    angle = 45

    # Rotate the image
    rotated_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Display the original and rotated images side by side
    cv2.imshow('Original', img)
    cv2.imshow('rotated', rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
