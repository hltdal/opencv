#40,30  --  100,80
#230,30  --  290,80
x1,x2=40,100
y1,y2=30,80
x3,x4=230,290
y3,y4=30,80

import numpy as np
import cv2 as cv

img=cv.imread('C:/Users/halit/Desktop/opencv/about_picture_2/ronaldo.png')

award=img[y1:y2,x1:x2]
img[y3:y4,x3:x4]=award

cv.imshow('image',img)

cv.waitKey(0)