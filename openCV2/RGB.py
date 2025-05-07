import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("openCV2\image/fak.png")
plt.imshow(img)

plt.waitforbuttonpress()
plt.close('all')