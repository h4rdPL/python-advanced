import cv2

# Wczytaj obraz
image = cv2.imread("../images/image.jpg")

if image is None:
    print("Błąd: nie można wczytać obrazu!")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    center = (x + w // 2, y + h // 2)
    radius = max(w, h) // 2
    cv2.circle(image, center, radius, (255, 0, 0), 3)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)

    for (ex, ey, ew, eh) in eyes[:2]:
        eye_center = (x + ex + ew // 2, y + ey + eh // 2)
        eye_radius = ew // 2
        cv2.circle(image, eye_center, eye_radius, (0, 0, 255), -1)

    mouths = mouth_cascade.detectMultiScale(roi_gray, 1.7, 11)
    for (mx, my, mw, mh) in mouths:
        mouth_y = y + my + mh // 2
        if mouth_y > y + h // 2:
            cv2.rectangle(image, (x + mx, y + my + mh // 4), (x + mx + mw, y + my + mh), (0, 255, 0), -1)
            break

cv2.imshow("Ukryte szczegóły", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
