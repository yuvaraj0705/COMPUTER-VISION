import cv2

# Load the image
img = cv2.imread("C:/Users/ASUS/OneDrive/Documents/COMPUTER VISION/images/musk.jpg")

# Check if the image was loaded properly
if img is None:
    print("Error: Image not loaded properly.")
else:
    # Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow('original Image', img)
    cv2.imshow('Grayscale Image', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
