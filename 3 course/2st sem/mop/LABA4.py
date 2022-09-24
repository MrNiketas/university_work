import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


k_T = 6500
c_T = 4190
ro = 1000
T_T = 80
L = 1
D = 0.05
u = 0.2
t_max = 10

delta_alf = 0.3
delta_bet = 0.2

T_0_l = lambda l: 30-5*l
T_vh = lambda t: t-6*math.sin(t)+30
t_s = L/u

T1 = []
t = []
l = []

for i in np.arange(-t_s / 2, 0, delta_bet):
    T0 = T_0_l(-2 * u * i)
    for j in np.arange(-i, i + t_s, delta_alf):
        l.append(u*(j - i))
        t.append(j + i)
        T0 = T0 + (T_T - T0) * ((4 * k_T) / (c_T * ro * D))
        T1.append(T0)


for i in np.arange(0, (t_max - t_s)/2, delta_bet):
    T0 = T_vh(2 * i)
    for j in np.arange(i, i + t_s, delta_alf):
        l.append(u*(j - i))
        t.append(j + i)
        T0 = T0 + (T_T - T0) * ((4 * k_T) / (c_T * ro * D))
        T1.append(T0)


for i in np.arange((t_max - t_s)/2, t_max/2, delta_bet):
    T0 = T_vh(2 * i)
    for j in np.arange(i, -i + t_max, delta_alf):
        l.append(u*(j - i))
        t.append(j + i)
        T0 = T0 + (T_T - T0) * ((4 * k_T) / (c_T * ro * D))
        T1.append(T0)

axes = Axes3D(plt.figure(figsize=(8,7)))
axes.plot_trisurf(l, t, T1, cmap='plasma', edgecolor='none', antialiased=True)
axes.set_xlabel('l')
axes.set_ylabel('τ')
axes.set_zlabel('T')
plt.show()