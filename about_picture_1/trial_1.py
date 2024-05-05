import cv2
img=cv2.imread("C:/Users/halit/Desktop/opencv/about_picture/tuna_tavus.png",cv2.IMREAD_COLOR) #resmi renkli yapar
cv2.imshow("Tuna Tavus",img)
cv2.waitKey(3000)
img=cv2.imread("C:/Users/halit/Desktop/opencv/about_picture/tuna_tavus.png",cv2.IMREAD_GRAYSCALE) #resimi siyah beyaz yapar
cv2.imshow("Tuna Tavus",img)
cv2.waitKey(3000)
img=cv2.imread("C:/Users/halit/Desktop/opencv/about_picture/tuna_tavus.png",cv2.IMREAD_UNCHANGED) #resmi oldugu gibi alır
cv2.imshow("Tuna Tavus",img) 
cv2.waitKey(0) #0 yazarsak bir tuşa basana kadar bekler
#cv2.imwrite("tuna_tavus_gray.png",img) #resmi kaydeder

cv2.destroyAllWindows() #tüm pencereleri kapatır