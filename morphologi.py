import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("image/CoinNoise.png",0)
thresh , result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)
##สร้างตัวกรองข้อมูล
kernel = np.ones((2,2),np.uint8)
##สร้าง dilation ขยายภาพ
dilation = cv2.dilate(result,kernel,iterations=5) #cv2.dilation(thresh,kernel(ones),loop(iterations))
##การกร่อนภาพ
erodes = cv2.erode(dilation,kernel,iterations=7) ##ทำงานกับ dilation เอา result จาก dilation มา

##opening ลบจุดรบกวนจากภาพ
opening = cv2.morphologyEx(dilation,cv2.MORPH_OPEN,kernel,iterations=7)

##closing
closing = cv2.morphologyEx(result,cv2.MORPH_CLOSE,kernel,iterations=7)

titles = ["Original","Thresh","Dilation","Erodes","Opening","Close"]
images = [img,result,dilation,erodes,opening,closing]

for i in range(len(images)):
    plt.subplot(2,3,i+1) ##1row 3 column
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()