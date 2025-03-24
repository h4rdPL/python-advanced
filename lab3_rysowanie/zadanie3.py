import cv2
import numpy as np

img = np.zeros((300, 300, 3), dtype=np.uint8)

cv2.circle(img, (50, 50), 40, (255, 0, 0), -1)

cv2.circle(img, (150, 150), 60, (0, 0, 255), -1)

cv2.imshow('Okręgi', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
