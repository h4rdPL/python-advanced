import cv2

image = cv2.imread('image.jpg')

image[50:100, 50:100] = [255, 255, 255]

cv2.imshow('Po zmianie', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
