import cv2

RGB_img = cv2.imread('Lenna.png')

G_img = cv2.cvtColor(RGB_img, cv2.COLOR_RGB2GRAY)

# Here we use thsholding method
th1, B_img = cv2.threshold(G_img, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite('Binary1_Lenna.png', B_img)
cv2.imshow('Binary1_lenna', B_img)
cv2.waitKey(5000)

th2, B_img = cv2.threshold(G_img, 127, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite('Binary2_Lenna.png', B_img)
cv2.imshow('Binary2_lenna', B_img)
cv2.waitKey(5000)

th3, B_img = cv2.threshold(G_img, 127, 255, cv2.THRESH_TRUNC)
cv2.imwrite('Binary3_Lenna.png', B_img)
cv2.imshow('Binary3_lenna', B_img)
cv2.waitKey(5000)

th4, B_img = cv2.threshold(G_img, 127, 255, cv2.THRESH_TOZERO)
cv2.imwrite('Binary4_Lenna.png', B_img)
cv2.imshow('Binary4_lenna', B_img)
cv2.waitKey(5000)

th5, B_img = cv2.threshold(G_img, 127, 255, cv2.THRESH_TOZERO_INV)
cv2.imwrite('Binary5_Lenna.png', B_img)
cv2.imshow('Binary5_lenna', B_img)
cv2.waitKey(5000)


cv2.destroyAllWindows()
