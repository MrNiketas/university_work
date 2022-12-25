import numpy as np
from matplotlib import pyplot as plt

# построение графика
def draw_graphic(x, y, low_x, high_x, low_y, high_y, function):
    x1 = np.arange(low_x, high_x, 1)
    x2 = np.arange(low_y, high_y, 1)

    X1, X2 = np.meshgrid(x1, x2)

    z = function(X1, X2)

    lev = 100

    plt.figure(figsize=(10, 8))
    cs = plt.contour(X1, X2, z, lev, cmap='jet')
    plt.plot(x, y, marker=".")
    plt.clabel(cs)
    plt.title('Function')

    plt.show()
