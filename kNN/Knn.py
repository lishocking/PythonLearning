#!python3.6
#encoding=utf-8
import csv
import numpy as np
import matplotlib.dates as dt
import matplotlib.pyplot as plt
import pylab as pl
import pdb
VECTORLENGTH=10
STOCKDATE,TOPEN,HIGH,LOW,TCLOSE,VOTURNOVER,ADJCLOSE= \
               list(range(0,7)) 
STOCKCODE=0
STOCKNAME=0
VATURNOVER=VOTURNOVER
#python区分大小写，把这个设置成一个长度来计算KNN的距离,认为如果股票5天内的涨幅相似的话，第6天也是一样的涨幅。
def knn_onestock(str_filename):
    #temp=np.loadtxt(str_filename,dtype=np.str,delimiter=',')
    temp=np.genfromtxt(str_filename,delimiter=',')
    data=temp[1:,0:]
    #stock_date=dt.datestr2num(data[0:,STOCKDATE])
    #stock_code=data[0,STOCKCODE]
    #stock_name=data[0,STOCKNAME]
    #stock_tclose=data[0:,TCLOSE].astype(np.float)
    #stock_high=data[0:,HIGH].astype(np.float)
    #stock_low=data[0:,LOW].astype(np.float)
    #stock_topen=data[0:,TOPEN].astype(np.float)
    #stock_voturnover=data[0:,VOTURNOVER].astype(np.float)
    print(data[0:,ADJCLOSE])
    stock_adjclose=data[0:,ADJCLOSE].astype(np.float)
    stock_xdate=stock_adjclose[0:-1]
    stock_x1date=stock_adjclose[1:]
    stock_rate=stock_x1date/stock_xdate
    tmp=stock_rate[0:VECTORLENGTH]
    datasize=len(stock_rate)-VECTORLENGTH
    for i in range(1,len(stock_rate)-VECTORLENGTH):
        tmp=np.vstack((tmp,stock_rate[i:i+VECTORLENGTH]))
    #tmp是2维的了
    #扩展成3维.
    d_tmp=np.tile(tmp,(datasize,1,1))
    #0 维和1维转置.
    # x1=[1,2]
    # x2=[2,3]
    # a=[x1,x2]
    # b=[x1,x2]
    #   [x1,x2]
    # d_tmp.transpose(1,0,2)相当于b.tanspose
    # b.transpose=[x1,x1]
    #             [x2,x2]
    d_tran=d_tmp.transpose(1,0,2)
    error=d_tran-d_tmp
    sqError=error**2
    sqDistances=sqError.sum(axis=2)
    distance=sqDistances**0.5
    distance=distance+np.eye(distance.shape[0])
    bool_table=np.logical_and(distance>0.01,distance<0.015)
    rst_list=[]
    #print np.sort(distance)
    for i  in range(0,bool_table.shape[0]-2):
        for j in range(i,bool_table.shape[0]-2):
            if bool_table[i][j]==True:
                print(i,j)
                pl.clf()
                pl.plot(stock_rate[i:i+VECTORLENGTH+2])
                pl.plot(stock_rate[j:j+VECTORLENGTH+2])
                pl.title("i=%i,j=%i"%(i,j))
                pl.savefig("%i_%i"%(i,j))
    print(rst_list)            

    
    
if  __name__ == '__main__':
    str_filename="c:/stockdata/000001.ss.csv"
    knn_onestock(str_filename)
