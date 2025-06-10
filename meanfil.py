import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/Noise.png")
##filter
filter2D = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25)

##blur เพิ่มขนาดเยอะจะยิ่งเบลอ mean
blur = cv2.blur(img,(5,5))

##median blur
MBlur = cv2.medianBlur(img,5)

gblur = cv2.GaussianBlur(img,(5,5),1) #sigma mainkey

titles = ["origin","filter2D","blur","Median","gaussian"]
images = [img,filter2D,blur,MBlur,gblur]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()