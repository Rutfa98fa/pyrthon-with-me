import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image/ant.jpg")
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

thresh_value = [50.100,130,200,230]
plt.subplot(231,xticks=[],yticks=[]) ## 2 row 3 column  1 ให้ img
plt.title("output")
plt.imshow(gray_img,cmap="gray")

for i in range(len(thresh_value)): ##ลูปตามนับค่าใน thres value
    thresh,result = cv2.threshold(gray_img,thresh_value[i],255,cv2.THRESH_BINARY) ##แปลง th เป็น  def binary
    plt.subplot(232+i) ##ตัวถัดจากรูปแรก
    plt.title("%d"%thresh_value[i]) ##แสดงค่าตาม th value ใน data
    plt.imshow(result,cmap="gray") ##กำหนดเป็น gray scale
    plt.xticks([]),plt.yticks([]) ##แสดงตาม subplot
plt.show()