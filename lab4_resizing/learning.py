import cv2
import imutils
# load the original input image and display it on our screen
image = cv2.imread("example.jpg")
cv2.imshow("Original", image)
# let's resize our image to be 150 pixels wide, but in order to
# prevent our resized image from being skewed/distorted, we must
# first calculate the ratio of the *new* width to the *old* width
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))
# perform the resizing
# resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
# cv2.imshow("Resized", resized)
# resized = imutils.resize(image, width=100)
resized = imutils.resize(image, height=75)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)