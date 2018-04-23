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
import find_cross as fc
def FussyVote(list_v,step=5):
    list_v.sort()
    for i in range(0,len(list_v)):
        list_v[i]=list(list_v[i])
    for i in range(0,len(list_v)-step):
        if list_v[i+1][0]-list_v[i][0]>step:
            continue
        else:
           tmp=[]
           leng=0
           for k in range(1,step+1):
               if(list_v[i+k][0]-list_v[i][0] > step ):
                   leng=k
                   break
           weight_sum = 0
           max_index = 0
           max_value = list_v[i][1]
           for k in range(0,leng):
               weight_sum=weight_sum+list_v[i+k][1]
               if max_value < list_v[i+k][1]:
                   max_value = list_v[i+k][1]
                   max_index = i+k
           list_v[max_index][1]=weight_sum
    return list_v


def VoteByDistance(chosen_arr):
    #不满足要求，去掉2个最小值，3个最大值取平均（计算最有可能的值，然后从每个点开始投票，每个点加平均值，计算最近的点，
    line_count=len(chosen_arr)
    tmp_dis=chosen_arr[1:line_count]-chosen_arr[0:line_count-1]
    tmp_dis_l=tmp_dis.tolist()
    tmp_dis_l.remove(max (tmp_dis_l))
    tmp_dis_l.remove(max (tmp_dis_l))
    tmp_dis_l.remove(max (tmp_dis_l))
    tmp_dis_l.remove(max (tmp_dis_l))
    
    tmp_dis_l.remove(min (tmp_dis_l))
    tmp_dis_l.remove(min (tmp_dis_l))
    tmp_dis_l.remove(min (tmp_dis_l))

    average_dis=np.average(tmp_dis_l)
    weight=np.zeros(chosen_arr.shape) 

    for i in range(0,line_count):
        for k in range(0,line_count):
           vote_pt=chosen_arr[i]+(k-i)*average_dis
           abs_dis=np.abs(chosen_arr-vote_pt)
           min_abs=min(abs_dis)
           for j in range(0,line_count):
               if min_abs==abs_dis[j]:
                  weight[j]=weight[j]+1/(0.1+min_abs)
                  break
               
               
    #print "weight"       
    #print weight


    return weight
def FindMostLikelyLines(list_v,line_count=9,error=5):
    #因为圆心不一定在交叉点上（精度问题）所以把圆心的投票记到最大点上
    list_sorted_weight=sorted(list_v,key=lambda list_v:list_v[1],reverse=True)
    arr=np.array(list_sorted_weight)
    print arr.shape
    chosen_arr=np.copy(arr[0:line_count,0])
    chosen_arr=np.sort(chosen_arr)
    for i in range(0,10):
        tmp_dis=chosen_arr[1:line_count]-chosen_arr[0:line_count-1]
        print tmp_dis
        tmp_error=np.abs(tmp_dis-np.average(tmp_dis))
        print tmp_error
        if (tmp_error< error).all():
            return chosen_arr
        else:       
            weight=VoteByDistance(chosen_arr)
            for k in range(0,line_count):
                if weight[k]==min(weight):
                    chosen_arr[k]=arr[line_count+i,0]
                    chosen_arr=np.sort(chosen_arr)
                    break
            print "chosen"
            print chosen_arr
    
            

    return  chosen_arr
    
    
def Vote_Chessboard(list_p,list_c):
    vote_list_line_v=dict()
    vote_list_line_h=dict()
    for i in list_p:
        if vote_list_line_v.has_key(i[0]):
            vote_list_line_v[i[0]]=vote_list_line_v[i[0]]+2
        else:
            vote_list_line_v[i[0]]=2

        if vote_list_line_h.has_key(i[1]):
            vote_list_line_h[i[1]]=vote_list_line_h[i[1]]+2
        else:
            vote_list_line_h[i[1]]=2

    for i in list_c:
        if vote_list_line_v.has_key(i[0]):
            vote_list_line_v[i[0]]=vote_list_line_v[i[0]]+2
        else:
            vote_list_line_v[i[0]]=3

        if vote_list_line_h.has_key(i[1]):
            vote_list_line_h[i[1]]=vote_list_line_h[i[1]]+2
        else:
            vote_list_line_h[i[1]]=3
            
    l_h=vote_list_line_h.items()
    l_v=vote_list_line_v.items()
    l_h=FussyVote(l_h)
    arr_h=FindMostLikelyLines(l_h,10)
    l_v=FussyVote(l_v)
    arr_v=FindMostLikelyLines(l_v,9)
    

    return  arr_h,arr_v

if __name__ == '__main__':
    img =  cv2.imread('d:/5.bmp')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #plt.imshow(lap,'gray')
    ret,img_bin = cv2.threshold(gray,100,1,cv2.THRESH_BINARY)
    plt.subplot(121)
    plt.imshow(img_bin,'gray')
#    list=FindCrossLineP(img_bin)
#    list_1=FindLineH(img_bin,20)
#    for i in list[:]:
#        cv2.circle(img,(i[0],i[1]),10,(255,0,0),5)
#    for i in  list_1:
#        cv2.line(img,i[0],i[1],255,2)
#    list_2=FindLineV(img_bin,20)
#    for i in  list_2:
#        cv2.line(img,i[0],i[1],(0,255,0),2)
    radio = 20
    circles =[]
    lap = cv2.Laplacian(gray, cv2.CV_64F)
    lap = np.uint8(np.absolute(lap))
    circles1 = cv2.HoughCircles(gray,cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=20,maxRadius=50)
    #pdb.set_trace()
    if circles1 is not None:
        circles = circles1[0,:,:]
        circles = np.uint16(np.around(circles))
        radio=np.average(circles[:,2])
        radio=int(radio)
        circles1 = cv2.HoughCircles(gray,cv.CV_HOUGH_GRADIENT,1,10,param1=100,param2=30,minRadius=radio-10,maxRadius=radio+10)
        if circles1 is not None:
               circles = circles1[0,:,:]
               circles = np.uint16(np.around(circles))
               radio=np.average(circles[:,2])
               radio=int(radio)
           


    list_p=fc.FindCrossLineP1(img_bin,r=radio/2)

    arr_h,arr_v=Vote_Chessboard(list_p,circles)

    for i in list_p:
        cv2.circle(img,(i[0],i[1]),5,(255,0,0),5)
    for i in circles:
        cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),5)    
    
  #  for i in arr_v:
  #      cv2.line(img,(i[0],0),(i[0],i[1]),(0,0,255),3)
  #  for i in arr_h:
  #      cv2.line(img,(0,i[0]),(i[1],i[0]),(0,0,255),3)
    for i in arr_v:    
        cv2.line(img,(i,arr_h[0]),(i,arr_h[9]),(0,0,255),3)
    for i in arr_h:    
        cv2.line(img,(arr_v[0],i),(arr_v[8],i),(0,0,255),3)
    #print list_p
    plt.subplot(122)
    plt.imshow(img)
    plt.show()
