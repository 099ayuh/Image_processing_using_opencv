import cv2 as c
import numpy as np
import matplotlib.pyplot as plt

img = c.imread('low_contrast.jpg', 0)
c.imshow('low', img)

h, w = img.shape

Lmax = 255
Lmin = 0

Mmax = np.max(img)
Mmin = np.min(img)

# Histogram before Streching
histogram = c.calcHist([img], [0], None, [256], [0, 255])
plt.plot(histogram)
plt.show()


def evaluatePixel(pixel):
    global Lmax, Lmin, Mmax, Mmin
    out_pixel = (((Lmax - Lmin) * (pixel - Mmin))/(Mmax - Mmin)) + Lmin
    return out_pixel

for i in range(h):
    for j in range(w):
        img[i][j] = evaluatePixel(img[i][j])

c.imshow('Streched', img)

# Histogram after Streching
histogram = c.calcHist([img], [0], None, [256], [0, 255])
plt.plot(histogram)
plt.show()

c.waitKey(0)


