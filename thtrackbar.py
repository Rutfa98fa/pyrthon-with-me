import cv2

def display(value):
    pass

cv2.namedWindow("output")
cv2.createTrackbar("value","output",0,255,display)

while True:
    gray = cv2.imread("image/ant.jpg",0) ## 0 = grayscale
    thresh_value = cv2.getTrackbarPos("value","output")
    thresh, result = cv2.threshold(gray,thresh_value,255,cv2.THRESH_BINARY) ##
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

    cv2.imshow("output",result)

cv2.destroyAllWindows()