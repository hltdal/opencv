import numpy as np
import cv2 as cv


global r,g,b,size
r,g,b,size = 0,0,0,0

def nothing(x):
    pass

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1

def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing


    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            cv.circle(img,(x,y),size,(b,g,r),-1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img,(x,y),size,(b,g,r),-1)

# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)

cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)

cv.createTrackbar('size','image',0,10,nothing)


while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    size= cv.getTrackbarPos('size','image')

    cv.setMouseCallback('image',draw_circle)

cv.destroyAllWindows()