import numpy
import cv2

cap =cv2.VideoCapture(0) #dahili kamerayı kullanır

while True:
    ret , frame = cap.read()
    ret=cap.set(cv2.CAP_PROP_FRAME_WIDTH,320) #cercevenin genisligini ayarlıyorsun
    ret=cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #cercevenin yuksekligini ayarlıyorsun
    cv2.imshow("cerceve ismi",cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)) #kamera goruntusunu siyah beyaz yapar
    #cv2.imshow("cerceve ismi",frame)
    if cv2.waitKey(1) == ord('q'): #q tusuna basınca kamera kapanır
        break

cap.release()
cv2.destroyAllWindows()


