#!python2.7
#encoding=utf-8
import numpy as np
import matplotlib as plt
import matplotlib.dates as dt
from CSVDataStructure import *
def FindPeak(c_ndarry):
        for i in range(len(c_ndarry)):
                if c_ndarry[i-1]>c_ndarry[i] < c_ndarry[i+1]:
                            #   print "low peak %f" % c_ndarry[i]
                elif c_ndarry[i-1]<c_ndarry[i] > c_ndarry[i+1]:
                            #    print "high peak %f" % c_ndarry[i]
#test
if __name__ == '__main__':
        import pdb
        import win32ui
 
#        dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
#        dlg.SetOFNInitialDir('c:/stockdata/') # 设置打开文件对话框中的初始显示目录
#        dlg.DoModal()
# 
#        str_filename = dlg.GetPathName() # 获取选择的文件名称
#       print filename
        str_filename="c:/stockdata/601169.ss.csv"
        temp=np.loadtxt(str_filename,dtype=np.str,delimiter=',')
        data=temp[1:,0:]
        stock_date=dt.datestr2num(data[0:,STOCKDATE])
        stock_code=data[0,STOCKCODE]
        stock_name=data[0,STOCKNAME]
        stock_tclose=data[0:,TCLOSE].astype(np.float)
        stock_high=data[0:,HIGH].astype(np.float)
        stock_low=data[0:,LOW].astype(np.float)
        stock_topen=data[0:,TOPEN].astype(np.float)
        stock_voturnover=data[0:,VOTURNOVER].astype(np.float)
        #stock_vaturnover=data[0:,VATURNOVER].astype(np.float)
        
        stock_diff=(stock_tclose-stock_topen)
        FindPeak(stock_tclose)
        #DrawHistogram(str_filename,1000)
        #str_filename="c:/stockdata/000100.sz.csv"
        #DrawHistogram(str_filename,1000)
#       str_filename="c:/stockdata/601169.ss.csv"
#        pdb.set_trace()
#!/usr/bin/env python

