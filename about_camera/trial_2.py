import numpy
import cv2

cap=cv2.VideoCapture(0) 
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("C:/Users/halit/Desktop/opencv/about_camera/editted.mp4",fourcc,20.0,(640,480)) #söylenen aderese kayıt yapar

while cap.isOpened:
    ret , frame = cap.read()
    out.write(frame)
    cv2.imshow("cerceve ismi",frame) 
    if cv2.waitKey(1) == ord('q'): 
        break

cap.release()
out.release()
cv2.destroyAllWindows()
