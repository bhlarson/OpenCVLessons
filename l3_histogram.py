import numpy as np
import matplotlib.pyplot as plt
import cv2

# Read grayscale image into a numpy array
img = cv2.imread('notre_dame_fire.jpg',0) 


# img.ravel() converts a 2D array into a 1-D vector.
# plt.hist makes a plot of the number of pixels of each color there are in the image
plt.hist(img.ravel(), bins=256, range=(0.0, 255.0), fc='k', ec='k')
plt.show()