import cv2
import numpy as np
import matplotlib.pyplot as plt
   
# Read an image
image = cv2.imread('low_contrast.jpg', 0)
   
# Apply log transformation method
c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))
   
# Specify the data type so that
# float value will be converted to int
log_image = np.array(log_image, dtype = np.uint8)
   
# Display both images
cv2.imshow('first',image)

histogram = cv2.calcHist([image], [0], None, [256], [0, 255])
plt.plot(histogram)
plt.show()

# plt.show()
cv2.imshow('second',log_image)

histogram = cv2.calcHist([image], [0], None, [256], [0, 255])
plt.plot(histogram)
plt.show()
# plt.show()

cv2.waitKey(0)