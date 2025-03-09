import cv2

image = cv2.imread('image.jpg')

pixel_value = image[0, 0]

print(f'Wartość piksela w lewym górnym rogu (0,0): B={pixel_value[0]}, G={pixel_value[1]}, R={pixel_value[2]}')
