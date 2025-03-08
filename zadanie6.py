import cv2

image = cv2.imread("image_gray.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

    cv2.namedWindow("Obraz w skali szarości", cv2.WINDOW_NORMAL)

    cv2.imshow("Obraz w skali szarości", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
