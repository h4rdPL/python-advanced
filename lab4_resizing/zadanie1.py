import cv2
import imutils

image = cv2.imread("../images/image.jpg")

resized = imutils.resize(image, width=image.shape[1] // 2, height=image.shape[1] // 2)

cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)