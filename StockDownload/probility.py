import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
def probgen(counter=1):
    c=[]
    if counter==1:
        return [[0],[1]]
    else:
        counter-=1
        x=probgen(counter)
        for m in x:
            a,b=[0],[1]
            a.extend(m)
            b.extend(m)
            c.append(a)
            c.append(b)
        return c

def calculate_probility(result_list,p):
    result_probility=[]
    for m in result_list:
        s=sum(m)
        l=len(m)
        r=p**s*\
                (1-p)**(l-s)
        result_probility.append(r)
    return result_probility
def stage_1(total_money,bet_count,last_count):
    return total_money
def stage_2(total_money,bet_count,last_count):
    return total_money/bet_count
def stage_3(total_money,bet_count,last_count):
    return total_money/10

def betmodel(total_money,win_probility,bet_count,stage_1):
    possiblity=probgen(bet_count)
    r_probility=calculate_probility(possiblity,win_probility)
    result=[]
    for x in possiblity:
        total_money_tmp=total_money
        count_tmp=bet_count
        for i in x:
            count_tmp-=1
            bet_money=stage_1(total_money_tmp,bet_count,count_tmp)
            if i == 0:#lostmoney
                total_money_tmp-=bet_money;
                if total_money_tmp<=0:
                    break
            else:
                total_money_tmp+=bet_money;
        result.append(total_money_tmp)
    return [result,r_probility]

def statistic(result,r_probility):
    s_r=[[],[]]
    l=len(result)
    i=0
    while i < l:
        if result[i] not in s_r[0]:
            s_r[0].append(result[i])
            s_r[1].append(r_probility[i])
        else:
            index=s_r[0].index(result[i])
            s_r[1][index]+=r_probility[i]
        i+=1
            
    return s_r
    
def statistic_histogram(result,r_probility):
    s_r=[[],[]]
    l=len(result)
    i=0
    s_max=max(result)
    s_min=min(result)
    step=(s_max-s_min)/10.0
    s_r[0]=range(int(s_min-step/2.0),int(s_max+step/2.0),int(step))
    s_r[1]=[0]*12
    while i < l:
        k=0
        while k < 10:
            if s_r[0][k]<=result[i]<s_r[0][k+1]:
                s_r[1][k]+=r_probility[i]
                break;
            k+=1
        i+=1
            
    return s_r
   

if  __name__ == '__main__':
        import pdb
#                pdb.set_trace()
        a=betmodel(10000.0,0.7,15,stage_2)
       # st=statistic(a[0],a[1])
        st=statistic_histogram(a[0],a[1])
        np.array(st)
        pl.plot(st[0],st[1],'bo')
        a=betmodel(10000.0,0.7,15,stage_3)
        st=statistic_histogram(a[0],a[1])
        np.array(st)
        pl.plot(st[0],st[1],'gx')
        pl.show()

    

    
