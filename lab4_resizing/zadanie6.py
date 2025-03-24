import cv2

image = cv2.imread("../images/image.jpg")


height_ratio = 400 / image.shape[0]
new_width = int(image.shape[1] * height_ratio)
resized_height = cv2.resize(image, (new_width, 400))
cv2.imshow("Height resized to 400", resized_height)
cv2.waitKey(0)
