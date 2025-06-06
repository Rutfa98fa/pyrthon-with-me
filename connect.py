import cv2
import numpy
img = cv2.imread("image/Coin.png")
imgre = cv2.resize(img,(400,400))

##สร้างตำแหน่งสองตำแหน่งเพื่อเชื่อมกัน
points = []

def clickPosition(event,x,y,flags,param):#สร้างฟังก์ชั่นสำหรับเมาส์
    if event == cv2.EVENT_LBUTTONDOWN:
       ##กำหนดวงกลม ตัวแปรภาพ พิกัด ความเข้ม สี
        cv2.circle(imgre,(x,y),10,(0,0,255),4)
        points.append((x,y))
        print(points)
        if len(points)>=2:
           cv2.line(imgre,points[-2],points[-1],(0,255,0),5)
        
        cv2.imshow("output",imgre)

cv2.imshow("output",imgre)
##แสดงพิกัดด้วยเมาส์
cv2.setMouseCallback("output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()