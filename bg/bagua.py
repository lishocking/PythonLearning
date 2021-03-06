#!python3.6
#encoding=utf8
import pdb
import numpy as np
import pylab as pl
from scipy import stats
from CSVDataStructure import *

def DrawHistogram(str_filename,i_bins):
        temp=np.loadtxt(str_filename,dtype=np.str,delimiter=',')
        #temp=np.loadtxt(open(str_filename,encoding='latin-1'),dtype=np.str,delimiter=',')
        data=temp[1:,0:]
        close_value=data[0:,TCLOSE].astype(np.float)
        for i in range(1,len(close_value-8)):
            temp=(close_value[i+1:i+7]/close_value[i:i+6] -1)*100
            print(temp)
            #print(close_value[i+8:i+14]/close_value[i+7:i+13]-1)
            if i > 1000:
                pdb.set_trace()
                pl.plot(close_value[i:i+14])
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


