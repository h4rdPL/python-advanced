import cv2
import imutils

image = cv2.imread("../images/image.jpg")


resized_width = imutils.resize(image, width=500)
cv2.imshow("Width resized to 500", resized_width)
cv2.waitKey(0)