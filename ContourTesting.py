import numpy as np
import cv2

#Testing Contour Boundary boxes with a still image

img = cv2.imread('BlueGrid.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray,127,255,1)

im2,contours,h = cv2.findContours(thresh,1,2)

cv2.drawContours(img, contours, -1, (0,0,255), 2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
