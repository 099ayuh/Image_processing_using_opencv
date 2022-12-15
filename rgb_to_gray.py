import cv2 as cv


img = cv.imread('image2.jpg')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('tera photo', gray)

cv.waitKey(0)