#!python2.7
#*=*encoding: utf-8*=*
from CSVDataStructure import *
#STOCKDATE,STOCKCODE,STOCKNAME,TCLOSE,HIGH,LOW,TOPEN,VOTURNOVER,VATURNOVER= \
#               range(0,9) 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime
from scipy import stats
from matplotlib.dates import AutoDateLocator, DateFormatter ,YearLocator, MonthLocator
import matplotlib.dates as dt

def DrawCandelStickChart(str_filename):
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
        years = YearLocator()   # every year
        months = MonthLocator()  # every month
        yearsFmt = DateFormatter('%Y')
        fig, ax = plt.subplots()
        last_color='b'
        for date,topen,tclose,high,low in zip(stock_date,stock_topen,stock_tclose,stock_high,stock_low):
                if (tclose-topen) > 0:
                        ax.bar(left=date-0.3,width=0.6,bottom=topen,height=tclose-topen,edgecolor='r',fill=False)
                        ax.vlines(date,tclose,high,color='r')
                        ax.vlines(date,low,topen,color='r')
                elif (tclose-topen)<0:
                        ax.bar(left=date-0.3,width=0.6,bottom=tclose,height=topen-tclose,edgecolor='g',color='g',fill=True)
                        ax.vlines(date,tclose,low,color='g')
                        ax.vlines(date,high,topen,color='g')
                else:
                        ax.bar(left=date-0.3,width=0.6,bottom=tclose,height=topen-tclose,edgecolor=last_color,color=last_color,fill=True)
                        ax.vlines(date,tclose,low,color=last_color)
                        ax.vlines(date,high,topen,color=last_color)

        ax.grid()
        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(yearsFmt)
        ax.xaxis.set_minor_locator(months)
        ax.autoscale_view()
        def price(x):
                return '$%1.2f' % x
        ax.fmt_xdata = DateFormatter('%Y-%m-%d')
        ax.fmt_ydata = price
        ax.grid(True)
        
        fig.autofmt_xdate()
#        autodates = AutoDateLocator()  
#        yearsFmt = DateFormatter('%Y-%m-%d')  
#        figure.autofmt_xdate()        #设置x轴时间外观  
#        ax.xaxis.set_major_locator(autodates)       #设置时间间隔  
#        ax.xaxis.set_major_formatter(yearsFmt)      #设置时间显示格式  
#        ax.set_xticks() #设置x轴间隔  
#        ax.set_xlim(
#        plt.plot_date(stock_date,stock_tclose)
        plt.show()
        
if __name__ == '__main__':
        import pdb
        #DrawHistogram(str_filename,1000)
        #str_filename="c:/stockdata/000100.sz.csv"
        #DrawHistogram(str_filename,1000)
        #pdb.set_trace()
        str_filename="c:/stockdata/600004.ss.csv"
        #str_filename="c:/stockdata/000001.ss.csv"
        DrawCandelStickChart(str_filename)

