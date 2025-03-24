import cv2

image = cv2.imread("../images/image.jpg")

for scale in range(100, 301, 20):
    factor = scale / 100
    resized_loop = cv2.resize(image, None, fx=factor, fy=factor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(f"Resized {scale}%", resized_loop)
    cv2.waitKey(500)