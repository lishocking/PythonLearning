import pandas as pd
import pdb
import os
import mpl_finance as mpf
import matplotlib.pyplot as plt
def plt_hist(filename,savefile=''):
    df=pd.read_csv(filename)
    if len(df) < 100:
        return
    #mpf.candlestick2_ochl(pd[1],pd[2],pd[3],pd[4],pd[5])
    #fig,ax=plt.subplots()
    #mpf.candlestick2_ochl(ax,df['o'],df['c'],df['h'],df['l'])
    #arr=plt.hist(df['r'],bins=20)
    #plt.hist(df['r'],bins=30,range=(-10,10))
    down_arr=plt.hist(df['r'],bins=20,range=(-10,0),color='g')
    up_arr=plt.hist(df['r'],bins=20,range=(0,10),color='r')
    pdown=sum(down_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
    pup=sum(up_arr[0])/(sum(down_arr[0])+sum(up_arr[0]))*100
    plt.text(-10,max(down_arr[0]),"down"+str(pdown))
    plt.text(7,max(down_arr[0]),"up"+str(pup))
    #pdb.set_trace()
    plt.text(-10,max(down_arr[0])/2,""+df['code'][1])
    if savefile == '':
        plt.show()
    else:
        plt.savefig(savefile)
    #pdb.set_trace()

if __name__ == '__main__':
    fdir='''d:\stockdata'''
    picdir='''d:\stockfig\\'''
    # filename='''d:\stockdata\sz300024.day.csv'''
    os.chdir(fdir)
    #pdb.set_trace()
    for i in os.listdir(): 
        plt_hist(i,picdir+i.split('.')[0]+'.png')


