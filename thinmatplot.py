import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/gradient.png")
##def threshold in opeencv 
thresh,th1 = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
thresh,th2 = cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
thresh,th3 = cv2.threshold(img,128,255,cv2.THRESH_TRUNC)
thresh,th4 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO)
thresh,th5 = cv2.threshold(img,128,255,cv2.THRESH_TOZERO_INV) ##ใส่ thresh ค่าเทสและผลลัพท์


images = [img,th1,th2,th3,th4,th5]
titles = ["output","BINARY","BINARY_INV","TRUNC","Tozeros","Tozeros_INV"]

for i in range(len(images)):
     plt.subplot(2,3,i+1) ##เริ่มต้นที่ภาพแรกแสดงผล
     plt.imshow(images[i]) #โชว์ image ที่ i เรียงตามลูป
     plt.title(titles[i])
     plt.xticks([]),plt.yticks([])

plt.show()