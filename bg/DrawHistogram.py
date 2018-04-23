#!python3.6
#encoding=utf8
import numpy as np
import pylab as pl
from scipy import stats
from CSVDataStructure import *

def DrawHistogram(str_filename,i_bins):
        temp=np.loadtxt(str_filename,dtype=np.str,delimiter=',')
        #temp=np.loadtxt(open(str_filename,encoding='latin-1'),dtype=np.str,delimiter=',')
        data=temp[1:,0:]
        close_value=data[0:,TCLOSE].astype(np.float)
        print ( close_value)
        log_temp=np.log(close_value[1:]/close_value[:-1])
        loc_1,scale_1=stats.norm.fit(log_temp)
        p,t=np.histogram(log_temp,bins=i_bins)
        t=(t[:-1]+t[1:])/2
        pl.plot(t,p)
        pl.plot(t,stats.norm.pdf(t,loc=loc_1,scale=scale_1))
        pl.show()



#test
if __name__ == '__main__':
        import pdb
        #str_filename="c:/stockdata/000001.ss.csv"
        #DrawHistogram(str_filename,1000)
        #str_filename="c:/stockdata/000100.sz.csv"
        #DrawHistogram(str_filename,1000)
        #pdb.set_trace()
        str_filename="d:/stockdata/000001.sz.csv"
        DrawHistogram(str_filename,1000)

