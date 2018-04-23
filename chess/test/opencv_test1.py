# -*- coding: utf-8 -*-


import cv2

img=cv2.imread('d:/1.png',cv2.IMREAD_GRAYSCALE)# 读入彩色图片

cv2.imshow('image',img)#建立image窗口显示图片

k=cv2.waitKey(0)#无限期等待输入

if k==27:#如果输入ESC退出

    cv2.destroyAllWindows()

   

elif k==ord('s'):

    cv2.imwrite('test.png',img)

    print "OK!"

    cv2.destroyAllWindows()
