import cv2

image = cv2.imread('image.jpg')

height, width, _ = image.shape
third_height, third_width = height // 3, width // 3

center_fragment = image[third_height:2*third_height, third_width:2*third_width]

cv2.imshow('Wycięty fragment', center_fragment)
cv2.waitKey(0)
cv2.destroyAllWindows()
