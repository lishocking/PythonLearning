import numpy as np
import pandas
import matplotlib as plt
import matplotlib.dates as dt
import pdb
# MA(CLOSE,7)-MA(OPEN,7)>0 买入
# MA(CLOSE,7)-MA(OPEN,5)<0 卖出

def calma(price,step_ma):
    sum_price=np.zeros(len(price)-step_ma) 
    #pdb.set_trace()
    for i in range(0,step_ma):
        sum_price+=price[i:-step_ma+i];
    return np.insert(sum_price/step_ma,0,price[0:step_ma]);


a=[1,2,3,4,5,6,7,8]
a=np.array(a)
print(calma(a,4))
