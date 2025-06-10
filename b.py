import cv2
import matplotlib.pyplot as plt
img =cv2.imread("image/girl.jpg")
cv2.imshow("output",img)

img =cv2.cvtColor(img,cv2.COLOR_BGR2RGB) ##เปลีย่นสี 
plt.imshow(img) ##เเปลงสี rgb ถ้าเอา bgr มาภาพจะเพี้ยนต้องแปลงภาพก่อน 
plt.show()