import cv2

# Load the image
image_path = 'C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg'
img = cv2.imread(image_path)

# Check if the image was loaded properly
if img is None:
    print("Error: Image not loaded properly.")
else:
    # Scale the image
    scaled_img = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

    # Display the original and scaled images side by side
    cv2.imshow('Original', img)
    cv2.imshow('scaled_img', scaled_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
