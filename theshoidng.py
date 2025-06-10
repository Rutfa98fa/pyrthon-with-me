import cv2


img = cv2.imread("image/gradient.png")
##def threshold in opeencv 
thresh,th1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
thresh,th2 = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
thresh,th3 = cv2.threshold(img,128,255,cv2.THRESH_TRUNC) ##ใส่ thresh ค่าเทสและผลลัพท์

cv2.imshow("output",img)
cv2.imshow("BINARY",th1)
cv2.imshow("BINARY_INV",th2)
cv2.imshow("TRUNC",th3)
cv2.waitKey(0)
cv2.destroyAllWindows()