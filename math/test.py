from scipy.signal import lfilter
from spectrum import *
from numpy.random import randn
A  =[1, -2.7607, 3.8106, -2.6535, 0.9238]
noise = randn(1, 1024)
y = lfilter([1], A, noise); 
 #filter a white noise input to create AR(4) process

rho = []
for i in range(1,4) :
    [ar, var, reflec] = aryule(y[0], 4)
    rho.append(ar)
 # ar should contains values similar to A
kktua = []
print(rho)
for i in rho : 
    kktua.append(i.tolist())

print(kktua)
