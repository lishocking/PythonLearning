# -*- coding: utf-8 -*-
import cv2
import cv 
import numpy as np
import matplotlib.pyplot as plt
import pdb
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
def FindCrossLineP(img_bin,r=40/2):

    
    block=np.ones((r,r),dtype=np.int8)
    block_c1=np.copy(block)
    block_c1[0,:]=0
    block_c1[:,0]=0

    block_c2=np.copy(block)
    block_c2[0,:]=0
    block_c2[:,r-1]=0


    block_c3=np.copy(block)
    block_c3[r-1,:]=0
    block_c3[:,r-1]=0

    block_c4=np.copy(block)
    block_c4[r-1,:]=0
    block_c4[:,0]=0

    block_c1x=np.copy(block_c1)
    block_c2x=np.copy(block_c2)
    block_c3x=np.copy(block_c3)
    block_c4x=np.copy(block_c4)
    start =  time.clock() 
    for i in range(0,r):
        block_c1x[i,i]=0
        block_c3x[i,i]=0
        block_c2x[r-i-1,i]=0
        block_c4x[i,r-i-1]=0
    height,width=img_bin.shape
    save_list=[]
    for i in range(0,width-r):
        for k in range(0,height-r):
            tmp=img_bin[i:i+r,k:k+r]
            if ((tmp[0][0]!=0 ) and (tmp[0,r-1]!=0) and (tmp[r-1,r-1]!=0) and (tmp[r-1,0]!=0)):
                continue
            if (tmp == block_c1).all():
                save_list.append([i,k,'c1'])
                continue
            if (tmp == block_c2).all():
                save_list.append([i,k,'c2'])
                continue
            if (tmp == block_c3).all():
                save_list.append([i,k,'c3'])
                continue
            if (tmp == block_c4).all():
                save_list.append([i,k,'c3'])
                continue
            if (tmp == block_c1x).all():
                save_list.append([i,k,'c1x'])
                continue
            if (tmp == block_c1x).all():
                save_list.append([i,k,'c2x'])
                continue
            if (tmp == block_c1x).all():
                save_list.append([i,k,'c3x'])
                continue
            if (tmp == block_c1x).all():
                save_list.append([i,k,'c4x'])
                continue
            if (tmp == block_c1x).all():
                save_list.append([i,k,'c1x'])
                continue

    end = time.clock()
    print "time:%f s" % (end-start)
#    print save_list
#    plt.subplot(221)
#    plt.imshow(block_c1x,'gray')
#
#    plt.subplot(222)
#    plt.imshow(block_c2x,'gray')
#
#    plt.subplot(223)
#    plt.imshow(block_c3x,'gray')
#
#    plt.subplot(224)
#    plt.imshow(block_c4x,'gray')
#
#    plt.show()
    cross_point=0
    return save_list

def FindLineH(img_bin,min_length):
    line_h=[]
    height,width=img_bin.shape
    for i in range(1,height):
        l1=img_bin[i-1,:]
        l2=img_bin[i,:]
        line_start=-1
        line_end=-1
        for k in range(0,width):
            if ( (l2[k]==0) and (l1 [k] == 1)):
                if(line_start == -1):
                    line_start=k
                else:
                    line_end=k
            else:
                if (line_end-line_start > min_length):
                    line_h.append([(line_start,i),(line_end,i)])
                line_end=-1
                line_start=-1
    return line_h
def FindLineV(img_bin,min_length):
    line_v=[]
    height,width=img_bin.shape
    for i in range(1,width):
        l1=img_bin[:,i-1]
        l2=img_bin[:,i]
        line_start=-1
        line_end=-1
        for k in range(0,height):
            if ( (l2[k]==0) and (l1 [k] == 1)):
                if(line_start == -1):
                    line_start=k
                else:
                    line_end=k
            else:
                if (line_end-line_start > min_length):
                    line_v.append([(i,line_start),(i,line_end)])
                line_end=-1
                line_start=-1

    return line_v
def FindCrossLineP1(img_bin,r=40/2):
    line_h=FindLineH(img_bin,r)
    line_v=FindLineV(img_bin,r)
    cross_point=[]
    for lh in line_h:
        pt1=lh[0]
        pt2=lh[1]
        for lv in line_v:
            pt3=lv[0]
            pt4=lv[1]
            if((pt3[0]+5>pt1[0])\
                   and (pt3[0]-5<pt2[0])\
                   and (pt1[1]+5>pt3[1])\
                   and (pt1[1]-5<pt4[1]) ):
                cross_point.append([pt3[0],pt1[1]])
    return cross_point


if __name__ == '__main__':
    img =  cv2.imread('d:/1.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #plt.imshow(lap,'gray')
    ret,img_bin = cv2.threshold(gray,100,1,cv2.THRESH_BINARY)
#    list=FindCrossLineP(img_bin)
#    list_1=FindLineH(img_bin,20)
#    for i in list[:]:
#        cv2.circle(img,(i[0],i[1]),10,(255,0,0),5)
#    for i in  list_1:
#        cv2.line(img,i[0],i[1],255,2)
#    list_2=FindLineV(img_bin,20)
#    for i in  list_2:
#        cv2.line(img,i[0],i[1],(0,255,0),2)
    start=time.clock()
    list_p=FindCrossLineP1(img_bin)
    end=time.clock()
    print "time:%f s" % (end-start)
    for i in list_p:
            cv2.circle(img,(i[0],i[1]),5,(255,0,0),5)
    print list_p
    plt.imshow(img)
    plt.show()
