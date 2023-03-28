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
f=2.0
m=2.0
k=1.0
c=0.3
x=0.0
v=1.0

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
Force=f
#label=f'Force:{Force}'

plt.plot(time, sol_x,'r',label="position")
plt.plot(time, sol_v,'--',label="velocitiy")
plt.grid(True)
plt.legend()
plt.title(name)
plt.show()
