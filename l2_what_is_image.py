import numpy as np
import matplotlib.pyplot as plt
import cv2

# Display pixel value when mouse moves over pixel
class Formatter(object):
    def __init__(self, im):
        self.im = im
    def __call__(self, x, y):
        z = self.im.get_array()[int(y), int(x)]
        #return 'x={:.01f}, y={:.01f}, z={:.01f}'.format(x, y, z)
        return 'x={:.0f}, y={:.0f}'.format(x, y)

img = cv2.imread('notre_dame_fire.jpg') # Read image into a numpy array
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # convert from BGR to RGB
data = img[1080:1100,1500:1520,:] # Take 20x20 pixels from image
print('shape={}'.format(data.shape)) # print array shape to console
print(data) # print array values to console

# Plot using matplotlib
fig, ax = plt.subplots()
im = ax.imshow(data, interpolation='none')
ax.format_coord = Formatter(im)
plt.show()

print("Now change line 16 to see other parts of the image")