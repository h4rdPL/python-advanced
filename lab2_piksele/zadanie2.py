import cv2

image = cv2.imread('image.jpg')

cv2.imshow('Przed zmianą', image)

height, width, _ = image.shape
image[height-1, width-1] = [0, 0, 255]

cv2.imshow('Po zmianie', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
