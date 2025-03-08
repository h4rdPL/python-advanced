from PIL import Image
import cv2

# Wczytanie obrazu z pliku
image = cv2.imread("image.jpg", cv2.IMREAD_GRAYSCALE)
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

cv2.imwrite('pies_szary.jpg', image)