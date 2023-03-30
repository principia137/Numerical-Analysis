import matplotlib.pyplot as plt
import numpy as np
from math import *

#setting
delta_t=0.001
t_min=0
t_max=30
time=np.arange(t_min,t_max,delta_t)
sol_x=[] #array of solution of positon
sol_v=[] #array of solution of velocity

#initial condition
f=0.0
m=2.0
k=1.0
c=0.0
x=1.0
v=0.0
omega=sqrt(k/m)

#1st order Runge Kunta method for Driven oscillation
A=np.array([[m,0],[0,1]])
B=np.array([[c,k],[-1,0]])
F=np.array([f,0])
y=np.array([v,x])

#print(A)

for t in time:
    G=np.matmul(np.linalg.inv(A),(F-np.matmul(B,y)))
    y=y+G*delta_t
    sol_x.append(y[1])
    sol_v.append(y[0])

name="Driven Oscillation"

plt.plot(time, sol_x,'r',label="position")
plt.plot(time, sol_v,'b',label="velocity")
plt.grid(True)
plt.legend()
plt.title(name)
plt.show()