import numpy as np
import matplotlib.pyplot as plot


#Данные по варианту 6
# Концентрация
C0 = 7
C1 = 12
Cvx = 10

# Расход
M0 = 3.9
M1 = 5.4
Mvx = 4

# Температура
T0 = 125
T1 = 145
Tpi = 138

#Константы
Tp = 90
Tau = 2.25 * 10E6
Kt = 5000
F = 10
Ct = 4187


deltaC = 0.4
deltaM = 0.2
deltaT = 0.5


def function(mvx, cvx, tpi):
    return (mvx*cvx)/(mvx+(Kt*F*(tpi-Tp)/(Ct*Tp-Tau)))


def grafC():
    tArray = np.linspace(C0, C1, int((C1-C0)/deltaC))
    Cvix = [function(Mvx, i, Tpi) for i in tArray]
    plot.plot(tArray, Cvix)
    plot.grid()
    plot.xlabel('Концентрация входа')
    plot.ylabel('Концентрация выхода')
    plot.show()

def grafM():
    tArray = np.linspace(M0, M1, int((M1 - M0) / deltaM))
    Cvix = [function(i, Cvx, Tpi) for i in tArray]
    plot.plot(tArray, Cvix)
    plot.grid()
    plot.xlabel('Масса')
    plot.ylabel('Концентрация выхода')
    plot.show()

def grafT():
    tArray = np.linspace(T0, T1, int((T1 - T0) / deltaT))
    Cvix = [function(Mvx, Cvx, i) for i in tArray]
    plot.plot(tArray, Cvix)
    plot.grid()
    plot.xlabel('Температура')
    plot.ylabel('Концентрация выхода')
    plot.show()
    return 0


if __name__ == '__main__':
    grafC()
    grafM()
    grafT()
