#--encoding
import cv2
import cv 
import numpy as np
import matplotlib.pyplot as plt
import pdb
img = cv2.imread('d:/3.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))


plt.subplot(121)
plt.imshow(gray,'gray')
plt.xticks([]),plt.yticks([])

circles1 = cv2.HoughCircles(lap,cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=20,maxRadius=30)
circles = circles1[0,:,:]
circles = np.uint16(np.around(circles))
#for i in circles[:]: 
#    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),5)
#    cv2.circle(img,(i[0],i[1]),2,(255,0,255),10)
#plt.subplot(122),plt.imshow(img)
#plt.xticks([]),plt.yticks([])
#plt.show()
