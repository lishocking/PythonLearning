#!python3.6
#encoding=utf8
import numpy as np
import pylab as pl
#from scipy import stats
from CSVDataStructure import *
from math import log

def calcShannonEntropy(str_filename):
        temp=np.loadtxt(str_filename,dtype=np.str,delimiter=',')
        #temp=np.loadtxt(open(str_filename,encoding='latin-1'),dtype=np.str,delimiter=',')
        data=temp[1:,0:]
        close_value=data[0:,TCLOSE].astype(np.float)
        print ( close_value)

def calcProbility(str_filename,split_days,split_count):
        temp=np.loadtxt(str_filename,dtype=np.str,delimiter=',')
        #temp=np.loadtxt(open(str_filename,encoding='latin-1'),dtype=np.str,delimiter=',')
        data=temp[1:,0:]
        close_value=data[0:,TCLOSE].astype(np.float)
        rate=(close_value[1:]/close_value[0:-1]-1)*100
        print(rate)
        step=20/split_count
        for i in range(0,len(rate)):
            for k in range(0,split_count-1):
                if(rate[i]<(-10+step*k)):
                    rate[i]=k
                    break
                elif(rate[i]>(-10+step*k) and  rate[i] < (-10+step*k+step)):
                    rate[i]=k
                    break
                if(rate[i]>10):
                    rate[i]=split_count
        rate=rate.astype(np.int)      
        rate=rate-10
        pdb.set_trace()
        print(rate)
        pl.plot(rate) 
        pl.show()
         
        

def splitDataSet(dataSet,axis,value):
    return
        

#test
if __name__ == '__main__':
        import pdb
        #str_filename="c:/stockdata/000001.ss.csv"
        #DrawHistogram(str_filename,1000)
        #str_filename="c:/stockdata/000100.sz.csv"
        #DrawHistogram(str_filename,1000)
        #pdb.set_trace()
        str_filename="d:/stockdata/000002.sz.csv"
        calcProbility(str_filename,5,30)
