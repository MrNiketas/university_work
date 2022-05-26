import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

lya_1 = 5**9
lya_2 = 3**8
M0 = 13
disp = 8
a0 = 0.12
A_1 = 0.5

A_2 = 0.5
Z_max = 190
N_s = 10

#конгруэнтный алгоритм
X = []
cong = []
x = 1

def Cong():
    for i in range(200):
        if i == 0:
            X.append(x)
        else:
            X_i = (lya_1 * X[i-1]) % lya_2
            X.append(X_i)
    for i in range(200):
        cong.append((X[i]/lya_2)-0.5)
    return cong

def M(z):
    return (1/len(z))*sum(z)

def Disper(z):
    sum_z = 0
    for i in z:
        sum_z += (i-M(z))**2
    return ((1/len(z))*sum_z)


def Z(z):
    Z_k = []
    for i in range(len(z)-N_s):
        sum_z = 0
        for j in range(i, i+N_s):
            sum_z += z[j] * math.sqrt(math.sqrt(disp)/( Disper(z) *a0)) * A_1 * math.exp(-1*a0*(i - j)) + M0
        Z_k.append((1/N_s)*sum_z)
    return Z_k


listt = Cong()
Z_k = Z(listt)
print(Z_k)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

x1 = [i for i in range(200)]
z1 = [i for i in range(190)]
axes[0].plot(x1, listt, color='green')
axes[1].plot(z1, Z_k, color='blue')


plt.subplots_adjust(wspace=0.5, hspace=0)
plt.show()