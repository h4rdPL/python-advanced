import cv2
import numpy as np

img = np.zeros((400, 400, 3), dtype=np.uint8)

cv2.rectangle(img, (10, 10), (110, 60), (0, 255, 0), -1)

cv2.rectangle(img, (290, 350), (390, 390), (0, 0, 255), 3)

cv2.imshow('Prostokąty', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
