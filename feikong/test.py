# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:52:46 2017

@author: Administrator
"""

import numpy as np
from numpy import cos,sin,arcsin,arctan2,sqrt,dot

import matplotlib.pyplot as plt
data=np.loadtxt("C:/PythonLearning/feikong/data_in1.txt")
step = 0.006
gx=data[:,0]
gy=data[:,1]
gz=data[:,2]

ax=data[:,3]
ay=data[:,4]
az=data[:,5]
KI = 0.01#0.005/2
KP = 2.2#2.0/100
exInt = 0.0
eyInt = 0.0
ezInt = 0.0
dt=0.006
gyro_x_zero_bias = 0.0
gyro_y_zero_bias = 0.0
gyro_z_zero_bias = 0.0

def degree_to_radian(roll,pitch,yaw):
    gyro_x=roll*np.pi/180
    gyro_y=pitch*np.pi/180
    gyro_z=yaw*np.pi/180
    return gyro_x,gyro_y,gyro_z
  
def init_quaternion(roll,pitch,yaw):
    #format data
    roll=roll*np.pi/180
    pitch=pitch*np.pi/180
    yaw=yaw*np.pi/180
    #init
    q0=cos(yaw/2)*cos(pitch/2)*cos(roll/2)+sin(yaw/2)*sin(pitch/2)*sin(roll/2)
    q1=cos(yaw/2)*cos(pitch/2)*sin(roll/2)-sin(yaw/2)*sin(pitch/2)*cos(roll/2)
    q2=cos(yaw/2)*sin(pitch/2)*cos(roll/2)+sin(yaw/2)*cos(pitch/2)*sin(roll/2)
    q3=sin(yaw/2)*cos(pitch/2)*cos(roll/2)-cos(yaw/2)*sin(pitch/2)*sin(roll/2)
    return q0,q1,q2,q3
def quarternion_matrix_update(q0,q1,q2,q3,gyro_x,gyro_y,gyro_z,acc_x,acc_y,acc_z,dt):
    q_matrix = np.array([[q0],[q1],[q2],[q3]])
    q_upate_matrix = np.array([[-q1,-q2,-q3],[q0,-q3,q2],[q3,q0,-q1],[-q2,q1,q0]])
    gyro_matrix = np.array([[gyro_x],[gyro_y],[gyro_z]])
    q_matrix = q_matrix + 0.5*dt*dot(q_upate_matrix,gyro_matrix)
    return q_matrix[0,0],q_matrix[1,0],q_matrix[2,0],q_matrix[3,0]
def quaternion_update(q0,q1,q2,q3,gyro_x,gyro_y,gyro_z,acc_x,acc_y,acc_z,dt):
    #remove gyro zero-bias
    gyro_x,gyro_y,gyro_z=gyro_remove_zerobias(gyro_x,gyro_y,gyro_z)
     
    #Normlise acc to norm vector
    if (acc_x==0 and acc_y==0 and acc_z==0):
        print '!!!!error acc is all zero in iterate:',i
        print 'acc_x:',acc_x,'acc_y:',acc_y,'acc_z',acc_z
        while 1:
            pass
    norm = sqrt(acc_x**2+acc_y**2+acc_z**2)
    ax=acc_x/norm
    ay=acc_y/norm
    az=acc_z/norm
    #use rotate matrix caculate gravity norm vector
    vx=2*(q1*q3-q0*q2)
    vy=2*(q2*q3+q0*q1)
    vz=(q0**2-1+q3**2)
    #vz=(q0**2-q1**2-q2**2+q3**2)#add negtive sign because earth frame is NED so gravity is -9.8
     
    ex = (ay*vz - az*vy);
    ey = (az*vx - ax*vz);
    ez = (ax*vy - ay*vx);

    global exInt,eyInt,ezInt
    exInt=KP*ex+ex*KI
    eyInt=KP*ey+ey*KI
    ezInt=KP*ez+ez*KI

    #print 'exInt',exInt
    gyro_x = gyro_x + KP*ex+exInt
    gyro_y = gyro_y + KP*ey+eyInt
    gyro_z = gyro_z + KP*ez+ezInt
     

    q0=q0+0.5*dt*(-gyro_x*q1-gyro_y*q2-gyro_z*q3)
    q1=q1+0.5*dt*(gyro_x*q0+gyro_z*q2-gyro_y*q3)
    q2=q2+0.5*dt*(gyro_y*q0-gyro_z*q1+gyro_x*q3)
    q3=q3+0.5*dt*(gyro_z*q0+gyro_y*q1-gyro_x*q2)
     
    #Formlise quarternion
    norm = sqrt(q0**2+q1**2+q2**2+q3**2)
    q0=q0/norm
    q1=q1/norm
    q2=q2/norm
    q3=q3/norm
     
    return q0,q1,q2,q3

def quaternion_to_euler(is_radian,q0,q1,q2,q3):
    roll = arctan2(2*(q2*q3+q0*q1),(q0**2-q1**2-q2**2+q3**2))
    pitch = (-1)*arcsin(2*(q1*q3-q0*q2))
    yaw = arctan2(2*(q1*q2+q0*q3),(q0**2+q1**2-q2**2-q3**2))
    #print 'roll:',roll,'pitch:',pitch,'yaw:',yaw
    if not(is_radian):
        return roll*(180/np.pi),pitch*(180/np.pi),yaw*(180/np.pi)
    else:
        return roll,pitch,yaw
def init_data_correction(gyro_x,gyro_y,gyro_z):
    #save gyro bais
    global gyro_x_zero_bias,gyro_y_zero_bias,gyro_z_zero_bias
    gyro_x_zero_bias = gyro_x
    gyro_y_zero_bias = gyro_y
    gyro_z_zero_bias = gyro_z
    print 'gyro_x_zero_bias:',gyro_x_zero_bias,'gyro_y_zero_bias:',gyro_y_zero_bias,'gyro_z_zero_bias:',gyro_z_zero_bias

def gyro_remove_zerobias(gyro_x,gyro_y,gyro_z):
    return gyro_x-gyro_x_zero_bias,gyro_y-gyro_y_zero_bias,gyro_z-gyro_z_zero_bias
def offline_simulate(filename,color):
    #read log
    lines = np.loadtxt(filename)
    #caculate size
    data_length = lines[:,1].size
    print '########Offline Simulate#######'
    print '#Data length:',data_length
    #define a matrix to save euler angle
    euler_result = np.zeros((data_length,3))
    #init quarternion
    q0,q1,q2,q3=init_quaternion(0,0,0)
    #init gyro zero-bias
    init_data_correction(lines[0,0],lines[0,1],lines[0,2])
     
    #iteration update
    for i in range(data_length):
        q0,q1,q2,q3 = quaternion_update(q0,q1,q2,q3,lines[i,0],lines[i,1],lines[i,2],lines[i,3],lines[i,4],lines[i,5],0.006)
        euler_result[i]=quaternion_to_euler(0,q0,q1,q2,q3)
        print euler_result[i]
    plt.plot(range(data_length),euler_result[:,0]/np.pi*180,color)
    #plt.plot(range(data_length/10),euler_result[:,1],'red')
    #plt.plot(range(data_length/10),euler_result[:,2],'green')
   # plt.plot(range(data_length),lines[0:data_length,0]/np.pi*180,'red')
    plt.show()

def test_quaternion():
    q0,q1,q2,q3=init_quaternion(0,0,0)
    #q0,q1,q2,q3 = quarternion_matrix_update(q0,q1,q2,q3,2,0,0,0,0,0,2)
    gyro_x,gyro_y,gyro_z=degree_to_radian(0,0,2)
    q0,q1,q2,q3 = quaternion_update(q0,q1,q2,q3,gyro_x,gyro_y,gyro_z,0,0,0,2)
    print quaternion_to_euler(0,q0,q1,q2,q3)




#return roll,pitch,yaw
if __name__ == '__main__':
 #  offline_simulate("C:/PythonLearning/feikong/data_in1.txt",'red')
    offline_simulate("C:/PythonLearning/feikong/data_in2.txt",'blue')