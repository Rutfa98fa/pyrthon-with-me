import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/Noise.png")
##kernel = np.ones((3,3),np.float32)/9 ##หารด้วยขนาด 3*3
##convolution
convo1 = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/9)
convo2 = cv2.filter2D(img,-1,np.ones((5,5),np.float32)/25)

titles = ["origin","Convo1","Convo2"]
images = [img,convo1,convo2]

for i in range(len(images)):
    plt.subplot(1,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()