import cv2

image = cv2.imread('image.jpg')

height, width, _ = image.shape
half_height, half_width = height // 2, width // 2

image[:half_height, :half_width] = [255, 0, 0]

cv2.imshow('Po zmianach', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
