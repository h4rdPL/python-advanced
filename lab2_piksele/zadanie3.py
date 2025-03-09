import cv2

image = cv2.imread('image.jpg')

height, width, _ = image.shape
center = (width // 2, height // 2)

pixel_value = image[center[1], center[0]]

print(f'Wartość piksela w środku obrazu: B={pixel_value[0]}, G={pixel_value[1]}, R={pixel_value[2]}')
