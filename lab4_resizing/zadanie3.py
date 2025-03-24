import cv2

image = cv2.imread("../images/image.jpg")
if image is None:
    raise ValueError("Nie można wczytać obrazu.")

resized_fixed = cv2.resize(image, (200, 300))
cv2.imshow("Resized to 200x300", resized_fixed)
cv2.waitKey(0)