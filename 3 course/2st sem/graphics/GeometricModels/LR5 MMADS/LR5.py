import math
import numpy as np
import matplotlib.pyplot as plot
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


A = 1.3 * 10**(-1)
Delta_X = 0.1
X = 1
Tau_Max = 10
Delta_Tau = 0.5 * Delta_X ** 2

def function_fiX(x):
    return 30-5*x

def function_f1(t):
    return t - 6*math.sin(t) + 30 

def function_f2(t):
    return 25 + 0.11*t

def plotCreator():
    time = np.arange(0,Tau_Max+Delta_Tau,Delta_Tau)
    L = np.arange(0,X+Delta_X,Delta_X)
    T = np.array([[0.1 for i in np.arange(len(L))] for _ in np.arange(len(time))])

    for j in np.arange(0, len(time) - 1):
        T[j+1][0] = function_f1(time[j])
        for i in np.arange(1, 10):
            T[j+1][i] = T[j][i] + (((A * Delta_Tau)/Delta_X**2)*(T[j][i + 1] - 2 * T[j][i] + T[j][i-1]))
        T[j+1][-1]=function_f2(time[j])
        
    L, time = np.meshgrid(L, time)
    axes = Axes3D(plot.figure())
    axes.plot_surface(L, time, T, rstride=4, cstride=4, cmap=cm.cool)
    axes.set_xlabel('l')
    axes.set_ylabel('τ')
    axes.set_zlabel('T')
    plot.show()

if __name__ == '__main__':
    plotCreator()