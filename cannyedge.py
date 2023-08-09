import cv2

# Load the image
img = cv2.imread("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg", cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to reduce noise and improve edge detection
img_blur = cv2.GaussianBlur(img, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(img_blur, 100, 200)  # You can adjust the threshold values

# Display the original image, the blurred image, and the edges
cv2.imshow('Original Image', img)
cv2.imshow('Blurred Image', img_blur)
cv2.imshow('Canny Edge Detection', edges)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
