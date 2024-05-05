import numpy as np
import cv2 as cv

drawing = False # true if mouse is pressed
ix,iy = -1,-1
color=(0,0,0)
pixel=5

def nothing(x):
    pass

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,color
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(img,(x,y),pixel,color,-1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img,(x,y),pixel,color,-1)


img =np.ones((511,511,3), np.uint8)*255 # create a white image
cv.namedWindow('Paint')
cv.setMouseCallback('Paint',draw_circle)


cv.createTrackbar('Red','Paint',0,255,nothing)
cv.createTrackbar('Green','Paint',0,255,nothing) # create trackbars for color change
cv.createTrackbar('Blue','Paint',0,255,nothing)
cv.createTrackbar('Size','Paint',1,10,nothing)

while 1:
    cv.waitKey(25)
    r=cv.getTrackbarPos('Red','Paint')
    g=cv.getTrackbarPos('Green','Paint') # get current positions of four trackbars
    b=cv.getTrackbarPos('Blue','Paint')
    s=cv.getTrackbarPos('Size','Paint')
    pixel=s
    color=(b,g,r)
    cv.imshow("Paint",img)
    
cv.destroyAllWindows()
