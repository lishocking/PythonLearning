import pandas as pd
import pdb
import os
import mpl_finance as mpf
import matplotlib.pyplot as plt
import datetime
from datetime import date
import re
import threading
threadingmax=threading.BoundedSemaphore(300)
def plt_hist(filename,savefile=''):
    threadingmax.acquire()
    df=pd.read_csv(filename,index_col='dd',parse_dates=True)
    if len(df) < 100:
        return
    #pdb.set_trace()
    m=re.compile("5\d\d\d\d\d")
    if m.search(df['code'][0]):
        return
    #mpf.candlestick2_ochl(pd[1],pd[2],pd[3],pd[4],pd[5])
    #fig,ax=plt.subplots()
    #mpf.candlestick2_ochl(ax,df['o'],df['c'],df['h'],df['l'])
    #arr=plt.hist(df['r'],bins=20)
    #plt.hist(df['r'],bins=30,range=(-10,10))
    #pdb.set_trace()
    #for i in range(0,len(df['dd'])):
    #    y,m,d=df['dd'][i].split('-')
    #    df.loc['dd',i]=date(int(y),int(m),int(d))
    #    if i % 100 == 0:print(i)
    #index=pd.to_datetime(df['dd'])

    #pdb.set_trace()
    #df.replace(['dd'],index)
    #df.set_index(['dd'])
    #pdb.set_trace()
    try:
        plt.figure(figsize=(20,15))
        plt.subplot(2,2,1)
        down_arr=plt.hist(df['r'],bins=20,range=(-10,0),color='g')
        up_arr=plt.hist(df['r'],bins=20,range=(0,10),color='r')
        pdown=sum(down_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
        pup=sum(up_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
        plt.text(-10,max(down_arr[0]),"down"+str(pdown))
        plt.text(7,max(down_arr[0]),"up"+str(pup))
        #pdb.set_trace()
        plt.text(-10,max(down_arr[0])/2,""+df['code'][1]+'all')

        plt.subplot(2,2,2)
        end=date.today()
        st=end-datetime.timedelta(365)
        df1=df[st:end]

        down_arr=plt.hist(df1['r'],bins=20,range=(-10,0),color='g')
        up_arr=plt.hist(df1['r'],bins=20,range=(0,10),color='r')
        pdown=sum(down_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
        pup=sum(up_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
        plt.text(-10,max(down_arr[0]),"down"+str(pdown))
        plt.text(7,max(down_arr[0]),"up"+str(pup))
        #pdb.set_trace()
        plt.text(-10,max(down_arr[0])/2,""+df1['code'][1]+'last_year')

        plt.subplot(2,2,3)
        end=date.today()
        st=end-datetime.timedelta(90)
        df1=df[st:end]
        down_arr=plt.hist(df1['r'],bins=20,range=(-10,0),color='g')
        up_arr=plt.hist(df1['r'],bins=20,range=(0,10),color='r')
        pdown=sum(down_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
        pup=sum(up_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
        plt.text(-10,max(down_arr[0]),"down"+str(pdown))
        plt.text(7,max(down_arr[0]),"up"+str(pup))
        #pdb.set_trace()
        plt.text(-10,max(down_arr[0])/2,""+df1['code'][1]+'last_3_month')
        
        plt.subplot(2,2,4)
        end=date.today()
        st=end-datetime.timedelta(30)
        df1=df[st:end]
        down_arr=plt.hist(df1['r'],bins=20,range=(-10,0),color='g')
        up_arr=plt.hist(df1['r'],bins=20,range=(0,10),color='r')
        pdown=sum(down_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
        pup=sum(up_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
        plt.text(-10,max(down_arr[0]),"down"+str(pdown))
        plt.text(7,max(down_arr[0]),"up"+str(pup))
        #pdb.set_trace()
        plt.text(-10,max(down_arr[0])/2,""+df1['code'][1]+'last_month')
        if savefile == '':
            plt.show()
        else:
            plt.savefig(savefile)
        plt.clf()
        plt.cla()
        plt.close()
        #pdb.set_trace()
    except Exception as e:
        #print(str(e.message))
        try:
            plt.clf()
            plt.cla()
            plt.close()
        except:
            pass
    threadingmax.release()
if __name__ == '__main__':
    fdir='''d:\stockdata'''
    picdir='''d:\stockfig\\'''
    # filename='''d:\stockdata\sz300024.day.csv'''
    os.chdir(fdir)
    #pdb.set_trace()
    count=0
    for i in os.listdir(): 
        count+=1
        #plt_hist(i)
        strpath=picdir+i.split('.')[0]+'.png'

        plt_hist(i,picdir+i.split('.')[0]+'.png')
        #t=threading.Thread(target=plt_hist,args=(i,strpath))
        
        #t.start()
        if count % 100 ==0 :print(count)

