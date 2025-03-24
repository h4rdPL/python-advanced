import cv2

image = cv2.imread("../images/image.jpg")


resized_down = cv2.resize(image, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
cv2.imshow("Scaled Down x5 - INTER_AREA", resized_down)
cv2.waitKey(0)
