import cv2
import numpy as np

img = cv2.imread('openCV2/image 2/Screenshot_16.png')
cv2.imshow('image', img)

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('blank', blank)

blur = cv2.GaussianBlur(img, (5,5), cv2.BORDER_DEFAULT)

canny = cv2.Canny(blur, 125, 175)
#cv2.imshow('image', canny)

ret, thresh = cv2.threshold(canny, 125,cv2.THRESH_BINARY)
#cv2.imshow('Thresh', thresh)
contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, 
cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)}')

cv2.drawContours(blank,contours,-1,(0,0,255),1)
cv2.imshow('blank', blank)

cv2.waitKey(0)
cv2.destroyAllWindows()