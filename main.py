import cv2

# Load an image from file
image_path = 'path_to_your_image.jpg'
frame = cv2.imread(image_path)

# Display the image
cv2.imshow('Image', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()


