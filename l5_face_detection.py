# from https://www.datacamp.com/community/tutorials/face-detection-python-opencv
# from https://github.com/parulnith/Face-Detection-in-Python-using-OpenCV
# Import the necessary libraries
import numpy as np
import cv2 
import matplotlib.pyplot as plt

def convertToRGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def detect_faces(cascade, test_image, scaleFactor = 1.1):
    # create a copy of the image to prevent any changes to the original one.
    image_copy = test_image.copy()
    
    #convert the test image to gray scale as opencv face detector expects gray images
    gray_image = cv2.cvtColor(image_copy, cv2.COLOR_BGR2GRAY)
    
    # Applying the haar classifier to detect faces
    faces_rect = cascade.detectMultiScale(gray_image, scaleFactor=scaleFactor, minNeighbors=5)
    
    for (x, y, w, h) in faces_rect:
        cv2.rectangle(image_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    return image_copy


#loading image
test_image = cv2.imread('data/baby1.png')

#call the function to detect faces
haar_cascade_face = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')
faces = detect_faces(haar_cascade_face, test_image)

#convert to RGB and display image
plt.imshow(convertToRGB(faces))
plt.show()
