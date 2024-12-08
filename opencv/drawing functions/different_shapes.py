import numpy as np
import cv2 as cv
 
# Create a black image
img = np.zeros((512,512,3), np.uint8)
 
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(0,0),(511,511),(255,0,0),5)

# Draw a rectangle with green color filled inside
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a circle with red color filled inside
cv.circle(img,(447,63), 63, (0,0,255), -1)

# Draw an ellipse with yellow color filled inside
cv.ellipse(img,(256,256),(100,50),0,0,180,(255,255,0),-1)

# Draw a polygon with yellow color filled inside
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

# Draw a text with white color
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 3,(255,255,255),5,cv.LINE_AA)

# Display the image
cv.imshow('image', img)

while True:
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()

