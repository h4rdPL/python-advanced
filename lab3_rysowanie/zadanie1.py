import cv2

image = cv2.imread("../images/image.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")


blue = (255, 0, 0)
(centerX, centerY) = (image.shape[1] // 2, image.shape[0] // 2)

cv2.line(image, (centerX), (0,0), blue)
cv2.imshow("Canvas", image)
cv2.waitKey(0)
