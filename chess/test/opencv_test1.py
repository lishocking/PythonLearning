# -*- coding: utf-8 -*-


import cv2

img=cv2.imread('d:/1.png',cv2.IMREAD_GRAYSCALE)# �����ɫͼƬ

cv2.imshow('image',img)#����image������ʾͼƬ

k=cv2.waitKey(0)#�����ڵȴ�����

if k==27:#�������ESC�˳�

    cv2.destroyAllWindows()

   

elif k==ord('s'):

    cv2.imwrite('test.png',img)

    print "OK!"

    cv2.destroyAllWindows()
