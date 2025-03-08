import cv2

image = cv2.imread("image_gray.jpg")
image2 = cv2.imread("image.jpg")

cv2.imshow("Obraz w skali szarościx", image)
cv2.imshow("Obraz w skali szarości", image2)
cv2.waitKey(0)
