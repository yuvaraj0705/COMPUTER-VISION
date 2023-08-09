import cv2

# Load the image
image = cv2.imread("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/input.jpg")

# Get original image dimensions
original_height, original_width = image.shape[:2]

# Set the target output size (width, height)
output_size = (800, 600)  # Adjust this as needed

# Calculate scale factors for width and height
scale_factor_width = output_size[0] / original_width
scale_factor_height = output_size[1] / original_height

# Resize the image using different interpolation methods
resized_smaller = cv2.resize(image, output_size, interpolation=cv2.INTER_AREA)
resized_larger = cv2.resize(image, output_size, interpolation=cv2.INTER_LINEAR)

# Display the original, smaller, and larger images
cv2.imshow("Original Image", image)
cv2.imshow("Smaller Image", resized_smaller)
cv2.imshow("Larger Image", resized_larger)
cv2.waitKey(0)
cv2.destroyAllWindows()
