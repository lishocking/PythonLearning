import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('D:/1.png') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,200)
plt.subplot(121),plt.imshow(edges,'gray')
plt.xticks([]),plt.yticks([])
lines = cv2.HoughLinesP(edges,5,np.pi/360,30,minLineLength=0,maxLineGap=10)
lines1 = lines[:,0,:]
for x1,y1,x2,y2 in lines1[:]: 
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)

plt.subplot(122),plt.imshow(img,)
plt.xticks([]),plt.yticks([])
plt.show()
