import cv2

capture = cv2.VideoCapture(0)

while  True:
    _, frame = capture.read()
    cv2.imshow("Capture from webcam", frame)
    if cv2.waitKey(1) == 27:  # Corrected from waitkey to waitKey
        break

capture.release()
cv2.destroyAllWindows()
