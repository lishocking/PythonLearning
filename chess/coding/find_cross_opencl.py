from __future__ import absolute_import, print_function
import numpy as np
import pyopencl as cl
import os
import cv2
import cv 
import numpy as np
import matplotlib.pyplot as plt
import pdb
import time
os.environ['PYOPENCL_COMPILER_OUTPUT'] = '1'
os.environ['PYOPENCL_CTX']='0:0'
def FindCrossLineP(img_bin,r=40/2):
    return 0
def FindLineH(img_bin,min_length):
    height,width=img_bin.shape
    ctx = cl.create_some_context()
    queue = cl.CommandQueue(ctx)
    mf = cl.mem_flags
    img_bin_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=img_bin)

    return 0
def FineLineV(img_bin,min_length):
    return 0

"""
__kernel void sub(
    __global const float *a_g, __global const float *b_g, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] - b_g[gid];
}
"""


a_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a_np)
b_g = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b_np)

prg = cl.Program(ctx, """
__kernel void sum(
    __global const float *a_g, __global const float *b_g, __global float *res_g)
{
  int gid = get_global_id(0);
  res_g[gid] = a_g[gid] + b_g[gid];
}
""").build()

res_g = cl.Buffer(ctx, mf.WRITE_ONLY, a_np.nbytes)
prg.sum(queue, a_np.shape, None, a_g, b_g, res_g)

res_np = np.empty_like(a_np)
cl.enqueue_copy(queue, res_np, res_g)

# Check on CPU with Numpy:
print(res_np - (a_np + b_np))
print(np.linalg.norm(res_np - (a_np + b_np)))

def FindCrossLineP1(img_bin,r=40/2):
    line_h=FindLineH(img_bin,r)
    line_v=FindLineV(img_bin,r)
    cross_point=[]
    for lh in line_h:
        pt1=lh[0]
        pt2=lh[1]
        for lv in line_v:
            pt3=lv[0]
            pt4=lv[1]
            if((pt3[0]+5>pt1[0])\
                   and (pt3[0]-5<pt2[0])\
                   and (pt1[1]+5>pt3[1])\
                   and (pt1[1]-5<pt4[1]) ):
                cross_point.append([pt3[0],pt1[1]])
    return cross_point

if __name__ == '__main__':
    img =  cv2.imread('d:/1.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #plt.imshow(lap,'gray')
    ret,img_bin = cv2.threshold(gray,100,1,cv2.THRESH_BINARY)
#    list=FindCrossLineP(img_bin)
#    list_1=FindLineH(img_bin,20)
#    for i in list[:]:
#        cv2.circle(img,(i[0],i[1]),10,(255,0,0),5)
#    for i in  list_1:
#        cv2.line(img,i[0],i[1],255,2)
#    list_2=FindLineV(img_bin,20)
#    for i in  list_2:
#        cv2.line(img,i[0],i[1],(0,255,0),2)
    start=time.clock()
    list_p=FindCrossLineP1(img_bin)
    end=time.clock()
    print "time:%f s" % (end-start)
    for i in list_p:
            cv2.circle(img,(i[0],i[1]),5,(255,0,0),5)
    print list_p
    plt.imshow(img)
    plt.show()
