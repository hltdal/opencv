import numpy as np
import cv2 as cv
 
cap = cv.VideoCapture(0)# 0: default camera

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
 
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Mevcut çözünürlükleri kontrol et
    print(f"Genişlik: {cap.get(cv.CAP_PROP_FRAME_WIDTH)}")
    print(f"Yükseklik: {cap.get(cv.CAP_PROP_FRAME_HEIGHT)}")

    # Yeni çözünürlük ayarlarını set et
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)


    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
 
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()

