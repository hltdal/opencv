import numpy
import cv2

cap=cv2.VideoCapture("C:/Users/halit/Desktop/opencv/about_video/kimminjae.mp4") #videoyu oynatır

while cap.isOpened:
    ret , frame =cap.read()
    cv2.imshow("cerceve ismi",cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY))
    if cv2.waitKey(25) == ord('q'): #q tusuna basınca video kapanır
        break
    

cap.release()
cv2.destroyAllWindows()


