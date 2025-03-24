import cv2
import imutils

image = cv2.imread("../images/image.jpg")

resized = imutils.resize(image, width=image.shape[1] * 2, height=image.shape[1] * 2, interpolation = cv2.INTER_LINEAR)

cv2.imshow("Resized via imutils + INTER_LINEAR", resized)
cv2.waitKey(0)