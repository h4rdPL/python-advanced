import cv2
import imutils

image = cv2.imread("../images/image.jpg")

methods = [cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_LANCZOS4]
names = ["INTER_NEAREST", "INTER_LINEAR", "INTER_CUBIC", "INTER_LANCZOS4"]
for method, name in zip(methods, names):
    resized = cv2.resize(image, None, fx=3, fy=3, interpolation=method)
    cv2.imshow(f"Scaled x3 - {name}", resized)
    cv2.waitKey(0)
