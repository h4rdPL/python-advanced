import cv2

image = cv2.imread("../images/image.jpg")
if image is None:
    raise ValueError("Nie można wczytać obrazu.")

flipped_horizontal = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped_horizontal)
cv2.waitKey(0)

flipped_vertical = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped_vertical)
cv2.waitKey(0)

flipped_both = cv2.flip(image, -1)
cv2.imshow("Flipped Both Axes", flipped_both)
cv2.waitKey(0)

cv2.imshow("Original", image)
cv2.imshow("Flipped Horizontally", flipped_horizontal)
cv2.imshow("Flipped Vertically", flipped_vertical)
cv2.imshow("Flipped Both Axes", flipped_both)
cv2.waitKey(0)

height, width = image.shape[:2]
crop = image[:, width//2:]
crop_flipped = cv2.flip(crop, 1)
image[:, width//2:] = crop_flipped
cv2.imshow("Partial Flip", image)
cv2.waitKey(0)

choice = int(input("Wybierz sposób odbicia (0 – pionowe, 1 – poziome, -1 – oba): "))
flipped_custom = cv2.flip(image, choice)
cv2.imshow("Custom Flip", flipped_custom)
cv2.waitKey(0)

cv2.destroyAllWindows()
