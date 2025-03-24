resized_output = imutils.resize(image, width=800)
cv2.imwrite("resized_output.jpg", resized_output)
print("Obraz zapisano jako 'resized_output.jpg'")

cv2.destroyAllWindows()
