import cv2
# Wczytanie obrazu z pliku
image = cv2.imread("image.jpg")
image_gray = cv2.imread("image_gray.jpg", cv2.IMREAD_GRAYSCALE)
# Sprawdzenie, czy obraz został poprawnie wczytany
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")


(h, w, c) = image.shape[:3]

print(f'width: {w} pixels')
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')

# cv2.imshow("Wyświetlony obraz", image) # Tworzy okno i wyświetla obraz
# cv2.waitKey(0) # Czeka na dowolny klawisz, by zamknąć okno
# cv2.destroyAllWindows() # Zamknięcie wszystkich okien


cv2.imshow("Obraz w skali szarości", image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()