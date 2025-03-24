import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype=np.uint8)

center = (200, 200)

for i in range(1, 6):
    size = i * 20
    top_left = (center[0] - size // 2, center[1] - size // 2)
    bottom_right = (center[0] + size // 2, center[1] + size // 2)
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 255), 1)

cv2.imshow('Kwadraty', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
