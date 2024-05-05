import numpy as np
import cv2 as cv

width , height = 400, 300
points=[]
def perspective(event,x,y,flags,param):
    global points
    if event == cv.EVENT_LBUTTONDOWN and len(points)<4:
        cv.circle(img,(x,y),5,(0,0,255),cv.FILLED)
        points.append((x,y))

img=cv.imread("C:/Users/halit/Desktop/opencv/about_picture_2/iskambil.jpg")
cv.namedWindow("Image")
cv.setMouseCallback("Image",perspective)

while 1:
    cv.imshow("Image",img)
    if len(points) == 4:
        pts1=np.float32([[points[0][0],points[0][1]],[points[1][0],points[1][1]],[points[2][0],points[2][1]],[points[3][0],points[3][1]]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv.getPerspectiveTransform(pts1, pts2)
        imgoutput = cv.warpPerspective(img, matrix, (width, height))
        cv.imshow("Output", imgoutput)
        cv.waitKey(0)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
