import math
from re import L
import numpy as np
import matplotlib.pyplot as plot
from mpl_toolkits.mplot3d import Axes3D

def function_T0L(l):
    return 25+5*l

def function_Tinput(t):
    return 25-math.sin(t)

Kt = 6500 # Vt/m^2 коэффициент теплопередачи допущение
Ct = 4190 # Dj/kg*grad теплоемкость нагреваемой жидкости допущение
Ro = 1000 # kg/m^3 плотность нагреваемой жидкости допущение
T = 80 # *C температура теплоносителя допущение
L = 1 # m длина трубы
D = 0.05 # m диаметр трубы
U = 0.2 # m/c скорость движения жидкости в трубе
TauMax = 10 # c время 
DeltaAlpha = 0.25
DeltaBeta = 0.2
TauS = L/U # Среднее время пребывания

def plotCreator():
    T1 = []
    Tau = []
    l = []

    for i in np.arange(-TauS/2,0,DeltaBeta):
        T0 = function_T0L(-2*U*i)
        for j in np.arange(-i,i+TauS,DeltaAlpha):
            l.append(U*(j-i))
            Tau.append(j+i)
            T0 = T0 + (T-T0) * ((4*Kt/(Ct*Ro*D)))
            T1.append(T0)

    for i in np.arange(0,(TauMax-TauS)/2,DeltaBeta):
        T0 = function_T0L(2*i)
        for j in np.arange(i,i+TauS,DeltaAlpha):
            l.append(U*(j-i))
            Tau.append(j+i)
            T0 = T0 + (T-T0) * ((4*Kt/(Ct*Ro*D)))
            T1.append(T0)
    
    for i in np.arange((TauMax-TauS)/2,TauMax/2,DeltaBeta):
        T0 = function_T0L(2*i)
        for j in np.arange(i,-i+TauS,DeltaAlpha):
            l.append(U*(j-i))
            Tau.append(j+i)
            T0 = T0 + (T-T0) * ((4*Kt/(Ct*Ro*D)))
            T1.append(T0)
    
    axes = Axes3D(plot.figure())
    axes.plot_trisurf(l,Tau,T1,cmap='plasma',edgecolor='none',antialiased = True)
    axes.set_xlabel('l')
    axes.set_ylabel('tau')
    axes.set_zlabel('T')
    plot.show()


if __name__ == '__main__':
    plotCreator()
