import matplotlib.pyplot as plt
import numpy as np
from math import *

#setting
delta_t=0.001
t_min=0
t_max=100
time=np.arange(t_min,t_max,delta_t)
sol_x=[]
sol_v=[]

#initial condition
f=0.0
m=2.0
k=1.0
c=0.0
x=1.0
v=0.0
omega=sqrt(k/m)

A=np.array([[m,0],[0,1]])
B=np.array([[c,k],[-1,0]])
F=np.array([0,0])
y=np.array([v,x])

A_inverse=np.linalg.inv(A)

def G(t,y):
    F[0]=f*np.cos(omega*t)
    return A_inverse.dot(F-B.dot(y))

def RK4(t,y,delta_t):
    k1=G(t,y)
    k2=G(t+0.5*delta_t,y+0.5*delta_t*k1)
    k3=G(t+0.5*delta_t,y+0.5*delta_t*k2)
    k4=G(t+0.5*delta_t,y+0.5*delta_t*k3)
    return 1./6.0*k1 + 2./6*k2+2./6*k3+1./6*k4
    #return k1

#print(A)
for t in time:
    y=y+delta_t*RK4(t,y,delta_t)
    sol_x.append(y[1])
    sol_v.append(y[0])

#G=RK4(t,y,delta_t)

name="Driven Oscillation"

plt.plot(time, sol_x,'r',label="position")
#plt.plot(time, sol_v,'--',label="velocitiy")
plt.grid(True)
plt.legend()
plt.title(name)
plt.show()
