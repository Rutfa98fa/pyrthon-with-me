import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("image/currency.jpg",0)

sob = cv2.Sobel(img,-1,1,0)
soby = cv2.Sobel(img,-1,0,1) #Dx Dy หาแนวนอน
sobelxy = cv2.bitwise_or(sob,soby)

images = [img,sob,sobelxy,soby]
titles = ["ori","sobelx","sobelxy","soby"]

for i in range(len(images)):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()