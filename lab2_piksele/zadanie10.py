import cv2

image = cv2.imread('image.jpg')

pixel1 = image[50, 50]
pixel2 = image[200, 200]

difference = [abs(pixel1[i] - pixel2[i]) for i in range(3)]

print(f'Różnica w wartościach R, G, B: {difference}')
