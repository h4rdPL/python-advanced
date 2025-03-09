import cv2
import numpy as np

image = cv2.imread('image.jpg')

brightness = np.sum(image, axis=2)

y, x = np.unravel_index(np.argmax(brightness), brightness.shape)

bright_pixel = image[y, x]
print(f'Współrzędne najjaśniejszego piksela: ({x}, {y})')
print(f'Wartość najjaśniejszego piksela: B={bright_pixel[0]}, G={bright_pixel[1]}, R={bright_pixel[2]}')
