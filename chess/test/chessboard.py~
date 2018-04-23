# -*- coding: utf-8 -*-
import cv2
import cv
import numpy as np
import matplotlib.pyplot as plt
img =  cv2.imread('d:/d.jpg')
#利用棋盘的横平坚直来统计直线，根据统计的值来估算棋盘的位置

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
print lap
#plt.figure()
#plt.imshow(lap,'gray')
#newimg=cv2.adaptiveThreshold(lap,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,2)
#plt.show()
#cv2.calcHist(gray, 0, None, 256, [0.0,255.0])   
ret,thresh1 = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
plt.imshow(thresh1,'gray')
plt.show()



