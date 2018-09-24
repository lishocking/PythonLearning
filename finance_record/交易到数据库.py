import sqlite3
import os
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import mpl_finance as mpf
import re
fl=os.listdir()
conn=sqlite3.connect("finance.sql3")
c=conn.cursor()
if("finance.sql3" not in fl):
    command='''create table fr(
交割日期,
业务名称,
证券代码,
证券名称,
成交价格,
成交数量,
剩余数量,
成交金额,
清算金额,
剩余金额,
佣金,
印花税,
过户费,
结算费,
附加费,
币种,
成交编号,
股东代码,
资金帐号,
primary key(交割日期,成交编号))'''
    c.execute(command)
os.chdir('./stock_finace')
fl=os.listdir()
for i in fl:
    f=open(i,'r')
    for l in f.readlines():
        cmd=re.sub('\s+',',',l)
        cmd=cmd.strip(',')
        cmd_l=cmd.split(',')
        a=len(cmd_l)
        if a <5:
            continue;
        if cmd_l[0]=='交割日期':
            continue;
        if cmd_l[1] in ('利息归本' , '证券转银行' ,'银行转证券'):
            cmd_l.insert(2,'')
            cmd_l.insert(2,'')
            cmd_l.insert(-2,'bank'+cmd_l[1]+cmd_l[9])
            cmd_l.insert(-2,'bank'+cmd_l[1]+cmd_l[9])
        if cmd_l[1] in ('红股入账','红利入账'):
            cmd_l.insert(-2,'bonus')
        cmd=str(cmd_l).strip('[]')
        command='insert or ignore into fr values('+cmd+')'
        print(command)
        c.execute(command)
    f.close()
conn.commit()
conn.close()
'''
select distinct 证券名称  from fr where 业务名称 like '%证券%'
select *  from fr where 业务名称 like '%证券%'
select sum(佣金+印花税+过户费) from fr where 业务名称 like '%证券%'
select * from fr where 业务名称 like '%融券%'
'''
