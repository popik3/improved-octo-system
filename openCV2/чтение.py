import cv2

img = cv2.imread("openCV2/fak.png", cv2.IMREAD_COLOR)

cv2.imshow("image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

n = img.shape
print(n)