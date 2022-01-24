#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 01:22:04 2022

@author: lyth
"""


t = 100000
d = 128
dt = 0.0001
x = np.zeros((d,d))
v = np.zeros((d,d))

x[int(d/2)-int(d/16):int(d/2)+int(d/16),int(d/2)-int(d/16):int(d/2)+int(d/16)] = 1

def CN(Z):
    D = np.zeros(np.shape(Z))
    D+= np.roll(Z, -1, axis = 1)
    D+=np.roll(Z, 1, axis = 1)
    D+=np.roll(Z, -1, axis = 0)
    D+= np.roll(Z, 1, axis = 0)
    
    D+=np.roll(np.roll(Z, -1, axis = 0), -1, axis = 1)
    D+=np.roll(np.roll(Z, 1, axis = 0), -1, axis = 1)
    D+=np.roll(np.roll(Z, 1, axis = 0), 1, axis = 1)
    D+=np.roll(np.roll(Z, -1, axis = 0), 1, axis = 1)
    
    return D



def stp(x,v,dt):
    
    #a = -(x*9 -CN(x))
    a = -(9*x*x-2*x*CN(x)+CN(x*x))
    return x + dt*v,v + dt * a

X = np.zeros((t,d,d))
for i in range(t):
    if i % 100==0:
        print(i,x.max())
       # x[int(d/2)-int(d/32):int(d/2)+int(d/32),int(d/2)-int(d/32):int(d/2)+int(d/32)] = 1  
    X[i] = x
    #plt.imsave('./membrane_plts/plt'+str(i),x)
    x,v = stp(x,v,dt)
    #x,v = x/x.sum(), v/v.sum()
'''    
for i in range(len(X)):
    print(i)
    plt.imsave('./membrane_plts/plt'+str(i),X[i],vmin=X.min(),vmax=X.max())
#plt.imshow(x)
'''
def lapse(X,s,st,stp):
    #var = pc.read_var()
    d = stp
    n = int((st-s)/stp)
    fig ,ax = plt.subplots(1,n)
    for i in range(n):
        ax[i].imshow(X[s+d*i])
        ax[i].xaxis.set_visible(False)
        ax[i].yaxis.set_visible(False)