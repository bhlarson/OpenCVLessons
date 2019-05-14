import numpy as np
import cv2

print('try displaying other images')
print ('try changing the scale factor')
print ('change the image interpolation described here: https://docs.opencv.org/4.1.0/da/d54/group__imgproc__transform.html#ga47a974309e9102f5f08231edc7e7529d')

img = cv2.imread('notre_dame_fire.jpg') # Read image into a numpy array
height, width = img.shape[:2]

# Resize the image using OpenCV resize function
scaleFactor = 1/3
img = cv2.resize(img,(int(scaleFactor*width), int(scaleFactor*height)), interpolation = cv2.INTER_CUBIC)

cv2.imshow('image',img) # Display the image to a window
cv2.waitKey(0)  # Keep window open until a key is pressed
cv2.destroyAllWindows() # Close the image window  