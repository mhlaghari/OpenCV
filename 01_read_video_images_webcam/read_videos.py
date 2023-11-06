import cv2

cap = cv2.VideoCapture("/Users/mhlaghari/PycharmProjects/OpenCV/Videos/2.mp4")

while True:
    success, frame = cap.read()
    if success:
        cv2.imshow("Output", frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyWindow("Output")
