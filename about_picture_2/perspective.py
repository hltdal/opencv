import numpy as np
import cv2 as cv

#Bir ABCD dörtgeninin dört köşe noktasının koordinatları verilmiştir.

#A-374,135    B-584,231    C-87,384      D-307,535

width , height = 400, 300

img=cv.imread("C:/Users/halit/Desktop/opencv/about_picture_2/iskambil.jpg")

pts1=np.float32([[374,135],[584,231],[87,384],[307,535]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv.getPerspectiveTransform(pts1,pts2) #pts1 matrisini pts2 matrisine dönüştürür.
imgoutput=cv.warpPerspective(img,matrix,(width,height)) 


#Buranın çok önemi yok sadece noktaları girdim ve işaretledim.
for x in range(0, 4):
    cv.circle(img, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 0, 255), cv.FILLED)


cv.putText(img, "A", (int(pts1[0][0]), int(pts1[0][1])), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv.putText(img, "B", (int(pts1[1][0]), int(pts1[1][1])), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv.putText(img, "C", (int(pts1[2][0]), int(pts1[2][1])), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
cv.putText(img, "D", (int(pts1[3][0]), int(pts1[3][1])), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

cv.imshow("Image",img)
cv.imshow("Output",imgoutput)
cv.waitKey(0)
cv.destroyAllWindows()

