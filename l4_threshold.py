import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

# From https://docs.opencv.org/4.1.0/d7/d4d/tutorial_py_thresholding.html

# Read grayscale image into a numpy array
img = cv.imread('notre_dame_fire.jpg',0)
# Resize the image using OpenCV resize function
height, width = img.shape[:2]
scaleFactor = 1/2
img = cv.resize(img,(int(scaleFactor*width), int(scaleFactor*height)), interpolation = cv.INTER_CUBIC)

img = cv.medianBlur(img,5) # 5x5 average of all pixels

# pixels above 127 become white (255).  Pixels below 128 become black (0)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY) 

th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,2)
            
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,2)
            
titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()