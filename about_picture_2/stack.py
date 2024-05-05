import cv2 as cv
import numpy as np

img1=cv.imread('C:/Users/halit/Desktop/opencv/about_picture_2/ronaldo.png')
img2=cv.imread('C:/Users/halit/Desktop/opencv/about_picture_2/messi.png')
img3=cv.imread('C:/Users/halit/Desktop/opencv/about_picture_2/kenan_karaman.png')

#iki resmi birleştirmek için hstack ve vstack fonksiyonlarını kullanacağım
#birleştireceğim resimlerin boyutlarını aynı yapmam gerekiyor
img1=cv.resize(img1,(300,300))
img2=cv.resize(img2,(300,300)) 
img3=cv.resize(img3,(300,300))

#iki resmi birleştirme işlemi
hor=np.hstack((img1,img2,img3)) #uc resmi yatay birleştirme
ver=np.vstack((img1,img2)) #iki resmi dikey birleştirme
cv.imshow('horizontal',hor) 
cv.imshow('vertical',ver) 
cv.waitKey(0)

