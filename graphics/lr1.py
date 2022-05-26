import matplotlib.pyplot as plt
from pylab import mpl
import numpy as np

x = [0, 20, 40, 60, 80]
y = [0, 10, 0, 0, 0]


def ParametersOfLagrangeInterpolation(data_x, data_y, size):
    parameters = []
    # i используется для управления количеством параметров
    i = 0
    while i < size:
        # jПеременная, используемая для управления циклом, умножается
        j = 0
        temp = 1
        while j < size:
            if (i != j):
                temp *= data_x[i] - data_x[j]
            j += 1
        parameters.append(data_y[i] / temp)
        i += 1
    return parameters


def CalculateTheValueOfLarangeInterpolation(data_x, parameters, x):
    returnValue = 0
    i = 0
    while i < len(parameters):
        temp = 1
        j = 0
        while j < len(parameters):
            if (i != j):
                temp *= x - data_x[j]
            j += 1
        returnValue += temp * parameters[i]
        i += 1
    return returnValue


def Draw(data_x, data_y, new_data_x, new_data_y):
    plt.plot(new_data_x, new_data_y, label="соответствующая кривая", color="black")
    plt.scatter(data_x, data_y, label="дискретные данные", color="red")
    mpl.rcParams['axes.unicode_minus'] = False
    plt.title("Данные подгонки лагранжевой интерполяции")
    # plt.legend(loc="upper left")
    plt.show()


parameters = ParametersOfLagrangeInterpolation(x, y, 5)
datax = np.linspace(0, 80, 100)
# datax=[0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80]
datay = []
for temp in datax:
    datay.append(CalculateTheValueOfLarangeInterpolation(x, parameters, temp))
Draw(x, y, datax, datay)