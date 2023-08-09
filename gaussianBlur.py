import cv2

# Load the image
image_path = 'C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg'
img = cv2.imread(image_path)

# Check if the image was loaded properly
if img is None:
    print("Error: Image not loaded properly.")
else:
    # Apply Gaussian blur
    blurred_img = cv2.GaussianBlur(img, (5, 5), 0)  # You can adjust the kernel size (5, 5) and sigma as needed

    # Display the original and blurred images side by side
    cv2.imshow('Original', img)
    cv2.imshow('Gaussian',blurred_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
