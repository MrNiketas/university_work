import pylab
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

T = 1250
L = 190

R = 8.31
E1 = 251000
E2 = 297000
A1 = 2 * (10**11)
A2 = 8 * (10**12)
ro = 1.4
D = 0.1

delta_l = 0.5

delta_C = 0.05
delta_m = 0.15
delta_T = 0.25

C_vhod_0 = 0.25 * (ro/0.2805)
m0 = 0.5
m1 = 1

k1 = A1 * np.exp((-E1) / (R * T))
k2 = A2 * np.exp((-E2) / (R * T))

d_C1 = lambda C1, M1: (-k1 * C1 * (ro * (np.pi * (D ** 2)) / 4)) / M1
d_C2 = lambda C1, C2, M1: ((k1 * C1 - k2 * C2) * ro * (np.pi * D ** 2) / 4) / M1

res_1 = []
res_2 = []

l = [i for i in np.arange(0, L + delta_l, delta_l)]
fig, axes = pylab.subplots(nrows=1, ncols=2, figsize=(12, 5))

while m0 < m1:
    C1 = C_vhod_0
    C2 = 0
    M1 = m0
    C1_percent = C1 * (100 * 0.2805) / ro
    C2_percent = C2 * (100 * 0.2805) / ro

    for i in l:
        C1_percent = C1 * (100 * 0.2805) / ro
        C2_percent = C2 * (100 * 0.2805) / ro
        res_1.append(C1_percent)
        res_2.append(C2_percent)
        C1 = C1 + d_C1(C1, M1) * delta_l
        C2 = C2 + d_C2(C1, C2, M1) * delta_l
    axes[0].plot(l, res_1, color='black')
    axes[0].set_xlabel("L, метры")
    axes[0].set_ylabel("C1, %")


    axes[1].plot(l, res_2, color='black')
    axes[1].set_xlabel("L, метры")
    axes[1].set_ylabel("C2, %")
    res_1.clear()
    res_2.clear()
    m0 += delta_m


pylab.subplots_adjust(wspace=0.5, hspace=0)
pylab.show()