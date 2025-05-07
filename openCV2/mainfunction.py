import cv2
 
img = cv2.imread('openCV2/image 2/Screenshot_16.png')
cv2.imshow('original image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray image', gray)

blur = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
#cv2.imshow('Blur image', blur)

canny = cv2.Canny(img, 250, 260)
#cv2.imshow('Canny image', canny)

dilated = cv2.dilate(canny, (7,7), iterations=3)
#cv2.imshow('dilated image', dilated)

eroded = cv2.erode(dilated, (7,7), iterations=3)
#cv2.imshow('Eroded', eroded)

resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('resized image', resized)

cropped = img[50:200, 200:400]
cv2.imshow('cropped image', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()