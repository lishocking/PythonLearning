#!python3.6
# -*- coding: utf-8 -*-
import struct
import pdb
import os
import csv
def exactStockByDay(fileName, code):
    ofile = open(fileName,'rb')
    buf=ofile.read()
    ofile.close()
    num=len(buf)
    no=num/32
    b=0
    e=32
    items = list() 
    for i in range(int(no)):
        a=struct.unpack('IIIIIfII',buf[b:e])
        year = int(a[0]/10000);
        m = int((a[0]%10000)/100);
        month = str(m);
        if m <10 :
            month = "0" + month;
        d = (a[0]%10000)%100;
        day=str(d);
        if d< 10 :
            day = "0" + str(d);
        dd = str(year)+"-"+month+"-"+day
        openPrice = a[1]/100.0
        high = a[2]/100.0
        low =  a[3]/100.0
        close = a[4]/100.0
        amount = a[5]/10.0
        vol = a[6]
        unused = a[7]
        if i == 0 :
            preClose = close
        ratio = round((close - preClose)/preClose*100, 2)
        preClose = close
        item=[code, dd, str(openPrice), str(high), str(low), str(close), str(ratio), str(amount), str(vol)]
        items.append(item)
        b=b+32
        e=e+32
        
    return items
def writeitems2csv(items,file_path):
    with open(file_path,'w') as csvfile:
        spamwriter=csv.writer(csvfile)
        for i in items:
            spamwriter.writerow(i)
        csvfile.flush()
        csvfile.close()
def tdx_lday_to_csv(source_dir_list,dest_dir):
    for dir_i in source_dir_list:
        for input_file in os.listdir(dir_i):
            code=input_file.split('.')[0]
            ouput_path=dest_dir+input_file+'.csv'
            items=exactStockByDay(dir_i+input_file,code)
            writeitems2csv(items,ouput_path)

if __name__ == '__main__':
    source_dir_list=['D:\\zd_cczq\\vipdoc\\sh\\lday\\','D:\\zd_cczq\\vipdoc\\sz\\lday\\']
    dest_dir='D:\\stockdata\\'
    tdx_lday_to_csv(source_dir_list,dest_dir)


