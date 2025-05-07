import cv2

path = r'openCV2\image\geeks14.png'

image = cv2.imread(path, 0)

window_name = 'image'

cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()