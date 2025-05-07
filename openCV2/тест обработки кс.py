import cv2
import numpy as np
import os

class detected():
    def build_pyramid(image, scale=1.5, min_size=30):
        """making pyramid image"""
        pyramid = [image]
        while True:
            """берет последние изображение из масива,
            получает размер изображения по второй оси
            делит на scale"""
            w = int(pyramid[-1].shape[1] / scale)
            h = int(pyramid[-1].shape[0] / scale)
            if w < min_size or h < min_size:
                break
            resized = cv2.resize(pyramid[-1], (w, h))
            pyramid.append(resized)
        return pyramid
    
    def non_max_supression(boxes, scores, threshold=0.3):
        if len(boxes) == 0:
            return
        
        x1 = boxes[:, 0]
        y1 = boxes[:, 1]
        x2 = boxes[:, 2]
        y2 = boxes[:, 3]
        
        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        indices = np.argsort(scores)[::-1]
        
        keep = []
        while len(indices) > 0:
            i = indices[0]
            keep.append(i)
            
            xx1 = np.maximum(x1[i], x1[indices[1:]])
            yy1 = np.maximum(y1[i], y1[indices[1:]])
            xx2 = np.minimum(x2[i], x2[indices[1:]])
            yy2 = np.minimum(y2[i], y2[indices[1:]])
            
            w = np.maximum(0, xx2 - xx1 + 1)
            h = np.maximum(0, yy2 - yy1 + 1)