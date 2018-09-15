import numpy as np
import pdb
import matplotlib.pyplot as plt
import os
def statistic(item,step=15):
    bar_list={}
    for i in item:
        key=i[0][0]//step
        color=i[0][1]
        if key > 10:
            key=11
        if (key,color) not in bar_list:
            bar_list[(key,color)]=i[1]*i[0][0]
        else:
            bar_list[(key,color)]+=i[1]*i[0][0]
    return bar_list
            
        
def plot_bar(filename):
    f=open(filename,'r')
    count=0
    count_list={}
    for i in f.readlines():
        if('B' in i ) or ('S' in i):
            count=count+1
            s=i.split('\t')
            key=(int(s[2]),s[4]) 
            if key not in count_list:
                count_list[key]=1
            else:
                count_list[key]=count_list[key]+1
    
    item=list(count_list.items())
    item.sort()
    bar_list=statistic(item)
    item=list(bar_list.items())
    print(item)
    
    for i in item:
        left=i[0][0]
        height=i[1]
        width=0.4
        if i[0][1] == 'B':
            color='red'
        else:
            #height=-height
            left=left+0.4
            color='green'
        plt.bar(left,height,width,color=color)   

if __name__=='__main__':
    os.chdir('.\\000895') 
    #pdb.set_trace()
    file_list=os.listdir()
    for f in file_list:
        if f[-3:] == 'txt':
            plot_bar(f)
            plt.savefig(f[0:-4]+'.png')
            plt.clf()
            #plt.show()
            
