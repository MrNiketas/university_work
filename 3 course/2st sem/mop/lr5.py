import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

a = 1.3 * 10**(-1)
delt_x = 0.1
X = 1
t_max = 10
delt_t = 0.5 * delt_x ** 2

#начальное
fi = lambda x: 25+5*x
#первое граничное
f_1 = lambda t: 25-math.sin(t)
#второе граничное
f_2 = lambda t: 30+0.0004*t**2-0.1*t

#d_T = lambda t, x: a * (delt_t/delt_x**2)*(d_T(t, x)- 2*d_T(t, x) + d_T(t, x)) + d_T(t, x)


time = []
L = []

fi_s = []
f_1s = []
f_2s = []

x = 0
t = 0

while x <= X:
    fi_s.append(fi(x))
    L.append(x)
    x += delt_x
    #print(L)

while t <= t_max:
    f_1s.append(f_1(t))
    f_2s.append(f_2)
    time.append(t)
    t += delt_t

T = np.array([[0.1 for i in np.arange(len(L))] for _ in np.arange(len(time))])
#Time_mesh = np.meshgrid(time)
#time = list(Time_mesh)

for j in np.arange(0, len(time) - 1):
    T[j+1][0] = f_1(time[j])
    #print(T)
    for i in np.arange(1, 10):
        T[j+1][i] = T[j][i] + (((a * delt_t)/delt_x**2)*(T[j][i + 1] - 2 * T[j][i] + T[j][i-1]))
    T[j+1][-1]=f_2(time[j])

print(T)

L, time = np.meshgrid(L, time)
print(len(L))
print(len(time))
print(len(T))
fig = plt.figure()
axes = Axes3D(fig)

axes.plot_surface(L, time, T, rstride=4, cstride=4, cmap=cm.cool)
axes.set_xlabel('l')
axes.set_ylabel('τ')
axes.set_zlabel('T')

plt.show()


