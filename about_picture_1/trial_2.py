import numpy 
import cv2 

#  https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing_functions.html

img=numpy.zeros((511,511,3), numpy.uint8) #siyah bir resim oluşturduk
#img=cv2.imread("C:/Users/halit/Desktop/opencv/about_picture/tuna_tavus.png")  #img değişkenine resmi de atayabiliriz
cv2.line(img,(0,100),(100,0),(255,0,0),5) #5 px kalınlığında mavi bir çizgi çizdik
cv2.imshow("Line",img)
cv2.waitKey(3000) 
cv2.destroyAllWindows()


img=numpy.zeros((511,511,3), numpy.uint8)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),5) #5 px kalınlığında yeşil bir dikdörtgen çizdik
cv2.imshow("Rectangle",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()

img=numpy.zeros((511,511,3), numpy.uint8)
cv2.circle(img,(447,63), 63, (0,0,255), -1) #içi dolu kırmızı bir daire çizdik
cv2.imshow("Circle",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()


img=numpy.zeros((511,511,3), numpy.uint8)
cv2.ellipse(img,(256,256),(100,50),0,90,180,255,-1) #içi dolu mavi bir elips çizdik
cv2.imshow("Ellipse",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()


img=numpy.zeros((511,511,3), numpy.uint8)
pts = numpy.array([[10,5],[20,30],[70,20],[50,10]], numpy.int32) #4 köşeli bir çokgen çizdik
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow("Polygon",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()


img=numpy.zeros((511,511,3), numpy.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA) #yazı yazdık
cv2.imshow("Text",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()



