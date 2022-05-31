import numpy as np
import matplotlib.pyplot as plt

def inter_spline(p):
    array = []
    i = 0
    while i <= len(p) - 4:
        for t in np.arange(0, 1.01, 0.01):
            array.append(0.5 * (-t * (1 - t) ** 2 * p[i] + (2 - 5 * t ** 2 + 3 * t ** 3) * p[i + 1]
                                + t * (1 + 4 * t - 3 * t ** 2) * p[i + 2] - t ** 2 * (1 - t) * p[i + 3]))
        i += 1
    return array


x = [1, 2, 3, 4, 5, 6, 6]
y = [3, 4, 3.5, 1, 1.5, 2, 2]

x_new = inter_spline(x)
y_new = inter_spline(y)

fig, ax = plt.subplots()
plt.plot(x,y,'o',x_new, y_new)
plt.grid()
plt.show()