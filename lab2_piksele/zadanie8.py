import cv2

image = cv2.imread('image.jpg')

image[99, :] = [0, 255, 0]

cv2.imshow('Po zmianie', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
