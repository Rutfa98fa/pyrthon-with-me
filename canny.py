import cv2

img = cv2.imread("image/currency.jpg",0)
can = cv2.Canny(img,50,200)

cv2.imshow("original",img)
cv2.imshow("canny",can)
cv2.waitKey(0)
cv2.destroyAllWindows()