#!python2.7
#encoding=utf-8
import csv
import os
from datetime import date
from datetime import timedelta
from urllib import urlopen
import re
str_dir="d:\\stockdata\\"

def DownLoad(str_stockurl): 
        l_data=urlopen(str_stockurl)
        print l_data
        return l_data


def AddNewData(str_filename):
        url_code=TranslateToURL163(str_filename)
        #url_code=TranslateToURLYahoo(str_filename)
        print url_code
        data=DownLoad(url_code)
        if (len(data) <3):
            return
        h_file=file(str_filename,'wb+')
        h_file.writelines(data.readlines())
        h_file.close()
        data.close()
        

def IsLatest(str_filename):
        h_file=file(str_filename,'rb')
        csvreader=csv.reader(h_file,delimiter=',')
        #CSV的第一行是表头
        csvreader.next()
        #CSV的第二行是时间信息
        s_olddate=csvreader.next()[0]
        h_file.close()
        c_today=date.today()
        #把字符串日期换成数字格式 
        l_olddate=[int(x) for x in s_olddate.split('-')]
        #
        c_olddate=date(l_olddate[0],l_olddate[1],l_olddate[2])
        if ((c_today-c_olddate) > timedelta(1)):
                return (False,c_olddate)
        else :
                return (True,c_olddate)
def TranslateToURLYahoo(str_filename,c_lastdate=date(1991,1,1)):
        url="http://table.finance.yahoo.com/table.csv?s=%s.%s&a=%i&b=%i&c=%i"
        str_fn = os.path.basename(str_filename)
        str_stocknum,str_stockcode,str_fileext=str_fn.split('.') 
        i_year,i_month,i_day=c_lastdate.timetuple()[0:3]
        i_month = i_month-1
        i_day = i_day+1
#http://ichart.yahoo.com/table.csv?s=<string>&a=<int>&b=<int>&c=<int>&d=<int>&e=<int>&f=<int>&g=d&ignore=.csv
#参数
#s – 股票名称
#a – 起始时间，月
#b – 起始时间，日
#c – 起始时间，年
#d – 结束时间，月
#e – 结束时间，日
#f – 结束时间，年
#g – 时间周期。Example: g=w, 表示周期是’周’。d->’日’(day), w->’周’(week)，m->’月’(mouth)，v->’dividends only’
#一定注意月份参数，其值比真实数据-1。如需要9月数据，则写为08。
        return url % (str_stocknum,str_stockcode,i_month,i_day,i_year)
def TranslateToURL163(str_filename,c_lastdate=date(1991,1,1)):
#        url="http://quotes.money.163.com/service/chddata.html?code=000001&start=19901219&end=20160120&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;VOTURNOVER;VATURNOVER"
        url="http://quotes.money.163.com/service/chddata.html?code=0%s&start=%4i%02i%02i&fields=TCLOSE;HIGH;LOW;TOPEN;VOTURNOVER;VATURNOVER"
        str_fn = os.path.basename(str_filename)
        str_stocknum,str_stockcode,str_fileext=str_fn.split('.') 
        i_year,i_month,i_day=c_lastdate.timetuple()[0:3]
        i_month = i_month
        i_day = i_day+1
        print(url)
        return url % (str_stocknum,i_year,i_month,i_day)



def UpdateData(str_filename,c_lastdate):
        #str_filename必须以股票数据开头
        str_stockurl=TranslateToURL163(str_filename,c_lastdate)
        #str_stockurl=TranslateToURLYahoo(str_filename,c_lastdate)
        stockdata=DownLoad(str_stockurl)
        h_file=file(str_filename,'r')
        h_file.readline()
        old_data= h_file.readlines()
        h_file.close()
        h_file=file(str_filename,'w')
        h_file.writelines(stockdata.readlines())
        h_file.writelines(old_data)
        h_file.close()
        stockdata.close()
        
def UpdateList(str_filename_list):
        h_file=file(str_filename_list,'r') 
        for str_filename in h_file.readlines():
            try:
                str_filename=str_filename.strip('\n')
                str_filepath=str_dir+str_filename
                if os.path.exists(str_filepath):
                        b_latest,c_olddate=IsLatest(str_filepath)
                        if b_latest==False:
                                UpdateData(str_filepath,c_olddate)
                else:
                        AddNewData(str_filepath)
                print("update %s"%str_filepath)
            except:
                continue

def remove_codenum(filename):
     #pdb.set_trace()
     f=open(filename,'r')
     left=[]
     for line in f.readlines():
         if re.match("2",line):
             continue
         if re.match("5",line):
             continue
         if re.match("9",line):
             continue
         left.append(line)
     f.close()
     f=open(filename,'w')
     for line in left:
         f.writelines(line)
     f.close()
     #pdb.set_trace()

def remove_nullfile(str_filenamelist):
    f_hl=open(str_filenamelist,"r")
    for filename in f_hl.readlines():
        #pdb.set_trace()
        try:
            f=open(str_dir+filename[0:-1],"r")
            if (len (f.readlines()) <2):
                f.close()
                file_path=str_dir+filename[0:-1]
                os.system("del "+file_path)
            else:
                f.close()
        except:
            continue

    f_hl.close()


        




        
         
#测试代码

if  __name__ == '__main__':
        import DownloadStockInform
        import pdb
#        str_filename='c:/StockData/000001.ss.csv'
#        b_latest,c_olddate=IsLatest(str_filename)
#        print( b_latest, c_olddate)
#        if b_latest==False :
#                print TranslateToURL(str_filename,c_olddate)
#              #  pdb.set_trace()
#                UpdateData(str_filename,c_olddate)
#        
#        pdb.set_trace()
        #AddNewData('c:/StockData/601169.ss.csv')
        #str_filename_list='c:/StockData/stocklist_scrapy.txt'
        str_filename_list='d:/stockdata/stocklist_scrapy.txt'
        remove_codenum(str_filename_list)
        UpdateList(str_filename_list)
        remove_nullfile(str_filename_list)
        



