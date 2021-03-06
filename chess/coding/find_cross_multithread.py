#!python2.7
# -*- coding: utf-8 -*-
import cv2
import cv2
import cv 
import numpy as np
import matplotlib.pyplot as plt
import pdb
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

def FindLineH_Judge(line_list):
    line_h_p=[]
    l1=line_list[0]
#    pdb.set_trace()
    l2=line_list[1]
    i=line_list[2]
    min_length=line_list[3]
    width=line_list[4]
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
                line_h_p.append([(line_start,i),(line_end,i)])
            line_end=-1
            line_start=-1
    return line_h_p

def FindLineH(img_bin,min_length):
    
    height,width=img_bin.shape
    line_list=[]
    for i in range(1,height):
        line_list.append([img_bin[i-1,:],img_bin[i,:],i,min_length,width])
#        FindLineH_Judge([img_bin[i-1,:],img_bin[i,:],i,min_length,width])
    line_h=[]
    pool = ThreadPool(16)
    line_h=pool.map(FindLineH_Judge,line_list)
    pool.close()
    pool.join()
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
            if((pt3[0]+3>pt1[0])\
                   and (pt3[0]-3<pt2[0])\
                   and (pt1[1]+3>pt3[1])\
                   and (pt1[1]-3<pt4[1]) ):
                cross_point.append([pt3[0],pt1[1]])
    return cross_point


if __name__ == '__main__':
    img =  cv2.imread('d:/1.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #plt.imshow(lap,'gray')
    ret,img_bin = cv2.threshold(gray,100,1,cv2.THRESH_BINARY)
#    list=FindCrossLineP(img_bin)
    start=time.clock()
    list_1=FindLineH(img_bin,20)
    end=time.clock()
    print (list_1)
#    for i in list[:]:
#        cv2.circle(img,(i[0],i[1]),10,(255,0,0),5)
    print ("time:%f s" % (end-start))
    for i in  list_1[:]:
        if i!=[]:
            for k in i:
                cv2.line(img,k[0],k[1],255,2)
#    list_2=FindLineV(img_bin,20)
#    for i in  list_2:
#        cv2.line(img,i[0],i[1],(0,255,0),2)
#    list_p=FindCrossLineP1(img_bin)
#    for i in list_p:
#            cv2.circle(img,(i[0],i[1]),5,(255,0,0),5)
#    print list_p
    plt.imshow(img)
    plt.show()
