import numpy as np
import matplotlib.pyplot as plt

#Данные по варианту 6
# Концентрация
C0 = 7
C1 = 12
Cvx = 10

# Расход
M0 = 3.9
M1 = 5.4
Mvx = 4

# Температурa греющего пара
T0 = 125
T1 = 145
Tpi = 138

#Константы
Tp = 90 #Температура кипения раствора
Tau = 2.25 * 10**6 #Теплота парообразования вторичного пара
Kt = 5000 # коэффициент теплопередачи
F = 10 # Площадь теплообмена
Ct = 4187   # Теплоемкость раствора


deltaC = 0.4
deltaM = 0.2
deltaT = 0.5


def function(mvx, cvx, tpi):
    return (mvx*cvx)/(mvx-(Kt*F*(tpi-Tp)/(-Ct*Tp+Tau)))


def graf():
    tArray = np.linspace(C0, C1, int((C1 - C0) / deltaC))
    Cvix = [function(Mvx, i, Tpi) for i in tArray]
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(12, 5))
    ax[0].grid(True)
    ax[0].plot(tArray, Cvix, color='black')

    tArray = np.linspace(M0, M1, int((M1 - M0) / deltaM))
    Cvix = [function(i, Cvx, Tpi) for i in tArray]
    ax[1].plot(tArray, Cvix, color='red')

    tArray = np.linspace(T0, T1, int((T1 - T0) / deltaT))
    Cvix = [function(Mvx, Cvx, i) for i in tArray]
    ax[2].plot(tArray, Cvix, color='green')

    ax[0].set(title='C(вых) от C')
    ax[1].set(title='C(вых) от m')
    ax[2].set(title='C(вых) от T')
    ax[0].grid(True)
    ax[1].grid(True)
    ax[2].grid(True)
    plt.show()


if __name__ == '__main__':
    graf()


