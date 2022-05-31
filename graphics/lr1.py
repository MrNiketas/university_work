import math
import matplotlib.pyplot as plot
import numpy as np

x = np.array([0, 1, 2, 3, 4.5], dtype=float)
y = np.array([0,1, 2, 3, 4], dtype=float)


def lagranz(x, y, t):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (t - x[i])
                p2 = p2 * (x[j] - x[i])
        z = z + y[j] * p1 / p2
    return z


if __name__ == '__main__':
    xnew = np.linspace(np.min(x), np.max(x), 100)
    ynew = [lagranz(x, y, i) for i in xnew]
    plot.plot(x, y, 'o', xnew, ynew)
    plot.grid(True)
    plot.show()
