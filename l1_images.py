import numpy as np
import cv2

img = cv2.imread('notre_dame_fire.jpg') # Read image into a numpy array
cv2.imshow('image',img) # Display the image to a window
cv2.waitKey(0)  # Keep window open until a key is pressed
cv2.destroyAllWindows() # Close the image window  