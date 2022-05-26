import matplotlib.pyplot as plt
import numpy as np


# Расчет производной от базовой функции
def dl(i, xi):
    result = 0.0
    for j in range(0, len(xi)):
        if j != i:
            result += 1 / (xi[i] - xi[j])
    result *= 2
    return result


# Расчет значения базовой функции
def l(i, xi, x):
    deno = 1.0
    nu = 1.0
    for j in range(0, len(xi)):
        if j != i:
            deno *= (xi[i] - xi[j])
            nu *= (x - xi[j])
    return nu / deno


# Интерполяционная функция Эрмита
def get_Hermite(xi, yi, dyi):
    def he(x):
        result = 0.0
        for i in range(0, len(xi)):
            result += (yi[i] + (x - xi[i]) * (dyi[i] - 2 * yi[i] * dl(i, xi))) * ((l(i, xi, x)) ** 2)
        return result

    return he


import math

sr_x = [(i * math.pi) + (math.pi / 2) for i in range(-3, 3)]
sr_fx = [math.sin(i) for i in sr_x]
dx = [0 for i in sr_x]  # все производные 0
Hx = get_Hermite(sr_x, sr_fx, dx)  # Получить функцию интерполяции
tmp_x = [i * 0.1 * math.pi for i in range(-26, 27)]  # тестовых случаев
tmp_y = [Hx(i) for i in
         tmp_x]  # Получить вертикальную координату контрольного примера в соответствии с функцией интерполяции
plt.plot(sr_x, sr_fx, 'ro')
plt.plot(tmp_x, tmp_y, 'b-')
plt.title('Интерполяция Эрмита')
plt.show()