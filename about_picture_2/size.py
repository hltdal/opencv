import numpy as np
import cv2 as cv

path="C:/Users/halit/Desktop/opencv/about_picture_2/ronaldo.png"
img=cv.imread(path)

print(img.shape)
weidth,height=600,600
imgresize=cv.resize(img,(weidth,height)) #resmi yeniden boyutlandırır
cv.imshow('imgresized',imgresize)

imgcrop=imgresize[0:300,0:300] #verdiğim koordinatlar arasındaki kısmı alır
cv.imshow('imgcrop',imgcrop)

imgcropresize=cv.resize(imgresize,(img.shape[1],img.shape[0])) #resmi eski haline getirir
cv.imshow('imgcropresize',imgcropresize)
cv.waitKey(0)

cv.destroyAllWindows()

