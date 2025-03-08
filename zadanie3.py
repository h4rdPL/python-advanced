import cv2

image = cv2.imread("pies_szary.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

(h, w, c) = image.shape[:3]
print(f'channels: {c}')
