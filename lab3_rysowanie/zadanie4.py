import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype=np.uint8)

center = (200, 200)

cv2.rectangle(img, (150, 150), (250, 250), (0, 255, 0), 2)

cv2.circle(img, center, 30, (255, 0, 0), -1)

cv2.imshow('Figura', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
