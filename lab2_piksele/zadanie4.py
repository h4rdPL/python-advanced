import cv2

image = cv2.imread('image.jpg')

x = int(input("Podaj współrzędną x: "))
y = int(input("Podaj współrzędną y: "))

height, width, _ = image.shape
if x < 0 or x >= width or y < 0 or y >= height:
    print("Współrzędne poza zakresem obrazu!")
else:
    image[y, x] = [0, 0, 0]

    cv2.imshow('Po zmianie', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
